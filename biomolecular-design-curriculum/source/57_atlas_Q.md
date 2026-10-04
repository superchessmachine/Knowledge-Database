# Atlas Q — Sequence and Language Models

> **Problem.** Learn a distribution over sequences from evolution alone, with no
> structures and no labels, and then use it to predict function, score variants,
> or generate new sequences.
>
> This family is the purest expression of the learning-first culture. It also
> contains the field's sharpest internal argument — **whether these models learn
> biology or learn the database** — and that argument has a clean experimental
> answer you will meet in Q.6.

---

## Q.1 The ESM line

| Talk | Speaker / host | Length | Link |
|---|---|---|---|
| **Evolutionary Scale Language Models** | Alexander Rives (MLCB 2023) | 54:32 | [▶](https://www.youtube.com/watch?v=TiDo7xXMbUI) |
| **ESM3: Simulating 500 million years of evolution** | Roshan Rao (ML4PE) | 1:05:08 | [▶](https://www.youtube.com/watch?v=qeqbm8a1-ZA) |
| Learning to read and write protein evolution | Brian Hie (Broad MIA) | 1:02:35 | [▶](https://www.youtube.com/watch?v=WF_9YPYS4V8) |
| Efficient evolution of human antibodies from general PLMs | Brian Hie (ML4PE) | 54:11 | [▶](https://www.youtube.com/watch?v=7szFo_IPUcE) |
| Early Career Seminar #3 | Brian Hie (ML4PE) | 49:35 | [▶](https://www.youtube.com/watch?v=dPNqe5uUOMM) |
| Multimodal Deep Learning for Protein Engineering | Kevin K. Yang (Valence) | 1:02:31 | [▶](https://www.youtube.com/watch?v=qFSVVWcCRHs) |
| Protein Language Models (tutorial) | RosettaCommons | 33:49 | [▶](https://www.youtube.com/watch?v=9DL1aX5fM_I) |
| **How to Make the Most of Your Masked LM for Protein Engineering** | Calvin McCarter, BigHat (ML4PE) | 53:10 | [▶](https://www.youtube.com/watch?v=Lcmo8wo54Uc) |
| Scaling down: MSA Pairformer | Yo Akiyama, MIT (ML4PE) | 37:59 | [▶](https://www.youtube.com/watch?v=poYqZ7Ml88E) |

**Papers:** **Rives et al. 2021, *PNAS* 118:e2016239118 (ESM-1b)** ·
**Lin et al. 2023, *Science* 379:1123 (ESM-2 / ESMFold)** · Hayes et al. 2025,
*Science* 387:850 (ESM3) · Hie et al. 2024, *Nat Biotechnol* 42:275 (antibody
evolution) · Meier et al. 2021, NeurIPS (ESM-1v zero-shot variant effects).

---

## Q.2 Generative protein language models

| Model | Talk | Speaker / host | Length | Link |
|---|---|---|---|---|
| ProtGPT2 | A Deep Unsupervised Language Model for Protein Design | Noelia Ferruz (ML4PE) | 1:05:20 | [▶](https://www.youtube.com/watch?v=BA5C0kLcErM) |
| ProtGPT2 / ZymCTRL | Early Career Seminar #2 | Noelia Ferruz (ML4PE) | 56:15 | [▶](https://www.youtube.com/watch?v=cwYuJfqzyRk) |
| **ProGen3** | Scaling Unlocks Broader Generation and Deeper Functional Understanding | Aadyot Bhatnagar, Profluent (ML4PE) | 1:07:20 | [▶](https://www.youtube.com/watch?v=843BIibICpU) |
| **PoET-2** | Understanding protein function with a multimodal retrieval-augmented foundation model | Tristan Bepler (ML4PE) | 54:12 | [▶](https://www.youtube.com/watch?v=Xa2yksdpUrI) |
| Dayhoff Atlas | Scaling sequence diversity for improved protein generation | Alex Lee, UCSF/MSR (ML4PE) | 57:46 | [▶](https://www.youtube.com/watch?v=ke8IJIOtV_Y) |
| DPLM | Diffusion Language Models Are Versatile Protein Learners | Zaixiang Zheng, ByteDance (ML4PE) | 1:13:19 | [▶](https://www.youtube.com/watch?v=JXrJavEJi80) |
| EvoDiff | Protein generation with evolutionary diffusion | Kevin Yang, MSR (ML4PE) | 59:46 | [▶](https://www.youtube.com/watch?v=e1e-_SkyNjw) |
| Discrete diffusion | Discrete diffusion models for generative protein design | Sarah Alamdari (BPDMC) | 1:00:13 | [▶](https://www.youtube.com/watch?v=iV_7mgxe4OI) |
| Walk-jump | Protein Discovery with Discrete Walk-Jump Sampling | Nathan Frey (Valence) | 55:11 | [▶](https://www.youtube.com/watch?v=O3YBEnvvPZY) |
| Guided discrete diffusion | Protein Design with Guided Discrete Diffusion | Stanton & Gruver (ML4PE) | 58:05 | [▶](https://www.youtube.com/watch?v=Hm8Z0SIyLqw) |
| Raygun | Template-based protein editing | Kapil Devkota, Duke (ML4PE) | 40:51 | [▶](https://www.youtube.com/watch?v=vDX3we6sim8) |
| Concept bottlenecks | Concept Bottleneck Language Models for Protein Design | Abdelsalam & Frey (ML4PE) | 51:46 | [▶](https://www.youtube.com/watch?v=wCvtjoON45E) |
| Reasoning models | Proteo-R1: Reasoning Foundation Models for De Novo Protein Design | ML4PE | 52:36 | [▶](https://www.youtube.com/watch?v=pRhjVfCo1KU) |
| **The CRISPR case** | Design of highly functional genome editors by modeling the universe of CRISPR-Cas sequences | Ruffolo & Nayfach, Profluent (ML4PE) | 1:00:14 | [▶](https://www.youtube.com/watch?v=gyn7UsSfc68) |

**Papers:** Ferruz et al. 2022, *Nat Commun* 13:4348 (ProtGPT2) ·
**Madani et al. 2023, *Nat Biotechnol* 41:1099 (ProGen)** · Nijkamp et al. 2023,
*Cell Systems* 14:968 (ProGen2) · **Truong & Bepler 2023, NeurIPS (PoET)** ·
Alamdari et al. 2023, bioRxiv (EvoDiff) · Ruffolo et al. 2024, *Nature* 637:1176
(OpenCRISPR-1) · Elnaggar et al. 2022, *IEEE TPAMI* 44:7112 (ProtTrans).

> **OpenCRISPR-1 is the strongest single existence proof in this family.** A
> language model trained on CRISPR-Cas sequences generated a gene editor that was
> hundreds of mutations from any natural protein and that worked in human cells.
> If you want one answer to "do PLMs learn biology," it is this talk — and then
> Q.6 is the counterargument.

---

## Q.3 Fitness prediction and variant effects

| Method | Talk | Speaker / host | Length | Link |
|---|---|---|---|---|
| EVE / DeepSequence | Structure &amp; fitness from genomic sequences | Debora Marks (Broad MIA) | 1:48:55 | [▶](https://www.youtube.com/watch?v=97q2wtoquQk) |
| Alignment-free | Alignment-free models for protein and antibody design | Marks & Kollasch (Broad MIA) | 1:40:20 | [▶](https://www.youtube.com/watch?v=GUt9NQcll5c) |
| Variant interpretation | Interpreting gene variants | Dias, Frazer & Shin (Broad MIA) | 1:37:29 | [▶](https://www.youtube.com/watch?v=KVzm0jN7Kfk) |
| **TranceptEVE** | Hybrid protein language models for fitness prediction | Pascal Notin (ML4PE) | 52:58 | [▶](https://www.youtube.com/watch?v=m0QVNWcRi8Y) |
| METL | Mutational Effect Transfer Learning for Protein Design | Sam Gelman (ML4PE) | 59:13 | [▶](https://www.youtube.com/watch?v=38M6kOTR5gI) |
| Evolutionary + experimental | Learning Protein Fitness Models from Evolutionary and Experimental Data | Chloe Hsu (ML4PE) | 56:51 | [▶](https://www.youtube.com/watch?v=UfeXApKTufQ) |
| Few-shot | Rapid protein evolution by few-shot learning with a PLM | Kaiyi Jiang, MIT (ML4PE) | 58:18 | [▶](https://www.youtube.com/watch?v=zV_yhnCxjuM) |
| Site-wise effects | Site-wise mutation effects enable combinatorial protein variant design | David Ding (ML4PE) | 51:49 | [▶](https://www.youtube.com/watch?v=OaOj3znHPn0) |
| **AlphaMissense** | AlphaMissense | Jun Cheng, DeepMind (Broad MIA) | 1:22:31 | [▶](https://www.youtube.com/watch?v=IuLuCbI5UG4) |
| 3D CNNs | Engineering Proteins with 3D Convolutional Neural Networks | Danny Diaz, UT Austin (ML4PE) | 1:12:19 | [▶](https://www.youtube.com/watch?v=Gaoeipwx5p4) |
| **Epistasis theory** | Sparsity, Epistasis, and Models of Fitness Functions | Aghazadeh & Brookes (Broad MIA) | 1:36:47 | [▶](https://www.youtube.com/watch?v=gxYd1cHmbl8) |
| **Distribution shift** | Conformal prediction under feedback covariate shift for biomolecular design | Clara Wong-Fannjiang (ML4PE) | 58:45 | [▶](https://www.youtube.com/watch?v=AOyDjBSQjhk) |
| **Distribution shift** | Beyond the training set: detecting distribution shift | Farhan Damani (MLCB 2023) | 24:14 | [▶](https://www.youtube.com/watch?v=DeHt1LgtjyQ) |
| Bayesian optimization | Bayesian Optimization of Antibodies Informed by a Generative Model of Evolving Sequences | Alan Amin, NYU (ML4PE) | 39:53 | [▶](https://www.youtube.com/watch?v=AqAiYfyuR6g) |
| Bayesian optimization | Pre-trained Ensembles for Bayesian Optimization of Protein Sequences | Ziyue Yang (Valence) | 49:01 | [▶](https://www.youtube.com/watch?v=o8vtTWjxrUQ) |

**Papers:** **Riesselman et al. 2018, *Nat Methods* 15:816 (DeepSequence)** ·
**Frazer et al. 2021, *Nature* 599:91 (EVE)** · Notin et al. 2022, ICML
(Tranception); Notin et al. 2023, NeurIPS (**ProteinGym**) · Cheng et al. 2023,
*Science* 381:eadg7492 (AlphaMissense) · Hopf et al. 2017, *Nat Biotechnol*
35:128 (EVcouplings) · Fannjiang & Listgarten 2020, NeurIPS (design by
adaptive sampling); Fannjiang et al. 2022, NeurIPS (conformal under FCS).

> **ProteinGym is the benchmark that disciplines this subsection.** When a talk
> claims a new state of the art on variant effect prediction, the first question
> is which ProteinGym split, and the second is whether the improvement survives
> the MSA-depth stratification. Many do not.
>
> The two distribution-shift talks are the theoretical core of the whole family,
> and they are the same argument Listgarten makes in Atlas R.10. Design queries
> a model outside its training distribution; conformal prediction under feedback
> covariate shift is the only entry here that tries to *quantify* that honestly.
> **Derivation checkpoint 45 lives in this pair.**

---

## Q.4 Interpretability of protein models

| Talk | Speaker / host | Length | Link |
|---|---|---|---|
| **InterPLM: Discovering Interpretable Features in PLMs via Sparse Autoencoders** | Elana Simon, Stanford (ML4PE) | 59:42 | [▶](https://www.youtube.com/watch?v=JlTLUObdO1A) |
| **Decomposing protein and genomic language models to understand what they learn** | Sergey Ovchinnikov (MLCB 2024) | 56:09 | [▶](https://www.youtube.com/watch?v=MZhEadNUSa4) |
| Small But Mighty: What an LSTM Reveals About Protein Design and About ML | Joanna Slusky (BPDMC) | 1:14:04 | [▶](https://www.youtube.com/watch?v=aBUjooyvdnk) |
| Towards biophysically interpretable sequence models | Maria Chikina (MLCB 2024) | 51:41 | [▶](https://www.youtube.com/watch?v=M5cgGPiTomY) |
| Singular value decomposition of protein sequences | Gina El Nesr (ML4PE) | 36:17 | [▶](https://www.youtube.com/watch?v=vJm31ewj9mw) |
| Jointly Embedding Protein Structures and Sequences through Residue Level Alignment | Foster Birnbaum (BPDMC) | 1:05:21 | [▶](https://www.youtube.com/watch?v=vGHrLbxyU-Y) |
| Adaptive Protein Tokenization | Rohit Dilip, Caltech (Valence) | 1:00:04 | [▶](https://www.youtube.com/watch?v=MrBl1w7XmgA) |
| CHEAP: Tokenized and Continuous Embedding Compressions | Amy Lu, Berkeley (Valence) | 1:27:22 | [▶](https://www.youtube.com/watch?v=4xdL067I0pw) |
| The Continuous Language of Protein Structure | Ben Murrell, Karolinska (Valence) | 55:56 | [▶](https://www.youtube.com/watch?v=lT6cRbjD1C8) |

**Papers:** Simon & Zou 2024, bioRxiv (InterPLM) · Rao et al. 2021, ICML
(MSA Transformer) · Vig et al. 2021, ICLR (BERTology meets biology — attention
recovers contacts) · Bhattacharya et al. 2022, *Bioinformatics* 38:ii119.

**This is the direct bridge to Part III.** InterPLM applies Anthropic's sparse
autoencoder method to a protein model; Ovchinnikov's MLCB talk is a structural
biologist doing mechanistic interpretability. Watch them alongside D.7, and note
that the *evaluation* problem is easier here: a protein feature can be checked
against a known binding site or a Pfam domain, which is a luxury language
interpretability does not have. That asymmetry is **Capstone VIII.**

---

## Q.5 Genomic and RNA language models

| Model | Talk | Speaker / host | Length | Link |
|---|---|---|---|---|
| **Evo** | Sequence modeling and design from molecular to genome scale | Nguyen & Hie (ML4PE) | 1:06:46 | [▶](https://www.youtube.com/watch?v=VhRBYcCyXlA) |
| **Evo 2** | Genome modeling and design across all domains of life | Garyk Brixi, Stanford (ML4PE) | 34:46 | [▶](https://www.youtube.com/watch?v=VraBp8uACec) |
| Genome design | Generative design of novel bacteriophages with genome language models | Samuel King (ML4PE) | 40:23 | [▶](https://www.youtube.com/watch?v=gBnwz6X9zYk) |
| Genome design | Generative Genome Design | King, primer by Hie (Broad MIA) | 2:00:11 | [▶](https://www.youtube.com/watch?v=BROeb0GWecM) |
| Nucleotide Transformer | The Nucleotide Transformer: building and evaluating robust foundation models | Thomas Pierrot, InstaDeep (MLCB) | 19:05 | [▶](https://www.youtube.com/watch?v=KKhtWU-eriY) |
| gLM | Genomic language model predicts protein co-regulation and function | Yunha Hwang (MLCB 2023) | 19:52 | [▶](https://www.youtube.com/watch?v=0GFi-TrUPDM) |
| gLM | Shedding light on functional dark matter with genomic language modeling | Yunha Hwang (BPDMC) | 46:39 | [▶](https://www.youtube.com/watch?v=G01tGkcw-OA) |
| OMG dataset | An Open MetaGenomic corpus for mixed-modality genomic language modeling | Andre Cornman (ML4PE) | 20:38 | [▶](https://www.youtube.com/watch?v=QW-9gdYxO9U) |
| **Enformer / Borzoi lineage** | Personal genome interpretation with sequence-to-function models | Nilah Ioannidis, Berkeley (MLCB) | 51:35 | [▶](https://www.youtube.com/watch?v=IN2UhYBeSx4) |
| | Sequence basis of transcription initiation in the human genome | Jian Zhou, UTSW (MLCB) | 47:59 | [▶](https://www.youtube.com/watch?v=HDhU-MUB85o) |
| | Fine-tuning on Personal Genomes Improves Expression prediction | Shiron Drusinsky, UCSF (MLCB) | 19:53 | [▶](https://www.youtube.com/watch?v=rZXXdaGib-s) |
| **Benchmark critique** | **DART-Eval: a comprehensive benchmark for DNA language models** | Wang, Patel & Singhal, Stanford (MLCB) | 19:36 | [▶](https://www.youtube.com/watch?v=399s7HT9Db4) |
| RNA structure | RNA Function, Design, and Modeling | Silvi Rouskin, HMS (BPDMC) | 59:33 | [▶](https://www.youtube.com/watch?v=oS_Cb-YMymw) |
| RNA structure | AI-Driven RNA Structure Prediction | Mile Šikić (MLSB 2025) | 24:37 | [▶](https://www.youtube.com/watch?v=7JNhul_NSeo) |
| RNA design | gRNAde: Geometric Deep Learning for 3D RNA inverse design | Chaitanya Joshi, Cambridge (Valence) | 1:06:02 | [▶](https://www.youtube.com/watch?v=0i1-ada-HmM) |
| RNA design | RNA-FrameFlow: Flow Matching for RNA backbone generation | Rishabh Anand, NUS (MLCB) | 23:44 | [▶](https://www.youtube.com/watch?v=L70YMobBKL0) |
| RNA geometry | Beyond Sequence: Impact of Geometric Context for RNA Property Prediction | Valence | 53:32 | [▶](https://www.youtube.com/watch?v=oHWT8OeAbJ8) |
| RNA foundation | A long-context RNA foundation model for predicting transcriptome architecture | Ali Saberi (Valence) | 1:29:27 | [▶](https://www.youtube.com/watch?v=JaDkn0cPzUE) |
| RNA structure code | Deciphering the RNA structural code | Khoroshkin & Karimzadeh (Broad MIA) | 1:42:39 | [▶](https://www.youtube.com/watch?v=-qmIL5IZ06g) |
| DNA design | Designing DNA with Tunable Regulatory activity | Anirban Sarkar, CSHL (MLCB) | 20:08 | [▶](https://www.youtube.com/watch?v=0AkODFVvlfw) |
| DNA design | Deep exploration networks for engineering functional DNA sequences | Johannes Linder, UW (MLCB 2019) | 13:24 | [▶](https://www.youtube.com/watch?v=IG4SaU4jRJI) |
| Hybrid design | A high-level design language for generative biology with Proto | Aditi Merchant, Stanford/Arc (ML4PE) | 58:56 | [▶](https://www.youtube.com/watch?v=Iy7rX2uVOK0) |

**Papers:** **Nguyen et al. 2024, *Science* 386:eado9336 (Evo)** · Brixi et al.
2025, bioRxiv (Evo 2) · Nguyen et al. 2023, NeurIPS (HyenaDNA) · Dalla-Torre
et al. 2025, *Nat Methods* 22:287 (Nucleotide Transformer) · **Avsec et al.
2021, *Nat Methods* 18:1196 (Enformer)** · Linder et al. 2025, *Nat Methods*
22:2422 (Borzoi) · **Avsec et al. 2025, *Nature* (AlphaGenome)** ·
Townshend et al. 2021, *Science* 373:1047 (ARES, RNA) ·
Wayment-Steele et al. 2022, *Nat Methods* 19:1234 (EternaFold).

> **Rhiju Das's thread runs through here.** ARES is his, EternaFold comes from
> Eterna, and the RNA design entries are where the Atlas comes closest to his
> program. Note the structural fact worth holding onto: **RNA structure
> prediction remains visibly behind protein structure prediction**, and the CASP
> and RNA-Puzzles results say so plainly. That is one of the most honest open
> problems in the entire Atlas — and it is the subject of Capstone IX.

---

## Q.6 Function prediction and search

| Method | Talk | Speaker / host | Length | Link |
|---|---|---|---|---|
| **CLEAN** | Enzyme function prediction using contrastive learning | Tianhao Yu, UIUC (ML4PE) | 54:16 | [▶](https://www.youtube.com/watch?v=DekVDA_25N4) |
| **Foldseek** | Exploring the Protein Universe | Martin Steinegger, SNU (Broad MIA) | 1:17:41 | [▶](https://www.youtube.com/watch?v=lHNeBIGkroM) |
| Domain-PFP | Protein function prediction using function-aware domain embeddings | Nabil Ibtehaz, Purdue (ML4PE) | 57:46 | [▶](https://www.youtube.com/watch?v=IZmIiIWbsjA) |
| CAFA | Kaggle 1st place: CAFA 5 Protein Function Prediction | GoCurator, Fudan (ML4PE) | 35:49 | [▶](https://www.youtube.com/watch?v=FO7BI2Tud40) |
| Substrate prediction | A general model to predict small molecule substrates of enzymes | Alexander Kroll (ML4PE) | 57:47 | [▶](https://www.youtube.com/watch?v=ZDi0Wx1O8U0) |
| **CARE benchmark** | A Benchmark Suite for the Classification and Retrieval of Enzymes | Jason Yang, Caltech (ML4PE) | 47:02 | [▶](https://www.youtube.com/watch?v=cP2vH8mChzE) |
| ProTrek | Navigating the Protein Universe through Tri-Modal Contrastive Learning | Jin Su, Westlake (ML4PE) | 48:35 | [▶](https://www.youtube.com/watch?v=wp0UirWDeMo) |
| Multimodal | Multimodal protein language models for deciphering protein function | Zitnik Lab (Broad MIA) | 1:30:33 | [▶](https://www.youtube.com/watch?v=LcLmvtXHI1s) |
| PTMs | PTM-Mamba: A PTM-Aware Protein Language Model | Zhangzhi Peng, Duke (ML4PE) | 46:47 | [▶](https://www.youtube.com/watch?v=mjmw7rjxOs4) |
| Fold recognition | Protein Fold Recognition with Recurrent Kernel Networks | Dexiong Chen, Inria (MLCB) | 11:54 | [▶](https://www.youtube.com/watch?v=8wy__P9oMKA) |

**Papers:** **Yu et al. 2023, *Science* 379:1358 (CLEAN)** ·
**van Kempen et al. 2024, *Nat Biotechnol* 42:243 (Foldseek)** ·
Steinegger & Söding 2017, *Nat Biotechnol* 35:1026 (MMseqs2) ·
Radivojac et al. 2013, *Nat Methods* 10:221 (CAFA) · Barrio-Hernandez et al.
2023, *Nature* 622:637 (AFDB clustering).

> **The CARE benchmark talk is the one that closes the argument opened in Q.2.**
> It shows that when enzyme function prediction is evaluated with splits that
> enforce genuine sequence novelty, performance drops sharply — these models are
> substantially doing retrieval. Hold that against OpenCRISPR-1, which clearly
> generalized. Both are true. **Reconciling them is derivation checkpoint 46**,
> and it is the single most interesting unresolved question in Atlas Q.

---

## Q.7 BUILD — Atlas Q

1. **Score a DMS dataset** from ProteinGym with ESM-2 (zero-shot, masked-marginal),
   an MSA-based model (EVE or EVcouplings), and a simple site-independent
   frequency baseline. Report Spearman for each.
2. **Stratify by MSA depth.** Re-plot the three Spearmans against the depth of
   the target's alignment. The ordering usually inverts somewhere.
3. **Construct the retrieval test.** Hold out sequences by cluster identity at
   30%, 50% and 90%, retrain or re-evaluate, and plot performance against
   identity threshold. This is the CARE experiment on your own data.
4. **Write the one page.** At what sequence identity to the training set does
   your model stop knowing anything? Name the number.

**Derivation checkpoints due: 44, 45, 46.**

---

## Q.8 Paired reading — Atlas Q

| Watch this | Then read this | Hold this question |
|---|---|---|
| Rives, *Evolutionary Scale LMs* | **Rives et al. 2021, *PNAS* 118:e2016239118** | What does "unsupervised" mean when the data is a curated database? |
| Rao, *ESM3* | Lin et al. 2023, *Science* 379:1123; Hayes et al. 2025, *Science* 387:850 | ESMFold is fast and less accurate than AF2. Where exactly is the trade? |
| Ferruz, *ProtGPT2* | Ferruz et al. 2022, *Nat Commun* 13:4348 | Generated sequences look natural. What fraction folded? |
| **Ruffolo & Nayfach, *OpenCRISPR*** | **Ruffolo et al. 2024, *Nature* 637:1176** | Hundreds of mutations from anything natural, and it works. What generalized? |
| Bepler, *PoET-2* | Truong & Bepler 2023, NeurIPS | Retrieval-augmented, explicitly. Is that a concession or a design? |
| Marks, *Structure & fitness from sequences* | **Hopf et al. 2017, *Nat Biotechnol* 35:128; Riesselman et al. 2018, *Nat Methods* 15:816** | Couplings are statistical. When do they mean contact and when not? |
| Notin, *TranceptEVE* | **Notin et al. 2023, NeurIPS (ProteinGym)** | Look at the per-assay table, not the mean. Where does it fail? |
| Cheng, *AlphaMissense* | Cheng et al. 2023, *Science* 381:eadg7492 | Clinical variant classification. What is the circularity risk in the labels? |
| **Wong-Fannjiang, *Conformal prediction under FCS*** | Fannjiang et al. 2022, NeurIPS | Write the feedback loop formally. Why does ordinary conformal fail? |
| Aghazadeh & Brookes, *Sparsity and epistasis* | Their paper + Poelwijk et al. 2019, *Nat Commun* 10:4213 | Fitness landscapes are sparse in a Fourier basis. What does that license? |
| **Simon, *InterPLM*** | Simon & Zou 2024, bioRxiv | SAE features in a protein model. How were they validated, and could language do that? |
| **Ovchinnikov, *Decomposing protein and genomic LMs*** | Vig et al. 2021, ICLR | What is actually in the attention maps? |
| Nguyen & Hie, *Evo* | **Nguyen et al. 2024, *Science* 386:eado9336** | A single model across DNA, RNA, protein. What does the shared representation buy? |
| Brixi, *Evo 2* | Brixi et al. 2025, bioRxiv | Scaling to whole genomes. What broke, and what was redesigned? |
| Ioannidis, *Personal genome interpretation* | **Avsec et al. 2021, *Nat Methods* 18:1196 (Enformer)** | Long-range regulation from sequence. How far does the receptive field reach? |
| **MLCB, *DART-Eval*** | The DART-Eval paper | Do DNA language models beat a well-tuned CNN? On which tasks? |
| Šikić, *RNA structure prediction* | **Townshend et al. 2021, *Science* 373:1047 (ARES)** | Why is RNA harder than protein? Name three structural reasons. |
| Joshi, *gRNAde* | The gRNAde paper | Inverse folding for RNA. What changes versus ProteinMPNN? |
| Yu, *CLEAN* | **Yu et al. 2023, *Science* 379:1358** | Contrastive learning for EC numbers. What does the embedding space organize by? |
| **Yang, *CARE benchmark*** | The CARE paper | Enforce novelty in the split. How much performance is retrieval? |
| Steinegger, *Exploring the Protein Universe* | **van Kempen et al. 2024, *Nat Biotechnol* 42:243** | A 3Di structural alphabet. Why does discretizing structure make search tractable? |
