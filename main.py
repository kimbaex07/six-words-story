#!/usr/bin/env python3
"""Six Words, One Story entry.

Writes one original six-word story to /output/entry.txt (UTF-8,
trailing newline). The story is a complete miniature narrative:
a letter arrives too late, and the person it was meant for has
already moved on. Pure Python standard library only. No network,
no third-party imports.
"""

import os

STORY = "Her letter arrived. He'd already moved."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
