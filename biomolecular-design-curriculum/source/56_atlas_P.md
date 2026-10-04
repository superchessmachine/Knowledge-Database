# Atlas P — Learned Structure Prediction

> **Problem.** Sequence in, coordinates out, with no explicit energy function.
> AlphaFold2 solved the monomer case well enough that the question changed; what
> remains is complexes, ligands, nucleic acids, ensembles, and — the hardest and
> least solved — **knowing when the answer is wrong.**

Every entry below is a talk paired with the paper it narrates. Watch first, read
second, write the gap.

---

## P.1 The architecture, properly

| Method | Talk | Speaker | Length | Link |
|---|---|---|---|---|
| AlphaFold1 | AlphaFold: improved structure prediction using potentials from deep learning | IPD, 2019 | 1:02:40 | [▶](https://www.youtube.com/watch?v=uQ1uVbrIv-Q) |
| AlphaFold2 | **CASP-16: From AlphaFold1 to AlphaFold2** | John Jumper | 55:15 | [▶](https://www.youtube.com/watch?v=oaUIQfuV6FU) |
| AlphaFold2 | Kendrew Lecture: Highly accurate protein structure prediction | John Jumper (MRC LMB) | 58:49 | [▶](https://www.youtube.com/watch?v=jTO6odQNp90) |
| AlphaFold2 | AlphaFold and its implications for understanding biology | John Jumper (NGBS2022) | 34:50 | [▶](https://www.youtube.com/watch?v=uejO0Af3eQc) |
| AlphaFold2 | **ML for protein structure prediction, Part 2: AlphaFold2 architecture** | Nazim Bouatta (Harvard CMSA) | 1:18:32 | [▶](https://www.youtube.com/watch?v=ri39B0Voujc) |
| AlphaFold2 | Part 1: Algorithm space | Nazim Bouatta | 1:30:25 | [▶](https://www.youtube.com/watch?v=yqeUH4RsJp8) |
| AlphaFold2 | Part 3: AlphaFold2 and OpenFold | Nazim Bouatta | 1:32:35 | [▶](https://www.youtube.com/watch?v=kIkn5DGEJJw) |

**Papers:** Senior et al. 2020, *Nature* 577 (AF1) · **Jumper et al. 2021,
*Nature* 596 — and the Supplementary Information, which is the real paper.**

### The critical talks — watch these too

| Talk | Speaker / venue | Length | Link |
|---|---|---|---|
| **Initial reaction to AlphaFold2 right after CASP14** | BPDMC, Dec 2020 | 1:17:30 | [▶](https://www.youtube.com/watch?v=C0QJcy84W3s) |
| AlphaFold 2: Is Protein Folding Solved? | AISC, 2021 | 59:57 | [▶](https://www.youtube.com/watch?v=y7uhfjq3KhU) |

The BPDMC session is the field processing the result in real time, two weeks
after CASP14, with no hindsight and no press office. There is no better record
of what a paradigm shift feels like from inside.

---

## P.2 OpenFold — what retraining revealed

| Talk | Speaker | Length | Link |
|---|---|---|---|
| **OpenFold: Lessons and insights from rebuilding and retraining AlphaFold2** | Mohammed AlQuraishi (IPAM) | 48:13 | [▶](https://www.youtube.com/watch?v=1Y9n7g6xX4Q) |
| OpenFold (Valence Labs version) | Mohammed AlQuraishi | 39:28 | [▶](https://www.youtube.com/watch?v=KvCvdFQ4Mrk) |
| OpenFold, long technical version | OpenBioML | 1:03:55 | [▶](https://www.youtube.com/watch?v=W92xVnUMkU0) |
| OpenFold (practical) | SBGrid | 1:01:48 | [▶](https://www.youtube.com/watch?v=EnKqDD8fSZY) |
| OpenFold3 and AQAffinity | SandboxAQ | 56:50 | [▶](https://www.youtube.com/watch?v=_DUzHDwDX9Q) |
| OpenFold3 for Biological Structure Prediction | Vecura AI4LIFE | 42:44 | [▶](https://www.youtube.com/watch?v=S6H_INT5hzc) |

**Paper:** Ahdritz et al. 2024, *Nature Methods* 21 — **[landmark]**. The only
systematic account of what AF2 actually learns, in what order, and how much
training data it needs. Retraining is the one experiment that turns a black box
into an object of study.

---

## P.3 The RoseTTAFold line

| Method | Talk | Speaker | Length | Link |
|---|---|---|---|---|
| RoseTTAFold | CASP AI-SIG | Minkyung Baek | 55:57 | [▶](https://www.youtube.com/watch?v=VIdElYuWDAQ) |
| RoseTTAFold2 | CASP15 predictor talk | Minkyung Baek | 45:18 | [▶](https://www.youtube.com/watch?v=e-LcY3a2uK0) |
| RF All-Atom | **Generalized Biomolecular Modeling and Design with RFAA** | Rohith Krishna (Valence) | 1:04:54 | [▶](https://www.youtube.com/watch?v=LAQ4-E0Cd8Q) |
| RF All-Atom | Molecular ML Reading Group: RoseTTAFold All-Atom | MaomLab (critical) | 51:00 | [▶](https://www.youtube.com/watch?v=PARZP6GWJ0w) |
| RF3 / AtomWorks | Accelerating Biomolecular Modeling with AtomWorks and RF3 | ML4PE | 51:17 | [▶](https://www.youtube.com/watch?v=ux6TxDO3GSY) |
| — | ML4PE Early Career Talk | Rohith Krishna | 56:22 | [▶](https://www.youtube.com/watch?v=dIgoaPoIolg) |

**Papers:** Baek et al. 2021, *Science* 373 · Baek et al. 2023, bioRxiv (RF2) ·
Krishna et al. 2024, *Science* 384 (RFAA).

---

## P.4 AlphaFold3 and the co-folding era

| Method | Talk | Speaker | Length | Link |
|---|---|---|---|---|
| AlphaFold3 | Towards Rational Drug Design with AlphaFold 3 | Max Jaderberg (Isomorphic) | 50:28 | [▶](https://www.youtube.com/watch?v=AE35XCN5NuU) |
| AlphaFold3 | **Review and discussion of AlphaFold3** | Sergey Ovchinnikov (BPDMC) | 1:12:58 | [▶](https://www.youtube.com/watch?v=qjFgthkKxcA) |
| AlphaFold3 | **Lessons from implementing AlphaFold3 in the wild** | Arda Goreci (Ligo Biosciences) | 25:52 | [▶](https://www.youtube.com/watch?v=97K0_b65oto) |
| AlphaFold3 | What's new and why it matters (practical) | RosettaCommons | 24:46 | [▶](https://www.youtube.com/watch?v=P6sHA0EmzY8) |
| Boltz-1 | **Democratizing Biomolecular Interaction Modeling** | Wohlwend & Corso (Proxima) | 40:59 | [▶](https://www.youtube.com/watch?v=mN5pXxRW4bA) |
| Boltz-1 | Boltz-1 and the Future of Biomolecular Foundation Models | Corso & Wohlwend (BPDMC) | 1:09:45 | [▶](https://www.youtube.com/watch?v=K-gzTJMy1ag) |
| Boltz-2 | Towards Accurate and Efficient Binding Affinity Prediction | Valence Labs | 59:27 | [▶](https://www.youtube.com/watch?v=iHDauMATkr0) |
| Chai-1 | Chai Discovery's Bitter Lesson: Drug Design Is Another Scaling Problem | Meier & Dent (Sequoia) | 47:23 | [▶](https://www.youtube.com/watch?v=wv53mDmY-k0) |
| Chai-1 | No Priors Ep. 121 | Dent & Meier | 49:28 | [▶](https://www.youtube.com/watch?v=rFFi2Guv2nU) |
| SeedFold | Scaling Biomolecular Structure Prediction | Zhou & Lu (Valence) | 59:59 | [▶](https://www.youtube.com/watch?v=qyxftQJdE3I) |
| AlphaFold-Multimer | AlphaFold workshop Part 2 | Roland Dunbrack (Utah) | 1:05:56 | [▶](https://www.youtube.com/watch?v=WW_XPhY6I60) |

**Papers:** Abramson et al. 2024, *Nature* 630 (AF3) **[landmark]** · Evans et al.
2021, bioRxiv (AF-Multimer) · Wohlwend et al. 2024 (Boltz-1) · Passaro et al.
2025 (Boltz-2) · Chai Discovery Team 2024.

> **Goreci's twenty-six minutes are the most useful item in this subsection.**
> Reimplementing a paper from its description is the strongest possible
> reproducibility test, and his account of what was underspecified is worth more
> than three admiring reviews. **You run Boltz-2 in production — watch this one
> before you trust an affinity number.**

**No talk exists** for Protenix (ByteDance 2025) or HelixFold3 (Liu et al. 2024,
arXiv:2408.16975). Read the papers.

---

## P.5 Older lineages and single-sequence prediction

| Method | Talk | Speaker | Length | Link |
|---|---|---|---|---|
| trRosetta | CASP15 predictor talk | Jianyi Yang | 22:12 | [▶](https://www.youtube.com/watch?v=70o6okX06no) |
| I-TASSER | Protein Structure Prediction | Yang Zhang | 1:14:36 | [▶](https://www.youtube.com/watch?v=zdSsTiXQhKI) |
| D-I-TASSER | CASP-16 predictor talk | Wei Zheng | 14:24 | [▶](https://www.youtube.com/watch?v=qGuOjYqWED4) |
| MULTICOM | CASP-16 predictor talk | Jianlin Cheng | 14:43 | [▶](https://www.youtube.com/watch?v=ysB23pawlIE) |
| ESMFold | Structure Prediction with ESMFold | RosettaCommons | 10:32 | [▶](https://www.youtube.com/watch?v=IkckNa6fVXo) |
| ESMFold2 | Biomolecular Structure Prediction with ESMFold2 | Biohub | 56:59 | [▶](https://www.youtube.com/watch?v=3Efk1Du4v6I) |
| RGN2 | **Predicting protein structures from single sequences** | Nazim Bouatta (BPDMC) | 1:33:06 | [▶](https://www.youtube.com/watch?v=eobc7cMMpeY) |
| RGN | MIA: End-to-end differentiable learning of protein structure | Mohammed AlQuraishi (Broad) | 56:12 | [▶](https://www.youtube.com/watch?v=HOVdHAnC8LI) |
| ColabFold | Making protein folding accessible to all | BPDMC | 1:46:09 | [▶](https://www.youtube.com/watch?v=Rfw7thgGTwI) |
| — | Structure Prediction with AlphaFold2 and OpenFold | RosettaCommons | 1:39:36 | [▶](https://www.youtube.com/watch?v=Y5-lhdwdJC0) |

**Papers:** Yang et al. 2020, *PNAS* 117 (trRosetta) · Yang et al. 2015,
*Nat Methods* 12 (I-TASSER) · Lin et al. 2023, *Science* 379 (ESMFold) ·
Chowdhury et al. 2022, *Nat Biotechnol* 40 (RGN2) · AlQuraishi 2019,
*Cell Systems* 8 (RGN) · Mirdita et al. 2022, *Nat Methods* 19 (ColabFold).

---

## P.6 Conformational ensembles — the frontier

> This subsection is the live research front and the one that most directly
> concerns you. A structure predictor returns one structure. A protein is an
> ensemble. Everything here is an attempt to close that gap, and none of it has
> converged.

| Method | Talk | Speaker | Length | Link |
|---|---|---|---|---|
| AF-Cluster | **Understanding fold-switching proteins by combining AF2 and sequence clustering** | Hannah Wayment-Steele (BPDMC) | 59:18 | [▶](https://www.youtube.com/watch?v=rgGceDDnIEo) |
| AF-Cluster | Predicting and discovering proteins with multiple conformational states | Hannah Wayment-Steele (ML4PE) | 47:49 | [▶](https://www.youtube.com/watch?v=T5yknC0tr50) |
| AFsample | CASP15 predictor talk | Björn Wallner | 21:07 | [▶](https://www.youtube.com/watch?v=fomZv3SYnz8) |
| AlphaFlow / ESMFlow | **AlphaFold Meets Flow Matching for Generating Protein Ensembles** | Bowen Jing (Valence) | 56:30 | [▶](https://www.youtube.com/watch?v=yDDXF6XJZck) |
| BioEmu | **Scalable Emulation of Protein Equilibrium Ensembles** | Valence Labs | 1:17:02 | [▶](https://www.youtube.com/watch?v=zaZAAWUISGE) |
| BioEmu | Emulation of protein equilibrium ensembles | Jiménez-Luna & Xie (Proxima) | 53:45 | [▶](https://www.youtube.com/watch?v=8vsTsb-m7u4) |
| BioEmu | third treatment | Andrew Foong | 58:12 | [▶](https://www.youtube.com/watch?v=e38r-xW2lM0) |
| DiG | Towards Predicting Equilibrium Distributions for Molecular Systems | Shuxin Zheng (Valence) | 1:12:14 | [▶](https://www.youtube.com/watch?v=n-v5eckx2eg) |
| Boltzmann generators | Deep Generative Learning for Physics Many-Body Systems | Frank Noé (IPAM) | 1:01:56 | [▶](https://www.youtube.com/watch?v=XhAP2VNPVhg) |
| — | Advancing molecular simulation with deep learning | Frank Noé | 58:32 | [▶](https://www.youtube.com/watch?v=JZjeFBH0Jl4) |
| PepFlow | Direct Conformational Sampling From Peptide Energy Landscapes | Osama Abdin (Valence) | 55:42 | [▶](https://www.youtube.com/watch?v=B__DMqLJpSY) |
| — | Accelerating Cryptic Pocket Discovery Using AlphaFold and MSMs | Valence Labs | 31:32 | [▶](https://www.youtube.com/watch?v=nwNKpJVBzSo) |
| — | ML4PE Early Career Talk | Soojung Yang | 58:36 | [▶](https://www.youtube.com/watch?v=ndDxc8VdYKE) |

**Papers:** Wayment-Steele et al. 2024, *Nature* 625 **[landmark]** · Wallner
2023, *Bioinformatics* 39 · Jing et al. 2024, ICML (AlphaFlow) · **Lewis et al.
2025, *Science* 389 (BioEmu)** · Zheng et al. 2024, *Nat Mach Intell* 6 (DiG) ·
**Noé et al. 2019, *Science* 365 (Boltzmann generators)** · Abdin & Kim 2024,
*Nat Mach Intell* 6 (PepFlow).

**No talk found:** Str2Str (Lu et al. 2024, ICLR) · subsampled-MSA ensembles
(Monteiro da Silva et al. 2024, *Nat Commun* 15) · MDGen (Jing et al. 2024,
NeurIPS).

> **The question that organizes this subsection.** BioEmu and AlphaFlow emulate
> an equilibrium distribution; a Boltzmann generator *samples* one with an
> exactness guarantee; an MSM *estimates* one from trajectories. Three different
> epistemic statuses, routinely compared on the same plots. Atlas J.2's
> Wankowicz and Fraser talk asks how you would even score a predicted ensemble.
> **Nobody has answered that, and it gates the whole subsection.**

---

## P.7 Co-folding, ligands, and the validity critique

| Method | Talk | Speaker | Length | Link |
|---|---|---|---|---|
| DiffDock | Diffusion Steps, Twists, and Turns for Molecular Docking | Valence Labs / M2D2 | 56:43 | [▶](https://www.youtube.com/watch?v=gAmTGw601dA) |
| DiffDock | long version with discussion | BPDMC | 1:36:23 | [▶](https://www.youtube.com/watch?v=_KBqVh6YbgI) |
| DiffDock | practical | SBGrid | 43:41 | [▶](https://www.youtube.com/watch?v=_S-WbbyUUbo) |
| DiffDock-PP | Protein Docking with DiffDock-PP | RosettaCommons | 21:19 | [▶](https://www.youtube.com/watch?v=HSOscmos6nE) |
| **PoseBusters** | **AI-based docking methods fail to generate physically valid poses** | Martin Buttenschoen (Valence) | 34:28 | [▶](https://www.youtube.com/watch?v=MiZzRQt-5q8) |
| PLINDER | New benchmarks for molecular interactions | Cao, Durairaj, Kovtun (Proxima) | 59:55 | [▶](https://www.youtube.com/watch?v=DLniEFBhkWA) |
| PLINDER | second treatment | Vladas Oleinikovas (RDKit UGM) | 35:08 | [▶](https://www.youtube.com/watch?v=7-auGX9Z9Nw) |
| Umol | Molecular ML Reading Group | MaomLab | 54:07 | [▶](https://www.youtube.com/watch?v=flsNV36AtAU) |
| NeuralPLexer | Dynamic-backbone protein-ligand complex prediction | Zhuoran Qiao (ML4PE) | 42:49 | [▶](https://www.youtube.com/watch?v=73blwIx9QUg) |
| Flow-matching docking | Harmonic Self-Conditioned Flow Matching for Multi-Ligand Docking | Hannes Stärk (Valence) | 59:47 | [▶](https://www.youtube.com/watch?v=Xl7YNR1-CN8) |

**Papers:** Corso et al. 2023, ICLR (DiffDock) · **Buttenschoen, Morris & Deane
2024, *Chem Sci* 15 (PoseBusters) [landmark]** · Durairaj et al. 2024, ICML
ML4LMS (PLINDER) · Bryant et al. 2024, *Nat Commun* 15 (Umol) · Qiao et al.
2024, *Nat Mach Intell* 6 · Stärk et al. 2024, ICML.

> **PoseBusters is the most important thirty-four minutes in this family.** It
> shows that deep docking methods produce poses that are not physically valid —
> wrong stereochemistry, clashes, impossible geometry — while scoring well on
> RMSD. That is a benchmark measuring the wrong thing, caught by someone who
> looked at the molecules. It is the clearest existing template for Capstone III,
> and PLINDER is the data-side companion on memorization and leakage.

---

## P.8 Protein-peptide and specialist regimes

| Talk | Speaker / venue | Length | Link |
|---|---|---|---|
| **Interpreting state-of-the-art structure predictors for protein-peptide complexes** | BPDMC, 2025 | 58:12 | [▶](https://www.youtube.com/watch?v=R87pmoB3QF0) |
| Cyclic peptide structure prediction and design using AlphaFold | ML4PE | 1:07:20 | [▶](https://www.youtube.com/watch?v=SDxy5E8fvXY) |
| Disorder Challenge Virtual Discussion | CASP16, Kretsch & Oas | 39:05 | [▶](https://www.youtube.com/watch?v=oh_EnlACfiw) |
| CASP15 disorder assessment | Damiano Piovesan | 20:21 | [▶](https://www.youtube.com/watch?v=sdNwwzW3o4Y) |

The peptide-complex talk is directly load-bearing for any cyclic-peptide and
cyclic-peptide work. **Paper:** Rettie et al. 2023, *Nat Commun* 15 (cyclic
peptide design with AlphaFold).

---

## P.9 Where this goes next

| Talk | Speaker | Length | Link |
|---|---|---|---|
| **What could AlphaFold 4 look like?** | Sergey Ovchinnikov (Owl Posting) | 2:06:40 | [▶](https://www.youtube.com/watch?v=6_RFXNxy62c) |
| Inverting protein structure prediction models to solve problems in biology | Sergey Ovchinnikov | 1:29:16 | [▶](https://www.youtube.com/watch?v=kNDdAWy7sRk) |
| Using AI for protein structure modeling and design | Sergey Ovchinnikov (Harvard CMSA) | 47:32 | [▶](https://www.youtube.com/watch?v=VGL-Jq50268) |
| Protein Structure Prediction in a Post-AlphaFold2 World | Mohammed AlQuraishi | 54:16 | [▶](https://www.youtube.com/watch?v=j9UHcxucKZE) |
| The State of Protein Structure Prediction and Friends | Mohammed AlQuraishi (Simons) | 1:05:31 | [▶](https://www.youtube.com/watch?v=19fy0we14XM) |
| Lecture 11: Protein Language Models (MLCB24) | Manolis Kellis (MIT) | 1:23:08 | [▶](https://www.youtube.com/watch?v=uPoFdCUqBWk) |

**Two hours of Ovchinnikov forecasting is the single highest-yield item in this
Atlas for your open-problems file.** Mine it.

---

## P.10 BUILD — Atlas P

1. **Implement triangle multiplicative update and triangle attention.** Verify
   numerically that they reduce triangle-inequality violations in a distance
   matrix. Checkpoint 60 in code.
2. **MSA depth ablation.** Ten targets, MSA subsampled to 1/4/16/64/256
   sequences. Plot pLDDT against true accuracy at each depth. **Does pLDDT track
   accuracy or does it track MSA depth?** This single experiment teaches more
   than ten papers.
3. **Run PoseBusters-style validity checks on your own Boltz-2 outputs.** What
   fraction are physically valid? Report the number.
4. **The ensemble exercise.** Take one protein with a known conformational
   change. Generate ensembles with AF-Cluster, AFsample and a short MD run.
   Compare the three distributions. Then propose a metric that would say which
   is right, and explain why it is hard.

**Derivation checkpoints due: 59, 60.**

---

## P.11 Paired reading — Atlas P

| Watch this | Then read this | Hold this question |
|---|---|---|
| Jumper, CASP-16 AF1→AF2 | **Jumper et al. 2021 SI, Algorithms 1–32** | Trace one residue pair through every block. Where does geometry first enter? |
| Bouatta Part 2 | Jumper et al. 2021 | Why recycling? What would break without it? |
| **BPDMC, post-CASP14 reaction** | The CASP14 abstracts | What did the community believe before the paper existed? What were they wrong about? |
| **AlQuraishi, OpenFold** | **Ahdritz et al. 2024, *Nat Methods* 21** | In what order do structural concepts emerge? What does that suggest about curriculum learning? |
| Krishna, RFAA | Krishna et al. 2024, *Science* 384 | All-atom means ligands and nucleic acids. What had to change architecturally? |
| Jaderberg, AF3 | **Abramson et al. 2024, *Nature* 630** | The structure module became a diffusion head. What did that buy and cost? |
| **Ovchinnikov, AF3 review** | Abramson et al. 2024 | Which criticisms are about the model and which about the release? |
| **Goreci, Implementing AF3 in the wild** | Abramson et al. 2024 | List everything underspecified. That list is a reproducibility finding. |
| Wohlwend & Corso, Boltz-1 | Wohlwend et al. 2024 | What did open reproduction reveal that the AF3 paper did not state? |
| Boltz-2 | Passaro et al. 2025 | How was the affinity head trained, and what is its applicability domain? |
| Bouatta, RGN2 | Chowdhury et al. 2022, *Nat Biotechnol* 40 | Single-sequence prediction with no MSA. Where does the information come from? |
| **Wayment-Steele, AF-Cluster** | **Wayment-Steele et al. 2024, *Nature* 625** | MSA clustering reveals alternate states. Are the populations meaningful? |
| Jing, AlphaFlow | Jing et al. 2024, ICML | Flow matching on top of AF2. What distribution is being matched? |
| **BioEmu** | **Lewis et al. 2025, *Science* 389** | "Emulation" of equilibrium. What is the guarantee, and how is it validated? |
| Noé, Boltzmann generators | **Noé et al. 2019, *Science* 365** | Compare the guarantee here to BioEmu's. Which is stronger and why? |
| Zheng, DiG | Zheng et al. 2024, *Nat Mach Intell* 6 | Predicting equilibrium distributions directly. What is the training signal? |
| Corso, DiffDock | Corso et al. 2023, ICLR | Docking as diffusion over SE(3) plus torsions. What is the product manifold? |
| **Buttenschoen, PoseBusters** | **Buttenschoen, Morris & Deane 2024, *Chem Sci* 15** | List every validity check. Apply all of them to your own pipeline's output. |
| PLINDER | Durairaj et al. 2024 | How do you build a leakage-free protein-ligand split? Why is it hard? |
| Qiao, NeuralPLexer | Qiao et al. 2024 | Dynamic backbone co-folding. What does state-specificity require? |
| BPDMC, protein-peptide predictors | Verify current peptide-complex benchmark papers | Why do peptides break these models specifically? |
| Rettie, cyclic peptides with AF | Rettie et al. 2023, *Nat Commun* 15 | AF2 never saw cyclic backbones. Why does the offset trick work at all? |
| **Ovchinnikov, AlphaFold 4** | — | Extract every open problem named, with the date. |
