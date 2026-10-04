# Atlas T — RNA Structure, Folding and Design

> **Why this family is new in the third edition.** Rhiju Das is one of the ten
> scientists this curriculum is built around, and the second edition mentioned
> him three times. That was a real failure, and this family is the repair.
>
> **The thread to follow in Das's own work** is that he keeps rebuilding the same
> argument at larger scale: *if the bottleneck is data rather than architecture,
> go and manufacture the data.* Eterna, OpenVaccine, Ribonanza and OpenKnot are
> four passes at that one idea. Section T.10 answers, with numbers, why that is
> the right bet.
>
> **One sourcing note.** The richest standing seminar in this field is the
> **CASP RNA SIG** channel, a monthly series running since 2023. Twenty of its
> talks appear below. Nothing else in RNA comes close as a lecture series.

---

## T.1 Rhiju Das, in his own words

| Talk | Len | Link |
|---|---|---|
| **BioML Seminar — the RNA Folding Problem** | 1:23:58 | [▶](https://www.youtube.com/watch?v=XqFq_zYx7Vo) |
| **Ribonanza: big data for RNA structure prediction** | 1:01:58 | [▶](https://www.youtube.com/watch?v=R6-MwrGkj7M) |
| **CASP15 RNA assessment** | 29:12 | [▶](https://www.youtube.com/watch?v=oe-w1Xx1p1g) |
| Kaggle RNA 3D Folding Challenge: template-based prediction wins | 58:55 | [▶](https://www.youtube.com/watch?v=kKC5WjAqWsc) |
| RNA modelling and design (MRC LMB) | 35:54 | [▶](https://www.youtube.com/watch?v=2V09ne503V0) |
| Early results from the OpenKnot challenge | 41:12 | [▶](https://www.youtube.com/watch?v=PDI7wsdjtt0) |
| **EteRNA: RNA Nanoengineering through Crowd Science** (Stanford) | 55:03 | [▶](https://www.youtube.com/watch?v=j8ixwnEAE38) |
| EteRNA: A Videogame and a Massive Open Lab | 26:48 | [▶](https://www.youtube.com/watch?v=JMAv0NS6gnI) |
| **StepWise Monte Carlo for modeling and design** | 28:20 | [▶](https://www.youtube.com/watch?v=WtbTh9rFznY) |
| Atomic accuracy and blind predictions (ISMB 2011) | 20:48 | [▶](https://www.youtube.com/watch?v=qjT6oXAiasE) |
| Crowdsourced design of stabilized COVID-19 mRNAs | 11:41 | [▶](https://www.youtube.com/watch?v=8n3CEtj9LaU) |
| RNA Worlds panel with Cech, Krainer and Chin | 2:28:55 | [▶](https://www.youtube.com/watch?v=4mUAhtJAcrw) |
| State of Eterna (with Adrien Treuille) | 36:05 | [▶](https://www.youtube.com/watch?v=jV6ueodnZUk) |

**Start with the BioML seminar** — it runs Eterna through OpenVaccine to
Ribonanza as one continuous argument, which is the only way the program makes
sense. **Then the CASP15 assessment**, which is the canonical statement of where
RNA 3D prediction actually stands and which he delivered as assessor rather than
as advocate.

**Das lab and alumni:** Shujun He on Ribonanza architecture
([▶](https://www.youtube.com/watch?v=a8a41m_iCek)) · **Hannah Wayment-Steele on
EternaFold** — the only talk anywhere explaining the conditional log-linear model
and how it is retrained on crowdsourced chemical mapping, 20:19
([▶](https://www.youtube.com/watch?v=WWPUvlOfx2U)) · *Superfolder* thermostable
mRNA ([▶](https://www.youtube.com/watch?v=UA3ALXRkWSY)) · Rachael Kretsch on
RNA cryo-EM ([▶](https://www.youtube.com/watch?v=HDe_S89z3Yc)) and the **CASP16
RNA assessment** ([▶](https://www.youtube.com/watch?v=g-rOsECpH44)).

**Papers:** **He et al. 2024, bioRxiv (Ribonanza)** · Das et al. 2023, *Proteins*
(CASP15 RNA) · **Lee et al. 2014, *PNAS* 111:2122 (Eterna)** · Wayment-Steele
et al. 2022, *Nat Methods* 19:1234 (EternaFold) · Wayment-Steele et al. 2021,
*NAR* 49:10604 (mRNA stabilization) · Kappel et al. 2020, *Nat Methods* 17:699
(Ribosolve) · Watkins et al. 2018, *Sci Adv* 4:eaar5316 (StepWise Monte Carlo).

---

## T.2 Secondary structure prediction — the dynamic programming lineage

**This is the algorithmic core of the family**, and the talks that actually
*derive* the recursions turn out to be in algorithms courses, not bioinformatics
channels.

**The Nussinov recursion, derived:** Luay Nakhleh (Rice), 21:39
([▶](https://www.youtube.com/watch?v=rE2Q_ewhMfY)) · **Dan Gusfield (UC Davis),
two lectures** that set up the interval DP, fill the table, prove the ordering
and walk the traceback ([▶](https://www.youtube.com/watch?v=bzJNFhBWNTg)
[▶](https://www.youtube.com/watch?v=h60raqnvm0s)) · Steven Skiena (Stony Brook),
1:20:08, moving from base-pair maximization into the Zuker energy model
([▶](https://www.youtube.com/watch?v=BFdYqPrbyY0)).

**The Sebastian Wild unit (Marburg) — the best derivational sequence found.**
Treat as one 2.5-hour module; it derives Nussinov, the Zuker loop decomposition
and the SCFG/inside-outside material in order.

| # | Lecture | Len | Link |
|---|---|---|---|
| 8-1 | Noncoding RNA | 15:08 | [▶](https://www.youtube.com/watch?v=VyAFDf7P6QM) |
| 8-2 | RNA Secondary Structure | 20:41 | [▶](https://www.youtube.com/watch?v=kRHLx088hyo) |
| **8-3** | **Pseudoknot-free structures** — Nussinov, with the non-crossing condition shown to be what makes the decomposition valid | 18:19 | [▶](https://www.youtube.com/watch?v=6ExWx5FSqlk) |
| **8-4** | **Refined energy models** — the Zuker-Stiegler step, hairpin/bulge/internal/multibranch, the V/W split | 8:58 | [▶](https://www.youtube.com/watch?v=Oqu6BHGl4y8) |
| 8-6 | Probabilistic Context-Free Grammars | 23:23 | [▶](https://www.youtube.com/watch?v=I59Xa58NzUg) |
| **8-7** | **Probabilistic Parsing** — CYK and inside-outside, the structural twin of McCaskill | 20:00 | [▶](https://www.youtube.com/watch?v=1jNUCNYwzcI) |

**Vienna RNA from its authors — the highest-value find in this family.**
**Ivo Hofacker**, 1:29:43, derives the energy model, the MFE recursions *and*
the McCaskill partition function and base-pair probability matrix in one sitting
([▶](https://www.youtube.com/watch?v=hrxPBdmm36w)). **Ronny Lorenz**, 1:29:12,
goes past the textbook model into soft constraints, SHAPE-directed folding and
the ensemble quantities RNAfold actually reports
([▶](https://www.youtube.com/watch?v=KW3Cz1IQPx8)).

**Comparative methods and the covariation argument:** Sebastian Will on Sankoff
simultaneous alignment-and-folding, two lectures
([▶](https://www.youtube.com/watch?v=k4hKRu8UpnA)
[▶](https://www.youtube.com/watch?v=mYsha_TONVs)) · **Elena Rivas on why
covariation evidence, not free energy, is the real arbiter of a claimed
structure** — the statistical counterweight to the whole MFE enterprise, 37:04
([▶](https://www.youtube.com/watch?v=XciIQulpGVY)).

**Course lectures:** Christopher Burge (MIT 7.91J), 1:22:40
([▶](https://www.youtube.com/watch?v=kUN6rJ21Hno)) · Manolis Kellis (MIT 6.047)
([▶](https://www.youtube.com/watch?v=s3nMNAa-CdQ)) · Matthew Macauley's
combinatorial derivation ([▶](https://www.youtube.com/watch?v=HaGNjmbvGKo)).

**Linear-time methods — Liang Huang's line:** LinearFold
([▶](https://www.youtube.com/watch?v=0jP77tZkyyU)) · **LinearPartition**, which
is linear-time McCaskill ([▶](https://www.youtube.com/watch?v=nKaYyQGKsm4)) ·
the ISMB keynote on the whole Linear* family, including why beam pruning is
often *more* accurate on long sequences
([▶](https://www.youtube.com/watch?v=nDobViWTsZo)) · **Parsing Algorithms for
COVID-19**, Huang to an NLP audience, which is the clearest statement anywhere
of why RNA folding *is* parsing ([▶](https://www.youtube.com/watch?v=FPoEVj-T9Bw)).

**Grammars, homology and pseudoknots:** Rfam and Infernal covariance models
(EMBL-EBI, [▶](https://www.youtube.com/watch?v=NU63fazDZHs)) · **Anne Condon on
which pseudoknot classes are polynomial and which are NP-hard**
([▶](https://www.youtube.com/watch?v=WGe9OcFOiIw)) · Hosna Jabbari on Knotty and
HFold ([▶](https://www.youtube.com/watch?v=p_SE6pVi9c4)) · Henri Orland's
statistical-physics genus expansion
([▶](https://www.youtube.com/watch?v=Edz7ihsSZZ4)) · **Yann Ponty defending the
DP tradition against the deep-learning wave**
([▶](https://www.youtube.com/watch?v=hpqWv7cyVYY)).

**Papers:** **Nussinov & Jacobson 1980, *PNAS* 77:6309** · **Zuker & Stiegler
1981, *NAR* 9:133** · **McCaskill 1990, *Biopolymers* 29:1105** ·
Sankoff 1985, *SIAM J Appl Math* 45:810 · Eddy & Durbin 1994, *NAR* 22:2079 ·
**Rivas, Clements & Eddy 2017, *Nat Methods* 14:45** · Rivas & Eddy 1999,
*JMB* 285:2053 · Do, Woods & Batzoglou 2006, *Bioinformatics* 22:e90
(CONTRAfold) · Lorenz et al. 2011, *Algorithms Mol Biol* 6:26 (ViennaRNA) ·
Huang et al. 2019, *Bioinformatics* 35:i295 (LinearFold).

> **Derivation checkpoint 71.** Derive the Nussinov recursion and prove the
> non-crossing condition is what makes the interval decomposition valid. Then
> state exactly what the Zuker loop model adds, and why the partition function
> needs a *different* recursion rather than the same one with a max replaced by
> a sum. Wild 8-3, 8-4 and 8-7 are the three lectures that get you there.

---

## T.3 Thermodynamics and nearest-neighbour parameters

**This is the weakest-covered topic in the family relative to its importance**,
and the gap is specific: the people who built the parameter sets left no
lectures.

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **Nearest Neighbor Method** | Albert Courey (UCLA) | 24:25 | [▶](https://www.youtube.com/watch?v=jy5h9NwBEgk) |
| **Using Energy Values in Eterna** — the Turner rules made operational | Eterna community | 1:03:27 | [▶](https://www.youtube.com/watch?v=TRVJ7Uxv7Q8) |
| RNA, Mechanics, and the Partition Function | Jennifer Pearl (Eterna) | 55:40 | [▶](https://www.youtube.com/watch?v=2bq4an3uHGs) |
| Folding engines, models and thermodynamics | Eterna community | 39:07 | [▶](https://www.youtube.com/watch?v=mmdiGHgwYko) |
| High-throughput RNA tertiary contact thermodynamics | Joseph Yesselman (Nebraska) | 56:54 | [▶](https://www.youtube.com/watch?v=baRPkvAo0t0) |
| Thermodynamics of RNA structures by Wang-Landau sampling | Peter Clote (Boston College) | 29:13 | [▶](https://www.youtube.com/watch?v=35EmgGl-bZk) |

**The Courey lecture is the one real nearest-neighbour derivation on YouTube** —
thermodynamic relationships, duplex ΔH and ΔS, a worked calculation, the Tm
equation, and how the parameters were measured.

> **Honest gap: Doug Turner, David Mathews and John SantaLucia have no recorded
> lectures.** These are the people whose measurements every RNA folding program
> depends on. **Read instead:** SantaLucia 1998, *PNAS* 95:1460 · Mathews et al.
> 1999, *JMB* 288:911 and 2004, *PNAS* 101:7287 · **Turner & Mathews 2010,
> *NAR* 38:D280 (the NNDB)**. **Derivation checkpoint 6** in Module B.4 is the
> exercise.

---

## T.4 Chemical probing — what the data actually constrains

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **Chemically probing RNA-protein networks inside cells** | Chase Weidmann (Michigan, Weeks alum) | 1:00:53 | [▶](https://www.youtube.com/watch?v=t--WnACI4cY) |
| Mapping protein interaction networks on RNA (ISMB keynote) | Chase Weidmann | 28:14 | [▶](https://www.youtube.com/watch?v=tZsvAwr6to8) |
| **DMS mapping of higher-order structure and folding thermodynamics** | Anthony Mustoe (Baylor) | 58:03 | [▶](https://www.youtube.com/watch?v=DgZsPJ69_k0) |
| **Low-energy RNA fluctuations measured by chemical probing (PRIME)** | Edric Choi (Lucks lab) | 59:32 | [▶](https://www.youtube.com/watch?v=ITphUNFfnm4) |
| Drugging RNA Structure | **Silvi Rouskin** (HMS) | 56:31 | [▶](https://www.youtube.com/watch?v=bMVe8U5u6AA) |
| Landscape and variation of RNA secondary structures in the human transcriptome | Yue Wan (A*STAR) | 30:40 | [▶](https://www.youtube.com/watch?v=yg_q9BCzGCk) |
| In-cell ensemble mapping of structural switches | Danny Incarnato (Groningen) | 1:10:34 | [▶](https://www.youtube.com/watch?v=pwinGjkcPtM) |
| **Automated recognition of functional RNA elements by SHAPE signatures** | Sharon Aviran (UC Davis) | 46:58 | [▶](https://www.youtube.com/watch?v=xRMv6r8jbAY) |
| **Sparse Reconstruction of RNA Structure Landscapes** | Sharon Aviran (UC Davis) | 48:30 | [▶](https://www.youtube.com/watch?v=rvS2tC-uhMg) |
| Visualizing RNA Structural Dynamics Using NMR | **Hashim Al-Hashimi** (Columbia) | 20:52 | [▶](https://www.youtube.com/watch?v=O6XtwSFIbnw) |
| NMR contributions to RNA structural biology and viral genomes | Harald Schwalbe (Frankfurt) | 1:01:32 | [▶](https://www.youtube.com/watch?v=rvG-bTkQ6Dc) |
| Hydroxyl radical footprinting | Schlatterer (Brenowitz lab) | 13:40 | [▶](https://www.youtube.com/watch?v=aIXvVCjfdzc) |

> **Aviran's *Sparse Reconstruction* talk is the sharpest statement of what
> probing data actually constrains**: one averaged reactivity vector, many
> possible underlying populations. It is an inverse problem and it is
> ill-posed. Everyone who uses SHAPE restraints should watch it.
>
> **Choi's PRIME result is the number to remember:** base pairs dynamically open
> at **0.5–3 kcal/mol, roughly half the commonly inferred values.** RNA samples
> open states far more accessible than the models assume.

**Papers:** **Merino et al. 2005, *JACS* 127:4223 (SHAPE)** · Deigan et al.
2009, *PNAS* 106:97 · Siegfried et al. 2014, *Nat Methods* 11:959 (SHAPE-MaP) ·
Zubradt et al. 2017, *Nat Methods* 14:75 (DMS-MaPseq) · Spitale et al. 2015,
*Nature* 519:486 (icSHAPE) · Tomezsko et al. 2020, *Nature* 582:438 (DREEM) ·
Dethoff et al. 2012, *Nature* 491:724 (excited states by NMR).

> **The most surprising absence in this entire curriculum: Kevin Weeks has no
> recorded lecture anywhere.** SHAPE is his, and the search was exhaustive. Teach
> the lineage through his descendants — Weidmann, Mustoe, Choi — and read the
> papers. **Sarah Woodson is likewise absent**, with only a three-minute
> interview; read Woodson 2010, *Annu Rev Biophys* 39:61.

---

## T.5 Ribozymes and catalytic RNA

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **Discovering Ribozymes** | **Tom Cech** (iBiology) | 10:06 | [▶](https://www.youtube.com/watch?v=WAChisSiW3o) |
| Ribozymes, Telomerase, Aging, and Cancer | Tom Cech | 1:16:44 | [▶](https://www.youtube.com/watch?v=qJuGxHucqZk) |
| The Magic of RNA: From CRISPR to Coronavirus Vaccines | Tom Cech | 1:06:18 | [▶](https://www.youtube.com/watch?v=UtQkoW8yQ4A) |
| **Ribonuclease P: A Small Step in the RNA World** | **Sidney Altman** (Yale) | 51:01 | [▶](https://www.youtube.com/watch?v=uVMTWaqtL4o) |
| **How does RNA act like an enzyme?** | **David Lilley** (Dundee) | 38:28 | [▶](https://www.youtube.com/watch?v=1qJ8Fs56X84) |
| The extent of RNA catalysis — are there any limits? | David Lilley (MRC LMB) | 34:20 | [▶](https://www.youtube.com/watch?v=SQwO0qEbCQc) |
| **From Structure and Function of Ribosomes to New Antibiotics** | **Thomas Steitz** (Yale) | 51:04 | [▶](https://www.youtube.com/watch?v=FgEeLRTGKwc) |
| The Amazing Ribosome and its Origin | **Ada Yonath** (Weizmann) | 1:34:41 | [▶](https://www.youtube.com/watch?v=eliC9aM5BsA) |
| **Ribosomal RNA: The Kernel of Life** | **Harry Noller** (UCSC) | 39:58 | [▶](https://www.youtube.com/watch?v=rlFo77klWNg) |
| The Story of Deciphering the Ribosome | **Venki Ramakrishnan** (MRC LMB) | 1:06:42 | [▶](https://www.youtube.com/watch?v=RYVdDJ1cFrM) |
| ASBMB Plenary Lecture (group II introns) | **Anna Marie Pyle** (Yale) | 38:44 | [▶](https://www.youtube.com/watch?v=j8t4qoBi2lk) |
| **Pyle Part 1: RNA Structure** (iBiology) | Anna Marie Pyle | 23:04 | [▶](https://www.youtube.com/watch?v=WCrlm18KQ48) |
| Pyle Part 2: Inside an RNA Splicing Machine | Anna Marie Pyle | 28:55 | [▶](https://www.youtube.com/watch?v=ESXo3fTThBI) |
| Pyle Part 3: RNA Helicases | Anna Marie Pyle | 32:16 | [▶](https://www.youtube.com/watch?v=LjCDqL8n5F0) |
| Evolution of Nucleic Acids Under Abiological Conditions | **Gerald Joyce** (Scripps) | 23:38 | [▶](https://www.youtube.com/watch?v=_ayLUyNixI0) |
| Self-replicating synthetic systems | Gerald Joyce | 34:43 | [▶](https://www.youtube.com/watch?v=xz9SqM5RHj8) |
| RNA polymerase ribozyme program | **Philipp Holliger** (MRC LMB) | 1:02:23 | [▶](https://www.youtube.com/watch?v=WrygFFc8t8E) |
| The Origin of Cellular Life on Earth | **Jack Szostak** (Harvard) | 54:40 | [▶](https://www.youtube.com/watch?v=PqPGOhXoprU) |
| **CRISPR systems** (Rosalind Franklin Lecture) | **Jennifer Doudna** (Berkeley) | 1:15:53 | [▶](https://www.youtube.com/watch?v=jiK5taZEzyY) |

**Lilley's *How does RNA act like an enzyme?* is the best mechanism lecture on
the nucleolytic ribozymes** — general acid-base catalysis across hammerhead,
hairpin and glmS. **Pyle Part 1 is the best free introduction to RNA tertiary
structure anywhere.**

> **A note on the Doudna choice.** Her actual Nobel Lecture contains zero
> mentions of ribozymes or the group I intron. This lecture narrates the
> ribozyme-to-CRISPR arc, which is the intellectually honest lineage: Cate et
> al. 1996, *Science* 273:1678 leads to Jinek et al. 2012, *Science* 337:816.

**Papers:** **Kruger et al. 1982, *Cell* 31:147** · **Guerrier-Takada et al.
1983, *Cell* 35:849** · Ban et al. 2000 and Nissen et al. 2000, *Science*
289:905 and 289:920 · **Noller, Hoffarth & Zimniak 1992, *Science* 256:1416** ·
Toor et al. 2008, *Science* 320:77 · Lincoln & Joyce 2009, *Science* 323:1229 ·
Johnston et al. 2001, *Science* 292:1319.

---

## T.6 Riboswitches and RNA regulation

**Ron Breaker** — *The RNA World*, 58:09
([▶](https://www.youtube.com/watch?v=II1R3YV1whg)) · **Ancient RNA Relics and
Modern Drug Discovery** (NIH Director's Lecture), 1:10:23
([▶](https://www.youtube.com/watch?v=2dYabVyFFKo)) · ASBMB-Merck Award Lecture
([▶](https://www.youtube.com/watch?v=5nIrkXPakzI)) · **the comparative-genomics
discovery method** behind the new riboswitch and ribozyme classes
([▶](https://www.youtube.com/watch?v=Qa1G_dxUYwc)).

**Also:** Beatrix Suess on engineered riboswitches — the engineering counterpart
to Breaker's discovery work ([▶](https://www.youtube.com/watch?v=Ptsv5ZtnnXw)) ·
**Joan Steitz**, Mendel Lecture on viral and cellular noncoding RNAs, 1:14:35
([▶](https://www.youtube.com/watch?v=pJ-C7w7OO_A)) and the short iBiology
*SNURPs and Serendipity* ([▶](https://www.youtube.com/watch?v=7X9BgWE9NlI)).

**Papers:** **Winkler, Nahvi & Breaker 2002, *Nature* 419:952** ·
Weinberg et al. 2010, *Genome Biol* 11:R31 · Lerner & Steitz 1979, *PNAS*
76:5495.

---

## T.7 Three-dimensional structure prediction

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **Unlocking the RNA Universe** (ARES) | **Raphael Townshend** (Atomic AI) | 1:00:10 | [▶](https://www.youtube.com/watch?v=Z3e9fJ0fGs4) |
| **CASP15 RNA assessment** | **Eric Westhof** (Strasbourg) | 37:26 | [▶](https://www.youtube.com/watch?v=oVaABC2oTs0) |
| CASP16 RNA assessment | Eric Westhof | 22:45 | [▶](https://www.youtube.com/watch?v=6WTUflum_4A) |
| **Computer-based Predictions of RNA Structures: Where do we stand?** | Eric Westhof | 1:01:32 | [▶](https://www.youtube.com/watch?v=PBEPpLkRlOw) |
| CASP15 assessment | Marta Szachniuk (Poznań) | 16:19 | [▶](https://www.youtube.com/watch?v=hfzSQaVBBIo) |
| CASP15 (SimRNA) | Janusz Bujnicki (IIMCB) | 19:55 | [▶](https://www.youtube.com/watch?v=9hmyGS17sRk) |
| DeepFoldRNA | Robin Pearce (Michigan) | 59:28 | [▶](https://www.youtube.com/watch?v=ZsjA4iWZmiA) |
| trRosettaRNA | Yang & Wang (Shandong) | 1:00:39 | [▶](https://www.youtube.com/watch?v=LTp21NolEak) |
| **RoseTTAFoldNA** | **Frank DiMaio** (IPD) | 1:04:00 | [▶](https://www.youtube.com/watch?v=8qWrEAyB1Ok) |
| **Limits of deep-learning-based RNA prediction** | Marko Ludaic | 31:09 | [▶](https://www.youtube.com/watch?v=NMfwfwVJbBQ) |
| **Has AlphaFold3 achieved success for RNA?** | Clément Bernard (Évry) | 24:12 | [▶](https://www.youtube.com/watch?v=0xN_fwjFtOI) |
| **Ab initio RNA ensembles with RNAnneal** | **Pratyush Tiwary** (Maryland) | 1:00:19 | [▶](https://www.youtube.com/watch?v=OZQeE4J4YA8) |
| **RNA with water, Mg²⁺ ions and chemical probes** | **Giovanni Bussi** (SISSA) | 33:31 | [▶](https://www.youtube.com/watch?v=NRCgrG-QWHI) |
| Simulations of RNA and RNP; fitting cryo-EM | Karissa Sanbonmatsu (LANL) | 55:56 | [▶](https://www.youtube.com/watch?v=TXlFprgadxA) |
| A Bottom-Up Approach to RNA Architecture | Bohdan Schneider (Czech Acad.) | 1:01:24 | [▶](https://www.youtube.com/watch?v=jCUhNEvS4Sw) |
| **X3DNA-DSSR: structural bioinformatics of nucleic acids** | Xiang-Jun Lu (Columbia) | 58:43 | [▶](https://www.youtube.com/watch?v=0l22ixzYEDU) |
| Non-canonical base pair interactions | Jérôme Waldispühl (McGill) | 38:02 | [▶](https://www.youtube.com/watch?v=-3Vp1MZ2isc) |
| **Hidden errors in cryo-EM and crystal structure models** | Grzegorz Chojnowski (EMBL) | 1:04:05 | [▶](https://www.youtube.com/watch?v=aNrtHMQJqy0) |

**Townshend's ARES talk is the single most important data point in T.10**: an
accurate scoring function learned from only **eighteen** known RNA structures.
**Pair it immediately with Ludaic's *Limits of deep-learning-based RNA
prediction***, which is the explicit skeptic's talk.

**Chojnowski's talk belongs here and is easy to skip:** the ground truth is not
as solid as the benchmarks assume. Read it before trusting any RNA RMSD.

**Papers:** **Townshend et al. 2021, *Science* 373:1047 (ARES)** ·
Das et al. 2023, *Proteins* (CASP15) · Westhof et al. 2026, *Proteins* (CASP16) ·
Pearce et al. 2022, *Nat Commun* 13:5093 · Wang et al. 2023, *Nat Commun*
14:7266 · **Baek et al. 2024, *Nat Methods* 21:117 (RoseTTAFoldNA)** ·
**Leontis & Westhof 2001, *RNA* 7:499 (base-pair classification)** ·
**Bernard et al. 2025, *Acta Cryst* D81 (Has AlphaFold3 achieved success for
RNA?)**.

---

## T.8 RNA design

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **gRNAde — geometric deep learning for 3D RNA inverse design** | Chaitanya Joshi (Cambridge) | 1:03:01 | [▶](https://www.youtube.com/watch?v=_MiGPjS-aIA) |
| 3D RNA Design with Deep Learning | Chaitanya Joshi (Eternacon) | 26:35 | [▶](https://www.youtube.com/watch?v=giQplhQdVDE) |
| **RNA design in theory and practice** (inverse folding, 90 min) | **Sven Findeiß** (Leipzig/Vienna) | 1:31:18 | [▶](https://www.youtube.com/watch?v=eEVME4dLT7A) |
| RNA Design: From Discrete to Continuous Optimization | Liang Huang | 24:56 | [▶](https://www.youtube.com/watch?v=qjYcbRztPKI) |
| **LinearDesign: optimized mRNA design** | Liang Huang | 19:13 | [▶](https://www.youtube.com/watch?v=18ymep_7fsE) |
| RNA origami | Ewan McRae (Houston Methodist) | 49:18 | [▶](https://www.youtube.com/watch?v=nzrBUXfvwf4) |
| Crowdsourced design of RNA molecular switches | Stohr & Townley (Eterna) | 47:12 | [▶](https://www.youtube.com/watch?v=whVa8JMdAQI) |
| Predicting mutations that stabilize the ribosome | Kate Shulgina (Harvard) | 28:31 | [▶](https://www.youtube.com/watch?v=D5m7oCgZkGs) |
| Scalable platforms for RNA sensors and controllers | Christina Smolke (Stanford) | 1:02:27 | [▶](https://www.youtube.com/watch?v=Y6JoSBJ9Mn0) |
| Aptamers and SELEX | Paloma Giangrande (OTS) | 31:57 | [▶](https://www.youtube.com/watch?v=ZQujMqXm2wQ) |

**LinearDesign solves joint codon-and-structure optimization as a lattice
parsing problem** — the mRNA stability question answered by an algorithm rather
than by screening. **Findeiß's ninety minutes is the inverse-folding lecture.**

**Papers:** Joshi et al. 2025, ICLR (gRNAde) · **Zhang et al. 2023, *Nature*
621:396 (LinearDesign)** · Geary, Rothemund & Andersen 2014, *Science* 345:799
(RNA origami) · **Tuerk & Gold 1990, *Science* 249:505** and Ellington &
Szostak 1990, *Nature* 346:818 (SELEX).

---

## T.9 Biophysics — the ion atmosphere

**This is the thinnest cluster, and the thinness is itself the finding.**

**Lois Pollack** on time-resolved scattering to watch RNA fold, 53:34
([▶](https://www.youtube.com/watch?v=4rLZsMjxn-I)) · Wide-angle X-ray scattering
of structured RNA, including the ill-posedness of 1D → 3D
([▶](https://www.youtube.com/watch?v=uaiaH-bjD10)) · **Bussi's talk is the
closest thing to a dedicated ion-atmosphere lecture that exists**
([▶](https://www.youtube.com/watch?v=NRCgrG-QWHI)) · Al-Hashimi on transient and
excited states ([▶](https://www.youtube.com/watch?v=CRBcq4gkX1M)) ·
Felix Ritort on single-molecule pulling
([▶](https://www.youtube.com/watch?v=0bXu42sex8c)).

**Papers:** **Draper 2004, *RNA* 10:335** · **Lipfert, Doniach, Das & Herschlag
2014, *Annu Rev Biochem* 83:813** · Liphardt et al. 2001, *Science* 292:733.

---

## T.10 Why RNA structure prediction trails protein structure prediction

**The question answered with evidence rather than folklore.** Six causes recur,
and they are not equally weighted.

**1. The training data is roughly a hundredfold smaller, and more redundant than
it looks.** A direct RCSB PDB query on 2026-10-04 returns **255,456 entries
containing protein, 10,475 containing RNA, and only 2,378 that are RNA-only.**
That RNA-only set is dominated by redundant tRNAs, ribozymes and riboswitches,
so the effective number of independent folds is smaller still. Townshend et al.
state the consequence plainly: ARES was *"trained with only 18 known RNA
structures,"* and the architectural contribution is framed as a way to work
around having no data. **This is why Das's program is a data-manufacturing
program rather than an architecture program.**

**2. Deep learning did not win the first fair contest.** The CASP15 assessment
is explicit: the top three groups *"did not use deep learning,"* and
*"predictions from deep learning approaches were significantly worse."* That is
the exact inverse of CASP13 and CASP14 for proteins. **It held in 2026 too** —
the Kaggle RNA 3D Folding Challenge was won by template-based methods.

**3. The failure is in base-pair geometry, not the global fold — and
protein-derived metrics hide this.** CASP15 found that models *"correctly
predicted the global fold"* while *"challenges remain in modeling fine details
such as noncanonical pairs."* The CASP16 assessment sharpens it: good secondary
structure *"is insufficient to guarantee chemical precision or to correctly
identify residues involved in non-Watson-Crick interactions."* Proteins have one
backbone torsion problem and twenty side chains. RNA has four bases but
**twelve geometric base-pair families** in the Leontis-Westhof classification, a
six-torsion backbone, and sugar pucker. GDT and lDDT were built for proteins.

**4. RNA is an ensemble, and so is the experimental ground truth.** CASP15 lists
*"prediction of multiple structures resolved by cryo-EM or crystallography"* as
an open problem — the target is not a single structure. PRIME quantifies the
floor: base pairs open at 0.5–3 kcal/mol, about half commonly inferred values.

**5. The ion atmosphere is a real physical term that essentially no predictor
models.** RNA is a dense polyanion that cannot fold without counterions,
Mg²⁺ especially. Predictors output coordinates in a vacuum while the folded
state's stability depends on an ion distribution they never compute. **Protein
folding has no comparable term.**

**6. There was no CASP-grade assessment until 2022.** RNA-Puzzles launched in
2011 but was smaller and less adversarial. CASP15 was, in the assessors' words,
*"the first CASP exercise that involved RNA structure modeling."* Protein
prediction had fourteen CASP rounds before AlphaFold2. **RNA has had two.**

> **The synthesis worth carrying.** Causes 1 and 6 are contingent and are being
> fixed — by Ribonanza-style data manufacturing and by CASP's new RNA category.
> **Causes 3, 4 and 5 are structural facts about the molecule and will not be
> fixed by scale alone.** That is the honest read, and it is also the argument
> for why Das's data-first strategy is the right bet on the fixable half.
>
> **A caution on the general-model claim.** AlphaFold3 asserts *"much higher
> accuracy for protein-nucleic acid interactions compared with
> nucleic-acid-specific predictors."* That was tested independently and did not
> hold cleanly: Bernard et al. 2025 benchmark AF3 across five test sets against
> ten methods and conclude the limitations for RNA *"are unclear,"* because the
> AF3 paper reported only the CASP-RNA set. **Capstone IX is this question.**

---

## T.11 BUILD — Atlas T

1. **Implement Nussinov from scratch**, then the Zuker loop model, then
   McCaskill's partition function. Compare your base-pair probabilities to
   RNAfold's on the same sequence.
2. **Add SHAPE data as a soft constraint** and re-fold. Measure how much the
   prediction changes and whether it changes toward the known structure.
3. **Run the ensemble-deconvolution experiment.** Generate a synthetic mixture
   of two known structures, compute the population-averaged reactivity, then try
   to recover the two components. This is Aviran's ill-posed inverse problem,
   and doing it once will permanently change how you read a reactivity profile.
4. **Write the one page.** Given a reactivity vector, what can you and cannot you
   conclude? Be specific about where the information runs out.

**Derivation checkpoints due: 71, 72, 73.**

---

## T.12 Paired reading — Atlas T

| Watch this | Then read this | Hold this question |
|---|---|---|
| **Das, *BioML Seminar*** | **He et al. 2024 (Ribonanza)** | Four passes at one idea. What is the idea? |
| **Das, *CASP15 assessment*** | **Das et al. 2023, *Proteins*** | Deep learning lost. What does that tell you about data? |
| Wild 8-3 and 8-4 | **Nussinov & Jacobson 1980; Zuker & Stiegler 1981** | Why does non-crossing make the decomposition valid? |
| **Hofacker, *RNA secondary structures*** | **McCaskill 1990, *Biopolymers* 29:1105** | Why does the partition function need a different recursion? |
| Lorenz, *Improving prediction* | Lorenz et al. 2011 | What does a soft constraint do to the recursion? |
| **Rivas, *Evolutionary conservation*** | **Rivas et al. 2017, *Nat Methods* 14:45** | Covariation or free energy — which is the arbiter? |
| Huang, *Parsing Algorithms for COVID-19* | Huang et al. 2019 | RNA folding is parsing. What does that buy algorithmically? |
| Condon, *Computational Challenges* | **Rivas & Eddy 1999, *JMB* 285:2053** | Which pseudoknot classes are tractable, and why does the hierarchy stop? |
| Courey, *Nearest Neighbor Method* | **SantaLucia 1998, *PNAS* 95:1460** | Compute a Tm by hand. Why is RNA harder than DNA? |
| **Aviran, *Sparse Reconstruction*** | Her papers | One reactivity vector, many populations. What is determined? |
| Choi, *PRIME* | The PRIME paper | Base pairs open at half the assumed energy. What breaks? |
| **Townshend, *ARES*** | **Townshend et al. 2021, *Science* 373:1047** | Eighteen structures. How did that possibly work? |
| **Ludaic, *Limits of deep learning for RNA*** | Compare to the above | Which of the two is right, and on what evidence? |
| Bernard, *Has AlphaFold3 succeeded for RNA?* | **Bernard et al. 2025, *Acta Cryst* D81** | A general model's claim, independently tested. What held? |
| Bussi, *RNA is not alone* | **Draper 2004; Lipfert et al. 2014** | Quantify the ion-atmosphere contribution to stability. |
| Lilley, *How does RNA act like an enzyme?* | Lilley 2011, *Phil Trans R Soc B* 366:2910 | General acid-base catalysis without side chains. How? |
| Pyle, *RNA Structure* (Part 1) | **Leontis & Westhof 2001, *RNA* 7:499** | Learn the twelve base-pair families. They are the vocabulary. |
| Findeiß, *RNA design* | Lorenz et al. 2011 | Inverse folding against an energy model. Where does it fail? |
| Huang, *LinearDesign* | **Zhang et al. 2023, *Nature* 621:396** | Codon choice and structure jointly. What made it tractable? |
