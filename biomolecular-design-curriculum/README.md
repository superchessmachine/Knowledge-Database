# Biomolecular Design Curriculum

See the [repository README](../README.md) for the full description.

| File | What it is |
|---|---|
| `Biomolecular_Design_Curriculum.pdf` | The document — 479 pages |
| `Biomolecular_Design_Curriculum_Tracker.xlsx` | Progress tracker, 9 sheets |
| `source/` | Markdown source, 49 numbered parts, concatenated in filename order |
| `build/build.sh` | markdown → pandoc → HTML → Chrome → PDF |
| `build/gen_hours.py` | Regenerates the runtime budget (section 0.9) |
| `build/gen_index.py` | Regenerates the method index (Appendix E) |
| `build/parse_curriculum.py` | Extracts videos, papers, pairs and checkpoints to JSON |
| `build/make_workbook.py` | Builds the tracker workbook from that JSON |
| `all_links.txt` | Every URL, deduplicated |

## The tracker

| Sheet | Use |
|---|---|
| **Start Here** | Orientation and totals |
| **Progress Tracker** | Every video in reading order. Set *Status* and the Dashboard follows. Filter by Part, Section or Priority. |
| **Dashboard** | Live completion by part and section. Formula-driven. |
| **Core Path** | The flagged essentials — roughly 150 hours |
| **Paired Reading** | Watch this → read that → hold this question |
| **Checkpoints** | 73 derivations. Only "can reproduce from blank paper" counts. |
| **Capstones** | 11 projects with prerequisites |
| **Papers** | 547 citations by section |
| **Sections** | Table of contents with counts and hours |
