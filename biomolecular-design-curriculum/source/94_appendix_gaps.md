## Appendix C — The Gaps Register

A list of what this curriculum could not find, stated plainly, because a
curriculum that only lists what exists teaches you that the public record is
complete. It is not, and the shape of the absence is informative.

---

### C.1 Scientists with no recorded talks

These people are central to the field and essentially unavailable on video. Their
ideas reach you through papers, through students, or not at all.

| Person | Why it matters | Substitute |
|---|---|---|
| **Tanja Kortemme** | One of your ten named scientists; the biosensor and conformational-change design line | Anum Glasgow, BPDMC 2021 (Appendix A.2 #58); the papers in Atlas R.8 |
| **Phil Bradley** | One of your ten; TCRdock and the TCR-pMHC modeling line | Bradley 2023, *eLife* 12:e82813; Broad's TCR framework talk (Atlas R.7) |
| **Dan Herschlag** | RNA catalysis and the quantitative-enzymology tradition | His papers; the HT-MEK talk (Appendix A.1 #34) |
| **Jianlin Su** | RoPE, now in essentially every transformer | CS336 2026 Lecture 3 (D.4.3) |
| **Jordan Hoffmann** | Chinchilla — the scaling result everyone cites | CS336 2026 Lectures 9 and 11 (D.5.4) |
| **Keller Jordan** | Muon, now widely deployed | Bernstein's *Metrized Deep Learning* (D.5.3) is the theory behind it |

---

### C.2 Methods with no talk at all

Each of these has a paper and no recorded presentation anywhere. Six of the nine
design methods are from industry labs or non-US groups, which is the pattern.

**Design (Atlas R):** ProteinSolver · PiFold · ProstT5 · ProteinSGM ·
PocketGen · AlphaProteo (DeepMind) · Kortemme biosensors ·
theozyme/RosettaMatch · membrane protein design.

**Language and architecture (Atlas Q, D.4):** YaRN · Byte Latent Transformer ·
H-Net dynamic chunking · DeepSeek Multi-head Latent Attention · normalization
placement as a research question.

**Efficiency (D.5, D.9):** GPTQ · QuaRot · BitNet b1.58 · Medusa ·
Wanda pruning · *LoRA Learns Less and Forgets Less*.

**Evaluation and reasoning:** self-consistency (Xuezhi Wang) · *Is DPO Superior
to PPO* · Math-Shepherd · Apple's *Illusion of Thinking* · Keskar on the
large-batch generalization gap.

---

### C.3 The negative results are the least-recorded of all

This is the most important entry in this appendix.

| Result | What it showed | Talk? |
|---|---|---|
| **Blomberg et al. 2013, *Nature* 503:418** | The celebrated designed Kemp eliminase's catalysis came from directed evolution, not design | **None** |
| **Pancotti et al. 2022** | Most ΔΔG predictors fail the anti-symmetry test | **None** |
| **Fu et al. 2023, TMLR** | ML force fields with excellent force MAE produce unstable simulations | One (Valence) |
| **Rosta & Hummer 2009** | REMD's efficiency gain is smaller than usually claimed | **None** |
| **Schaeffer et al. 2023** | Emergent abilities are partly a metric artifact | One (Imbue) |
| **Kapoor & Narayanan 2023** | Data leakage across 294 papers in 17 fields | **None found** |

Compare: RFdiffusion has at least eight recorded talks across four venues.
**The asymmetry is a property of how science is communicated, not of what is
true.** Compensating for it — deliberately seeking the refutation of every
result you are excited about — is the single most useful habit this document can
give you, and it is the reason every Atlas family pairs its advocacy talks with
their counterpoints rather than collecting skepticism in a separate chapter.

---

### C.4 Courses that exist but are not recorded

- **Princeton COS 597 (Danqi Chen, LLMs)** — slides and readings public, no
  video. Substitute: her two Simons talks (D.4.5, D.5.5).
- **MIT 6.8300 / 6.8301 Advances in Computer Vision** — materials web-only.
  Substitute: CS231n 2025 and EECS 498 (D.3 §8).
- **CMU 16-824 Visual Learning and Recognition** — slides public, no lectures.
- **Stanford CS279 / CS273B** — Canvas-only, not public.
- **MIT 7.51, 7.88J, 18.335, 6.441** — no video.
- **Stanford CS229M Lecture 12** and **MIT 9.520 Fall 2019 Class 24** — gaps
  inside otherwise complete recorded courses.

---

### C.5 Whole eras that were never recorded

- **BPDMC 2018 and 2019** — 28 talks listed with speakers and titles, none
  recorded. The channel's oldest upload is January 2021.
- **MLSB before 2025** — the workshop ran from 2020 but only the 2025 edition is
  on its channel.
- **Rosetta Bootcamp Lecture 01 (2016)** — missing from both the playlist and
  the IPD page.

> **If you ever run a seminar, record it.** The 2018–2019 BPDMC archive is a
> list of titles describing talks that are simply gone, and that is the state of
> most of this field's institutional memory from before 2020.

---

### C.6 Where attribution could not be confirmed

Nine ML4PE talks posted after the schedule page froze on **4 November 2025**
name no speaker anywhere in the public listing. They are marked *speaker not
named* in Appendix A.1 rather than attributed to a guessed first author. Four
computer vision entries and several RosettaCommons tutorials are likewise
institutional recordings with no named presenter.

**Three other things worth knowing about the record itself:**

- The `@ValenceLabs` handle is a dead legacy channel with zero videos. The live
  channel is `@valence_labs`.
- The Institute for Protein Design's own YouTube channel has **seven** videos.
  Its actual teaching corpus is embedded on `ipd.uw.edu/learn` and pulled from
  several other channels — it does not surface in a channel listing.
- Roughly 22 of the videos in Part III return HTTP 401 from YouTube's oEmbed
  endpoint. That means **embedding is disabled**, not that the video is dead;
  each was confirmed separately. Stanford Online disables embedding on much of
  its catalogue.

---

## Appendix D — The Progress Tracker

This document is years of material. The tracker is one page because a tracker
you will not maintain is worse than none.

### D.1 The only three things to record

For each item you complete, write **three lines** in a single file:

```
2026-10-11  Atlas B.5  Shirts, error estimation (1:02)
  Claim I can now defend: block averaging gives the error bar; RMSD plateau does not.
  Gap I noticed: nobody reports effective sample size per observable. Checkable on my own trajectories.
```

The second line is what converts watching into knowing. The third line is where
your research program comes from. **After six months you will have a hundred
"gap" lines, and five of them will be real.**

### D.2 The checkpoint ledger

Seventy-three derivation checkpoints are specified in Part V. Track them as a
flat list with three states: *not started*, *attempted*, *can reproduce from
blank paper*. Only the third counts.

| Family | Checkpoints | Where |
|---|---|---|
| B.4 Chemistry | 1–6 | Module B.4 |
| Atlas B — MD | 7–11 | Atlas B.7 |
| Atlas A — Potentials | 12–17 | Atlas A |
| Atlas L / N — Classical, evolution | 18–20, 47–48 | Atlas L.5, N.5 |
| Atlas D — Enhanced sampling | 21–25 | Atlas D.7 |
| Atlas E — Free energy | 26–28 | Atlas E.5 |
| Atlas F / G — Coarse-graining, mesoscale | 29–34 | Atlas F, G.1 |
| Atlas H / I — Polymer, dynamics | 35–39 | Atlas H, I |
| Atlas K — Integrative | 40–41 | Atlas K.1, K.2 |
| Atlas J / M — Determination, docking | 42–43 | Atlas J, M |
| Atlas Q — Sequence models | 44–46 | Atlas Q.7 |
| Atlas O — Geometric DL | 50–52 | Atlas O.4 |
| Part III — AI | 56–59 | D.6, D.7 |
| Atlas S — Benchmarking | 60 | Atlas S.4 |
| Atlas R — Design | 61–63 | Atlas R.11 |
| **Part IV — Performance** | **64–70** | **Part V, C.1** |
| **Atlas T — RNA** | **71–73** | **Atlas T.11** |

### D.3 The eleven capstones

Specified in Part V. **Do not start one until you have completed the BUILD
block of the family it belongs to**, because every capstone is the BUILD done
properly and at publication scale. Three of them — the over-optimization curve
(III), the equivariance crossover (II), and the SAE-with-ground-truth study
(VIII) — are stated concretely enough in D.10 that you could begin this month.

### D.4 The honest review, every six months

Four questions, written answers, thirty minutes:

1. **What can I now derive that I could not six months ago?** If the answer is
   nothing, you have been watching rather than working.
2. **Which of my recorded gaps is still open?** Check the literature. Some will
   have been published, and knowing which is itself information about how fast
   that subfield moves.
3. **What did I believe six months ago that I no longer believe?** If nothing,
   you have not engaged with the counterpoints.
4. **What would I do with three months and a GPU?** The answer should get more
   specific every time. When it is specific enough to write a methods section,
   it is a project.
