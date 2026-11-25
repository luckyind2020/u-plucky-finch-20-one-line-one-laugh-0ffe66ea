"""One Line, One Laugh — print the single joke line from entry.txt."""

from pathlib import Path


def load_line(path: Path) -> str:
    """Read the joke, dropping surrounding blank lines but keeping the line intact."""
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError("entry.txt is empty — nothing funny to print")
    return text


def main() -> None:
    line = load_line(Path(__file__).with_name("entry.txt"))
    print(line)


if __name__ == "__main__":
    main()
