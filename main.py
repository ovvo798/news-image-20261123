#!/usr/bin/env python3
"""Write the competition entry image to /output/entry.png.

Simplest correct program: copy the repo-held entry.png to
/output/entry.png. Deterministic (byte-identical on every run),
no network access, no extra dependencies (Python 3 standard library).
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    print("Wrote " + DST)


if __name__ == "__main__":
    main()
