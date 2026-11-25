"""News-image entry for make.fun bounty news-image-20261125.

Copies the bundled entry.png (a newspaper front page summing up Wednesday
25 November 2026) to /output/entry.png. Deterministic: the same input bytes
produce the same output bytes on every run. No network, no randomness, no
arguments. Python 3.13 standard library only.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
