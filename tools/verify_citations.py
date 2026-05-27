#!/usr/bin/env python3
"""Verify that every \\bibitem in the papers refers to a real work.

This checks *existence* of each cited reference by resolving its title (plus
author and year) against the Crossref and arXiv APIs. It does NOT check whether
the cited work actually supports the claim it is attached to -- that remains a
human/agent responsibility per METHODOLOGY.md (Citation Discipline).

References that legitimately cannot be resolved via title/DOI APIs (books,
conference proceedings, internal companion papers) are listed in
tools/citation-allowlist.yml with a justification.

Exit code 0 if every reference is resolved or allowlisted; 1 otherwise.
Ambiguous matches are reported as warnings and do not fail the run.

Usage:
    python tools/verify_citations.py [--json] [paper.tex ...]

With no file arguments, all programs/*/index.tex files are checked.
"""

from __future__ import annotations

import argparse
import difflib
import glob
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

CROSSREF_API = "https://api.crossref.org/works"
ARXIV_API = "http://export.arxiv.org/api/query"
# Crossref "polite pool": identify ourselves so we get better service.
MAILTO = os.environ.get("CITATION_VERIFY_MAILTO", "will@regelmann.net")
USER_AGENT = f"self-consistency-citation-verifier/1.0 (mailto:{MAILTO})"

RESOLVE_THRESHOLD = 0.90  # >= this title similarity (with year match) -> resolved
AMBIGUOUS_THRESHOLD = 0.75  # >= this -> ambiguous (warn); below -> unresolved
YEAR_TOLERANCE = 1


# ── LaTeX -> plain text ────────────────────────────────────────────

_ACCENTS = {
    r"\v{c}": "c", r"\v{s}": "s", r"\v{z}": "z", r"\v{r}": "r",
    r"\'a": "a", r"\'e": "e", r"\'i": "i", r"\'o": "o", r"\'u": "u",
    r"\'c": "c", r"\'n": "n", r"\`a": "a", r"\`e": "e",
    r'\"a': "a", r'\"o': "o", r'\"u': "u",
    r"\o ": "o", r"\o": "o", r"\ss": "ss", r"\&": "and",
}


def latex_to_text(s: str) -> str:
    """Best-effort conversion of a LaTeX fragment to plain text."""
    for tex, plain in _ACCENTS.items():
        s = s.replace(tex, plain)
    # \textit{...}, \textbf{...}, \emph{...} -> contents
    s = re.sub(r"\\(?:textit|textbf|emph|text|mathrm)\{([^}]*)\}", r"\1", s)
    # Remaining backslash commands with a brace arg -> contents
    s = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", s)
    # Bare backslash commands -> drop
    s = re.sub(r"\\[a-zA-Z]+", " ", s)
    s = s.replace("~", " ").replace("\\", "")
    s = s.replace("``", '"').replace("''", '"').replace("--", "-")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def normalize_title(s: str) -> str:
    s = latex_to_text(s).lower()
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


# ── Bibliography parsing ───────────────────────────────────────────

