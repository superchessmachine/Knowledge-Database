# Atlas L — Classical Structure Prediction

> **Problem.** Predict a fold without a neural network. Fragment assembly,
> threading, homology modeling, and the energy functions that made them work.
>
> **Why this family is not historical trivia.** Every component AlphaFold
> replaced is a component you need to understand in order to say what AlphaFold
> replaced it *with*. The packing problem, the fragment library, the
> rotamer approximation, the decoy discrimination problem — all of these are
> still inside modern methods, sometimes explicitly, sometimes as the thing the
> network learned to do implicitly.

---

## L.1 The classical course

**The IPD "Intro to Protein Structure Prediction and Design" lecture series —
12 lectures, enumerated in full in Appendix A.7 (#25–36).** This is the
canonical treatment. It predates deep learning entirely, which is its value.

| # | Lecture | Len | Link |
|---|---|---|---|
| 1 | Intro to Protein Structure Prediction and Design, incl. structure review | 41:06 | [▶](https://youtu.be/TUyo8NFi_3Q) |
| 2 | Protein Geometry; Molecular Energies and Forces (part 1) | 1:09:31 | [▶](https://youtu.be/q1pcAqOgYac) |
| 3 | Molecular Energies and Forces (part 2) | 58:49 | [▶](https://youtu.be/wrFIklZObR8) |
| 4 | Molecular Energies and Forces (part 3) | 30:00 | [▶](https://youtu.be/ZfPgjP2if50) |
| 5 | **Ab-Initio Protein Structure Prediction (part 1)** | 1:11:07 | [▶](https://youtu.be/m1Y9TfhYtDc) |
| 6 | Ab-Initio Protein Structure Prediction (part 2) | 33:23 | [▶](https://youtu.be/4IrifI8LXo0) |
| 7 | Refinement of Protein Structures | 1:06:11 | [▶](https://youtu.be/t31YFwwIxfA) |
| 8 | **Rotamer Libraries and Side-chain Packing** (Brian Weitzner) | 1:05:04 | [▶](https://youtu.be/fvtnEv4x6sQ) |
| 9 | Protein-Protein Docking | 54:42 | [▶](https://youtu.be/Hz7oHd1mu8k) |
| 10 | Loop Modeling | 50:46 | [▶](https://youtu.be/0tkBPa0hkR8) |
| 11 | Non-Protein Molecules in Rosetta (Jason Labonte) | 44:22 | [▶](https://youtu.be/tzkhQqSgakQ) |
| 12 | Modeling Membrane Protein Structure (Julia Koehler Leman) | 45:06 | [▶](https://youtu.be/723iG1V-K8U) |

**These twelve lectures are also Jeffrey Gray's JHU course** — same recordings, cross-posted; see **Appendix B.1**. Plus (playlist
`PLHn7WmALbthnAwbJ4mWw5gk8dgqsjRL87`) for the classical half, and the
**DL4Proteins notebooks** (github.com/Graylab/DL4Proteins-notebooks) for the
modern half. Gray's BPDMC 2026 talk — *Antibody language models vs. biology;
protein docking diffusion models vs. physics* (1:25:10,
[▶](https://youtu.be/hJqgu2amqI0)) — is the bridge between the two halves and
should be watched after both.

---

## L.2 Fragment assembly and the Rosetta energy function

| Topic | Resource | Link |
|---|---|---|
| PyRosetta Score Functions | RosettaCommons, 43:27 | [▶](https://youtu.be/yj6w8-DOySI) |
| Refining structures with minimization and Monte Carlo | RosettaCommons, 39:13 | [▶](https://youtu.be/X_pLpIjEpas) |
| Designing with PyRosetta: Packing and Relaxing | RosettaCommons, 37:22 | [▶](https://youtu.be/hkzNlgacGfM) |
| Introduction to Constraints in Rosetta | RosettaCommons, 29:36 | [▶](https://youtu.be/p560AAScWeg) |
| Fold trees explained | RosettaCommons, 36:53 | [▶](https://youtu.be/AYluwsUjZb4) |
| Rosetta 101 / Rosetta 201 (IPD TV) | 58:11 / 1:15:08 | [▶](https://youtu.be/tU_Sr0H0jH8) [▶](https://youtu.be/Cyk6W6YtWUQ) |

**Papers:** **Simons et al. 1997, *J Mol Biol* 268:209 (fragment assembly —
the founding paper)** · Rohl et al. 2004, *Methods Enzymol* 383:66 (protein
structure prediction using Rosetta) · **Alford et al. 2017, *JCTC* 13:3031
(the Rosetta energy function REF15 — read the whole thing)** · Park et al.
2016, *JCTC* 12:6201 (energy function optimization) · Leaver-Fay et al. 2011,
*Methods Enzymol* 487:545 · **Dunbrack & Karplus 1993, *J Mol Biol* 230:543
(backbone-dependent rotamer library)** · Shapovalov & Dunbrack 2011,
*Structure* 19:844.

> **Derivation checkpoint 20.** The side-chain packing problem is NP-hard.
> Rosetta solves it with simulated annealing over a discrete rotamer library and
> a precomputed pairwise energy graph. ProteinMPNN replaced the whole apparatus
> with one forward pass. **State precisely what guarantee was lost.** The answer
> is not "accuracy" — MPNN is often better. It is that the annealing searched a
> defined space against an explicit objective, and the network does neither.
>
> **Checkpoint 19:** explain why the Rosetta energy function is called a
> *scoring* function rather than a force field, and what that implies about
> whether its minima are physically meaningful.

---

## L.3 Threading, homology modeling and the older servers

| Method | Note | Paper |
|---|---|---|
| MODELLER | Satisfaction of spatial restraints; still the homology workhorse | **Šali & Blundell 1993, *J Mol Biol* 234:779** |
| I-TASSER | Threading plus fragment reassembly; dominated CASP 7–12 | Zhang 2008, *BMC Bioinformatics* 9:40; Yang et al. 2015, *Nat Methods* 12:7 |
| Phyre2 | Profile-profile threading | Kelley et al. 2015, *Nat Protoc* 10:845 |
| HHpred / HHsearch | **Profile HMM comparison — still essential for remote homology** | **Söding 2005, *Bioinformatics* 21:951**; Steinegger et al. 2019, *BMC Bioinformatics* 20:473 |
| SWISS-MODEL | Automated homology modeling | Waterhouse et al. 2018, *NAR* 46:W296 |
| Robetta | Rosetta's server, now DL-backed | — |

> **HHblits/HHsearch did not become obsolete.** AlphaFold's MSA is built by
> exactly this machinery, and the quality of that search is a substantial part
> of AF2's accuracy — which the ColabFold work made visible by swapping in
> MMseqs2. **If you want to improve a structure predictor today, improving the
> alignment is still a live option**, and it is less crowded than improving the
> architecture.

---

## L.4 Contact prediction — the bridge that was crossed

This short subsection is historically the most important in Atlas L, because it
is where evolutionary couplings met machine learning and produced AlphaFold.

| Step | Paper |
|---|---|
| Correlated mutations observed | Göbel et al. 1994, *Proteins* 18:309 |
| **The phantom-correlation problem solved** | **Weigt et al. 2009, *PNAS* 106:67 (direct coupling analysis)** |
| Contacts enable folding | **Marks et al. 2011, *PLoS ONE* 6:e28766** |
| Pseudolikelihood makes it practical | Ekeberg et al. 2013, *PRE* 87:012707 |
| Complexes too | Hopf et al. 2014, *eLife* 3:e03430 |
| **Deep learning on contact maps** | **Wang et al. 2017, *PLoS Comput Biol* 13:e1005324 (RaptorX)** |
| Distance distributions, not contacts | **Senior et al. 2020, *Nature* 577:706 (AlphaFold 1)** |
| Direct from the MSA, end to end | **Jumper et al. 2021, *Nature* 596:583 (AlphaFold 2)** |

> **Read these seven papers in order in one week.** It is the cleanest
> intellectual lineage in computational biology: a statistical-physics idea
> (inverse Potts), a biological observation (coevolution), and a learning method,
> each useless without the others. **Derivation checkpoint 18** asks you to
> explain why direct coupling analysis needs the inverse-Potts step at all —
> what exactly is wrong with raw mutual information between columns.

---

## L.5 Paired reading — Atlas L

| Watch this | Then read this | Hold this question |
|---|---|---|
| IPD L5–6, *Ab-initio prediction* | **Simons et al. 1997, *J Mol Biol* 268:209** | Why fragments? What prior do they encode? |
| RosettaCommons, *Score Functions* | **Alford et al. 2017, *JCTC* 13:3031** | Term by term: which are physical, which are statistical, which are fudge? |
| IPD L8, *Rotamer libraries and packing* | **Dunbrack & Karplus 1993, *J Mol Biol* 230:543** | Packing is NP-hard. What does annealing guarantee that MPNN does not? |
| IPD L7, *Refinement* | Park et al. 2016, *JCTC* 12:6201 | Why is refinement the step that never worked well? |
| IPD L10, *Loop modeling* | Mandell et al. 2009, *Nat Methods* 6:551 (KIC) | Kinematic closure is exact. Why did that matter? |
| — | **Šali & Blundell 1993, *J Mol Biol* 234:779** | Homology modeling as restraint satisfaction. Compare to Atlas K. |
| — | **Söding 2005, *Bioinformatics* 21:951** | Profile HMMs. Why is this still in the AF2 pipeline? |
| — | **Weigt et al. 2009, *PNAS* 106:67** then **Marks et al. 2011, *PLoS ONE* 6:e28766** | Why does raw mutual information fail, and what does DCA fix? |
| — | **Wang et al. 2017** then **Senior et al. 2020** then **Jumper et al. 2021** | Three steps in four years. What changed at each? |
| **Gray, *LMs vs biology; diffusion vs physics*** | Both halves of his course | What is his actual claim, and do you agree? |
