# Knowledge-Database

Long-form reference material I build and maintain. Each directory is a
self-contained project: a rendered document, the source it was built from, and
the scripts that rebuild it.

---

## biomolecular-design-curriculum

**A multi-year self-study program in computational biomolecular design** —
every computational method for proteins, DNA and RNA, the AI research upstream
of it, and the engineering that makes it fast.

| | |
|---|---|
| **Document** | 479 pages, ~155,000 words |
| **Videos** | 3,271 individually verified talks and lectures |
| **Runtime** | ~3,500 hours of timed content |
| **Papers** | 547 citations, each paired to the section that discusses it |
| **Checkpoints** | 73 derivations to reproduce from a blank page |
| **Capstones** | 11 projects |

### Contents

- **`Biomolecular_Design_Curriculum.pdf`** — the document.
- **`Biomolecular_Design_Curriculum_Tracker.xlsx`** — a progress tracker.
  Every video in reading order with links, durations and paired papers; status
  dropdowns that drive a live dashboard; separate sheets for the core path,
  watch-then-read pairs, checkpoints, capstones, papers and the table of
  contents.
- **`source/`** — the markdown the PDF is built from, 49 numbered parts.
- **`build/`** — the build chain.
- **`all_links.txt`** — every URL in the document, deduplicated.

### How it is organised

**Part I — Foundations.** Mathematics, statistical mechanics, computer science,
chemistry. The part that does not go out of date.

**Part II — The Method Atlas.** Twenty families (A–T) covering every
computational method for proteins, DNA and RNA, organised by *the problem each
one solves* rather than by which software implements it. Potential energy
functions, molecular dynamics, Monte Carlo, enhanced sampling, free energy,
coarse-graining, continuum and mesoscale, polymer theory, dynamics and
allostery, structure determination, integrative modelling, classical
prediction, docking, evolution, geometric deep learning, learned structure
prediction, language models, generative design, benchmarking, RNA.

**Part III — Upstream AI Research.** Vision, architecture research, training at
scale, post-training and reinforcement learning, reasoning, deep learning
theory, interpretability — the literature that produces the ideas Part II
inherits two years later. It closes with fourteen specific transfers between
the two fields, in both directions.

**Part IV — Performance Engineering.** GPU and kernel programming, accelerators
and compilers, simulation-engine internals, and the systems engineering of
structure-prediction models. This part exists because making something ten
times faster is a real contribution and is usually treated as plumbing. Anton
is a hardware-software codesign result; FlashAttention introduced no new
mathematics; ColabFold's speedup came from replacing the sequence search, not
the network. It ends with eight open engineering problems.

**Part V — Contribution.** Derivation checkpoints, capstone projects, the
generators by which new methods get invented, and research craft — choosing
problems, writing, speaking, refereeing, and not fooling yourself.

**Part VI — Appendices.** The standing seminar archives enumerated talk by talk
(~500 entries), ten major courses enumerated lecture by lecture, an honest
register of what is missing from the public record, a progress tracker, and a
generated index of every method and package.

### Two conventions worth knowing

**Individual videos, never bare playlists.** A link to a 70-video course is a
deferral of the work of deciding what to watch. Every entry has a title, a
runtime and a direct link.

**Papers paired to talks.** Watch the talk, read the paper it narrates, and
write the gap between them. Thirty paired-reading tables run on this principle,
and it is the core study device of the whole document.

### A note on the gaps

Appendix C is a register of what the public record is *missing*, and it is
deliberate. Several foundational methods have no recorded talk anywhere; some
widely-cited researchers have never been filmed; and negative results are
recorded far less often than positive ones. Where something does not exist, the
document says so and names the paper to read instead rather than substituting a
lower-quality video.

### Rebuilding

Requires `pandoc`, Python 3, and a Chrome or Chromium binary.

```sh
cd biomolecular-design-curriculum
./build/build.sh                                  # markdown -> HTML -> PDF
python3 build/parse_curriculum.py source/full.md build/parsed.json
python3 build/make_workbook.py build/parsed.json Biomolecular_Design_Curriculum_Tracker.xlsx
```

The runtime budget and the method index are regenerated on every build, so
neither can drift out of date.

### Verification

All links were checked in October 2026 against the YouTube oEmbed endpoint and
`yt-dlp`. No dead links were found in sampling. A small number of entries have
embedding disabled by the uploader, which means they play normally on YouTube
but cannot be embedded in a page; those are flagged in the document.

---

*Compiled with [Claude Code](https://claude.com/claude-code).*
