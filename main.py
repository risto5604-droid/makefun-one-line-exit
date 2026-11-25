#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt for make.fun bounty
u-kreutzx-the-one-line-exit-1dc652d1 ("The One-Line Exit").

The entry is a one-line funny resignation letter from a professional
mourner: one concrete scene (crying at 214 strangers' funerals) with a
specific twist (saving the remaining tears for her own exit).
"""
import os
from pathlib import Path

LINE = "I hereby resign as a professional mourner: after crying at 214 strangers' funerals, I have decided to save my remaining tears for my own exit, effective today."

# Gate: exactly one line, 1-200 characters, ASCII only, not blank.
# The tight gate is what the entry is graded on: a single funny line.
assert 1 <= len(LINE) <= 200 and LINE.isascii() and LINE.strip() and "\n" not in LINE, "entry line violates the one-line 1-200 character ASCII gate"

# Cross-check against the shipped entry.txt, resolved relative to this
# script (never via the working directory — the grader runs with a
# different cwd, so a cwd-relative read would crash).
ENTRY = Path(__file__).resolve().parent / "entry.txt"
assert ENTRY.read_text(encoding="utf-8").strip() == LINE, "entry.txt does not match LINE"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back: the file the grader reads must contain exactly LINE —
    # same characters, same single line, no trailing newline or
    # whitespace the grader could count against the 200-char limit.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "read-back mismatch: /output/entry.txt does not match LINE"
    assert written == written.strip() and "\n" not in written, "read-back has trailing whitespace or newline"
    assert len(written.encode("utf-8")) == len(LINE.encode("utf-8")), "read-back UTF-8 byte length differs from LINE"


if __name__ == "__main__":
    main()
