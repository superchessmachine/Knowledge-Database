# Atlas R — Generative Design

> **Problem.** Produce a molecule that does not yet exist and that does
> something. This is the destination family, and it is the one where the three
> cultures of Section 0.2 are most visibly in tension, because here the ground
> truth is unambiguous: the protein works in the tube or it does not.
>
> That clarity makes practitioners unusually candid about failure rates.
> **Listen for the numbers.** When a speaker says a campaign had a 1% success
> rate, that is the most informative sentence in the talk and it will almost
> never be on a slide.

Every entry is a talk paired with its paper. Where no talk exists — and there
are nine such methods — the paper is given alone, because the gap is itself
information about which groups give seminars.

---

## R.1 Inverse folding and sequence design

| Method | Talk | Speaker / host | Length | Link |
|---|---|---|---|---|
| **ProteinMPNN** | Robust deep learning based protein sequence design using ProteinMPNN | Justas Dauparas (ML4PE) | 53:42 | [▶](https://www.youtube.com/watch?v=aVQQuoToTJA) |
| ProteinMPNN | Sequence Design with ProteinMPNN (hands-on) | RosettaCommons | 33:41 | [▶](https://www.youtube.com/watch?v=zbpWFKjiXEk) |
| ProteinMPNN | MPNN: ML for protein sequence design | RosettaCommons | 25:31 | [▶](https://www.youtube.com/watch?v=6z4XmUAwdNA) |
| ProteinMPNN | Inverse folding using ProteinMPNN | RosettaCommons | 29:56 | [▶](https://www.youtube.com/watch?v=o8JWPjSH1Ig) |
| LigandMPNN | Sequence Design with LigandMPNN | RosettaCommons | 17:39 | [▶](https://www.youtube.com/watch?v=5drpdgMtwu4) |
| ESM-IF | Adapting protein language models for structure-conditioned design | ML4PE | 55:47 | [▶](https://www.youtube.com/watch?v=MkwM3t80XpQ) |
| ThermoMPNN | ThermoMPNN Tutorial: Finding Stabilizing Protein Mutations | RosettaCommons | 42:39 | [▶](https://www.youtube.com/watch?v=vtusNLxgxTg) |
| Stability at scale | **Mega-scale experimental analysis of protein folding stability** | ML4PE | 50:57 | [▶](https://www.youtube.com/watch?v=M3fARv8GYA8) |
| Stability | Early Career Seminar #7 | Gabe Rocklin (ML4PE) | 1:00:26 | [▶](https://www.youtube.com/watch?v=Hge5FHsC_h4) |
| Stability + aggregation | Predicting folding stability and aggregation from large-scale experiments | BPDMC | 1:00:30 | [▶](https://www.youtube.com/watch?v=KKXe8a_h88c) |
| Rosetta fixbb | Sequence Design Introduction | RosettaCommons | 13:46 | [▶](https://www.youtube.com/watch?v=a975ZPy4tdw) |
| — | Computational Protein Design Then & Now (1988–2024) | Baker, DeGrado, Mayo, Kuhlman (IPD) | 59:50 | [▶](https://www.youtube.com/watch?v=BuJGTn7OhxQ) |
| Ensemble-conditioned | Ensemble-conditioned protein sequence design with Caliby | ML4PE | 34:00 | [▶](https://www.youtube.com/watch?v=_9xOtXiZbGM) |

**Papers:** **Dauparas et al. 2022, *Science* 378:49 (ProteinMPNN) [landmark]** ·
Dauparas et al. 2025, *Nat Methods* 22:717 (LigandMPNN) · Hsu et al. 2022, ICML
(ESM-IF) · Dieckhaus et al. 2024, *PNAS* 121:e2314853121 (ThermoMPNN) ·
**Tsuboyama et al. 2023, *Nature* 620:434 [landmark]** · Kuhlman & Baker 2000,
*PNAS* 97:10383 · Kuhlman et al. 2003, *Science* 302:1364 (Top7).

### The metric critique — watch immediately after Dauparas

| Talk | Host | Length | Link |
|---|---|---|---|
| **Protein sequence design by explicit energy landscape optimization** | BPDMC | 1:30:36 | [▶](https://www.youtube.com/watch?v=3iH9n6iAwVc) |
| **Beyond sequence recovery: improved modeling of the sequence-energy landscape** | BPDMC | 33:23 | [▶](https://www.youtube.com/watch?v=w-NddBw2FJk) |

> Sequence recovery — how often the model reproduces the native residue — is the
> headline metric for inverse folding, and these two talks argue it is the wrong
> objective. **That is derivation checkpoint 61 argued in public.** Maximizing
> the likelihood of a sequence given a backbone is not the same as maximizing the
> probability that the sequence folds to that backbone.

*No talk exists for ProteinSolver (Strokach et al. 2020, *Cell Systems* 11:402),
PiFold (Gao et al. 2023, ICLR), or ProstT5 (Heinzinger et al. 2024, *NARGAB*
6:lqae150).*

---

## R.2 Backbone generation

| Method | Talk | Speaker / host | Length | Link |
|---|---|---|---|---|
| **RFdiffusion** | Accurate protein design using structure prediction and diffusion | Watson & Juergens (ML4PE) | 43:52 | [▶](https://www.youtube.com/watch?v=wIHwHDt2NoI) |
| **RFdiffusion** | **Molecular ML Reading Group: RFdiffusion (critique)** | MaomLab, Michigan | 1:00:21 | [▶](https://www.youtube.com/watch?v=agiHi6hOE3Q) |
| RFdiffusion | Backbone Generation with RFdiffusion (hands-on) | RosettaCommons | 25:35 | [▶](https://www.youtube.com/watch?v=gYJLw40UojU) |
| RFdiffusion | Fundamentals of protein binder design with RFdiffusion | RosettaCommons | 20:32 | [▶](https://www.youtube.com/watch?v=6imf4vFmtbo) |
| RFdiffusion-AA | Backbone Generation with RFdiffusion All-Atom | RosettaCommons | 13:41 | [▶](https://www.youtube.com/watch?v=2FHNM6USHw0) |
| RFAA | Generalized Biomolecular Modeling and Design with RFAA | Rohith Krishna (Valence) | 1:04:54 | [▶](https://www.youtube.com/watch?v=LAQ4-E0Cd8Q) |
| **RFdiffusion2** | Atom level enzyme active site scaffolding | Ahern & Yim (ML4PE) | 51:56 | [▶](https://www.youtube.com/watch?v=F7dcrWKaHrs) |
| RFdiffusion2 | long form | Yim & Ahern (Valence) | 1:12:41 | [▶](https://www.youtube.com/watch?v=bd6bFXRmEGA) |
| **RFdiffusion3** | De novo Design of All-atom Biomolecular Interactions | ML4PE | 48:07 | [▶](https://www.youtube.com/watch?v=0JyPWQ1FBow) |
| RFdiffusion3 | Protein Binder Design with RFdiffusion3 | RosettaCommons | 30:59 | [▶](https://www.youtube.com/watch?v=LVN2l587C3M) |
| RFdiffusion3 | Simple Motif Scaffolding Guided Tutorial | RosettaCommons | 10:21 | [▶](https://www.youtube.com/watch?v=bFSW4x96vEk) |
| **Chroma** | Illuminating protein space with a programmable generative model | Grigoryan & Costello (Proxima) | 1:03:38 | [▶](https://www.youtube.com/watch?v=yIt8vgfGyog) |
| FrameDiff | Diffusion probabilistic modelling of protein backbones in 3D | Yim & Trippe (Valence) | 1:02:39 | [▶](https://www.youtube.com/watch?v=UymQ-iE23MY) |
| FrameFlow | Sequence-Augmented SE(3)-Flow Matching | ML4PE | 48:47 | [▶](https://www.youtube.com/watch?v=xgA8T9h8mm0) |
| FoldFlow | SE(3)-Stochastic Flow Matching for Protein Backbone Generation | Bose & Tong (Proxima) | 58:53 | [▶](https://www.youtube.com/watch?v=t1Pqdl6RB2I) |
| FoldFlow-2 | Flow Matching For Protein Backbone Generation | Huguet & Vuckovic (Proxima) | 1:00:30 | [▶](https://www.youtube.com/watch?v=ATYtM_by0w0) |
| Genie 2 | Designing and Scaffolding Proteins at the Scale of the Structural Universe | ML4PE | 53:11 | [▶](https://www.youtube.com/watch?v=jYMkxHD4-34) |
| ProtDiff / SMCDiff | Diffusion modeling of backbones for motif-scaffolding | ML4PE | 1:03:59 | [▶](https://www.youtube.com/watch?v=f4hhZYeAgPU) |
| — | Framework for conditional diffusion models in motif scaffolding | ML4PE | 1:01:57 | [▶](https://www.youtube.com/watch?v=GrtWwD8pPWY) |
| — | Protein Structure and Sequence Generation with Equivariant DDPMs | ML4PE | 55:19 | [▶](https://www.youtube.com/watch?v=i8fGzddGbU8) |
| Protpardelle | ML in Drug Discovery Symposium 2023 | Possu Huang (Broad) | 21:48 | [▶](https://www.youtube.com/watch?v=zdF86-TfkY0) |
| **ProteinGenerator** | Multistate and functional design using sequence space diffusion | Gershon, Lisanza & Tipps (ML4PE) | 54:47 | [▶](https://www.youtube.com/watch?v=hbkDL_vxGKE) |
| ProteinGenerator | alternate venue | Computational Intelligence Group | 58:46 | [▶](https://www.youtube.com/watch?v=2LnJFJGKS7E) |
| Multiflow | Protein structure and sequence co-generation | Yim & Campbell (Valence) | 54:54 | [▶](https://www.youtube.com/watch?v=yzc29vhM2Aw) |
| Multiflow | Generative Flows on Discrete State-Spaces (theory) | Campbell & Yim (Proxima) | 52:12 | [▶](https://www.youtube.com/watch?v=-L9ekyTI21k) |
| Proteina | Scaling Flow-based Protein Structure Generative Models | ML4PE | 1:09:24 | [▶](https://www.youtube.com/watch?v=Y2dRj9_ZEHw) |
| Proteina | first authors | Kreis & Geffner (Proxima) | 1:02:02 | [▶](https://www.youtube.com/watch?v=-Qlc4dNj4e8) |
| La-Proteina | Atomistic Protein Generation via Partially Latent Flow Matching | ML4PE | 1:05:13 | [▶](https://www.youtube.com/watch?v=kA6-x5CpJIU) |
| — | Programming Biomolecular Interactions with All-Atom Generative Model | ML4PE | 54:24 | [▶](https://www.youtube.com/watch?v=P5rUgHrLpt4) |
| EvoDiff | **Protein generation with evolutionary diffusion: sequence is all you need** | ML4PE | 59:46 | [▶](https://www.youtube.com/watch?v=e1e-_SkyNjw) |
| — | Discrete diffusion models for generative protein design | BPDMC | 1:00:13 | [▶](https://www.youtube.com/watch?v=iV_7mgxe4OI) |
| Symmetric design | RFdiffusion for Symmetric Applications | RosettaCommons | 23:09 | [▶](https://www.youtube.com/watch?v=etV20qEpXrk) |
| Nanoparticles | ML-based design of nanoparticle vaccines | Neil King (AI Proteins) | 53:20 | [▶](https://www.youtube.com/watch?v=OPRMfRnlx1k) |
| Survey | Diffusion models for protein structure generation and design | RosettaCommons | 44:43 | [▶](https://www.youtube.com/watch?v=OEnY2yA3jy8) |
| Survey | Recent methods for protein structure generation and design | BPDMC | 1:21:22 | [▶](https://www.youtube.com/watch?v=smjYJSudwr0) |
| **Benchmark critique** | **MotifBench: a standardized benchmark for motif-scaffolding** | ML4PE | 54:48 | [▶](https://www.youtube.com/watch?v=YLIBvA1dsQ4) |

**Papers:** **Watson et al. 2023, *Nature* 620:1089 (RFdiffusion) [landmark]** ·
Krishna et al. 2024, *Science* 384:eadl2528 (RFAA) · Ahern et al. 2026,
*Nat Methods* 23:96 (RFdiffusion2) · Butcher et al. 2025, bioRxiv (RFdiffusion3,
preprint) · **Ingraham et al. 2023, *Nature* 623:1070 (Chroma)** · Yim et al.
2023, ICML (FrameDiff) · Bose et al. 2024, ICLR (FoldFlow) · Lin & AlQuraishi
2023, ICML; Lin et al. 2024, arXiv (Genie) · Trippe et al. 2023, ICLR
(SMCDiff) · Chu et al. 2024, *PNAS* 121:e2311500121 (Protpardelle) ·
Lisanza et al. 2025, *Nat Biotechnol* 43:1288 · Campbell et al. 2024, ICML
(Multiflow) · Geffner et al. 2025, arXiv (La-Proteina) · Fallas et al. 2017,
*Nat Chem* 9:353 · Bale et al. 2016, *Science* 353:389; Walls et al. 2020,
*Cell* 183:1367.

> **Watch the RFdiffusion first-author talk and the Michigan critique back to
> back, in one sitting.** The gap between how authors present a method and how a
> sharp external group reads it is the single most useful calibration available,
> and it is rarely this cleanly paired.

*No talk exists for ProteinSGM (Lee et al. 2023, *Nat Comput Sci* 3:382).*

---

## R.3 Hallucination and inverting predictors

| Method | Talk | Speaker / host | Length | Link |
|---|---|---|---|---|
| **Hallucination** | Inverting protein structure prediction models to solve problems in biology | Sergey Ovchinnikov | ~1 hr | [▶](https://www.youtube.com/watch?v=kNDdAWy7sRk) |
| AfDesign / ColabDesign | Tutorial on using structure prediction methods for protein design | Ovchinnikov & Jue Wang (BPDMC) | 2:04:03 | [▶](https://www.youtube.com/watch?v=2HmXwlKWMVs) |
| Motif scaffolding | Scaffolding protein functional sites using deep learning | Tischer & Juergens (ML4PE) | 52:05 | [▶](https://youtu.be/-EJ8SXTBin0) |
| Classical grafting | Motif Grafting and Scaffolding using Rosetta | Meiler Lab | 16:59 | [▶](https://www.youtube.com/watch?v=_H3XfzGGJGI) |
| Classical grafting | Motif Grafting walkthrough | Meiler Lab | 1:05:34 | [▶](https://www.youtube.com/watch?v=vmY37lrdnGk) |
| **BindCraft** | One-shot design of functional protein binders | Valence Labs | 1:36:09 | [▶](https://www.youtube.com/watch?v=u5yijcBsonw) |
| BindCraft | second account | BPDMC | 1:15:23 | [▶](https://www.youtube.com/watch?v=qQihl6If9vU) |
| BoltzDesign1 | BoltzDesign and Protein Hunter: Inverting Structure Prediction Models | ML4PE | 48:46 | [▶](https://www.youtube.com/watch?v=vMfRRRqVBFE) |
| BoltzDesign1 | How AF3-style models can be used for design | BPDMC | 1:10:35 | [▶](https://www.youtube.com/watch?v=yCOlC_yj4kc) |
| Protein Hunter | Exploiting structure hallucination within diffusion | Yehlin Cho (Valence) | 1:14:12 | [▶](https://www.youtube.com/watch?v=GC5ouLbJ93E) |

**Papers:** **Anishchenko et al. 2021, *Nature* 600:547 (hallucination)** ·
Wang et al. 2022, *Science* 377:387 (motif scaffolding — note Wang is first
author, not Tischer) · **Pacesa et al. 2025, *Nature* 646:483 (BindCraft)** ·
Cho et al. 2025, bioRxiv (BoltzDesign1, preprint) · Goverde et al. 2023,
*Protein Sci* 32:e4653.

> **A citation lesson worth teaching.** AfDesign has no paper of its own. The
> BindCraft *Nature* paper, which is built on AfDesign, does not cite ColabDesign
> at all — it cites Anishchenko and Goverde instead. Cite the software through
> Zenodo (doi:10.5281/zenodo.13309080). How a field handles uncited
> infrastructure is a real thing to have an opinion about, and this is a clean
> case to form one on.

*No talk exists for BoltzGen (Stark et al. 2025, bioRxiv) or PocketGen (Zhang et
al. 2024, *Nat Mach Intell* 6:1382).*

---

## R.4 Binder design — and the honest hit rates

| Method | Talk | Speaker / host | Length | Link |
|---|---|---|---|---|
| Minibinders, pre-DL | Learning to design mini-proteins that bind specific targets | BPDMC | 1:12:12 | [▶](https://www.youtube.com/watch?v=JpLFhnVARVw) |
| Target-agnostic binders | Binder Design Methods Overview | RosettaCommons | 8:08 | [▶](https://www.youtube.com/watch?v=fRhhrfsszOU) |
| DL-improved binders | Fundamentals of protein binder design with RFdiffusion | RosettaCommons | 20:32 | [▶](https://www.youtube.com/watch?v=6imf4vFmtbo) |
| GPCR binders | De novo design of miniprotein agonists and antagonists for family B GPCRs | BPDMC | 51:20 | [▶](https://www.youtube.com/watch?v=T4b9YuMhchg) |
| Helical-peptide binders | De novo design of high-affinity binders of bioactive helical peptides | Vázquez Torres (Valence) | 37:28 | [▶](https://www.youtube.com/watch?v=_IxJBt-Ym9g) |
| **Adaptyv competition** | **Optimizing Cetuximab: Winning Adaptyv's Protein Design Competition** | Cradle | 53:53 | [▶](https://www.youtube.com/watch?v=6MwToW57YzQ) |
| Scaling + test-time compute | Scaling Atomistic Protein Binder Design | ML4PE | 55:28 | [▶](https://www.youtube.com/watch?v=DaOlUqlVxik) |
| — | long form | NVIDIA (Valence) | 1:38:57 | [▶](https://www.youtube.com/watch?v=-XNMSnFUPjk) |
| Neosurfaces | Targeting protein–ligand neosurfaces with a generalizable DL tool | Anthony Marchand (Valence) | 1:11:03 | [▶](https://www.youtube.com/watch?v=eZEG3e6pRSk) |
| Neosurfaces | ML4PE account | ML4PE | 52:30 | [▶](https://www.youtube.com/watch?v=setIzkcEAVs) |
| Drug-binding proteins | Zero-shot design via neural iterative selection-expansion | ML4PE | 36:24 | [▶](https://www.youtube.com/watch?v=BdILCc45TS8) |
| Therapeutic application | De novo design of miniprotein-based NK cell engagers | BPDMC | 59:56 | [▶](https://www.youtube.com/watch?v=e6oZgGWjD_0) |
| Production pipeline | BinderFlow: batch-based binder design with live monitoring | RosettaCommons | 16:23 | [▶](https://www.youtube.com/watch?v=AvBVGrBfaX0) |

### The three corrective talks

| Talk | Host | Length | Link |
|---|---|---|---|
| **Why designs fail, and how they move** | BPDMC | 1:09:30 | [▶](https://www.youtube.com/watch?v=eVRZjE3A5aQ) |
| **Creativity at Scale: Problem Formulation as the Frontier of Protein Design** | BPDMC | 1:29:26 | [▶](https://www.youtube.com/watch?v=rSfSWc9wdDg) |
| Protein design roundtable: real challenges and practical solutions | RosettaCommons | 23:55 | [▶](https://www.youtube.com/watch?v=9pQeQKXhS70) |

**Papers:** **Chevalier et al. 2017, *Nature* 550:74** · **Cao et al. 2022,
*Nature* 605:551** · Bennett et al. 2023, *Nat Commun* 14:2625 · Muratspahić
et al. 2026, *Nature* 656:1044 · Vázquez Torres et al. 2024, *Nature* 626:435 ·
**Cotet et al. 2025, bioRxiv (Adaptyv EGFR competition)**.

> **"Why designs fail, and how they move" is the single best corrective to
> published hit rates in this entire Atlas.** Watch it immediately after any
> advocacy talk in this subsection. The Adaptyv competition talk is the other
> half: a real campaign scored against a *public wet-lab benchmark*, which is the
> closest thing design has to CASP — and a standing argument for why Capstone VII
> matters.

*No talk exists for AlphaProteo (Zambaldi et al. 2024, arXiv:2409.08022).*

---

## R.5 Enzyme design — the field's most honest corner

| Method | Talk | Speaker / host | Length | Link |
|---|---|---|---|---|
| **Serine hydrolases** | **Computational design of serine hydrolases** | Lauko & Pellock (ML4PE) | 41:14 | [▶](https://www.youtube.com/watch?v=wdbDo9FQ4ns) |
| Overview | AI-driven de novo Enzyme Design | ML4PE | 35:36 | [▶](https://www.youtube.com/watch?v=dtYDfaNK7z8) |
| RFdiffusion3 enzymes | Enzyme design with RFdiffusion3 | RosettaCommons | 12:47 | [▶](https://www.youtube.com/watch?v=htA3HSXCkro) |
| Classical de novo enzymes | Computational Protein Design Then & Now | IPD panel | 59:50 | [▶](https://www.youtube.com/watch?v=BuJGTn7OhxQ) |
| PROSS / FuncLib | Designing COVID-19 Countermeasures | Sarel Fleishman (Weizmann) | 1:03:00 | [▶](https://www.youtube.com/watch?v=FsJUnABT01M) |
| Metalloenzymes | Zero-shot design of a de novo metalloenzyme | ML4PE | 51:08 | [▶](https://www.youtube.com/watch?v=F8ZrkFfFWcM) |
| Generative enzymes | Therapeutic enzyme engineering using a generative neural network | BPDMC | 1:18:46 | [▶](https://www.youtube.com/watch?v=9zm_WEHOSYg) |
| Parallel design | Massively Parallel Protein Design for Next-Generation Chemotherapy | BPDMC | 1:02:51 | [▶](https://www.youtube.com/watch?v=naNpjhRDq0o) |
| Design + screening | Engineering nuclease enzymes by ML and high-throughput screening | ML4PE | 58:00 | [▶](https://www.youtube.com/watch?v=eGNERw_nKQM) |
| Design + evolution | **AI-redesigned starting points enhance protein evolution** | Nicholas Krasnow (ML4PE) | 53:07 | [▶](https://www.youtube.com/watch?v=ViPPdY93XYw) |

**Papers:** **Lauko, Pellock et al. 2025, *Science* 388:eadu2454 [landmark]** ·
Ahern et al. 2026, *Nat Methods* 23:96 · Röthlisberger et al. 2008, *Nature*
453:190 (Kemp eliminase) · Jiang et al. 2008, *Science* 319:1387 (retro-aldol) ·
Siegel et al. 2010, *Science* 329:309 (Diels-Alderase) · Goldenzweig et al. 2016,
*Mol Cell* 63:337 (PROSS) · Khersonsky et al. 2018, *Mol Cell* 72:178 (FuncLib) ·
El Nesr et al. 2026, bioRxiv; Kim et al. 2026, *Nature* 649:246.

> **The essential pairing.** Assign the classical de novo enzyme papers
> alongside **Blomberg et al. 2013, *Nature* 503:418**, which showed that in the
> most celebrated case the catalysis came from *directed evolution*, not from the
> design. There is no talk for that paper, which is itself telling. It is the
> most important negative result in this family and the reason enzyme design
> remains the honest corner of the field.
>
> *Note on attribution: the zero-shot metalloenzyme work is Possu Huang's lab at
> Stanford with Röthlisberger at EPFL — not Baker.*

*No talk exists for theozyme/RosettaMatch (Zanghellini et al. 2006,
*Protein Sci* 15:2785; Richter et al. 2011, *PLoS ONE* 6:e19230).*

---

## R.6 Peptides and macrocycles

| Method | Talk | Speaker / host | Length | Link |
|---|---|---|---|---|
| AfCycDesign | Cyclic peptide structure prediction and design using AlphaFold | Rettie (ML4PE) | 1:07:20 | [▶](https://www.youtube.com/watch?v=SDxy5E8fvXY) |
| **RFpeptides** | Deep Learning Enabled Design of Functional Cyclic Peptides | Peptide Drug Hunting Consortium | 23:02 | [▶](https://www.youtube.com/watch?v=c5NowYLkFoI) |
| Hyperstable peptides | A computational approach to design structured peptides | BPDMC | 52:16 | [▶](https://www.youtube.com/watch?v=IPsQH62cJ8g) |
| Tertiary motifs | Tertiary motifs as building blocks for protein-binding peptides | BPDMC | 1:03:00 | [▶](https://www.youtube.com/watch?v=kiKIj4gGY7o) |
| Fragment-based | Fragment-based backbone sampling and NN potentials for peptide design | BPDMC | 1:19:48 | [▶](https://www.youtube.com/watch?v=CZn8BdvRYJU) |
| Experimental | Massively parallel discovery of peptides to inhibit protein interactions | BPDMC | 1:12:44 | [▶](https://www.youtube.com/watch?v=s31yC7nQqDs) |
| PepTune | Multi-Objective-Guided Discrete Diffusion for therapeutic peptides | Valence Labs | 1:12:13 | [▶](https://www.youtube.com/watch?v=KVr8ryclwdA) |
| Sequence-only | Structure-Independent Peptide Binder Design via Generative LMs | Pranam Chatterjee (Valence) | 1:00:55 | [▶](https://www.youtube.com/watch?v=Mt6VMDG8NUA) |
| **Critical** | Interpreting structure predictors for protein-peptide complexes | BPDMC | 58:12 | [▶](https://www.youtube.com/watch?v=R87pmoB3QF0) |

**Papers:** Rettie et al. 2025, *Nat Commun* 16:4730 (AfCycDesign) ·
**Rettie et al. 2025, *Nat Chem Biol* 21:1948 (RFpeptides)** · **Bhardwaj et al.
2016, *Nature* 538:329** · Hosseinzadeh et al. **2017**, *Science* 358:1461
(not 2018) · Renfrew et al. 2012, *PLoS ONE* 7:e32637 (non-canonical amino acids
in Rosetta) · Mandal et al. 2012, *PNAS* 109:14779 (D-protein, mirror-image).

**This is the subsection that matters most for macrocycle work.** The Renfrew and Mandal
papers have no talks, and they are exactly the two you need for D-residue and
non-canonical design — which is precisely what cyclic-peptide pipelines rely on.

---

## R.7 Antibodies and TCRs

| Method | Talk | Speaker / host | Length | Link |
|---|---|---|---|---|
| **Germinal** | Efficient generation of epitope-targeted de novo antibodies | ML4PE | 57:35 | [▶](https://www.youtube.com/watch?v=wJjSCtZTsX8) |
| Germinal | long form | Valence Labs | 1:09:18 | [▶](https://www.youtube.com/watch?v=wulNIgwXf8c) |
| IgFold / IgLM / AntiBERTy | Designing proteins with language models | Jeff Ruffolo (ML@Berkeley) | 1:16:16 | [▶](https://www.youtube.com/watch?v=8cPv9yAcNpo) |
| ABlooper / ABodyBuilder | Building the toolkit for computational antibody design | Charlotte Deane (AIRR) | 34:53 | [▶](https://www.youtube.com/watch?v=UdFevIESn9I) |
| AF-Multimer for antibodies | Computational design of antibody repertoires | BPDMC | 1:10:02 | [▶](https://www.youtube.com/watch?v=cQu6yUZINgo) |
| Experimental scale | mBER: controllable de novo antibody design with million-scale screening | BPDMC | 1:42:10 | [▶](https://www.youtube.com/watch?v=u9dznMvcDs4) |
| AbDiffuser | Full-Atom Generation of In Vitro Functioning Antibodies | ML4PE | 1:10:25 | [▶](https://www.youtube.com/watch?v=95w0Ht3m0JY) |
| Seq-structure co-design | Iterative Refinement GNN for Antibody Co-design | Wengong Jin (Valence) | 1:27:05 | [▶](https://www.youtube.com/watch?v=gcf5HiwLW2U) |
| — | Structured Refinement Network for Antibody Design | Wengong Jin (Valence) | 58:36 | [▶](https://www.youtube.com/watch?v=uDTccbg_Ai4) |
| Bayesian flow networks | Flexible Antibody Design with Multimodal Bayesian Flow Networks | ML4PE | 44:20 | [▶](https://www.youtube.com/watch?v=h9xZFRPDfk8) |
| Classical | RosettaAntibodyDesign (RAbD) walkthrough | Meiler Lab | 1:14:42 | [▶](https://www.youtube.com/watch?v=XeJ0SBLU9v0) |
| Classical | RosettaAntibody Introduction | Meiler Lab | 12:41 | [▶](https://www.youtube.com/watch?v=hxCMaHnb8qE) |
| Primer | Introduction to Antibody Structural Biology | Meiler Lab | 18:25 | [▶](https://www.youtube.com/watch?v=rrukxu0ZGu4) |
| **Critical** | **FLAb2: How Well Can Protein AI Predict Developability?** | RosettaCommons | 31:46 | [▶](https://www.youtube.com/watch?v=Ib9dVOCy3j4) |
| TCR | A structure-informed DL framework for TCR-peptide-HLA interactions | Broad Institute | 14:08 | [▶](https://www.youtube.com/watch?v=QAc90lI1AX4) |
| CAR design | Determinants of efficacious de novo chimeric antigen receptors | ML4PE | 46:34 | [▶](https://www.youtube.com/watch?v=qB7BJAj7jm0) |

**Papers:** Mille-Fragoso et al. 2026, *Nat Biotechnol* (Germinal) ·
**Bennett et al. 2026, *Nature* 649:183 (RFantibody)** · Ruffolo et al. 2023,
*Nat Commun* 14:2389 (IgFold) · Shuai et al. 2023, *Cell Systems* 14:979
(IgLM) · Abanades et al. 2023, *Commun Biol* 6:575 (ImmuneBuilder) ·
**Bradley 2023, *eLife* 12:e82813 (TCRdock)** · Yin et al. 2023, *NAR*
51:W569 (TCRmodel2) · Olsen et al. 2022, *Bioinform Adv* 2:vbac046 (AbLang).

**FLAb2 is the antibody equivalent of PoseBusters** — it asks whether these
models predict developability, which is what actually determines whether an
antibody becomes a drug. Watch it after any antibody design advocacy talk.

**No first-author talk exists for TCRdock or TCRmodel2**, despite TCR-pMHC being
directly relevant to any TCR-pMHC modelling work. Read Bradley 2023.

---

## R.8 Function, dynamics and the hard design problems

| Method | Talk | Speaker / host | Length | Link |
|---|---|---|---|---|
| Multistate design | Multistate and functional design via sequence space diffusion | ML4PE | 54:47 | [▶](https://www.youtube.com/watch?v=hbkDL_vxGKE) |
| **Conformational switches** | De novo design of small-molecule-induced conformational change | BPDMC | 1:03:21 | [▶](https://www.youtube.com/watch?v=q3Xn2-TIZEo) |
| Conformational bias | Computational design of conformation-biasing mutations | ML4PE | 51:45 | [▶](https://www.youtube.com/watch?v=5a9PC5yOqnc) |
| De novo luciferase | The Coming of Age of De Novo Protein Design | David Baker (NIH) | 54:33 | [▶](https://www.youtube.com/watch?v=oO-uR_3fL1g) |
| Small-molecule binders | Designing ligand-binding proteins from scratch | BPDMC | 1:18:23 | [▶](https://www.youtube.com/watch?v=ogDxIN0ttZo) |
| Small-molecule binders | Design of small molecule binding proteins using deep learning | BPDMC | 1:00:53 | [▶](https://www.youtube.com/watch?v=IgFgAYQrke4) |
| Channels and transporters | De Novo Designed Voltage-gated Anion Channels Suppress Neuron Firing | Chen Zhou (ML4PE) | 28:49 | [▶](https://www.youtube.com/watch?v=ypZxGTefgSc) |
| Proteolysis-gated | Autoinhibitory domains for a protease-activated PD-L1 antagonist | BPDMC | 1:11:19 | [▶](https://www.youtube.com/watch?v=ojuJ9MomfQQ) |
| Protease substrates | Deep learning guided design of protease substrates | ML4PE | 52:49 | [▶](https://youtu.be/-3yH6hR58io) |
| Glycoproteins | De novo Glycan Modeling and Design | BPDMC | 1:10:06 | [▶](https://www.youtube.com/watch?v=ZtMw1MJyRdI) |
| Cell engineering | Designer proteins for stem cell engineering | BPDMC | 1:18:23 | [▶](https://www.youtube.com/watch?v=2uzfyVjMu5o) |
| Therapeutic | Designing cKIT Receptor Inhibitors for Bone Marrow Transplant | BPDMC | 27:16 | [▶](https://www.youtube.com/watch?v=0PxJuKR9WCI) |

**Papers:** **Praetorius et al. 2023, *Science* 381:754 (two-state hinges)** ·
Boyken et al. 2019, *Science* 364:658 · **Langan et al. 2019, *Nature* 572:205
(LOCKR)** · **Glasgow et al. 2019, *Science* 366:1024 (Kortemme biosensor)** ·
Yeh et al. 2023, *Nature* 614:774 (luciferase) · Polizzi & DeGrado 2020,
*Science* 369:1227 · An et al. 2024, *Science* 385:276 · Xu et al. 2020,
*Nature* 585:129 (transmembrane pores) · Lu et al. 2018, *Science* 359:1042
(multipass membrane proteins) · Ambroggio & Kuhlman 2006, *JACS* 128:1154 ·
Leaver-Fay et al. 2011, *PLoS ONE* 6:e20937 (multistate).

> **The Kortemme biosensor paper and LOCKR both lack talks**, and they are the
> two clearest examples of *designing a function that requires motion*. That
> gap is the same one Atlas family R has throughout: nearly every method here
> generates a single static backbone, which is exactly what Section A.4 row five
> says is unexchanged.

---

## R.9 Protein-nucleic acid and co-design

| Method | Talk | Host | Length | Link |
|---|---|---|---|---|
| RNA and nucleoprotein design | RNA Function, Design, and Modeling | BPDMC | 59:33 | [▶](https://www.youtube.com/watch?v=oS_Cb-YMymw) |
| Protein-ligand co-design | Generalized Biomolecular Modeling and Design with RFAA | Rohith Krishna (Valence) | 1:04:54 | [▶](https://www.youtube.com/watch?v=LAQ4-E0Cd8Q) |
| Infrastructure | Accelerating Biomolecular Modeling with AtomWorks and RF3 | ML4PE | 51:17 | [▶](https://www.youtube.com/watch?v=ux6TxDO3GSY) |
| Infrastructure | first author | Nathaniel Corley (Valence) | 52:10 | [▶](https://www.youtube.com/watch?v=Jyv7a1LhBwE) |

**Papers:** Glasscock et al. 2025, *Nat Struct Mol Biol* 32:2252 (DNA-binding
design — NSMB, not *Nature*) · Favor et al. 2025, bioRxiv (RNA and nucleoprotein
design, preprint).

---

## R.10 The framing talks and the skeptics

| Talk | Speaker / host | Length | Link |
|---|---|---|---|
| Design of new protein functions using deep learning | David Baker (Allen School) | 59:14 | [▶](https://www.youtube.com/watch?v=3K1J83Yle5Q) |
| Protein design using deep learning | David Baker (Broad) | 52:07 | [▶](https://www.youtube.com/watch?v=-H27Kv5duYA) |
| Design of New Protein Functions Using Deep Learning | David Baker (NCATS NIH) | 25:09 | [▶](https://www.youtube.com/watch?v=EcPCQC1_4Ks) |
| **Nobel Lecture: De Novo Protein Design** | David Baker | 38:33 | [▶](https://www.youtube.com/watch?v=PLrY9DrbOkQ) |
| Part 1: Introduction to Protein Design | David Baker (iBiology) | 21:22 | [▶](https://www.youtube.com/watch?v=0LetJMbu7uY) |
| **Some thoughts on ML-based protein engineering** | Jennifer Listgarten (Simons) | ~62 min | [▶](https://www.youtube.com/watch?v=cunuHYHadPw) |
| ML-based Design of Proteins and Small Molecules | Jennifer Listgarten (Simons) | 45:48 | [▶](https://www.youtube.com/watch?v=SLRbGHXKkTw) |
| ML-Based Design Of Proteins | Jennifer Listgarten (Simons) | 31:56 | [▶](https://www.youtube.com/watch?v=A03qxNl_hkA) |
| The State of Protein Structure Prediction and Friends | Mohammed AlQuraishi (Simons) | 1:05:31 | [▶](https://www.youtube.com/watch?v=19fy0we14XM) |
| Review and discussion of AlphaFold3 | Sergey Ovchinnikov (BPDMC) | 1:12:58 | [▶](https://www.youtube.com/watch?v=qjFgthkKxcA) |

> **Listgarten's argument, stated as plainly as it can be: prediction is
> interpolation; design is extrapolation.** A model trained on natural proteins
> is asked, at design time, to score molecules drawn from a region of sequence
> space where it has no training data and no calibrated uncertainty. Every method
> in this family does this. The field's success rates are what they are because
> of it. If you take one idea from Atlas R, take that one — it is also a direct
> statement of an open problem, which is why it reappears as Capstone III.

---

## R.11 BUILD — Atlas R

1. **Generate 1,000 backbones** for a binder target with RFdiffusion. Design
   sequences with ProteinMPNN at three temperatures. Refold and compute
   self-consistency RMSD, interface pAE, and pLDDT.
2. **Find the filter that does no work.** Plot every filter metric's
   distribution and its correlation with every other. In most published
   pipelines at least one filter is nearly redundant and one is nearly
   uncorrelated with anything that matters. Identify both.
3. **Run PoseBusters-style physical validity checks** on your designs. Report
   the fraction that pass.
4. **Write the one page.** What fraction of 1,000 would you actually order, and
   defend the number against derivation checkpoint 63 — construct a concrete
   case where a design passes self-consistency with high confidence and still
   fails experimentally.

**Derivation checkpoints due: 61, 62, 63.**

---

## R.12 Paired reading — Atlas R

| Watch this | Then read this | Hold this question |
|---|---|---|
| Dauparas, *ProteinMPNN* | **Dauparas et al. 2022, *Science* 378:49** | Sequence recovery is the headline. What moved experimentally, and by how much? |
| **BPDMC, *Beyond sequence recovery*** | Compare to Dauparas 2022 | Write down why likelihood-given-backbone ≠ probability-of-folding. |
| ML4PE, *Mega-scale stability* | **Tsuboyama et al. 2023, *Nature* 620:434** | 500,000 measured stabilities. What can you now train that you could not before? |
| Watson & Juergens, *RFdiffusion* | **Watson et al. 2023, *Nature* 620:1089** | List every filter between generation and ordering. What fraction survives? |
| **MaomLab, RFdiffusion critique** | Same paper | Which claims does an external reading weaken? |
| Ahern & Yim, *RFdiffusion2* | Ahern et al. 2026, *Nat Methods* 23:96 | What failed in v1 that motivated atom-level generation? |
| Grigoryan & Costello, *Chroma* | **Ingraham et al. 2023, *Nature* 623:1070** | Conditioners are classifier guidance. What constraint class does that admit? |
| Yim & Trippe, *FrameDiff* | **Yim et al. 2023, ICML (SE(3) diffusion)** | Backbone frames live on SE(3). What breaks under a Euclidean treatment? |
| Bose & Tong, *FoldFlow* | Bose et al. 2024, ICLR | Flow matching vs diffusion on the same manifold. What is traded? |
| Campbell & Yim, *Multiflow* | Campbell et al. 2024, ICML | Discrete and continuous jointly. How is the discrete flow defined? |
| ML4PE, *EvoDiff* | Alamdari et al. 2023, bioRxiv | "Sequence is all you need." What does that claim give up? |
| **ML4PE, *MotifBench*** | The MotifBench paper | Are published scaffolding numbers comparable? Why not? |
| Ovchinnikov, *Inverting predictors* | **Anishchenko et al. 2021, *Nature* 600:547** | What does invertibility say about what a predictor represents? |
| Valence, *BindCraft* | **Pacesa et al. 2025, *Nature* 646:483** | One-shot binders. What is the experimental hit rate and against what baseline? |
| RosettaCommons, *Binder Design Overview* | **Cao et al. 2022, *Nature* 605:551** | Target structure alone. What information is actually being used? |
| **BPDMC, *Why designs fail*** | Any binder paper's supplement | Count the designs ordered versus designs reported. |
| **Cradle, *Adaptyv competition*** | **Cotet et al. 2025, bioRxiv** | A public wet-lab benchmark. Why does design not have a standing one? |
| Lauko & Pellock, *Serine hydrolases* | **Lauko et al. 2025, *Science* 388:eadu2454** | What kcat was achieved, and how far from a natural enzyme? |
| IPD panel, *Then & Now* | Röthlisberger 2008; Jiang 2008; Siegel 2010; **then Blomberg et al. 2013, *Nature* 503:418** | Where did the catalysis actually come from? |
| Fleishman, *PROSS/FuncLib* | Goldenzweig 2016; Khersonsky 2018 | Evolutionary data plus atomistic design. Which culture is this? |
| Rettie, *RFpeptides* | **Rettie et al. 2025, *Nat Chem Biol* 21:1948** | Macrocycles with a cyclic constraint. How is the constraint imposed? |
| BPDMC, *Structured peptides* | **Bhardwaj et al. 2016, *Nature* 538:329; Hosseinzadeh et al. 2017, *Science* 358:1461** | What makes a macrocycle designable where a linear peptide is not? |
| ML4PE, *Germinal* | Mille-Fragoso et al. 2026, *Nat Biotechnol* | Epitope-targeted de novo antibodies. What is the hit rate per epitope? |
| **RosettaCommons, *FLAb2*** | The FLAb2 paper | Developability, not affinity, kills antibodies. Can any model predict it? |
| Broad, *TCR-pMHC framework* | **Bradley 2023, *eLife* 12:e82813** | Why do general methods underperform on TCR-pMHC specifically? |
| BPDMC, *Conformational change design* | **Praetorius et al. 2023, *Science* 381:754; Langan et al. 2019, *Nature* 572:205** | Designing motion. What objective replaces a single backbone? |
| BPDMC, *Ligand-binding from scratch* | Polizzi & DeGrado 2020, *Science* 369:1227; An et al. 2024, *Science* 385:276 | A binding site is a geometric arrangement. What else must be true? |
| **Listgarten, *ML-based protein engineering*** | **Kapoor & Narayanan 2023** | Formalize the distribution shift between training and design-time input. |
| Baker, Nobel Lecture | Kuhlman et al. 2003 (Top7); Watson et al. 2023 | Twenty years apart. Which parts of the 2003 pipeline survived? |
