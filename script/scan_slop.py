#!/usr/bin/env python3
"""
scan_slop.py - first-pass detector for "AI slop" markdown patterns.

Usage:
    python3 scan_slop.py <file.md> [file2.md ...]

Reports line numbers and matches only. Does not modify the file:
fixing these needs human/model judgment so meaning and technical
content (code, flags, commands) stay intact.
"""

import re
import sys
from pathlib import Path

CHECKS = [
    ("em/en dash used as punctuation", re.compile(r"[\u2014\u2013]")),
    ("curly quotes / curly apostrophe", re.compile(r"[\u201c\u201d\u2018\u2019]")),
    ("ellipsis glyph (use ...)", re.compile(r"\u2026")),
    ("decorative emoji", re.compile(
        r"[\U0001F300-\U0001FAFF\u2600-\u27BF]"
    )),
    ("bold-colon list header (- **Word:**)", re.compile(
        r"^[ \t]*[-*][ \t]+\*\*[^*\n]+:\*\*|^[ \t]*[-*][ \t]+\*\*[^*\n]+\*\*[ \t]*:", re.MULTILINE
    )),
    ("title case heading", re.compile(
        r"^#{1,6}[ \t]+(?:[A-Z][a-z']*[ \t]+){2,}[A-Z][a-z']*[ \t]*$", re.MULTILINE
    )),
    ("horizontal rule divider (possible overuse)", re.compile(
        r"^[ \t]*---[ \t]*$", re.MULTILINE
    )),
]

CLICHE_PHRASES_EN = [
    "it is important to note",
    "in today's fast-paced",
    "plays a crucial role",
    "plays a pivotal role",
    "stands as a testament",
    "serves as a testament",
    "not just", "it's not just",
    "in conclusion",
    "i hope this helps",
    "let me know if",
    "additionally,", "moreover,", "furthermore,",
    "delve into",
    "rich tapestry",
    "underscores the importance",
]

CLICHE_PHRASES_ID = [
    "tidak hanya", "tetapi juga",
    "hal ini menunjukkan bahwa",
    "secara keseluruhan",
    "dalam rangka untuk",
    "berbagai macam",
    "memainkan peran penting",
    "memainkan peran krusial",
    "semoga membantu",
    "berikut adalah",
]


def scan_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    hits = 0

    print(f"\n=== {path} ===")

    for label, pattern in CHECKS:
        for m in pattern.finditer(text):
            line_no = text.count("\n", 0, m.start()) + 1
            snippet = lines[line_no - 1].strip()[:100] if line_no - 1 < len(lines) else ""
            print(f"[{label}] line {line_no}: {snippet}")
            hits += 1

    lowered = text.lower()
    for phrase in CLICHE_PHRASES_EN + CLICHE_PHRASES_ID:
        for m in re.finditer(re.escape(phrase), lowered):
            line_no = lowered.count("\n", 0, m.start()) + 1
            snippet = lines[line_no - 1].strip()[:100] if line_no - 1 < len(lines) else ""
            print(f"[cliche phrase: '{phrase}'] line {line_no}: {snippet}")
            hits += 1

    if hits == 0:
        print("No slop patterns found.")
    else:
        print(f"\n{hits} potential issue(s) found. Review manually, this script does not auto-edit.")

    return hits


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scan_slop.py <file.md> [file2.md ...]")
        sys.exit(1)

    total = 0
    for arg in sys.argv[1:]:
        path = Path(arg)
        if not path.exists():
            print(f"Skipping {arg}: not found")
            continue
        total += scan_file(path)

    sys.exit(0)


if __name__ == "__main__":
    main()