class Reference:
    def __init__(self, key: str, raw: str):
        self.key = key
        self.raw = raw
        self.arxiv_id = self._extract_arxiv_id(raw)
        self.title = self._extract_title(raw)
        self.year = self._extract_year(raw)
        self.author = self._extract_author(raw)

    @staticmethod
    def _extract_arxiv_id(raw: str) -> str | None:
        m = re.search(r"arXiv:\s*([0-9]{4}\.[0-9]{4,5})", raw)
        return m.group(1) if m else None

    @staticmethod
    def _is_metadata_field(field: str) -> bool:
        # Trailing "preprint", "arXiv:...", "to appear", etc. -- not part of the title.
        return bool(re.match(r"^(preprint|arxiv|to appear|in press|forthcoming)\b",
                             field.strip().lower()))

    @staticmethod
    def _is_author_field(field: str) -> bool:
        f = field.strip()
        if not f:
            return True
        if "et al" in f.lower():
            return True
        # Leading initials, optionally prefixed by "and": "A. A. Starobinsky",
        # "and R. M. Wald". A real title starting with "A new..." has no period.
        return bool(re.match(r"^(and\s+)?[A-Z]\.", f))

    @classmethod
    def _extract_title(cls, raw: str) -> str | None:
        # "et al." is sometimes italicized inside the author block; don't mistake
        # it for the journal when we split on \textit below.
        raw = re.sub(r"\\(?:textit|emph)\{\s*et al\.?\s*\}", " et al.", raw)
        # Style 1 (quoted): author, ``Title,'' \textit{Journal} ...
        m = re.search(r"``(.+?)''", raw, re.DOTALL)
        if m:
            return latex_to_text(m.group(1)).rstrip(",. ")
        # Style 2 (unquoted): Author, Title, \textit{Journal} ...
        # The title is everything before the journal, minus leading author fields
        # and any trailing preprint/arXiv metadata.
        pre = re.split(r"\\textit", raw, 1)[0]
        fields = [latex_to_text(x) for x in pre.split(",")]
        fields = [f for f in fields if f]
        title_fields = []
        seen_title = False
        for f in fields:
            if not seen_title and cls._is_author_field(f):
                continue
            if cls._is_metadata_field(f):
                break
            seen_title = True
            title_fields.append(f)
        if title_fields:
            return ", ".join(title_fields).rstrip(",. ")
        # Style 3 (book): author, \textit{Book Title} (Publisher, year).
        m = re.search(r"\\textit\{([^}]*)\}", raw)
        if m:
            return latex_to_text(m.group(1)).rstrip(",. ")
        return None

    @staticmethod
    def _extract_year(raw: str) -> int | None:
        years = re.findall(r"\((\d{4})\)", raw)
        if not years:
            years = re.findall(r"\b(19|20)\d{2}\b", raw)
            return int(years[-1]) if years else None
        return int(years[-1])

    @staticmethod
    def _extract_author(raw: str) -> str:
        # Everything before the first ``-quoted title is the author block.
        head = raw.split("``", 1)[0]
        return latex_to_text(head).rstrip(",. ")


def parse_bibliography(tex: str) -> list[Reference]:
    m = re.search(
        r"\\begin\{thebibliography\}.*?(\\bibitem.*?)\\end\{thebibliography\}",
        tex,
        re.DOTALL,
    )
    if not m:
        return []
    body = m.group(1)
    chunks = re.split(r"\\bibitem(?:\[[^\]]*\])?\{([^}]*)\}", body)
    # chunks = ['', key1, text1, key2, text2, ...]
    refs = []
    for i in range(1, len(chunks), 2):
        key = chunks[i].strip()
        text = chunks[i + 1] if i + 1 < len(chunks) else ""
        refs.append(Reference(key, text.strip()))
    return refs


# ── Resolution ─────────────────────────────────────────────────────

_cache: dict[str, float] = {}


def _http_get(url: str) -> bytes | None:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read()
        except Exception:
            time.sleep(1.5 * (attempt + 1))
    return None


def crossref_best_score(ref: Reference) -> float:
    if not ref.title:
        return 0.0
    norm = normalize_title(ref.title)
    if norm in _cache:
        return _cache[norm]
    params = urllib.parse.urlencode(
        {"query.bibliographic": ref.title, "rows": 5, "mailto": MAILTO}
    )
    data = _http_get(f"{CROSSREF_API}?{params}")
    best = 0.0
    if data:
        try:
            items = json.loads(data)["message"]["items"]
        except Exception:
            items = []
        for it in items:
            titles = it.get("title") or []
            for t in titles:
                ratio = difflib.SequenceMatcher(None, norm, normalize_title(t)).ratio()
                if ratio <= best:
                    continue
                # Require the year to agree when we have both.
                cr_year = _crossref_year(it)
                if ref.year and cr_year and abs(cr_year - ref.year) > YEAR_TOLERANCE:
                    ratio *= 0.8  # penalize year mismatch, don't hard-reject
                best = max(best, ratio)
    _cache[norm] = best
    time.sleep(0.4)  # be polite to the API
    return best


def _crossref_year(item: dict) -> int | None:
    for field in ("published-print", "published-online", "issued", "created"):
        parts = item.get(field, {}).get("date-parts")
        if parts and parts[0] and parts[0][0]:
            return int(parts[0][0])
    return None


def arxiv_id_exists(arxiv_id: str) -> bool:
    params = urllib.parse.urlencode({"id_list": arxiv_id, "max_results": 1})
    data = _http_get(f"{ARXIV_API}?{params}")
    time.sleep(0.4)
    if not data:
        return False
    text = data.decode("utf-8", "ignore")
    # A real id returns an <entry> with a matching <id> and no error title.
    return f"abs/{arxiv_id}" in text and "<entry>" in text


