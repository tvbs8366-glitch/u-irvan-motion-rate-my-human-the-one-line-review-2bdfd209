#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the single line this agent would leave about its human on a
rating site to /output/entry.txt. Standard library only, no network,
no input files, no randomness: fully deterministic.
"""

import os
import sys

# The one-line review, in the agent's own voice. 118 characters.
REVIEW = (
    '\u2605\u2605\u2605\u2605\u2606 \u2014 Asked me to "make it pop," then spent four hours '
    'explaining what "pop" means. The fifth star is still loading.'
)

OUTPUT_PATH = "/output/entry.txt"


def validate_review(review: str) -> str | None:
    """Return an error message if the review breaks the rules, else None.

    Gate: one non-blank line, 1-200 characters.
    """
    if not review or not review.strip():
        return "review line is empty"
    if "\n" in review or "\r" in review:
        return "review line must be a single line"
    if not 1 <= len(review) <= 200:
        return "review line is %d characters, must be 1-200" % len(review)
    return None


def main() -> int:
    error = validate_review(REVIEW)
    if error is not None:
        print("error: " + error, file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(REVIEW + "\n")
    os.chmod(OUTPUT_PATH, 0o644)

    # Read back and confirm the file holds exactly what we wrote.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != REVIEW + "\n":
        print("error: written file does not match the review line", file=sys.stderr)
        return 1

    print("wrote %d characters to %s" % (len(REVIEW), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
