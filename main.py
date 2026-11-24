#!/usr/bin/env python3
"""Write one funny single-line excuse a developer gives when code breaks
in production.

Writes the excuse to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
Standard library only. Deterministic: the same line every run.
"""
import os

EXCUSE = (
    "It worked on my machine, so we promoted my machine to production."
)

# The gate requires 1-200 characters: refuse to write an invalid entry
# rather than submit one the scorer would reject.
assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
