#!/usr/bin/env python3
"""Sum up 25 November's world news in one image - make.fun entry.

Copies the image this repository holds (news25.png) to /output/entry.png.
Deterministic: the same bytes on every run, no network.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "news25.png"), "/output/entry.png")

if __name__ == "__main__":
    main()