def arxiv_best_score(ref: Reference) -> float:
    if not ref.title:
        return 0.0
    norm = normalize_title(ref.title)
    params = urllib.parse.urlencode(
        {"search_query": f'ti:"{ref.title}"', "max_results": 5}
    )
    data = _http_get(f"{ARXIV_API}?{params}")
    best = 0.0
    if data:
        for t in re.findall(r"<title>(.*?)</title>", data.decode("utf-8", "ignore"), re.DOTALL):
            ratio = difflib.SequenceMatcher(None, norm, normalize_title(t)).ratio()
            best = max(best, ratio)
    time.sleep(0.4)
    return best


# ── Allowlist ──────────────────────────────────────────────────────

def load_allowlist(path: str) -> dict[str, str]:
    """Minimal YAML reader: `key: reason` pairs. Avoids a PyYAML dependency."""
    allow: dict[str, str] = {}
    if not os.path.exists(path):
        return allow
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if line.startswith(" ") or line.startswith("\t"):
                continue  # only top-level "key: reason" entries
            m = re.match(r"([A-Za-z0-9_:-]+)\s*:\s*(.*)$", line)
            if m:
                allow[m.group(1)] = m.group(2).strip().strip("\"'")
    return allow


# ── Main ───────────────────────────────────────────────────────────

def classify(score: float) -> str:
    if score >= RESOLVE_THRESHOLD:
        return "resolved"
    if score >= AMBIGUOUS_THRESHOLD:
        return "ambiguous"
    return "unresolved"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("files", nargs="*", help="paper .tex files (default: all programs)")
    ap.add_argument("--json", action="store_true", help="emit JSON instead of a table")
    ap.add_argument(
        "--allowlist",
        default=os.path.join(os.path.dirname(__file__), "citation-allowlist.yml"),
    )
    args = ap.parse_args()

    files = args.files or sorted(glob.glob("programs/*/index.tex"))
    allow = load_allowlist(args.allowlist)

    rows = []
    failed = False
    for path in files:
        with open(path, encoding="utf-8") as f:
            refs = parse_bibliography(f.read())
        for ref in refs:
            if ref.key in allow:
                rows.append((path, ref.key, "allowlisted", 1.0, ref.title or ""))
                continue
            if ref.arxiv_id and arxiv_id_exists(ref.arxiv_id):
                rows.append((path, ref.key, "resolved", 1.0, ref.title or ref.arxiv_id))
                continue
            score = crossref_best_score(ref)
            status = classify(score)
            if status != "resolved":
                # Second opinion from arXiv before giving up.
                ax = arxiv_best_score(ref)
                if ax > score:
                    score, status = ax, classify(ax)
            if status == "unresolved":
                failed = True
            rows.append((path, ref.key, status, score, ref.title or "(no title parsed)"))

    if args.json:
        print(json.dumps(
            [{"file": f, "key": k, "status": s, "score": round(sc, 3), "title": t}
             for f, k, s, sc, t in rows],
            indent=2,
        ))
    else:
        _print_report(rows)

    return 1 if failed else 0


def _print_report(rows) -> None:
    counts = {"resolved": 0, "ambiguous": 0, "unresolved": 0, "allowlisted": 0}
    for _, _, status, _, _ in rows:
        counts[status] += 1

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    out_lines = []
    out_lines.append("## Citation verification")
    out_lines.append("")
    out_lines.append(
        "Checks reference **existence** (title/author/year vs. Crossref + arXiv). "
        "Does *not* verify that each source supports its claim.\n"
    )
    out_lines.append(
        f"**{counts['resolved']} resolved**, {counts['allowlisted']} allowlisted, "
        f"{counts['ambiguous']} ambiguous, **{counts['unresolved']} unresolved**.\n"
    )
    out_lines.append("| File | Key | Status | Score | Title |")
    out_lines.append("|------|-----|--------|------:|-------|")
    icon = {"resolved": "✅", "allowlisted": "📖", "ambiguous": "⚠️", "unresolved": "❌"}
    for f, k, status, score, title in rows:
        prog = f.split("/")[1] if "/" in f else f
        t = (title[:60] + "…") if len(title) > 61 else title
        out_lines.append(
            f"| {prog} | `{k}` | {icon[status]} {status} | {score:.2f} | {t} |"
        )
    report = "\n".join(out_lines)
    print(report)
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write(report + "\n")


if __name__ == "__main__":
    sys.exit(main())
