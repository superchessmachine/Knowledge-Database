# Atlas K — Integrative and Hybrid Modeling

> **Problem.** You have cryo-EM at 8 Å, three crosslinks, a SAXS curve, two
> homology models and a hypothesis. Build a structure and say honestly how much
> of it you know.
>
> This is the family with the best-developed epistemology in structural biology.
> Its central question — *what did the data determine and what did the prior
> determine* — is the question every AlphaFold user should be asking and mostly
> is not.

---

## K.1 The integrative modeling platform

| Resource | What it is | Link |
|---|---|---|
| **IMP tutorials** | Sali lab's integrative modeling platform, full worked examples | [integrativemodeling.org](https://integrativemodeling.org) |
| **PDB-Dev / PDB-IHM** | The archive for integrative structures, with its own validation | [pdb-ihm.org](https://pdb-ihm.org) |
| wwPDB Integrative/Hybrid Methods task force reports | The standards documents | — |
| HADDOCK information-driven docking | → Atlas M.2 | — |

**Papers:** **Russel et al. 2012, *PLoS Biol* 10:e1001244 (Putting the pieces
together: integrative modeling platform software)** · **Alber et al. 2007,
*Nature* 450:683 (the nuclear pore complex — the landmark application)** ·
Rout & Sali 2019, *Cell* 177:1384 · **Sali et al. 2015, *Structure* 23:1156
(outcome of the first wwPDB hybrid/integrative methods task force)** ·
Schneidman-Duhovny et al. 2014, *Curr Opin Struct Biol* 28:96.

> **The nuclear pore paper is the one to study.** Thirty-plus proteins, no
> crystal structure of the assembly, and a model with explicit uncertainty
> bounds. Read how they report it: not as "the structure," but as an ensemble
> consistent with the data, with the resolution stated per region.
>
> **Derivation checkpoint 40.** Write the integrative modeling problem as
> Bayesian inference: what is the likelihood for each data type, what is the
> prior, and what does the sampled posterior mean? Then answer the hard part —
> **how would you detect that your model is determined by the prior rather than
> by the data?** The IMP answer is sampling exhaustiveness tests; make sure you
> can state why those are necessary and what they do not catch.

---

## K.1b The recorded literature, filled

The second edition had four videos in this family. Here is the rest.

### Sali, IMP, and the integrative modeling platform

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **Integrative modeling of assemblies and pathways, Lecture 1** | **Andrej Sali** (UCSF) | 1:05:24 | [▶](https://www.youtube.com/watch?v=Ty1UgvlMDCk) |
| Lecture 2 — the four-stage IMP protocol and scoring | Andrej Sali | 56:55 | [▶](https://www.youtube.com/watch?v=dxMbd_Qlh04) |
| Session 3 — sampling and validation | Andrej Sali | 18:37 | [▶](https://www.youtube.com/watch?v=CUd9t6n6TAI) |
| Session 4 — Q&A | Andrej Sali | 14:16 | [▶](https://www.youtube.com/watch?v=tyRfaqjJL4w) |
| **Faculty Research Lecture — the career retrospective, including the nuclear pore in full** | Andrej Sali | 1:32:58 | [▶](https://www.youtube.com/watch?v=nO7hfoWEJNk) |
| Why the PDB had to change its data model | Andrej Sali (PDB50) | 32:25 | [▶](https://www.youtube.com/watch?v=CRcqjuG-jGE) |
| The nuclear pore complex, visualized | Sali Lab | 5:06 | [▶](https://www.youtube.com/watch?v=ec9kuIa2GR4) |
| IMP architecture | Daniel Russel (UCSF, lead IMP author) | 8:40 | [▶](https://www.youtube.com/watch?v=T3UuWAAlxnU) |
| **PDB-IHM: deposition, curation, validation** | CCPBioSim | 41:18 | [▶](https://www.youtube.com/watch?v=MYAC8joRAoE) |
| PDB-Dev, the predecessor | BioExcel #45 | 1:02:47 | [▶](https://www.youtube.com/watch?v=D_ZllHnTL2w) |
| Depositing IHM data to the PDB | RCSB | 33:45 | [▶](https://www.youtube.com/watch?v=3Tome3TF1HM) |
| Assembline — the Kosinski-lab alternative | SBGrid | 49:22 | [▶](https://www.youtube.com/watch?v=XYkDL8Dl-2Q) |
| Integrative modeling of structure and dynamics | Dina Schneidman-Duhovny (HUJI) | 15:16 | [▶](https://www.youtube.com/watch?v=pmlg4HXOoXQ) |
| Data-driven docking and restraint quality | Ezgi Karaca (IBG Izmir) | 48:28 | [▶](https://www.youtube.com/watch?v=jmFxZDTmEBo) |
| Scoring-function construction | Riccardo Pellarin (Institut Pasteur) | 35:05 | [▶](https://www.youtube.com/watch?v=cN_VdUHDdNA) |
| Integrative modeling of complexes, Part 1 | BioExcel | 45:38 | [▶](https://www.youtube.com/watch?v=AULTBI3BqRY) |
| Integrative modeling of complexes, Part 2 | BioExcel | 43:15 | [▶](https://www.youtube.com/watch?v=qpx6bQZhWrU) |
| **Solving 3D puzzles by physics and AI-based integrative modelling** | **Alexandre Bonvin** (Utrecht) | 1:13:39 | [▶](https://www.youtube.com/watch?v=1AWPWKJQzi4) |

**Bonvin's 2026 talk is the most current here** — how AlphaFold changed, and did
not change, restraint-driven modeling. **Sali's Faculty Research Lecture is the
best single Sali talk**, because the nuclear pore work is told as a whole.

### Bayesian inference and ensemble reweighting

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **Reweighting simulations with explicit-solvent SAXS restraints** | Mattia Bernetti (SISSA) | 33:07 | [▶](https://www.youtube.com/watch?v=LME7_CT6Ig0) |
| **Molecular Simulation Meets Cryo-Electron Tomography** | **Gerhard Hummer** (MPI Biophysics) | 42:11 | [▶](https://www.youtube.com/watch?v=SOLtITFLBk8) |
| TCBG seminar — the SARS-CoV-2 glycan shield | Gerhard Hummer | 1:05:31 | [▶](https://www.youtube.com/watch?v=SJz4iCcquvk) |
| Shoot First, Ask Questions Later (ICTP colloquium) | Gerhard Hummer | 1:04:18 | [▶](https://www.youtube.com/watch?v=eDXDa7ah9Bg) |
| **Concepts of Probability in the Sciences** — why inference, not fitting | Gerhard Hummer | 38:16 | [▶](https://www.youtube.com/watch?v=ftsKVIPFDRQ) |
| **Bayesian inference of chromatin structure from Hi-C** | Simeon Carstens (Pasteur, Habeck-trained) | 1:05:42 | [▶](https://www.youtube.com/watch?v=oZj-oYPEwhA) |
| Bayesian nonparametrics for single molecule | Steve Pressé (ASU) | 27:06 | [▶](https://www.youtube.com/watch?v=rp2c7c_wgp8) |
| Bayesian inference of force fields | Open Force Field | 51:06 | [▶](https://www.youtube.com/watch?v=X-zZvgoOG1U) |
| **CASP SIG on Modeling Conformational Ensembles** | Wodak & Feig | 59:16 | [▶](https://www.youtube.com/watch?v=mkzP80YoKwM) |
| PLUMED Masterclass 22.1 part II — metainference machinery | PLUMED | 2:16:35 | [▶](https://www.youtube.com/watch?v=ZL81ZxN_eo0) |

> **Hummer's *Concepts of Probability in the Sciences* is the talk that states
> the thesis of this family directly**: structure determination is inference,
> and the output should be a posterior.
>
> **Honest gap, and it is significant.** There is **no recorded Bonomi, Habeck
> or Nilges lecture** on Bayesian structure determination, and **no BioEn talk**.
> Metainference and inferential structure determination are represented only
> indirectly, through the PLUMED masterclasses and the Carstens interview. **Read
> instead:** **Rieping, Habeck & Nilges 2005, *Science* 309:303** · **Bonomi et
> al. 2016, *Sci Adv* 2:e1501177 (metainference)** · **Hummer & Köfinger 2015,
> *JCP* 143:243150** and Köfinger et al. 2019, *JCTC* 15:3390 (BioEn) ·
> Cesari, Reißer & Bussi 2018, *Computation* 6:15 · Bottaro &
> Lindorff-Larsen 2018, *Science* 361:355.

### Fitting models into density

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **Introduction to Molecular Dynamics Flexible Fitting** | Ryan McGreevy (UIUC/TCBG) | 30:01 | [▶](https://www.youtube.com/watch?v=IrccZxgaJ_8) |
| Interactive MDFF demo | TCBG UIUC | 7:41 | [▶](https://www.youtube.com/watch?v=-KJiH_WF65s) |
| **Rosetta for CryoEM-Guided Structure Determination** (full workshop) | **Frank DiMaio** (UW) | 3:38:48 | [▶](https://www.youtube.com/watch?v=GBadIxFfcRE) |
| Cryo-EM refinement with density-guided simulations in GROMACS | BioExcel #82 | 59:01 | [▶](https://www.youtube.com/watch?v=zLYn9X5fuyQ) |
| Density guided simulations | Christian Blau (KTH) | 1:06:55 | [▶](https://www.youtube.com/watch?v=D8Cu06HVHe0) |
| **Cryo-EM densities vs stereochemistry** — the overfitting problem, short | Christian Blau (KTH) | 12:39 | [▶](https://www.youtube.com/watch?v=1Jul3KE1hoU) |
| **Validation of atomic models fitted in cryo-EM maps** | Agnel Joseph (CCP-EM) | 16:38 | [▶](https://www.youtube.com/watch?v=BFJ0ekvAE-w) |
| Recent developments in model fitting and validation (TEMPy) | Agnel Joseph (CCP-EM) | 29:56 | [▶](https://www.youtube.com/watch?v=ZW4mzOCoJDU) |
| Atomic flexible fitting — a full methods seminar | SBBf Biophysics | 1:34:40 | [▶](https://www.youtube.com/watch?v=xVKB1hP5kJc) |
| Flexible fitting into cryo-EM maps, L20 | IISER Thiruvananthapuram | 1:07:15 | [▶](https://www.youtube.com/watch?v=vV7msRgC4XI) |
| Flexible fitting into cryo-EM maps, L21 | IISER Thiruvananthapuram | 49:08 | [▶](https://www.youtube.com/watch?v=MA9sDo7bR3I) |
| Restraints in Phenix | Phenix developers | 26:28 | [▶](https://www.youtube.com/watch?v=_ZYCBUnH-5Y) |

**Blau's twelve-minute talk is the one to watch first** — it is directly about
how density pull destroys geometry if the weighting is wrong, which is
derivation checkpoint 41 in compressed form. *Note: the DiMaio workshop has
embedding disabled; it plays normally on YouTube.*

### Prediction plus sparse restraints

**Integrative structural modeling using SAXS data**, Dina Schneidman-Duhovny
(HUJI), 1:02:50 ([▶](https://www.youtube.com/watch?v=6lUCO-xXkb0)) — the
definitive SAXS-driven modeling lecture, by the author of FoXS ·
**Analyzing Flexible and Disordered Macromolecules with SAXS**, BioCAT, 44:55
([▶](https://www.youtube.com/watch?v=ABnxBq18ozo)) — the ensemble-from-SAXS
problem done carefully · Rigid-body modeling with SAXS
([▶](https://www.youtube.com/watch?v=mckbwfxc5-A)) · **Cross-linking MS from the
data-generation side**, Şule Yılmaz-Rumpf (MaxQuant Summer School), 36:24
([▶](https://www.youtube.com/watch?v=o0CpKeWfITY)) — essential, because most
modelers badly overtrust crosslink restraints · NMR-driven integrative
structural biology, Hugo van Ingen (Utrecht)
([▶](https://www.youtube.com/watch?v=693Aanfe3mw)).

**Papers:** Schneidman-Duhovny et al. 2016, *NAR* 44:W424 (FoXS/MultiFoXS) ·
Bernadó et al. 2007, *JACS* 129:5656 (EOM) · Leitner et al. 2016, *Trends
Biochem Sci* 41:20 (XL-MS) · **Stahl, Graef & Hummer 2024, *Nat Methods*
21:2224 (AlphaFold with experimental restraints)**.

> **Honest gap: HDX-guided modeling has no methods lecture** — every search
> returned vendor content. Read Bradshaw et al. 2021, *Protein Sci* 30:2300 and
> Lee et al. 2022, *Nat Methods* 19:1500.

---

## K.2 Fitting models into maps

| Topic | Resource | Link |
|---|---|---|
| Rigid and flexible fitting | ChimeraX `fitmap`; Situs; MDFF tutorials | [▶](https://www.ks.uiuc.edu/Research/mdff/) |
| **Rosetta density-guided refinement** | Frank DiMaio's work; RosettaES | → Atlas J.1 |
| Cryo-EM model building with deep learning | → Atlas J.1 | — |
| **EMReady and map post-processing** | — | — |

**Papers:** Trabuco et al. 2008, *Structure* 16:673 (**MDFF — molecular dynamics
flexible fitting**) · **DiMaio et al. 2015, *Nat Methods* 12:361 (Rosetta
density refinement)** · Wriggers 2010, *Biophys Rev* 2:21 (Situs) ·
Pintilie et al. 2010, *J Struct Biol* 170:427 (Segger).

> **The overfitting question is the whole game here.** A flexible fitting that
> drives a model into a 6 Å map will produce a model that fits the map. Whether
> it is *right* is a different question, answered by cross-validation against
> held-out data (half-maps, omitted restraints) and by checking that the
> stereochemistry did not degrade. **Derivation checkpoint 41: design the
> cross-validation for a flexible fit and state what it does not protect against.**

---

## K.3 Combining prediction with sparse experimental data

This is the most active and most design-relevant corner of Atlas K.

| Talk | Speaker / host | Length | Link |
|---|---|---|---|
| **Inverse problems with experiment-guided AlphaFold** | Vedula & Sellam, Technion (Valence) | 47:55 | [▶](https://youtu.be/0r25eXy-Bgc) |
| **Learning millisecond protein dynamics from what is missing in NMR spectra** | El Nesr & Wayment-Steele (ML4PE) | 47:43 | [▶](https://youtu.be/UM4Iff_jUXI) |
| same, longer | El Nesr (BPDMC) | 56:40 | [▶](https://youtu.be/I-utRMS84E8) |
| Exploring structural heterogeneity through cryoEM, cryoET and deep learning | Joey Davis, MIT (BPDMC) | 1:05:57 | [▶](https://youtu.be/Vrh2dNevlW4) |
| **AF3-style guidance with experimental restraints** | → Atlas K.3 | — |

**Papers:** Hummer & Köfinger 2015, *JCP* 143:243150 (**Bayesian inference of
ensembles — the correct way to combine simulation with averaged data**) ·
Bonomi et al. 2017, *Curr Opin Struct Biol* 42:106 (metainference) ·
Rieping, Habeck & Nilges 2005, *Science* 309:303 (**inferential structure
determination — the paper that made structure determination explicitly
Bayesian**) · Stevens et al. 2024 (AF2 with experimental restraints).

> **Rieping, Habeck & Nilges is the philosophical centerpiece of this family**
> and one of the best papers in structural biology. The argument: structure
> determination is inference, the output should be a posterior, and the
> single-structure convention is a lossy summary we adopted for historical
> reasons. Everything in Atlas J and Atlas P is downstream of whether you accept
> that.
>
> **The design-relevant version of the same point.** When you guide AlphaFold
> with a restraint — a crosslink, a known contact, a steric constraint — you are
> doing integrative modeling with a learned prior. The question Hummer and
> Köfinger answer for simulation is exactly the question nobody has answered for
> AF-style models: *what is the correct way to combine a learned prior with
> averaged experimental data without double-counting?* **That is Capstone V.**

---

## K.4 Paired reading — Atlas K

| Watch this | Then read this | Hold this question |
|---|---|---|
| IMP tutorials | **Russel et al. 2012, *PLoS Biol* 10:e1001244** | Write the problem as Bayesian inference. Name every likelihood. |
| — | **Alber et al. 2007, *Nature* 450:683** | How is per-region uncertainty reported, and why does that matter? |
| PDB-IHM validation docs | **Sali et al. 2015, *Structure* 23:1156** | What does "validated" mean for a model with no single right answer? |
| MDFF tutorials | Trabuco et al. 2008, *Structure* 16:673 | Design the cross-validation for a flexible fit. |
| DiMaio talks (Atlas J) | **DiMaio et al. 2015, *Nat Methods* 12:361** | When does density refinement improve a model and when does it bake in error? |
| Vedula & Sellam, *Experiment-guided AF* | Their paper + **Rieping et al. 2005, *Science* 309:303** | A learned prior plus sparse data. Where is the double-counting? |
| El Nesr & Wayment-Steele, *NMR* | **Hummer & Köfinger 2015, *JCP* 143:243150** | Averaged data, ensemble answer. What is the maximum-entropy argument? |
| Davis, *cryoEM heterogeneity* | Bonomi et al. 2017, *Curr Opin Struct Biol* 42:106 | One map or many states? What decides? |
