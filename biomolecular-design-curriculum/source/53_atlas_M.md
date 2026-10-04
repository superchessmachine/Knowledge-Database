# Atlas M — Docking and Virtual Screening

> **Problem.** What binds where, and how tightly? Two subproblems that are
> routinely conflated and should not be. **Pose prediction** — where does this
> ligand sit — is largely solved for well-behaved cases. **Affinity prediction**
> — how tightly does it bind — is not, and the scoring functions that do the
> first job well do the second badly. Understanding why is the single most
> useful thing in this family.

---

## M.1 Protein-ligand docking

| Title | Speaker | Length | Link |
|---|---|---|---|
| AutoDock Introduction | CCPBioSim | 55:00 | [▶](https://www.youtube.com/watch?v=B68HeAqk_L8) |
| AutoDock Specialized Docking Methods | CCPBioSim | 32:00 | [▶](https://www.youtube.com/watch?v=ah--5sDF_wE) |
| **AutoDock CrankPep** (peptide docking) | CCPBioSim | 48:00 | [▶](https://www.youtube.com/watch?v=jKHqH_tuLqI) |
| **How to Interpret Your Docking Scores: A Medicinal Chemistry Perspective** | CCPBioSim | 42:00 | [▶](https://www.youtube.com/watch?v=rMl3ukxTt3A) |
| Finding New Drugs Using Computers | Stefano Forli (Scripps) | 52:00 | [▶](https://www.youtube.com/watch?v=WAGwhVf4QnA) |
| Structure-Based Virtual Screening on the Cheap | David Koes (Pittsburgh) | 50:00 | [▶](https://www.youtube.com/watch?v=-9SlV7_AL2Q) |
| Intro to GOLD | CCDC | 33:00 | [▶](https://www.youtube.com/watch?v=5di4Ua1pMaU) |
| BioExcel #80: Protein and ligand flexibility in molecular docking | BioExcel CoE | 58:00 | [▶](https://www.youtube.com/watch?v=qj_QAp3GHSw) |
| Protein Ligand Interactions and Docking | ROSTLAB (TU München) | 1:24:00 | [▶](https://www.youtube.com/watch?v=4CXGGs0YSC8) |
| Covalent Docking Screening Webinar | MolSoft | 45:00 | [▶](https://www.youtube.com/watch?v=AoJc0qq7mP4) |
| Ligand Docking Introduction (Rosetta Workshop 2020) | Meiler Lab | 24:00 | [▶](https://www.youtube.com/watch?v=-4wgIuMfr_w) |
| **The Rosetta Scorefunction** | Meiler Lab | 21:00 | [▶](https://www.youtube.com/watch?v=ugRpgp-8sY4) |
| Flexible Induced Fit Docking and Screening | MolSoft | 55:00 | [▶](https://www.youtube.com/watch?v=I-MOQPC-Snc) |

**"How to Interpret Your Docking Scores" is the single most useful item in this
family.** It is an explicit argument that docking scores rank *poses* well and
*affinities* badly — the distinction the field most often elides and the one
that explains most disappointed expectations.

CrankPep is the peptide-docking extension and is directly relevant to your
cyclic-peptide work, where standard small-molecule docking assumptions fail.

The Rosetta scorefunction lecture belongs here as a cultural contrast: it is an
*empirical* energy function with terms that have no physical referent, sitting
next to a family of methods that at least aspire to physics. Both work. Neither
works for the reason its authors claim.

---

## M.2 Protein-protein and information-driven docking

| Title | Speaker | Length | Link |
|---|---|---|---|
| Basics of docking and introduction to HADDOCK | BioExcel CoE | 1:07:00 | [▶](https://www.youtube.com/watch?v=PiiEyRyO07g) |
| **WeNMR lecture on information-driven docking with HADDOCK** | Alexandre Bonvin (Utrecht) | 1:38:00 | [▶](https://www.youtube.com/watch?v=InwxoiVy3QQ) |
| HADDOCK lecture, CECAM BImBS2019 | Alexandre Bonvin | 1:48:00 | [▶](https://www.youtube.com/watch?v=KUbEwGv21n8) |
| BioExcel #46: The HADDOCK 2.4 server | BioExcel CoE | 1:03:00 | [▶](https://www.youtube.com/watch?v=9dWdaJ5jBqo) |
| BioExcel #67: Introducing HADDOCK3, modular integrative pipelines | BioExcel CoE | 47:00 | [▶](https://www.youtube.com/watch?v=V7uwFbVDKFE) |
| HADDOCK3 antibody-antigen tutorial | BioExcel CoE | 1:35:00 | [▶](https://www.youtube.com/watch?v=0pLOPev3ni0) |
| BioExcel #1: Integrative modelling of complexes with HADDOCK | BioExcel CoE | 57:00 | [▶](https://www.youtube.com/watch?v=kxEidXfUUB4) |
| **BioExcel #36: Prediction of protein-protein interactions in CAPRI** | BioExcel CoE | 1:21:00 | [▶](https://www.youtube.com/watch?v=yFV8-Tbjs5w) |
| BioExcel #7: PRODIGY, predicting binding affinities in complexes | BioExcel CoE | 44:00 | [▶](https://www.youtube.com/watch?v=xYlFARWGd88) |
| Protein-Protein Docking Walkthrough | Meiler Lab | 42:00 | [▶](https://www.youtube.com/watch?v=6XV3Qnslk5Y) |
| Protein-Protein Docking | Jeffrey Gray (JHU) | 54:43 | [▶](https://www.youtube.com/watch?v=Hz7oHd1mu8k) |
| pyDock | Juan Fernández-Recio (CSIC) | 30:00 | [▶](https://www.youtube.com/watch?v=yvH8-1kg94Y) |

**Bonvin's 98-minute WeNMR lecture is the definitive statement of
information-driven docking**: the idea that ambiguous restraints from *any*
experiment — chemical shift perturbation, mutagenesis, crosslinks, coevolution —
should bias the sampling rather than filter the output. That is the conceptual
bridge from docking to Atlas family K, and the ambiguous interaction restraint is
a construction worth stealing for other problems.

The CAPRI webinar is the only honest accounting of how well any of this works on
blind targets. Watch it before trusting a docking result, including your own.

---

## M.3 Virtual screening and cheminformatics

The **Strasbourg Summer School in Chemoinformatics** is effectively a free
graduate course taught by the people who built the field.

| Title | Speaker | Length | Link |
|---|---|---|---|
| Strasbourg 2022 | Jürgen Bajorath (Bonn) | 1:24:00 | [▶](https://www.youtube.com/watch?v=eSaqHvn0f5c) |
| **Strasbourg 2024** | Alexander Tropsha (UNC) | 1:07:00 | [▶](https://www.youtube.com/watch?v=oj_kKetKUgo) |
| Strasbourg 2022 | Thierry Langer (Vienna) | 42:00 | [▶](https://www.youtube.com/watch?v=ssYDstsZKNo) |
| Strasbourg 2024 | Didier Rognan (Strasbourg) | 44:00 | [▶](https://www.youtube.com/watch?v=9dyXbom-EJs) |
| Strasbourg 2024 | Artem Cherkasov (UBC) | 40:00 | [▶](https://www.youtube.com/watch?v=eJCelzzRo14) |
| Strasbourg 2024 | Matthias Rarey (Hamburg) | 36:00 | [▶](https://www.youtube.com/watch?v=R1ss6CkELuQ) |
| Strasbourg 2022 | Connor Coley (MIT) | 43:00 | [▶](https://www.youtube.com/watch?v=x8BudRNrY2s) |
| **Chemical screening library growth: Is bigger better?** | John Irwin (UCSF) | 49:00 | [▶](https://www.youtube.com/watch?v=BecixQzoYP4) |
| Where the Rubber Hits the Road: ML on Drug Discovery Projects | Pat Walters (Relay) | 42:00 | [▶](https://www.youtube.com/watch?v=m2cbh2R9iU0) |
| Applying Active Learning in Drug Discovery | Walters & Thompson (Valence) | 52:00 | [▶](https://www.youtube.com/watch?v=QsjyKuazFlA) |
| Drug Discovery in Readily Available Chemical Space (V-SYNTHES) | Chemspace / Katritch | 1:16:00 | [▶](https://www.youtube.com/watch?v=MYITNRw3nag) |
| State of the toolkit (RDKit UGM) | Greg Landrum | 34:00 | [▶](https://www.youtube.com/watch?v=wYrlHm7dBgE) |
| Clustering, sampling and filtering ultra-large chemical databases | Roger Sayle (RDKit UGM) | 43:00 | [▶](https://www.youtube.com/watch?v=ee1UlmhKKww) |

**Tropsha is the source of modern QSAR validation discipline** — y-randomization,
applicability domain, and the fact that a good cross-validated r² is not evidence
of anything. Those are the same lessons Atlas S teaches for protein design,
learned a decade earlier in a different field and largely unread by the protein
community.

**Irwin's talk is the deliberate skeptic**: *is bigger actually better?* Watch it
before committing a cluster to a billion-compound screen. Cherkasov's Deep
Docking is the active-learning trick that makes such screens tractable — train a
surrogate on a docked subset, then triage the rest.

---

## M.4 Binding free energy in practice

| Title | Speaker | Length | Link |
|---|---|---|---|
| SAMPL6 logP virtual workshop | David Mobley (UC Irvine) | 3:00:00 | [▶](https://www.youtube.com/watch?v=FWUPXG8U3UE) |
| Free Energy Calculations to Guide Pharmaceutical Lead Optimization | David Mobley | 1:00:00 | [▶](https://www.youtube.com/watch?v=ZahfL03lujo) |
| Accurate Calculation of Protein-Ligand Binding Energies | Chris Chipot (UIUC/CNRS) | 1:40:00 | [▶](https://www.youtube.com/watch?v=_guJYDwm5mU) |
| Free Energy Calculations from Butane to COVID-19 | William Jorgensen (Yale) | 36:00 | [▶](https://www.youtube.com/watch?v=a2axeq_E3RQ) |
| **Free energies: What we've learned about how to estimate them** | Michael Shirts (Colorado) | 30:00 | [▶](https://www.youtube.com/watch?v=fhMjOYvnGcY) |
| Pushing the Boundaries of Free Energy Calculations | Lingle Wang (Schrödinger) | 35:00 | [▶](https://www.youtube.com/watch?v=zNkRZENCg-8) |
| Tight integration of FE, ML and de novo design | Robert Abel (Schrödinger) | 1:11:00 | [▶](https://www.youtube.com/watch?v=_lQQNpmcUCg) |
| Attach-pull-release for pose refinement and ligand ranking | Germano Heinzelmann (UFSC) | 30:00 | [▶](https://www.youtube.com/watch?v=LdLVM4ZbW_o) |
| Binding free energy calculations for protein-ligand systems | Vytautas Gapsys (MPI-BPC) | 52:00 | [▶](https://www.youtube.com/watch?v=hHCUW50cRuA) |
| BioExcel #63: GROMACS/pmx large-scale alchemical screening | BioExcel CoE | 54:00 | [▶](https://www.youtube.com/watch?v=hXg61gmpQw4) |
| BioExcel #4: Mutation free energy calculations with pmx | BioExcel CoE | 1:02:00 | [▶](https://www.youtube.com/watch?v=tIAzMZP8BlU) |
| Study ligand dissociation kinetics using SILCS | Wenbo Yu | 30:00 | [▶](https://www.youtube.com/watch?v=ExUA8AGCj9k) |

Lingle Wang and Robert Abel are FEP+ from inside Schrödinger, which is the only
way to see a production workflow without a licence. Gapsys and the pmx webinars
are the free, open equivalent — and BioExcel #63 is specifically the
**screening-mode, large-scale** application, which is the one relevant to ranking
a series rather than computing a single number carefully.

---

## M.5 BUILD — Atlas M

1. **Implement a simple grid-based docking scoring function** and a rigid-body
   search. Dock a ligand with a known crystal pose. Measure your RMSD.
2. **Then do the thing that matters.** Take twenty complexes with measured
   affinities. Compute your score for each. Plot score against measured ΔG. The
   correlation will be poor. **Quantify how poor, and write one page on why pose
   prediction succeeds where affinity prediction fails.**
3. **Run HADDOCK with and without an ambiguous interaction restraint** on a
   complex where you know the interface. Measure how much information the
   restraint is worth, in units of success rate.
4. **The cross-family exercise.** Compare your docking score, an MM-GBSA estimate,
   and a proper alchemical free energy for the same three ligands. Three methods,
   three numbers, increasing cost. Decide where the cost stops being worth it and
   defend the decision.

**Derivation checkpoints due: 27, 52.**

---

## M.6 Paired reading — Atlas M

| Watch this | Then read this | Hold this question |
|---|---|---|
| CCPBioSim, *AutoDock Introduction* | **Trott & Olson 2010, JCC 31:455 (Vina)** | Separate the search from the scoring. Which one limits performance? |
| **CCPBioSim, *Interpret Your Docking Scores*** | Any docking-power vs scoring-power assessment | Why do scores rank poses well and affinities badly? Write the functional-form argument. |
| Koes, *Virtual Screening on the Cheap* | Koes et al. 2013 (smina); McNutt et al. 2021 (gnina) | A CNN replaces an empirical score. What does it learn that the empirical one cannot? |
| CCPBioSim, *CrankPep* | Zhang & Forli 2019, Bioinformatics | Peptides break small-molecule docking assumptions. Name three ways. |
| **Bonvin, *Information-driven docking*** | **Dominguez, Boelens & Bonvin 2003, JACS 125:1731** | Derive the ambiguous interaction restraint. What does the effective distance do? |
| BioExcel, *CAPRI* | **Lensink & Wodak CAPRI assessment papers** | What fraction of blind targets are solved, and did AlphaFold move it? |
| Gray, *Protein-Protein Docking* | Gray et al. 2003, JMB 331:281 (RosettaDock) | Centroid then full-atom. Why two stages? |
| **Tropsha, Strasbourg 2024** | **Tropsha 2010, Mol Inform 29:476** | Apply y-randomization and applicability domain to a protein design benchmark. |
| Langer, Strasbourg 2022 | Any pharmacophore methods paper | A pharmacophore is a low-dimensional summary. What does it discard? |
| Cherkasov, Strasbourg 2024 | **Gentile et al. 2020, ACS Cent Sci 6:939 (Deep Docking)** | A surrogate triages a billion compounds. What is the recall at a given budget? |
| **Irwin, *Is bigger better?*** | **Lyu et al. 2019, Nature 566:224** | Ultra-large screening works. What is the actual hit rate, and against what baseline? |
| Walters, *Active Learning in Drug Discovery* | Any active-learning screening paper | How many oracle calls, and what acquisition function? |
| **Shirts, *Free energies*** | **Bennett 1976; Shirts & Chodera 2008 (MBAR)** | State the overlap condition. How would you detect its failure from data alone? |
| Mobley, SAMPL6 | **Mobley & Gilson 2017, Annu Rev Biophys 46:531** | Blind challenges keep the field honest. What is the design-side equivalent? |
| Gapsys / BioExcel #63 | **Gapsys et al. 2020, Chem Sci 11:1140** | Large-scale alchemy at screening throughput. What accuracy survives the speedup? |
| Heinzelmann, *Attach-pull-release* | **Boresch et al. 2003, JPCB 107:9535** | Absolute binding free energy needs restraint corrections. Derive them. |
| Abel, *FE + ML + de novo design* | Any FEP+ retrospective | Where in a design pipeline does a rigorous free energy actually change a decision? |
