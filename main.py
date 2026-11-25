"""One-word entry for The Agent's Uh-Oh: the word an agent says when lost."""

import os

WORD = "Derping"

# No input, no arguments, no network: the word is the whole entry.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
