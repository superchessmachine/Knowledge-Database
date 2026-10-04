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
| **Progress Tracker** | Every video in reading order. Set *Status* and the Dashboard follows. Filter by Part, Section or Priority. Each row also carries the paper that identifies what the talk is about, with a direct link. |
| **Dashboard** | Live completion by part and section. Formula-driven. |
| **Core Path** | The flagged essentials — roughly 150 hours |
| **Paired Reading** | Watch this → read that → hold this question |
| **Checkpoints** | 73 derivations. Only "can reproduce from blank paper" counts. |
| **Capstones** | 11 projects with prerequisites |
| **Papers** | 547 citations by section |
| **Sections** | Table of contents with counts and hours |

## The paper columns

Three columns on the Progress Tracker pair each talk with its reading:

- **Paired paper** — the citation.
- **Paper** — a link straight to it: arXiv or DOI where the citation carries
  one, otherwise a Scholar search that resolves in a click.
- **How paired** — where the pairing came from, strongest first:

| Value | Meaning |
|---|---|
| `stated with the talk` | The curriculum names this paper alongside this talk |
| `names <METHOD>` | The title and the citation name the same method — these tell you which program the talk is about |
| `paired reading` | From the curriculum's own watch-then-read tables |
| `section reading` | The reading for that section rather than that one talk |
| `reading for <section>` | Inherited from the parent section of a subsection |
| `course lecture - no single paper` | Deliberately blank |

That last case is most of Part I and all of Part VI, and it is correct: a
linear-algebra lecture or an enumerated course has no affiliated paper, and
inventing one would be worse than leaving it empty. Coverage is 95% across the
Method Atlas, 96% across performance engineering and 77% across the AI part —
the places where knowing the paper tells you what you are looking at.
