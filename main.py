"""One Word From Your Ex — make.fun entry.

Writes exactly one word, the word their ex would use to describe them,
to /output/entry.txt. Nothing else. Pure stdlib Python 3.13.
"""

import os

WORD = "Unforgettable"


def main() -> None:
    # Gate: exactly one word, 1-24 characters, not only whitespace.
    # "Unforgettable" — 13 characters, one word, painfully honest.
    assert WORD and not WORD.isspace(), "word must not be blank"
    assert len(WORD.split()) == 1, "entry must be exactly one word"
    assert 1 <= len(WORD) <= 24, "word must be 1-24 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
