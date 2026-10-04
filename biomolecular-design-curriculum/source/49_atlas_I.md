# Atlas I — Dynamics Analysis, Allostery, Networks and Pockets

> **Problem.** A trajectory is a enormous pile of coordinates. Which projection
> of it means something? Which motions are functional and which are thermal
> noise? How does a perturbation at one site propagate to another? And where, on
> a surface that looks featureless in the crystal structure, is there a pocket
> that opens for a fraction of the time?
>
> This family is the analysis layer, and it is where most published figures in
> computational biophysics come from. **It is also where most of the
> irreproducibility lives**, because almost none of these analyses come with an
> error bar.

---

## I.1 Allostery: theory

| Title | Speaker | Length | Link |
|---|---|---|---|
| MWC model | Rob Phillips (Caltech, BE/APh 161) | 24:33 | [▶](https://www.youtube.com/watch?v=uFbvFMtowjE) |
| MWC model of chemoreceptors | Rob Phillips | 22:54 | [▶](https://www.youtube.com/watch?v=um8XA58I3pE) |
| Allostery, no physicists allowed | Rob Phillips | 8:55 | [▶](https://www.youtube.com/watch?v=bhQc14lkfG0) |
| **Opening Lecture at the European Conference on ALLODD** | Jean-Pierre Changeux (Institut Pasteur) | 1:10:23 | [▶](https://www.youtube.com/watch?v=HNtOUAc2u7I) |

Phillips's course is the only place online that **derives** MWC rather than
drawing the T/R cartoon. Changeux is the living author of the 1965 model
assessing it sixty years on — rare, and worth the hour.

### Evolutionary coupling and sectors

| Title | Speaker | Length | Link |
|---|---|---|---|
| The Evolutionary "Design" of Protein Machines | Rama Ranganathan (Chicago) | 58:35 | [▶](https://www.youtube.com/watch?v=xh6FQ5Pf-AY) |
| The Evolutionary Design of Proteins (NITMB, 2025) | Rama Ranganathan | 1:10:57 | [▶](https://www.youtube.com/watch?v=ma_e32OYQoI) |
| Evolutionary "Design" of Proteins (Aspen, 2019) | Rama Ranganathan | 48:52 | [▶](https://www.youtube.com/watch?v=pS1oBWB2wbk) |
| Part 1: What is Protein Design? | Rama Ranganathan (iBiology) | 27:06 | [▶](https://www.youtube.com/watch?v=W9J294X4FbY) |
| Part 3: Protein Function and Adaptability | Rama Ranganathan (iBiology) | 45:15 | [▶](https://www.youtube.com/watch?v=jJ3aQaDCoHc) |

**Watch Aspen 2019 then NITMB 2025** and notice how much the sector claim has
been walked back and re-grounded over six years. That trajectory is itself the
lesson: a strong structural claim meeting sustained scrutiny.

### Elastic network models and ANM-based allostery

| Title | Speaker | Length | Link |
|---|---|---|---|
| **Network models in biology** | Ivet Bahar (Pitt / Stony Brook) | 1:23:01 | [▶](https://www.youtube.com/watch?v=8DBAlYsvlbI) |
| EMBO Lecture: Confluence of structure-based models | Ivet Bahar | 48:58 | [▶](https://www.youtube.com/watch?v=CzqBLKIWiCM) |
| Elastic network models, targeting hinges for drug discovery (interview) | Ivet Bahar | 39:33 | [▶](https://www.youtube.com/watch?v=P1n2NBrIO8o) |
| Network Models In Biology: From Molecular Machinery To Chromosomal Dynamics | Ivet Bahar | 1:10:57 | [▶](https://www.youtube.com/watch?v=3z6pE_CBwxg) |
| Leveraging Hi-C with Elastic Network Models | Ivet Bahar | 23:38 | [▶](https://www.youtube.com/watch?v=QFogxyLK4zs) |
| **ProDy** (hands-on) | CCPBioSim | 54:34 | [▶](https://www.youtube.com/watch?v=8JwRC4Dcj_M) |
| ProDy (second treatment) | SBGrid | 55:32 | [▶](https://www.youtube.com/watch?v=IWMK_AHyi48) |
| Physical properties of folded peptide chains (domain decomposition NMA) | Konrad Hinsen (CNRS Orléans) | 43:53 | [▶](https://www.youtube.com/watch?v=RbOu1Vjp3Mc) |
| Chromosomal dynamics predicted by an elastic network model | She Zhang (ISMB 2018) | 6:35 | [▶](https://www.youtube.com/watch?v=caYDOlXt5AA) |
| Computational Biophysics Workshop Day 1, Part 2 (ENM theory) | MMBioS | 1:10:07 | [▶](https://www.youtube.com/watch?v=0e12cEe_C9U) |

> **The unexploited idea.** An elastic network model gives you a normal-mode
> spectrum from a single structure in seconds. Every generative design method
> produces structures. **Nobody designs for a target normal-mode spectrum**, even
> though Johnson and Edelman's lecture on derivatives of eigenproblems (Module
> B.1) gives you the gradient you would need. That is row five of the
> unexchanged-ideas table and it is unusually tractable.

### Dynamic allostery, networks, information-theoretic coupling

| Title | Speaker | Length | Link |
|---|---|---|---|
| Dissecting Allosteric Mechanisms and Protein Interactions | Amnon Horovitz (Weizmann) | 1:06:41 | [▶](https://www.youtube.com/watch?v=Bt48OqVSEGw) |
| A Nonequilibrium Approach to Allosteric Communication | Peter Hamm (Zurich) | 1:25:24 | [▶](https://www.youtube.com/watch?v=j1TfBDvHCco) |
| **Allostery under the lens of molecular dynamics simulations** | Julien Michel (Edinburgh) | 58:15 | [▶](https://www.youtube.com/watch?v=cIi38IZLLKw) |
| Insight into protein allostery from designed mechanical networks | Andrea Liu (Penn) | 29:36 | [▶](https://www.youtube.com/watch?v=l1nW5xTcgg0) |
| Predicting allosteric networks in protein complexes | NIMBioS | 50:38 | [▶](https://www.youtube.com/watch?v=s-E7E8rwdpY) |
| Dynamic network analysis of protein structural change | Aydin Wells (Notre Dame) | 25:47 | [▶](https://www.youtube.com/watch?v=7ZVh0lSamyg) |
| Identifying Allosteric Sites Through Network Analysis | RSG-Türkiye | 34:52 | [▶](https://www.youtube.com/watch?v=P-4va_F5U_s) |
| **Mapping the energetic and allosteric landscapes of protein binding domains** | André Faure (CRG Barcelona) | 28:56 | [▶](https://www.youtube.com/watch?v=AZfDRtWYseM) |
| Allostery in DNA drives phenotype switching | Hagen Hofmann (Weizmann) | 1:12:31 | [▶](https://www.youtube.com/watch?v=fXZCoa9KlaE) |

**Michel's hour is the best available on what MD can and cannot tell you about
allosteric coupling**, and he is honest about convergence.

**Faure's talk is the one that should unsettle you.** Double deep mutational
scanning measures allosteric coupling *experimentally*, at scale, and the
structure-plus-MD predictions do not do well against it. That is a benchmark
existing in the wild that almost nobody in the computational allostery community
tests against — which makes it an opportunity.

*Vincent Hilser, whose ensemble allosteric model is the conceptual heart of
entropic allostery, has no verifiable recorded research talk. Read Motlagh,
Wrabl, Li & Hilser 2014, Nature 508:331 instead. Same for Sandor Vajda on FTMap
and Heather Carlson on MixMD.*

---

## I.2 Pocket and site detection

| Title | Speaker | Length | Link |
|---|---|---|---|
| **Accelerating Cryptic Pocket Discovery With Deep Learning** | Greg Bowman (Penn) | 37:23 | [▶](https://www.youtube.com/watch?v=hNdPrioGQ7k) |
| Greg Bowman, TCBG seminar | Greg Bowman | 1:09:45 | [▶](https://www.youtube.com/watch?v=NebAz0YVPhU) |
| MSMs, excited states and cryptic pockets | Greg Bowman | 33:23 | [▶](https://www.youtube.com/watch?v=4vgBUXW5mn8) |
| Translational Allostery: From Cryptic Binding Pockets to Latent Networks | The Protein Society | 2:27:00 | [▶](https://www.youtube.com/watch?v=T4Q0M0TuUZ4) |
| Drugging the Undruggable: Detecting and Ranking Cryptic Pockets | OpenEye / Cadence | 46:46 | [▶](https://www.youtube.com/watch?v=xoNHt_8wmr4) |
| Investigating cryptic binding sites and allostery | ALLODD | 58:51 | [▶](https://www.youtube.com/watch?v=oCC6WEDO7O4) |
| Characterization of allosteric pockets in a protein-membrane environment | ALLODD | 1:05:13 | [▶](https://www.youtube.com/watch?v=_V9gxfRgDPM) |
| Design and synthesis of covalent allosteric probes | ALLODD | 1:09:17 | [▶](https://www.youtube.com/watch?v=K_ygoVWBpkc) |
| **SILCS** | CCPBioSim (MacKerell method) | 1:14:34 | [▶](https://www.youtube.com/watch?v=Ld5tK-fxJQE) |
| SILCS-WATER: the role of water in protein-ligand binding | SilcsBio | 56:17 | [▶](https://www.youtube.com/watch?v=wrTJOzMrH2w) |
| **Automating Structure-Based Design Using Fragment Hotspot Maps** | Chris Radoux (CCDC) | 34:56 | [▶](https://www.youtube.com/watch?v=4naf2YVBkzo) |
| Identifying Druggable Pockets for Protein Ensembles | Lane Votapka (Amaro lab) | 20:19 | [▶](https://www.youtube.com/watch?v=9Eby8N28qSM) |
| CASP-16 Predictor talk: ClusPro | Dima Kozakov (Stony Brook) | 20:02 | [▶](https://www.youtube.com/watch?v=tbtLAtBy7do) |

Bowman's Valence Labs talk is the PocketMiner talk and the one to assign.
**Given your own cosolvent-MD and cryptic-pocket work, this subsection is the
most directly operational in the entire Atlas** — SILCS, MixMD and fragment
hotspot maps are three routes to the same physics, and knowing which assumptions
differ between them is the difference between running a tool and choosing one.

---

## I.3 Interfaces and hot spots

| Title | Speaker | Length | Link |
|---|---|---|---|
| I, biochemist: Automation and AI in the lab | Tanja Kortemme (UCSF) | 49:41 | [▶](https://www.youtube.com/watch?v=uLQbaiTYIQY) |
| Protein-Protein Interfaces | RosettaCommons | 7:49 | [▶](https://www.youtube.com/watch?v=EhZqF0-VaJ8) |
| How FoldX works, with examples | FoldX team | 16:26 | [▶](https://www.youtube.com/watch?v=nn6ZWTYqrx4) |
| Computational Protein Design: Design of Protein-Protein Interactions | Julia Shifman (Hebrew University) | 42:32 | [▶](https://www.youtube.com/watch?v=go43vprvPHM) |
| **Deciphering interaction fingerprints from molecular surfaces (MaSIF)** | Correia lab method, journal club | 1:12:13 | [▶](https://www.youtube.com/watch?v=5TriwKQcVJY) |
| Massively parallel discovery of peptides to inhibit protein interactions | BPDMC | 1:12:44 | [▶](https://www.youtube.com/watch?v=s31yC7nQqDs) |
| Structural and functional determinants inferred from deep mutational scans | Priyanka Bajaj | 32:57 | [▶](https://www.youtube.com/watch?v=Pzdxsr8LmaA) |
| Predicting folding stability and aggregation from large-scale experiments | BPDMC | 1:00:30 | [▶](https://www.youtube.com/watch?v=KKXe8a_h88c) |
| Affinity Maturation walkthrough (Rosetta Workshop 2021) | Meiler Lab | 33:40 | [▶](https://www.youtube.com/watch?v=z2kaGqtY5UI) |
| New Capabilities in Computational Protein Design | The Protein Society | 2:44:17 | [▶](https://www.youtube.com/watch?v=xrPu1WQ8Q7A) |

MaSIF is worth particular attention: it treats the molecular surface as a
geometric object and learns fingerprints on it with geometric deep learning —
the most direct existing bridge between Atlas family I and Atlas family O, and
the method that later produced de novo interactions from learned surface
fingerprints.

---

## I.4 Trajectory analysis — and its pitfalls

| Title | Host | Length | Link |
|---|---|---|---|
| Intro to MD Trajectory Analysis using MDAnalysis | MDAnalysis project | 1:40:34 | [▶](https://www.youtube.com/watch?v=p3OUUnHXQjU) |
| Intro to MDAnalysis Workshop | MDAnalysis project | 2:09:37 | [▶](https://www.youtube.com/watch?v=njzoNzOwR78) |
| MDAnalysis Streaming Online Workshop | MDAnalysis project | 2:56:58 | [▶](https://www.youtube.com/watch?v=fjBTvnEADGs) |
| Intro to MDAnalysis and Molecular Nodes | MDAnalysis project | 3:33:02 | [▶](https://www.youtube.com/watch?v=3zKBjnRnAMg) |
| Amber (covers cpptraj) | SBGrid | 1:11:39 | [▶](https://www.youtube.com/watch?v=ADI3QODT6SY) |
| VMD | SBGrid | 1:23:25 | [▶](https://www.youtube.com/watch?v=OfMKr-2EtwA) |
| Visualization and analysis with VMD | David Winogradoff (UIUC) | 53:18 | [▶](https://www.youtube.com/watch?v=jySOUCZqq-M) |
| Quick setup and analysis of NAMD simulations with QwikMD | Rafael Bernardi (Auburn) | 55:15 | [▶](https://www.youtube.com/watch?v=ZpPW3MKq3iE) |

### Dimensionality reduction and Markov state models — the PyEMMA course

The single best free course on this material anywhere.

| # | Lecture | Length | Link |
|---|---|---|---|
| 2018-1 | Introduction to Markov state models | 1:07:35 | [▶](https://www.youtube.com/watch?v=YXppP_QTut8) |
| 2017-3 | **Featurization and TICA** | 36:16 | [▶](https://www.youtube.com/watch?v=95uyk-xMlT0) |
| 2018-7 | The variational approach | 32:25 | [▶](https://www.youtube.com/watch?v=A3AUWXqqONc) |
| 2018-3 | **MSM estimation and validation** | 1:01:40 | [▶](https://www.youtube.com/watch?v=pVl7TPFuHwk) |
| 2018-8 | How to select models with the VAMP score | 21:18 | [▶](https://www.youtube.com/watch?v=QHQBVmVq-Vo) |
| 2021-2 | MSM theory | 44:32 | [▶](https://www.youtube.com/watch?v=gSR2xp2NFIc) |
| 2021-5 | Introduction to VAMPNets | 36:45 | [▶](https://www.youtube.com/watch?v=C5KfGWV5dAw) |
| — | TICA, TCCA and time-autoencoders | 32:38 | [▶](https://www.youtube.com/watch?v=Sat_27wkyQ0) |
| — | Deep learning for molecular kinetics | 37:32 | [▶](https://www.youtube.com/watch?v=LOrjQJaJ6Gk) |
| — | Intro to Trajectory Analysis and MSMs | 32:58 | [▶](https://www.youtube.com/watch?v=HlZjvw-DJIg) |

Full 2017, 2018 and 2021 listings are in Atlas family B's enumeration.

### Convergence — assign these FIRST

| Title | Speaker | Length | Link |
|---|---|---|---|
| **Testing Molecular Simulation Results for Physical Validity** | Michael Shirts (Colorado) | 28:10 | [▶](https://www.youtube.com/watch?v=-Zxvi7EQwE4) |
| Reproducibility, Convergence and Accuracy in Biomolecular Simulation | NCSA / Blue Waters | 17:29 | [▶](https://www.youtube.com/watch?v=C3ptGf22Xiw) |
| Convergence and Reproducibility in MD Simulations of Nucleic Acids | NCSA / Blue Waters | 20:03 | [▶](https://www.youtube.com/watch?v=JBYfQ9mUFo8) |
| Reproducible molecular simulations with Python | Iván Pulido (Chodera lab) | 30:37 | [▶](https://www.youtube.com/watch?v=PHoVyqBYqIU) |

> **The question to hold.** RMSF appears in essentially every MD paper in this
> curriculum, including your own peptide-RMSF figures. It is a single number per
> residue, extracted from a trajectory that is almost never shown to be
> converged, after alignment to a reference that is itself a choice. Shirts's
> twenty-eight minutes are the antidote. Before believing any RMSF figure, ask
> for the block-averaged error bar.

---

## I.5 Intrinsically disordered proteins

| Title | Speaker | Length | Link |
|---|---|---|---|
| Charge-rich disordered proteins | Rohit Pappu (WashU/Hopkins) | 1:16:31 | [▶](https://www.youtube.com/watch?v=C0z_89ClQrM) |
| **Dewpoint Kitchen Table Talk, Part 1** | Rohit Pappu | 1:07:10 | [▶](https://www.youtube.com/watch?v=GrVHXe4FtrQ) |
| Dewpoint Kitchen Table Talk, Part 2 | Rohit Pappu | 1:09:49 | [▶](https://www.youtube.com/watch?v=IDKVLxWAT3E) |
| Dewpoint Kitchen Table Talk, Part 3 | Rohit Pappu | 1:07:05 | [▶](https://www.youtube.com/watch?v=nRbpiM3MDR4) |
| Interpreting experiments using simulations | Kresten Lindorff-Larsen (Copenhagen) | 1:27:01 | [▶](https://www.youtube.com/watch?v=a15IlXIhz1k) |
| Lindorff-Larsen, TCBG seminar | Kresten Lindorff-Larsen | 1:13:58 | [▶](https://www.youtube.com/watch?v=uIVR9EDNJAc) |
| From disordered proteins to complexes and assemblies | Robert Best (NIH) | 1:35:22 | [▶](https://www.youtube.com/watch?v=NxSeqlYiIU8) |
| HITS Colloquium: simulations of IDPs | Robert Best | 1:01:07 | [▶](https://www.youtube.com/watch?v=jFmGNUUVHzg) |
| BioExcel #98: Conformational ensembles of IDRs and IDPs | BioExcel CoE | 1:02:59 | [▶](https://www.youtube.com/watch?v=_6iAcwmknek) |
| **Current issues with MD force fields for IDPs** | Brigita Urbanc (Drexel) | 29:46 | [▶](https://www.youtube.com/watch?v=0cP6Q93TbWY) |
| The IDRome: Conformations of the Human Disordered Proteome | Giulio Tesei (Copenhagen) | 2:19 | [▶](https://www.youtube.com/watch?v=v7YqJVEswM0) |
| Single-molecule dynamics and interactions of disordered proteins | Ben Schuler (Zurich) | 38:03 | [▶](https://www.youtube.com/watch?v=J-0qlsFH3Pc) |
| Probing the rapid chain dynamics of disordered proteins and nucleic acids | Ben Schuler | 55:18 | [▶](https://www.youtube.com/watch?v=bzCKeH6lBFk) |
| It takes tau to tangle | Elizabeth Rhoades (Penn) | 1:10:54 | [▶](https://www.youtube.com/watch?v=sR1A9SCj52Q) |
| Small-molecule binding to intrinsically disordered proteins | Cambridge CMD | 19:01 | [▶](https://www.youtube.com/watch?v=Z6uAhzjeK_o) |

**The Dewpoint three-parter is the most complete recorded statement of Pappu's
position anywhere**, and it is conversational rather than a conference talk — he
says things there he would not put in a paper. Urbanc's talk names which IDP
force fields fail and how, which is information that is otherwise expensive to
acquire.

---

## I.6 Condensates and phase separation

| Title | Speaker | Length | Link |
|---|---|---|---|
| Phase Separation of Multivalent Proteins | Rohit Pappu | 56:49 | [▶](https://www.youtube.com/watch?v=CKsgv330V7Y) |
| Computational Approaches to Protein Condensates | The Protein Society | 1:46:03 | [▶](https://www.youtube.com/watch?v=UmNwzDyf0JQ) |
| Emergent properties of condensates and their effects on protein function | Tanja Mittag (St. Jude, KITP) | 44:59 | [▶](https://www.youtube.com/watch?v=CBai9DWegAE) |
| Instruct Biennial 2024 | Tanja Mittag | 34:54 | [▶](https://www.youtube.com/watch?v=Iftqku1ERWA) |
| Biomolecular condensates across the Tree of Life | Agnes Toth-Petroczy (MPI-CBG, KITP) | 39:36 | [▶](https://www.youtube.com/watch?v=TscSPW0Q0U0) |
| Multiscale modelling of liquid-like chromatin organisation | Rosana Collepardo-Guevara (Cambridge) | 51:04 | [▶](https://www.youtube.com/watch?v=MNh-9lmFmt0) |
| From Wiggles to Flow: Multiscale Dynamics of Charged Protein Condensates | Jeetain Mittal (Texas A&M) | 29:59 | [▶](https://www.youtube.com/watch?v=-FCzirVHKC0) |
| Principles of structure/function in biomolecular condensates | Jeremy Schmit (Kansas State) | 28:51 | [▶](https://www.youtube.com/watch?v=XKcxFrpqvFg) |
| Liquid Phase Separation in Living Cells | Cliff Brangwynne (Princeton/HHMI) | 46:05 | [▶](https://www.youtube.com/watch?v=AP47mIkd-h0) |
| Condensates at the nexus of cellular stress, disease and aging | Simon Alberti (TU Dresden) | 1:08:29 | [▶](https://www.youtube.com/watch?v=3n8xDFjRku0) |
| Measuring the liquid structure of condensates in live cells | Josh Riback (Baylor) | 37:43 | [▶](https://www.youtube.com/watch?v=RuP-YyrW-mk) |
| Predictive models of sequence determinants of nuclear condensates | HHMI Janelia | 17:11 | [▶](https://www.youtube.com/watch?v=nSjH5ow3VKk) |
| Droplets everywhere: cell organization by LLPS | NIH WALS | 1:00:13 | [▶](https://www.youtube.com/watch?v=Vezrj7FqMlY) |

---

## I.7 Membrane proteins and large assemblies

| Title | Speaker | Length | Link |
|---|---|---|---|
| **Structure and Dynamics of Biological Membranes: Lipid-Protein Interactions** | Erik Lindahl (KTH) | 2:07:23 | [▶](https://www.youtube.com/watch?v=uKjVufjewFI) |
| Application of molecular dynamics to biomolecular modeling | Emad Tajkhorshid (UIUC) | 1:37:29 | [▶](https://www.youtube.com/watch?v=mUxMUj21QTI) |
| Revealing the Structural Basis of GPCR Signaling | Ron Dror (Stanford) | 1:08:43 | [▶](https://www.youtube.com/watch?v=gExgG4qfEQI) |
| **Unraveling C-type inactivation in potassium channels** | Benoît Roux (Chicago) | 58:44 | [▶](https://www.youtube.com/watch?v=WpbKjN7KUWc) |
| TSRC Workshop on Protein Dynamics | Benoît Roux | 49:47 | [▶](https://www.youtube.com/watch?v=nKH42kSTzo0) |
| Roux, Free Energy Workshop 2018 | Benoît Roux | 33:43 | [▶](https://www.youtube.com/watch?v=k6B6U0dvf2o) |
| On MD modeling, force fields, and membrane channels (interview) | Benoît Roux | 31:09 | [▶](https://www.youtube.com/watch?v=_Wp0oSIZKJI) |
| Water and Ions in Membrane Nanopores and Channels | Mark Sansom (Oxford) | 48:14 | [▶](https://www.youtube.com/watch?v=MUZJStEyHbs) |
| Origins of CHARMM-GUI (interview) | Wonpil Im (Lehigh) | 44:00 | [▶](https://www.youtube.com/watch?v=bK8SMtxhDPY) |
| Whole cell simulation with Lattice Microbes, Part I | Zaida Luthey-Schulten (UIUC) | 1:11:20 | [▶](https://www.youtube.com/watch?v=rKRcPN9anHA) |
| Whole cell simulation with Lattice Microbes, Part II | Zaida Luthey-Schulten | 1:19:13 | [▶](https://www.youtube.com/watch?v=ibn6Owow99M) |
| 4D simulations of a growing minimal bacterial cell | Zaida Luthey-Schulten | 1:02:24 | [▶](https://www.youtube.com/watch?v=NG3jPxN7QbQ) |
| Freezing ribosomes, wet proteins, flying peptides | Helmut Grubmüller (MPI Göttingen) | 1:39:58 | [▶](https://www.youtube.com/watch?v=M-hr9RNgLn4) |
| Atomistic Simulation of Biomolecular Function: Ligand Binding Heterogeneity | Helmut Grubmüller | 1:29:07 | [▶](https://www.youtube.com/watch?v=cvMxXWRUR3w) |
| Juan Perilla, TCBG seminar (HIV capsid) | Juan Perilla (Delaware) | 1:00:53 | [▶](https://www.youtube.com/watch?v=XAdtBNiGxW0) |
| Nanotechnology with molecular simulation | Aleksei Aksimentiev (UIUC) | 47:25 | [▶](https://www.youtube.com/watch?v=cPat3E5JtbY) |
| Protein Dynamics in Cellular Environments | Rommie Amaro (UCSD) | 57:48 | [▶](https://www.youtube.com/watch?v=V_nwYl8c2-w) |
| **EMBL Keynote: In Situ Dynamics Reveal Unseen Vulnerabilities of Viral Glycoproteins** | Rommie Amaro | 47:58 | [▶](https://www.youtube.com/watch?v=zKP-8qViTQ4) |
| Computational Microscopy for In Situ Molecular Dynamics | Rommie Amaro | 1:16:49 | [▶](https://www.youtube.com/watch?v=96KHjQ3Vv3g) |

Amaro's glycan work is the clearest demonstration that a structure without its
glycan shield is a different molecule — directly relevant if you ever model a
glycoprotein surface as a design target.

---

## I.8 BUILD — Atlas I

1. **Implement the Gaussian network model from scratch.** Compute B-factors from
   the pseudo-inverse of the contact matrix and correlate with crystallographic
   B-factors for ten proteins. You will get r ≈ 0.6. Explain the residual.
2. **Implement the anisotropic network model** and visualize the lowest modes.
   Compare to the principal components of a real MD trajectory of the same
   protein. Measure the overlap.
3. **Community network analysis.** Build a dynamical network from a trajectory
   using generalized correlation, partition it, and identify the optimal paths
   between two sites. Then do the honest part: repeat on an independent replica
   and see whether you get the same communities.
4. **The convergence audit.** Take one of your own published RMSF figures.
   Recompute it with block averaging and error bars. Recompute it with a
   different alignment reference. Report how much the conclusion moves.

**Derivation checkpoints due: 39, 40, 41, 42.**

---

## I.9 Paired reading — Atlas I

| Watch this | Then read this | Hold this question |
|---|---|---|
| Phillips, *MWC model* | **Monod, Wyman & Changeux 1965, JMB 12:88** | Derive the MWC saturation curve. What are its three parameters? |
| Changeux, ALLODD lecture | Cooper & Dryden 1984, Eur Biophys J 11:103 | Allostery without conformational change. How would you detect it computationally? |
| Ranganathan, Aspen then NITMB | **Lockless & Ranganathan 1999; Halabi et al. 2009, Cell 138:774** | What has survived of the sector claim, and what was retracted? |
| Bahar, *Network models in biology* | **Atilgan et al. 2001, Biophys J 80:505; Bahar et al. 2010, Chem Rev 110:1463** | Derive the GNM. Why does a single-parameter model predict B-factors at all? |
| Bahar interview | Atilgan & Atilgan 2009, PLoS Comput Biol 5:e1000544 | Perturbation-response scanning. Could it be run in reverse, as a design objective? |
| Michel, *Allostery under MD* | Tsai & Nussinov 2014; Wodak et al. 2019, Structure 27:566 | Which allosteric signals survive a convergence test? |
| **Faure, *Energetic and allosteric landscapes*** | **Faure et al. 2022, Nature 604:175** | Double DMS measures coupling directly. How well does any prediction do against it? |
| Luthey-Schulten lineage (network analysis) | **Sethi et al. 2009, PNAS 106:6620; Melo et al. 2020, JCP 153:134104** | What does generalized correlation capture that linear correlation does not? |
| **Bowman, *Cryptic Pocket Discovery*** | **Meller et al. 2023, Nat Commun 14:1177 (PocketMiner)** | A cryptic pocket is a low-population excited state. What population is druggable? |
| Radoux, *Fragment Hotspot Maps* | Brenke et al. 2009 (FTMap); Kozakov et al. 2015 | Three routes to hotspots. Which assumptions differ? |
| CCPBioSim, *SILCS* | **Guvench & MacKerell 2009, PLoS Comput Biol 5:e1000435; Ghanakota & Carlson 2016** | Cosolvent MD gives a free energy map. What is the reference state? |
| MaSIF journal club | **Gainza et al. 2020, Nat Methods 17:184; Gainza et al. 2023, Nature 617:176** | Surface fingerprints bypass sequence and backbone. What is lost? |
| Kortemme, ASBMB | **Kortemme & Baker 2002, PNAS 99:14116** | Computational alanine scanning: what physical model underlies the hot spot prediction? |
| PyEMMA 2017-3, *TICA* | **Pérez-Hernández et al. 2013, JCP 139:015102** | Why does TICA find slow coordinates where PCA finds high-variance ones? |
| PyEMMA 2018-3, *estimation and validation* | **Prinz et al. 2011, JCP 134:174105** | Derive why the lag time must exceed the fastest resolved process. |
| PyEMMA, *VAMPNets* | Mardt et al. 2018, Nat Commun 9:5 | A learned featurization with a variational guarantee. What is being bounded? |
| **Shirts, *Testing Simulation Results for Physical Validity*** | **Grossfield et al. 2019, LiveCoMS 1:5067** | Apply every test to your own trajectory. Which does it fail? |
| Pappu, Dewpoint 1–3 | **Das & Pappu 2013, PNAS 110:13392; Choi, Holehouse & Pappu 2020** | Charge patterning (κ) predicts dimensions. What else does sequence predict? |
| Urbanc, *IDP force fields* | **Robustelli, Piana & Shaw 2018, PNAS 115:E4758; Huang et al. 2017, Nat Methods 14:71** | Which force fields over-compact IDPs, and how was that diagnosed? |
| Tesei, *IDRome* | **Tesei et al. 2024, Nature 626:897; Tesei et al. 2021 (CALVADOS)** | A coarse-grained model for the whole disordered proteome. What does it get wrong? |
| Schuler, *Disordered proteins* | Schuler et al. 2016, Annu Rev Biophys 45:207 | smFRET gives a distance distribution. What must a model output to be comparable? |
| Mittag / Pappu, condensates | **Martin et al. 2020, Science 367:694 (stickers and spacers)** | Aromatic patterning sets phase behaviour. Could you design a condensate? |
| Roux, *C-type inactivation* | **Bernèche & Roux 2001, Nature 414:73** | Free energy of ion conduction. What made this tractable where binding is not? |
| Amaro, *Viral glycoproteins* | **Casalino et al. 2020, ACS Cent Sci 6:1722** | Glycans shield most of the surface. What does that do to epitope prediction? |
| Luthey-Schulten, *Lattice Microbes* | **Thornburg et al. 2022, Cell 185:345** | A whole minimal cell. What is the coarsest level that still predicts behaviour? |
