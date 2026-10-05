"""Build the downloadable Claude ZIPs and single-file chat instructions."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parent.parent
SKILLS = ("reseptit", "viikkosuunnittelu", "lomasuunnittelu")


def main():
    output = ROOT / "downloads"
    output.mkdir(exist_ok=True)
    for name in SKILLS:
        source = ROOT / name
        files = [source / "SKILL.md", *sorted((source / "references").glob("*.md"))]
        with ZipFile(output / f"{name}.zip", "w", ZIP_DEFLATED) as archive:
            for file in files:
                archive.write(file, file.relative_to(ROOT).as_posix())

        sections = [
            f"Laari / {name}\n\n"
            "This file contains the skill and all its reference files. "
            "References to file paths below refer to sections in this same file. "
            "Read those sections when the skill requests them.\n"
        ]
        for file in files:
            relative = file.relative_to(source).as_posix()
            sections.append(f"\n--- FILE: {relative} ---\n\n{file.read_text(encoding='utf-8')}")
        (output / f"laari-{name}.txt").write_text("\n".join(sections), encoding="utf-8")
        print(f"Built {name}: ZIP and TXT")


if __name__ == "__main__":
    main()
