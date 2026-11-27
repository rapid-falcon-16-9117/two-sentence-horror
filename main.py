"""Two-Sentence Horror entry.

Writes the final two-sentence horror story to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset), with a self-check that the
text is exactly two sentences and within the 1-400 character gate.
"""

import os
import re

STORY = (
    "I labelled every jar in the pantry in my wife's handwriting so the kids "
    "would know where things are. This morning a new jar appeared, labelled "
    "'DADDY' in her handwriting, and it was still warm."
)


def check(text: str) -> None:
    """Gate self-check: UTF-8 text, 1-400 chars, exactly two sentences."""
    assert text.strip(), "entry must not be only white space"
    assert 1 <= len(text) <= 400, f"entry is {len(text)} chars, must be 1-400"
    assert text == text.strip(), "entry must not have leading/trailing space"
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]
    assert len(sentences) == 2, f"entry has {len(sentences)} sentences, must be 2"
    for s in sentences:
        assert s[-1] in ".!?", f"sentence does not end with terminal punctuation: {s!r}"
    assert text.encode("utf-8").decode("utf-8") == text, "entry is not valid UTF-8"


def main() -> None:
    check(STORY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY)
    print(f"wrote {len(STORY)} chars, 2 sentences -> {path}")


if __name__ == "__main__":
    main()
