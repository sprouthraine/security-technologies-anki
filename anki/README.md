# Security Technologies – Anki Cards

360 notes built from `../notes/`, covering Lectures 1, 2, 4, 5, 6 and 7.

## Import
1. Anki desktop: **File → Import** and choose `all_cards.txt` (or a single `lectureN_cards.txt`).
2. The file headers set the note type, deck and tags automatically. Click **Import**.
   - This needs Anki 2.1.55 or later, plus the default **Basic** and **Cloze** note types.
   - Decks are created as `Security Technologies::L1 Waves & Fields`, and so on.

## Card types (filter by tag in the Browser)
| Tag | Note type | Purpose |
|---|---|---|
| `concept` | Basic | Definitions, mechanisms, "explain how X works" |
| `recall` | Cloze | Numbers, constants, formulas, limits, dates |
| `calculation` | Basic | Numerical problems with worked solutions |
| `exam-style` | Basic | Long-form questions with **mark allocations** and **marking points**, modelled on the problem sheets. Official problem-sheet questions are labelled "(Problem sheet Qn)" |

All notes are also tagged `SecTech` and `L1` … `L7`.

**Exam tip:** for `exam-style` cards, write or say a full answer before flipping. Then count how many marking points you hit against the mark allocation.

## Editing / rebuilding
Card content lives in `src/lectureN.py`. After editing, rebuild with:
```
python anki/build_cards.py
```
Re-importing updates existing notes that have the same first field (Anki's default duplicate handling).
