"""Build Anki import files from the card data in ./src.

Usage:  python anki/build_cards.py

Each src/lectureN.py defines DECK, TAG and CARDS, a list of tuples:
    ("basic", front, back)   - concept / definition card       (Basic)
    ("exam",  front, back)   - long-form exam question + marking points (Basic)
    ("calc",  front, back)   - numerical problem + worked solution      (Basic)
    ("cloze", text, extra)   - fact/number recall                       (Cloze)

Light markup in card text:
    lines starting "- "  -> bullet list
    lines starting "1. " -> numbered list
    **bold**             -> <b>bold</b>
    other newlines       -> <br>
"""
import csv
import html
import importlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
LECTURES = ["lecture1", "lecture2", "lecture4", "lecture5", "lecture6", "lecture7"]
PARENT_DECK = "Security Technologies"
TYPE_LABEL = {"basic": "concept", "exam": "exam-style", "calc": "calculation", "cloze": "recall"}


def to_html(text):
    text = html.escape(text.strip(), quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    out, mode = [], None
    for line in text.split("\n"):
        bullet = re.match(r"\s*- (.*)", line)
        number = re.match(r"\s*\d+\. (.*)", line)
        want = "ul" if bullet else "ol" if number else None
        if mode and want != mode:
            out.append(f"</{mode}>")
            mode = None
        if want and mode is None:
            out.append(f"<{want}>")
            mode = want
        if want:
            out.append(f"<li>{(bullet or number).group(1)}</li>")
        elif line.strip():
            out.append(line + "<br>")
    if mode:
        out.append(f"</{mode}>")
    result = "".join(out)
    return result[:-4] if result.endswith("<br>") else result


def rows_for(module_name):
    mod = importlib.import_module(f"src.{module_name}")
    deck = f"{PARENT_DECK}::{mod.DECK}"
    for kind, front, back in mod.CARDS:
        notetype = "Cloze" if kind == "cloze" else "Basic"
        if kind == "exam":
            front = "📝 EXAM-STYLE\n" + front
        elif kind == "calc":
            front = "🧮 CALCULATION\n" + front
        tags = f"SecTech {mod.TAG} {TYPE_LABEL[kind]}"
        yield [notetype, deck, to_html(front), to_html(back), tags]


def write(path, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("#separator:tab\n#html:true\n#notetype column:1\n#deck column:2\n#tags column:5\n")
        csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)


def main():
    import sys
    sys.path.insert(0, str(ROOT))
    every, summary = [], []
    for name in LECTURES:
        rows = list(rows_for(name))
        write(ROOT / f"{name}_cards.txt", rows)
        every.extend(rows)
        counts = {}
        for r in rows:
            label = r[4].split()[-1]
            counts[label] = counts.get(label, 0) + 1
        summary.append(f"{name}: {len(rows)} notes {counts}")
    write(ROOT / "all_cards.txt", every)
    print("\n".join(summary))
    print(f"TOTAL: {len(every)} notes")


if __name__ == "__main__":
    main()
