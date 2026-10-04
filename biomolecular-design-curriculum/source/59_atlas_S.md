# Atlas S — Benchmarking and Evaluation

> **Problem.** Decide whether a method is better. This is harder than any
> individual method in this Atlas, and it is the family where a careful person
> can make the largest contribution with the least compute.
>
> **The thesis of this family in one sentence: most reported improvements in
> computational biology are benchmark artifacts, and the ones that are not become
> obvious in a blind assessment.**

---

## S.1 The blind assessments

These are the field's crown jewels and the reason structure prediction is
trustworthy in a way most of computational biology is not.

| Assessment | What it tests | Resource |
|---|---|---|
| **CASP** | Protein structure prediction, blind, biennial since 1994 | [predictioncenter.org](https://predictioncenter.org) |
| **CAPRI** | Protein-protein docking and complexes | [ebi.ac.uk/pdbe/capri](https://www.ebi.ac.uk/pdbe/complex-pred/capri/) |
| **CAFA** | Protein function prediction | [biofunctionprediction.org](https://biofunctionprediction.org) |
| **RNA-Puzzles** | RNA structure prediction | [rnapuzzles.org](https://www.rnapuzzles.org) |
| **CACHE** | Hit-finding for a given target, with experimental follow-up | [cache-challenge.org](https://cache-challenge.org) |
| **SAMPL** | Solvation, host-guest binding, partition coefficients | [samplchallenges.github.io](https://samplchallenges.github.io) |
| **D3R** | Pose and affinity prediction, blind | [drugdesigndata.org](https://drugdesigndata.org) |
| **Adaptyv** | **De novo binder design, scored in the wet lab** | [adaptyvbio.com](https://www.adaptyvbio.com) |

| Talk | Speaker / host | Length | Link |
|---|---|---|---|
| **Critical Assessment of Structure Prediction** | **John Moult & Krzysztof Fidelis** (MLSB 2025) | 36:17 | [▶](https://www.youtube.com/watch?v=SJtZpNb0lSE) |
| Initial reaction to AlphaFold2 right after CASP14 | AlQuraishi & Ovchinnikov (BPDMC) | 1:17:30 | [▶](https://youtu.be/C0QJcy84W3s) |
| **Optimizing Cetuximab: Winning Adaptyv's Competition** | Cradle | 53:53 | [▶](https://www.youtube.com/watch?v=6MwToW57YzQ) |
| **MotifBench: a standardized benchmark for motif-scaffolding** | ML4PE | 54:48 | [▶](https://www.youtube.com/watch?v=YLIBvA1dsQ4) |
| **FLAb2: How Well Can Protein AI Predict Developability?** | RosettaCommons | 31:46 | [▶](https://www.youtube.com/watch?v=Ib9dVOCy3j4) |
| **CARE: Benchmark Suite for Classification and Retrieval of Enzymes** | Jason Yang (ML4PE) | 47:02 | [▶](https://youtu.be/cP2vH8mChzE) |
| **PoseBusters: docking methods fail to generate physically valid poses** | Buttenschoen (Valence) | 34:28 | [▶](https://youtu.be/MiZzRQt-5q8) |
| **DART-Eval: a benchmark for DNA language models** | Stanford (MLCB) | 19:36 | [▶](https://www.youtube.com/watch?v=399s7HT9Db4) |
| Panel — Foundation models for biology, when are they useful? | MLCB 2024 | 51:23 | [▶](https://www.youtube.com/watch?v=KNefSdV5nSM) |
| Quantitative Affinity Data at Scale: the Data Bottleneck | Murakowska (BPDMC) | 47:16 | [▶](https://youtu.be/tjAPYPpQylo) |

**Papers:** **Moult et al. 1995, *Proteins* 23:ii (CASP's founding)** ·
Kryshtafovych et al. 2021, *Proteins* 89:1607 (CASP14 assessment) ·
**Buttenschoen et al. 2024, *Chem Sci* 15:3130 (PoseBusters)** ·
Notin et al. 2023, NeurIPS (ProteinGym) · Radivojac et al. 2013,
*Nat Methods* 10:221 (CAFA) · Cotet et al. 2025, bioRxiv (Adaptyv EGFR).

> **Why CASP worked and most benchmarks do not.** Targets are *not yet solved*
> when predictions are submitted, assessment is by third parties, and the
> assessors publish what failed. Every one of those is costly and every one is
> load-bearing. **A retrospective benchmark on a public test set has none of
> them**, which is why a method can be state-of-the-art on CASP-era data and
> useless on next year's structures.
>
> **Adaptyv is the most important entry in this table**, because it is the first
> standing blind assessment for *design*: you submit sequences, they synthesize
> and measure binding, and everyone sees the numbers. Design has had no CASP for
> thirty years. It now has the beginning of one.

---

## S.2 The failure modes, enumerated

Learn these by name. Each has cost someone a retraction.

1. **Train-test leakage by homology.** The canonical failure in this field. A
   30%-identity split is not sufficient when structural similarity survives below
   that. Foldseek-based structural splits are better and are rarely used.
2. **Temporal leakage.** Evaluating on structures deposited before the model's
   training cutoff. This is why CASP's "not yet solved" criterion matters.
3. **Thresholded metrics manufacturing discontinuity.** Schaeffer's argument
   (D.7.6) applied to biology: "fraction under 4 Å" is a step function over a
   continuous quantity. Report the continuous quantity.
4. **Means over heterogeneous splits.** A single ProteinGym number hides that
   performance inverts with MSA depth.
5. **Physical invalidity passing numeric checks.** PoseBusters: poses with good
   RMSD and impossible bond geometry.
6. **The missing baseline.** Compare to a nearest-neighbor retrieval baseline.
   In function prediction and in docking it is often not beaten.
7. **The anti-symmetry failure.** ΔΔG(A→B) ≠ −ΔΔG(B→A) in most predictors.
8. **Selection on the test set.** Tuning filters while looking at held-out
   results, which is what every design pipeline does by construction.
9. **Publication asymmetry in the benchmark itself.** The data were generated by
   experimentalists who report destabilizing mutations more often than neutral
   ones.
10. **Evaluating the wrong thing entirely.** FLAb2's point: antibody affinity
    prediction is not what determines whether an antibody becomes a drug.

> **Derivation checkpoint 60.** Take a benchmark you have used and audit it
> against all ten. Write one paragraph per item. **Most benchmarks fail three or
> four, and finding out which ones is more valuable than another model.**

---

## S.3 Statistics and experimental design

| Talk | Speaker / host | Length | Link |
|---|---|---|---|
| **Data thinning to avoid double dipping** | Lucy Gao (Broad MIA) | 1:31:46 | [▶](https://youtu.be/aY4duih4jMg) |
| **Knockoffs for Finding Variables with Statistical Guarantees** | Lucas Janson (Broad MIA) | 1:36:18 | [▶](https://youtu.be/3-OHVKOd2bc) |
| Bayesian methods for adaptive experimental design | Martin Jankowiak (Broad MIA) | 50:41 | [▶](https://youtu.be/2OjjsGhomMs) |
| **Conformal prediction under feedback covariate shift** | Wong-Fannjiang (ML4PE) | 58:45 | [▶](https://youtu.be/AOyDjBSQjhk) |
| Beyond the training set: detecting distribution shift | Damani (MLCB) | 24:14 | [▶](https://youtu.be/DeHt1LgtjyQ) |
| **Experimental Design and Data Annotation** | Graham Neubig (CMU Advanced NLP 9) | 1:17:22 | [▶](https://www.youtube.com/watch?v=hs37ze1j41A) |
| **Predictable Noise in LLM Benchmarks** | Sida Wang (Berkeley MOOC) | 44:04 | [▶](https://www.youtube.com/watch?v=HV8pugcFVO0) |
| **Six Principles for Evaluating Cognitive Capabilities in AI** | Melanie Mitchell (SFI) | 48:41 | [▶](https://www.youtube.com/watch?v=0DpJJFH9jvY) |
| Scaling Up "Vibe Checks" for LLMs | Shreya Shankar (MLSys #97) | 55:01 | [▶](https://www.youtube.com/watch?v=eGVDKegRdgM) |
| The Future of Language Models: A Perspective on Evaluation | Simons Institute | 1:05:41 | [▶](https://www.youtube.com/watch?v=wcPRW2YOqkA) |
| **CS336 2026 Lecture 12: Evaluation** | Stanford | 1:18:34 | [▶](https://www.youtube.com/watch?v=JpAxdTWQJxM) |

**Papers:** **Fannjiang et al. 2022, NeurIPS (conformal under feedback covariate
shift)** · Barber & Candès 2015, *Ann Stat* 43:2055 (knockoffs) ·
Neyshabur et al. 2021 (on the importance of a proper baseline) ·
**Kapoor & Narayanan 2023, *Patterns* 4:100804 (leakage and the reproducibility
crisis in ML-based science)**.

> **Kapoor & Narayanan is the paper to put on your wall.** They audited 294
> papers across 17 scientific fields and found data leakage in a large fraction
> of them. Their taxonomy of leakage types is the checklist in S.2 stated more
> rigorously. **If you read one paper from Atlas S, read that one.**
>
> **Sida Wang's *Predictable Noise in LLM Benchmarks* is the under-appreciated
> one.** Benchmark differences of a few points are frequently within run-to-run
> noise, and almost nobody reports error bars on a benchmark number. That
> criticism applies verbatim to every design hit rate in Atlas R.

---

## S.4 BUILD — Atlas S

1. **Pick a published comparison** in your own area where method A beat method
   B. Reproduce both on the stated benchmark.
2. **Re-split structurally** using Foldseek rather than sequence identity.
   Re-evaluate.
3. **Add the dumb baseline** — nearest neighbor by sequence, or by structure, or
   the training-set mode. Report it.
4. **Put error bars on everything** by bootstrapping over test examples and, if
   possible, over training seeds.
5. **Write the one page.** Does the original conclusion survive? Report the
   answer whichever way it comes out.

**Derivation checkpoint due: 60.**

> **This BUILD is the most likely of the nineteen to become a publication**, and
> it needs no new method and almost no compute. A careful re-evaluation that
> overturns or confirms a widely-cited comparison is a real contribution, and the
> field has very few people willing to do it.

---

## S.5 Paired reading — Atlas S

| Watch this | Then read this | Hold this question |
|---|---|---|
| **Moult & Fidelis, *Critical Assessment*** | **Moult et al. 1995, *Proteins* 23:ii** | What makes CASP's design work? Which parts are essential? |
| AlQuraishi & Ovchinnikov, *post-CASP14* | Kryshtafovych et al. 2021 | What convinced experts, in real time, that something had changed? |
| **Buttenschoen, *PoseBusters*** | **Buttenschoen et al. 2024, *Chem Sci* 15:3130** | Good RMSD, impossible chemistry. What else is your metric blind to? |
| ML4PE, *MotifBench* | The paper | Are published scaffolding results comparable? Why not? |
| RosettaCommons, *FLAb2* | The paper | Are you measuring the quantity that decides the outcome? |
| Yang, *CARE* | The paper | Enforce novelty in the split. How much performance was retrieval? |
| **Wong-Fannjiang, *Conformal under FCS*** | **Fannjiang et al. 2022, NeurIPS** | Design queries the model off-distribution. How do you get a valid interval? |
| Gao, *Data thinning* | Her paper | How do you use the same data twice without invalidating inference? |
| **Wang, *Predictable Noise in Benchmarks*** | The paper | Put error bars on the last benchmark number you quoted. |
| **Mitchell, *Six Principles*** | Her paper | Does your benchmark measure the capability or a correlate? |
| — | **Kapoor & Narayanan 2023, *Patterns* 4:100804** | Audit your own last project against their leakage taxonomy. |
| Cradle, *Adaptyv competition* | **Cotet et al. 2025, bioRxiv** | What would a standing CASP for design cost, and who would run it? |
