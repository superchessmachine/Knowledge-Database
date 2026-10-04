# D.9 Interpretability and the Science of Models

> **This is the section with the most obvious two-way traffic, and the traffic
> currently runs one way.**
>
> Mechanistic interpretability asks what computation a trained network is
> actually performing. The methods — activation patching, sparse autoencoders,
> circuit analysis, probing — are domain-general, and InterPLM (Atlas Q.4) has
> already shown they transfer to protein language models.
>
> **What has not been noticed is that the transfer is advantageous in the other
> direction.** Language interpretability's hardest problem is *validation*: when
> a sparse autoencoder surfaces a feature, there is no ground truth for what that
> feature should mean, so the field falls back on human inspection of top
> activations. A protein model does not have that problem. A feature can be
> checked against a catalytic triad, a Pfam domain boundary, a transmembrane
> helix, a disulfide — thousands of independently-established structural and
> functional labels that nobody had to invent for the purpose.
>
> **Molecular models are therefore a better testbed for interpretability methods
> than language models are**, and essentially nobody in the interpretability
> community has noticed. That observation is the whole of Capstone VIII, and it
> is the single clearest opportunity in this document.

---

## 1. Mechanistic interpretability

**Circuits, feature visualization, Chris Olah**

1. **CVPR'20 iMLCV tutorial: Introduction to Circuits in CNNs by Chris Olah** | Chris Olah (OpenAI→Anthropic), hosted by Bolei Zhou | 2020 | 44:54 | https://www.youtube.com/watch?v=gXsKyZ_Y_i8 — The original circuits program before it moved to transformers; curve detectors, high-low frequency detectors, equivariance. Papers: *Zoom In: An Introduction to Circuits* (Distill 2020); *Feature Visualization* (Distill 2017).
2. **Chris Olah - Looking Inside Neural Networks with Mechanistic Interpretability** | Chris Olah (Anthropic), FAR.AI Alignment Workshop | 2023 | 40:59 | https://www.youtube.com/watch?v=2Rdp9GvcYOE — The clearest single statement of the superposition framing and why it makes interpretability hard. Paper: *Toy Models of Superposition* (Elhage et al. 2022).
3. **Catherine Olsson - Mechanistic Interpretability: Getting Started** | Catherine Olsson (Anthropic), Cohere For AI | 2022 | 54:10 | https://www.youtube.com/watch?v=ll0oduwDEwI — An actual research-practice talk on how to begin, from a co-author of the induction-heads paper.
4. **What the hell is going on inside neural networks? | Chris Olah** | Chris Olah (Anthropic), 80,000 Hours | 2023 | 3:09:20 | https://www.youtube.com/watch?v=k_QVDwhR8FU — Long-form, but the best articulation of the research taste behind the whole agenda. Optional depth.

**Induction heads and the transformer-circuits line**

5. **Stanford CS25: V1 I Transformer Circuits, Induction Heads, In-Context Learning** | Chris Olah (Anthropic) | 2022 | 59:34 | https://www.youtube.com/watch?v=pC4zRb_5noQ — The canonical lecture on induction heads and the phase change in the loss curve. Papers: *A Mathematical Framework for Transformer Circuits* (2021); *In-context Learning and Induction Heads* (2022).
6. **A Walkthrough of A Mathematical Framework for Transformer Circuits** | Neel Nanda | 2022 | 2:50:13 | https://www.youtube.com/watch?v=KV5gbOmHbjU — Line-by-line reading of the hardest and most foundational paper in the field. Paper: Elhage et al. 2021.
7. **A Walkthrough of In-Context Learning and Induction Heads Part 1 of 2 (w/ Charles Frye)** | Neel Nanda with Charles Frye | 2022 | 1:03:51 | https://www.youtube.com/watch?v=dCkQQYwPxdM — Pairs directly with Olsson et al. 2022.
8. **What is a Transformer? (Transformer Walkthrough Part 1/2)** | Neel Nanda | 2023 | 1:03:00 | https://www.youtube.com/watch?v=bOYE6E8JrtU — The architecture as a mech-interp researcher needs to see it (residual stream as a communication channel).
9. **Implementing GPT-2 From Scratch (Transformer Walkthrough Part 2/2)** | Neel Nanda | 2023 | 1:19:25 | https://www.youtube.com/watch?v=dsjUDacBw8o — The hands-on companion; this is effectively the TransformerLens onboarding.

**Superposition, SAEs, dictionary learning**

10. **Towards Monosemanticity: Decomposing Language Models Into Understandable Components** | Arize AI paper-reading group | 2023 | 43:39 | https://www.youtube.com/watch?v=hlCxSqWS6Rw — Walkthrough of the paper that started the SAE wave. Paper: Bricken et al. 2023.
11. **Scaling interpretability** | Anthropic interpretability team | 2024 | 53:18 | https://www.youtube.com/watch?v=sQar5NNGbw4 — The engineering story behind scaling SAEs to Claude 3 Sonnet; unusually candid about what broke. Paper: *Scaling Monosemanticity* (Templeton et al. 2024).
12. **Hoagy Cunningham — Finding distributed features in LLMs with sparse autoencoders [TAIS 2024]** | Hoagy Cunningham (Anthropic) | 2024 | 28:49 | https://www.youtube.com/watch?v=HPLIl9ZOpUQ — From the author of the independent SAE paper. Paper: *Sparse Autoencoders Find Highly Interpretable Features in Language Models* (2023).
13. **Sparse Autoencoders: Progress & Limitations with Joshua Engels** | Joshua Engels (MIT), NDIF | 2025 | 1:03:47 | https://www.youtube.com/watch?v=eVlGeHA2Cnw — The negative results: not all features are linear, SAEs miss things. Paper: *Not All Language Model Features Are Linear* (2024).
14. **What Happened With Sparse Autoencoders?** | Neel Nanda (DeepMind) | 2025 | 2:49:15 | https://www.youtube.com/watch?v=Tgq7E4YcPKQ — A field leader explaining why the SAE hype cycle deflated. Essential antidote to the two talks above.
15. **Bayesian and Dynamical Transitions in a Toy Model of Superposition - SLT Seminar 53** | metauni / Timaeus | 2024 | 1:14:31 | https://www.youtube.com/watch?v=yL4ZkDCe2_c — Superposition analyzed with singular learning theory; the mathematically serious treatment.
16. **Introduction to Sparse AutoEncoders | ML@P Reading Group | Jinen Setpal** | Jinen Setpal, ML Purdue | 2025 | 1:03:33 | https://www.youtube.com/watch?v=_vUKIPYOaJw — Implementation-level tutorial.

**Attribution graphs and circuit tracing**

17. **Stanford CS25: V5 I On the Biology of a Large Language Model, Josh Batson of Anthropic** | Josh Batson (Anthropic) | 2025 | 1:12:32 | https://www.youtube.com/watch?v=vRQs7qfIDaU — The single best talk on attribution graphs: multi-step reasoning, planning in poetry, unfaithful chain-of-thought. Papers: *Circuit Tracing* and *On the Biology of a Large Language Model* (Anthropic 2025).
18. **Attribution Graphs for Dummies - 1. What are Attribution Graphs?** | Neuronpedia | 2025 | 49:09 | https://www.youtube.com/watch?v=ruLcDtr_cGo — Mechanics of transcoders and replacement models.
19. **Attribution Graphs for Dummies - 2. Building and Testing a Circuit** | Neuronpedia | 2025 | 1:23:41 | https://www.youtube.com/watch?v=hdi1a9MjwDs — The hands-on half: build and validate a circuit yourself.
20. **Anthropic: Circuit Tracing + On the Biology of a Large Language Model** | Latent Space, with Anthropic authors | 2025 | 56:27 | https://www.youtube.com/watch?v=ig5RNJJaFJE — Author Q&A on the same two papers.
21. **Interpretability: Understanding how AI models think** | Josh Batson, Emmanuel Ameisen, Jack Lindsey (Anthropic) | 2025 | 59:02 | https://www.youtube.com/watch?v=fGKNUvivvnc — Panel on hallucination and sycophancy mechanisms.

**Neel Nanda / getting started / open problems**

22. **An Introduction to Mechanistic Interpretability – Neel Nanda | IASEAI 2025** | Neel Nanda (DeepMind) | 2025 | 25:12 | https://www.youtube.com/watch?v=0704iLc55Fs — The tightest 25-minute orientation available.
23. **Neel Nanda – Mechanistic Interpretability: A Whirlwind Tour** | Neel Nanda, FAR.AI | 2024 | 21:31 | https://www.youtube.com/watch?v=veT2VI4vHyU
24. **Open Problems in Mechanistic Interpretability: A Whirlwind Tour** | Neel Nanda, Google TechTalks | 2023 | 55:27 | https://www.youtube.com/watch?v=ZSg4-H8L6Ec — Explicitly a research-problem list. Start here for picking a thesis topic.
25. **Concrete Open Problems in Mechanistic Interpretability: Neel Nanda at SERI MATS** | Neel Nanda | 2023 | 1:26:48 | https://www.youtube.com/watch?v=FnNTbqSG8w4 — Longer and more concrete than #24. Paper: *200 Concrete Open Problems in Mechanistic Interpretability*.
26. **The Story of Mech Interp** | Neel Nanda | 2025 | 2:06:05 | https://www.youtube.com/watch?v=kkfLHmujzO8 — Intellectual history of the field, which is exactly what you need to avoid redoing solved work.
27. **What Matters Right Now In Mechanistic Interpretability?** | Neel Nanda | 2025 | 59:21 | https://www.youtube.com/watch?v=XZX_CFfVgIc — Current research-direction triage.
28. **How Reasoning Models Break Mechanistic Interpretability Techniques** | Neel Nanda | 2025 | 42:21 | https://www.youtube.com/watch?v=s3HgyprprhM — The frontier problem: reasoning models invalidate existing tooling.
29. **Neel Nanda: Mechanistic Intepretability (HAAISS 2024)** | Neel Nanda, Alignment of Complex Systems | talk 2024, posted 2025 | 1:18:02 | https://www.youtube.com/watch?v=yG3TxLPO_Uc
30. **19 - Mechanistic Interpretability with Neel Nanda** | AXRP (Daniel Filan) | 2023 | 3:52:47 | https://www.youtube.com/watch?v=3YbE7zybc5k — Deepest available interview on methodology and epistemics.

**Activation patching, causal intervention, causal scrubbing**

31. **A Walkthrough of Interpretability in the Wild Part 1/2: Overview (w/ authors Kevin, Arthur, Alex)** | Neel Nanda with Kevin Wang, Arthur Conmy, Alexandre Variengien | 2022 | 57:20 | https://www.youtube.com/watch?v=gzwj0jWbvbo — The IOI circuit, the canonical worked example of path patching. Paper: *Interpretability in the Wild* (Wang et al. 2022).
32. **A Walkthrough of Interpretability in the Wild Part 2/2: Deep Dive (w/ authors Kevin, Arthur & Alex)** | same | 2022 | 1:46:05 | https://www.youtube.com/watch?v=b9xfYBKIaX4
33. **Causal Scrubbing | Intro to Neural Network Interpretability** | Cadenza Labs | 2023 | 7:27 | https://www.youtube.com/watch?v=_oCWsaFBY1M — Short but the only clear video explainer of Redwood's causal scrubbing. Paper: Chan et al., *Causal Scrubbing* (2022).
34. **Uncovering and Inducing Interpretable Causal Structure in Deep Learning Models | Atticus Geiger** | Atticus Geiger (Pr(Ai)²R), Valence Labs | 2024 | 56:13 | https://www.youtube.com/watch?v=EbVsoR7cjf0 — The formal theory (causal abstraction, DAS) under activation patching. Paper: *Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability*.
35. **A Walkthrough of Aligning Causal Variables and Distributed Representations w/ Atticus Geiger (1/3)** | Neel Nanda with Atticus Geiger | 2023 | 30:43 | https://www.youtube.com/watch?v=iZm0_l2H2CQ — Distributed Alignment Search explained by its author.
36. **Atticus Geiger - State of Interpretability & Ideas for Scaling Up [Alignment Workshop]** | Atticus Geiger, FAR.AI | 2024 | 21:14 | https://www.youtube.com/watch?v=eqZ1iEoor5s
37. **Formalizing Explanations of Neural Network Behaviors** | Paul Christiano (Alignment Research Center), Simons Institute | 2023 | 59:17 | https://www.youtube.com/watch?v=u0619QrWxQc — The critique that informal mech interp does not scale, and the heuristic-arguments alternative. Deeply relevant to anyone wanting to contribute foundationally.
38. **40 - Jason Gross on Compact Proofs and Interpretability** | AXRP | 2025 | 2:36:04 | https://www.youtube.com/watch?v=ZzEj7jPk5fc — Proof-length as a rigorous metric for whether an explanation is real.

**Grokking, modular addition, ARENA**

39. **A Walkthrough of Progress Measures for Grokking via Mechanistic Interpretability: What? (Part 1/3)** | Neel Nanda with Lawrence Chan | 2023 | 43:10 | https://www.youtube.com/watch?v=IHikLL8ULa4 — Paper: Nanda et al., ICLR 2023.
40. **A Walkthrough of Reverse-Engineering Modular Addition: Model Training (Part 1/3)** | Neel Nanda | 2023 | 34:37 | https://www.youtube.com/watch?v=ob4vuiqG2Go — The full reverse-engineering done live, Fourier features and all.
41. **ARENA Lecture, Week 1 Day 1: Transformers: Building, Training, Sampling** | ARENA – AI Safety Education | 2025 | 34:09 | https://www.youtube.com/watch?v=11Z50mi8dSg — Entry point to the ARENA curriculum.
42. **ARENA Lecture, Week 1 Day 2: Introduction to Mechanistic Interpretability** | ARENA | 2025 | 37:52 | https://www.youtube.com/watch?v=lfwT79Hgytc — Pair with the ARENA notebooks at arena.education.
43. **Vision Mechanistic Interpretability - MATS Talk Summer 2024** | Sonia Joseph | 2024 | 58:31 | https://www.youtube.com/watch?v=gQbh-RZtsq4 — Mech interp applied to ViTs; Prisma library.
44. **What do models learn during finetuning? A model diffing paper walkthrough w/ Clement & Julian** | Neel Nanda with Clément Dumas, Julian Minder | 2025 | 2:54:52 | https://www.youtube.com/watch?v=VQ_7zLXHf3s — Model diffing, one of the newest and most open subfields.
45. **NEURAL NETWORKS ARE WEIRD! - Neel Nanda (DeepMind)** | MLST | 2024 | 3:42:37 | https://www.youtube.com/watch?v=YpFaPKOeNME — Research-epistemics-heavy; good on how to not fool yourself.

## 2. Representation analysis

46. **Probing | Stanford CS224U Natural Language Understanding | Spring 2021** | Christopher Potts (Stanford) | recorded 2021, posted 2022 | 11:29 | https://www.youtube.com/watch?v=ElDtkhqv5ZE — Compact and rigorous framing of probing as a method.
47. **Talk 4: Probing** | Zining Zhu (Toronto) | 2021 | 47:23 | https://www.youtube.com/watch?v=hJ45rJgGyRw — Full treatment including the critique literature.
48. **INFORMATION-THEORETIC PROBING WITH MINIMUM DESCRIPTION LENGTH** | Elena Voita, USC ISI | 2020 | 1:03:08 | https://www.youtube.com/watch?v=CakeVH_svdo — The principal answer to "your probe just memorized the labels." Paper: Voita & Titov, EMNLP 2020. See also Hewitt & Liang, *Designing and Interpreting Probes with Control Tasks* (2019).
49. **Interpreting Natural Language Processing Models** | Yonatan Belinkov (Technion), Simons Institute | 2020 | 1:06:48 | https://www.youtube.com/watch?v=vKCvcG6SHWc — Paper: Belinkov, *Probing Classifiers: Promises, Shortcomings, and Advances* (CL 2022). This is the critique you must read before using a probe.
50. **Yonatan Belinkov - Causal Mediation Analysis for Interpreting Neural NLP: The Case of Gender Bias** | Yonatan Belinkov, UMass ML & Friends | 2020 | 1:10:29 | https://www.youtube.com/watch?v=ew-P4vU-2yI — The bridge from correlational probing to causal methods. Paper: Vig et al., *Investigating Gender Bias in Language Models Using Causal Mediation Analysis* (NeurIPS 2020).
51. **Feature learning & the linear representation hypothesis for steering & monitoring LLMs** | Mikhail Belkin (UC San Diego), Broad Institute Schmidt Center Symposium | 2026 | 29:52 | https://www.youtube.com/watch?v=0eL69dWZ1lA — A learning-theorist's take on why representations go linear.
52. **Linear Structure of High-Level Concepts in Text-Controlled Generative Models | Victor Veitch** | Victor Veitch (Chicago), Valence Labs | 2024 | 1:07:59 | https://www.youtube.com/watch?v=6yUuWknqSdM — The formal statement of the linear representation hypothesis. Paper: Park, Choe & Veitch, *The Linear Representation Hypothesis and the Geometry of Large Language Models* (2023).
53. **Oskar John Hollinsworth — Linear Representations of Sentiment in Large Language Models [TAIS 2024]** | Oskar Hollinsworth | 2024 | 29:10 | https://www.youtube.com/watch?v=8QNGVSVWukw — A concrete worked case of a concept direction.
54. **Andy Zou – Top-Down Interpretability for AI Safety [Alignment Workshop]** | Andy Zou (CMU), FAR.AI | 2024 | 19:07 | https://www.youtube.com/watch?v=ub1ivilmzSc — From the lead author of representation engineering. Paper: Zou et al., *Representation Engineering: A Top-Down Approach to AI Transparency* (2023).
55. **The Platonic Representation Hypothesis** | Phillip Isola (MIT), Simons Institute | 2024 | 44:27 | https://www.youtube.com/watch?v=1_xH2mUFpZw — Paper: Huh, Cheung, Wang & Isola, ICML 2024.
56. **Kathleen Creel (Northeastern University): 'Against the Platonic Representation Hypothesis'** | Kathleen Creel, LSE Philosophy | 2026 | 43:05 | https://www.youtube.com/watch?v=W1jIpcWgpcw — The rebuttal. Pair with #55; the disagreement is where the research is.
57. **Pekka Marttinen: How to better compare representations learned by neural networks** | Pekka Marttinen (Aalto), FCAI | 2023 | 41:45 | https://www.youtube.com/watch?v=dA7jKK3TNqc — Directly on CKA/CCA and why existing similarity measures misbehave. Paper: Kornblith et al., *Similarity of Neural Network Representations Revisited* (ICML 2019).
58. **Contributed Talks: "Representational Alignment" - CCN 2025** | Yiqing Bo, Itamar Avitan, Imran Thobani et al., CCN Amsterdam | 2025 | 57:22 | https://www.youtube.com/watch?v=vT-3kV89Rhk — Includes "Evaluating Representational Similarity Measures from the Lens of Functional Correspondence" and "Linear Probing Fails to Identify the Ground-Truth Model." This is the current state of the art on the validity of similarity metrics.
59. **Inspecting Neural Networks with CCA - A Gentle Intro (Explainable AI for Deep Learning)** | Jay Alammar | 2021 | 19:28 | https://www.youtube.com/watch?v=u7Dvb_a1D-0 — Visual primer on SVCCA before the harder material.
60. **Interpretability via Symbolic Distillation** | Miles Cranmer (Cambridge/Flatiron), Simons Institute | 2023 | 51:04 | https://www.youtube.com/watch?v=XHBJJ2N-kUc — A genuinely different route: distill the network into symbolic form. Paper: Cranmer et al., *Discovering Symbolic Models from Deep Learning with Inductive Biases* (2020).

## 3. Classical interpretability and attribution

61. **Quantitative Testing with Concept Activation Vectors (TCAV) -- Been Kim (Google) - 2018** | Been Kim (Google Brain), JHU CLSP | talk 2018, posted 2023 | 56:09 | https://www.youtube.com/watch?v=wBcrPDPUTrE — Paper: Kim et al., *Interpretability Beyond Feature Attribution: Quantitative Testing with Concept Activation Vectors*, ICML 2018.
62. **Interpretability Beyond Feature Attribution** | Been Kim, MLconf | 2018 | 27:56 | https://www.youtube.com/watch?v=Ff-Dx79QEEY — Shorter conference version of the same work.
63. **Interpretability - now what?** | Been Kim (Google Brain), Simons Institute "Frontiers of Deep Learning" | 2019 | 47:37 | https://www.youtube.com/watch?v=5w_rgBbwQHw — Where she presents the saliency-map failure results. Paper: Adebayo et al., *Sanity Checks for Saliency Maps* (NeurIPS 2018); also Kindermans et al., *The (Un)reliability of Saliency Methods*.
64. **SecML18: Been Kim on Interpretability for when NOT to use machine learning** | Been Kim | 2019 | 26:53 | https://www.youtube.com/watch?v=t1rJ9gIrYKM
65. **Been Kim wants interpretability for everyone** | Been Kim, OATML Oxford | 2021 | 1:05:18 | https://www.youtube.com/watch?v=06hIoM-cLVM — Covers the human-subject studies showing saliency maps do not help people.
66. **Alignment and Interpretability: How We Might Get It Right | Been Kim (Google DeepMind)** | FAR.AI | 2024 | 33:21 | https://www.youtube.com/watch?v=JVoYzS2RcRc — Her current position; pairs with *Beyond Interpretability: Towards a Machine-Centric Vocabulary*.
67. **Feature Attribution | Stanford CS224U Natural Language Understanding | Spring 2021** | Christopher Potts (Stanford) | recorded 2021, posted 2022 | 15:32 | https://www.youtube.com/watch?v=RFE6xdfJvag — Covers integrated gradients and its axioms cleanly. Paper: Sundararajan, Taly & Yan, *Axiomatic Attribution for Deep Networks* (ICML 2017).
68. **Scott Lundberg, Microsoft Research - Explainable Machine Learning with Shapley Values** | Scott Lundberg (MSR), H2O World | 2019 | 18:34 | https://www.youtube.com/watch?v=ngOBhhINWb8 — From the SHAP author. Paper: Lundberg & Lee, NeurIPS 2017.
69. **Explainable AI explained! | #4 SHAP** | DeepFindr | 2021 | 15:50 | https://www.youtube.com/watch?v=9haIOplEIGM — The mechanics, if the above is too high-level.
70. **Stop Explaining Black Box Machine Learning Models - Cynthia Rudin** | Cynthia Rudin (Duke), Caltech | 2021 | 30:15 | https://www.youtube.com/watch?v=4oXFEDoEcAk — Paper: Rudin, *Stop Explaining Black Box Machine Learning Models for High Stakes Decisions and Use Interpretable Models Instead* (Nature MI 2019).
71. **Stop explaining black box machine learning models for high stakes decisions and..... - Cynthia Rudin** | Cynthia Rudin, Institute for Advanced Study | 2022 | 1:04:02 | https://www.youtube.com/watch?v=HY2NoQQzRic — The long technical version with the optimal-sparse-decision-tree work.
72. **Interpretable Machine Learning for High-Stakes Decisions - Cynthia Rudin** | Chennai Mathematical Institute | 2022 | 1:05:24 | https://www.youtube.com/watch?v=2wj1Ztym5qY
73. **Allen School Colloquium: Pang Wei Koh (Stanford University)** | Pang Wei Koh | 2022 | 58:49 | https://www.youtube.com/watch?v=5tidNjeVG8s — Paper: Koh & Liang, *Understanding Black-box Predictions via Influence Functions* (ICML 2017 best paper).
74. **Interpreting Deep Neural Networks (DNNs)** | Bin Yu (UC Berkeley), Simons Institute | 2019 | 46:48 | https://www.youtube.com/watch?v=mCDv3kpzqwQ — The statistician's framing: stability and the PCS framework.
75. **25. Interpretability** | Peter Szolovits (MIT 6.S897) | recorded 2019, posted 2020 | 1:18:41 | https://www.youtube.com/watch?v=wDLzLN1tArA — Clean survey of the classical toolkit.
76. **#047 Interpretable Machine Learning - Christoph Molnar** | MLST | 2021 | 1:40:22 | https://www.youtube.com/watch?v=0LIACHcxpHU — Author of the *Interpretable Machine Learning* book; strong on method pitfalls.

## 4. Science of model behavior

77. **Datamodels: Predicting Predictions with Training Data** | Andrew Ilyas (MIT, Mądry Lab), Norbert Wiener Center | 2022 | 1:00:23 | https://www.youtube.com/watch?v=1djD0kK2uik — Paper: Ilyas, Park, Engstrom, Leclerc & Mądry, *Datamodels* (ICML 2022).
78. **MedAI #51: Datamodels - Predicting Predictions from Training Data | Andrew Ilyas** | Stanford MedAI | 2022 | 56:56 | https://www.youtube.com/watch?v=dgo7nRQcw_E — Shorter, more accessible version.
79. **ML Robustness & Engineering - Andrew Ilyas (MIT)** | MLST | 2024 | 1:28:01 | https://www.youtube.com/watch?v=9BC9BsZRCKQ — Covers the TRAK line and the broader "models are a function of their data" program. Paper: Park, Georgiev, Ilyas, Leclerc & Mądry, *TRAK: Attributing Model Behavior at Scale* (ICML 2023).
80. **What Do Our Models Learn? - Aleksander Mądry** | Aleksander Mądry (MIT), Institute for Advanced Study | 2020 | 1:27:40 | https://www.youtube.com/watch?v=_Osf6F7zZUM — The lab's foundational framing. Paper: *Adversarial Examples Are Not Bugs, They Are Features* (2019).
81. **Scalable Extraction of Training Data from (Production) Language Models** | Nicholas Carlini (Google DeepMind), Simons Institute | 2024 | 49:11 | https://www.youtube.com/watch?v=adCLAhoQhOQ — Paper: Nasr, Carlini et al. (2023), the divergence attack on ChatGPT.
82. **TrustML Seminar: Nicholas Carlini on "Extracting training data from neural networks"** | Nicholas Carlini | 2021 | 1:00:50 | https://www.youtube.com/watch?v=2Xl2B2R7_1M — Paper: Carlini et al., *Extracting Training Data from Large Language Models* (USENIX Security 2021).
83. **USENIX Security '19 - The Secret Sharer: Evaluating and Testing Unintended Memorization in Neural Networks** | Nicholas Carlini | 2019 | 20:36 | https://www.youtube.com/watch?v=U9XbFtCWedE — The origin of quantitative memorization measurement (exposure metric).
84. **Jesse Hoogland: Singular Learning Theory, Developmental interpretability (HAAISS 2024)** | Jesse Hoogland (Timaeus) | talk 2024, posted 2025 | 1:17:19 | https://www.youtube.com/watch?v=dtcRhr0gqKU — Papers: *Towards Developmental Interpretability*; Lau et al., *The Local Learning Coefficient*.
85. **31 - Singular Learning Theory with Daniel Murfet** | AXRP | 2024 | 2:32:06 | https://www.youtube.com/watch?v=hdB9gIwD6x4 — The mathematical foundation (Watanabe's SLT) at depth.
86. **ALIGN Webinar Series #12 Jesse Hoogland Singular Learning Theory for AI Safety** | AI Alignment Network | 2025 | 1:02:17 | https://www.youtube.com/watch?v=jgcatt6eZyY
87. **38.2 - Jesse Hoogland on Singular Learning Theory** | AXRP | 2024 | 18:18 | https://www.youtube.com/watch?v=P528XdjWvZg — Quick orientation if the above are too long.
88. **EI Seminar - Naomi Saphra - Interpreting Training** | Naomi Saphra (Harvard/Kempner), MIT | 2024 | 1:04:20 | https://www.youtube.com/watch?v=J0tHAZlFGSc — The argument that interpretability should study training dynamics, not just final checkpoints.
89. **Training Is Nothing Like Learning with Naomi Saphra (Harvard)** | The Information Bottleneck | 2026 | 1:11:34 | https://www.youtube.com/watch?v=2WqvUQY1nlg — Her current, sharper position.
90. **Naomi Saphra: Linear Connectivity Reveals Generalization Strategies** | Formal Languages and Neural Networks Seminar | 2022 | 54:23 | https://www.youtube.com/watch?v=zxtD9rW_3Bo — Loss-landscape connectivity as an interpretability signal. Paper: Juneja, Bansal, Cho, Sedoc & Saphra (ICLR 2023).
91. **"Dynamics of Concept Learning and Emergent Abilities in Neural Networks" - Ekdeep Lubana** | Ekdeep Singh Lubana (Harvard/Michigan), TTIC | 2025 | 1:03:31 | https://www.youtube.com/watch?v=nYGyeJRHqEA — Toy models that explain emergence as a dynamics phenomenon, not a scaling mystery.
92. **Explaining emergence in NN with model systems analysis - Ekdeep Singh Lubana (PIBBSS Speaker Series)** | Principles of Intelligence | 2024 | 1:24:56 | https://www.youtube.com/watch?v=bCEXKmDGUzQ — Methodological: how to build toy "model systems" like a biologist.
93. **The Surprising Simplicity of the Early-Time Learning Dynamics of Neural Networks in High Dimension** | Wei Hu (Princeton), Simons Institute | 2020 | 47:10 | https://www.youtube.com/watch?v=2ytGG5qtYvE — Theory side of training-dynamics analysis.

## 5. Evaluation as a science

94. **Keynote Talk: Sanmi Koyejo - Beyond Benchmarks; Building a Science of AI Measurement** | Sanmi Koyejo (Stanford), Deep Learning Indaba | 2025 | 53:03 | https://www.youtube.com/watch?v=xXYvsDJS9vw — The single best framing talk for this whole section. Paper: Schaeffer, Miranda & Koyejo, *Are Emergent Abilities of Large Language Models a Mirage?* (NeurIPS 2023 best paper).
95. **CITP Special Event: Sayash Kapoor: Final Public Oral (FPO) - The Missing Science of AI Evaluation** | Sayash Kapoor (Princeton) | 2026 | 1:17:59 | https://www.youtube.com/watch?v=8SGdYYtmmwI — A full dissertation defense on exactly this topic. Papers: *AI Agents That Matter*; *Leakage and the Reproducibility Crisis in ML-based Science*.
96. **Building and evaluating AI Agents — Sayash Kapoor, AI Snake Oil** | AI Engineer | 2025 | 19:59 | https://www.youtube.com/watch?v=d5EltXhbcfA — Compact version with the cost-control argument.
97. **The Challenge of Valid Evaluations** | Amanda Coston (UC Berkeley), Simons Institute | 2026 | 32:40 | https://www.youtube.com/watch?v=WUiTKvhjn90 — Construct validity and counterfactual evaluation done rigorously.
98. **The Inadequacy of Offline LLM Evaluations: A Need to Account for Personalization in Model Behavior** | Angelina Wang (Cornell Tech), Simons Institute | 2026 | 31:57 | https://www.youtube.com/watch?v=q4ilyQs3nEY — Why stateless benchmark inference misrepresents deployed behavior.
99. **Leaderboardism in NLP: panel with Kawin Ethayarajh, Jesse Dodge, Rachael Tatman & Anna Rogers** | Anna Rogers (chair) | 2020 | 1:10:10 | https://www.youtube.com/watch?v=VauPmCJSlH8 — The definitive critique of leaderboard culture, by the people who wrote it up. Paper: Ethayarajh & Jurafsky, *Utility is in the Eye of the User* (EMNLP 2020).
100. **Rasa Reading Group: What Will it Take to Fix Benchmarking in Natural Language Understanding (Part 2)** | Rasa | 2021 | 1:08:02 | https://www.youtube.com/watch?v=UDK6ZTUIvig — Paper: Bowman & Dahl, NAACL 2021. The four criteria any benchmark must meet.
101. **ACL 2022 Talk – The Dangers of Underclaiming** | Sam Bowman (NYU/Anthropic) | 2022 | 12:19 | https://www.youtube.com/watch?v=fPnX374CaFQ — The other half of the evaluation-rigor argument: over-correction is also a failure mode.
102. **Learning Machines Seminar @ Cornell: Sam Bowman (NYU)** | Sam Bowman | 2019 | 58:13 | https://www.youtube.com/watch?v=Ei_EKCDPYwQ — GLUE/SuperGLUE from the person who built them and then argued they were saturated.
103. **Naman Jain - "LiveCodeBench: Holistic and contamination free evaluation of LLMs for code"** | Naman Jain (UC Berkeley) | 2024 | 56:47 | https://www.youtube.com/watch?v=HGqhS9-rnQM — Contamination as a first-class design constraint. Paper: Jain et al., LiveCodeBench (ICLR 2025).
104. **Context for Interpreting Benchmark Performances** | Kenneth Church (Baidu/Northeastern) | 2021 | 24:35 | https://www.youtube.com/watch?v=3Lo-iqo1PjQ — Short and sharp on what a benchmark number does and does not license.
105. **Rishi Bommasani -- Holistic Evaluation of Language Models** | Rishi Bommasani (Stanford CRFM) | 2023 | 37:47 | https://www.youtube.com/watch?v=A0kD00WdlKY — Paper: *HELM* (Liang, Bommasani et al. 2022).
106. **Stanford CME295 Transformers & LLMs | Autumn 2025 | Lecture 8 - LLM Evaluation** | Stanford Online | 2025 | 1:49:25 | https://www.youtube.com/watch?v=8fNP4N46RRo — Current, technical, covers LLM-as-judge bias directly.
107. **LLM-as-a-Judge / Autoraters • Guest Lecture at Northeastern University • March 24, 2026** | Aman Chadha | 2026 | 56:39 | https://www.youtube.com/watch?v=N_DwZR--XCc — Position bias, self-preference, agreement-with-humans calibration.
108. **Joelle Pineau: Reproducibility, Reusability, and Robustness in Deep Reinforcement Learning ICLR 2018** | Joelle Pineau (McGill/Meta) | 2018 | 49:22 | https://www.youtube.com/watch?v=Vh4H0gOwdIg — The statistical-rigor talk: seed variance, confidence intervals, the ML reproducibility checklist. Paper: Henderson et al., *Deep RL That Matters* (AAAI 2018).

## 6. NeuroAI and biological inspiration

109. **Reverse engineering visual intelligence - James DiCarlo** | Jim DiCarlo (MIT), Stanford | 2018 | 40:59 | https://www.youtube.com/watch?v=Sc8-3XD3bDw — Paper: Yamins & DiCarlo, *Using goal-driven deep learning models to understand sensory cortex* (Nat Neuro 2016).
110. **Jim DiCarlo, MIT: Reverse engineering visual intelligence** | CCBM | 2018 | 40:54 | https://www.youtube.com/watch?v=5kq7M6pcQ5g — Alternate recording; covers Brain-Score.
111. **Stony Brook University Mind/Brain Lecture 2026 with Dr. James DiCarlo** | Jim DiCarlo | 2026 | 1:03:05 | https://www.youtube.com/watch?v=WVvZaMQLS6U — His current position, including model-driven neural control.
112. **BI 075 Jim DiCarlo: Reverse Engineering Vision** | Brain Inspired podcast | 2020 | 1:16:04 | https://www.youtube.com/watch?v=H7LzjJ2J7qw — Interview format, good on the epistemics of model-brain comparison.
113. **Deep Learning and the Brain 2019 – Prof. Daniel Yamins** | Dan Yamins (Stanford), ELSC Jerusalem | 2019 | 59:57 | https://www.youtube.com/watch?v=eq7abzaktM4 — Paper: Yamins et al., PNAS 2014.
114. **A Fruitful Reciprocity: The Neuroscience-AI Connection** | Dan Yamins (Stanford), MIT CBMM | 2023 | 1:10:35 | https://www.youtube.com/watch?v=6NOFtwKU3sA — Argues the exchange runs both ways; the best single NeuroAI framing talk.
115. **CSL seminar: Dan Yamins** | Dan Yamins, MIT Improbable AI | 2021 | 1:01:05 | https://www.youtube.com/watch?v=7pTH0cY01AU — Unsupervised and developmentally plausible models of cortex.
116. **On the Neural Machinery of Faces** | Doris Tsao (Caltech/Berkeley), MIT CBMM | 2018 | 1:03:18 | https://www.youtube.com/watch?v=n--C0YdJu_A — Paper: Chang & Tsao, *The Code for Facial Identity in the Primate Brain* (Cell 2017). The cleanest example anywhere of a decoded neural code; the direct biological analogue of a "feature basis."
117. **Doris Tsao: 2010 Allen Institute for Brain Science Symposium** | Doris Tsao | 2010 | 22:36 | https://www.youtube.com/watch?v=wpVm1QiNQEc — The earlier face-patch work.
118. **Surya Ganguli - Deep Learning Theory: From Generalization to the Brain** | Surya Ganguli (Stanford), DeepMath | 2020 | 1:00:22 | https://www.youtube.com/watch?v=UJ6FToAg7Ks — Paper: Saxe, McClelland & Ganguli, *Exact solutions to the nonlinear dynamics of learning in deep linear networks* (2014).
119. **Neural networks and the brain: from the retina to semantic cognition - Surya Ganguli** | Stanford | 2018 | 36:37 | https://www.youtube.com/watch?v=FKi6sWK9Qo0
120. **Surya Ganguli, A theory of neural dimensionality: McGovern Institute Symposium** | McGovern/MIT | 2016 | 40:08 | https://www.youtube.com/watch?v=3Kfei1_hAiY — Dimensionality of neural data as a measurable quantity; underrated methodologically.
121. **Konrad Kording - Why neuroscience needs deep learning theory** | Konrad Kording (UPenn), NAS Colloquia | 2019 | 14:16 | https://www.youtube.com/watch?v=GgzRdQ5nm0U — Short and provocative. Paper: Jonas & Kording, *Could a Neuroscientist Understand a Microprocessor?* (PLoS CB 2017) — arguably the most important methodological critique in this entire curriculum.
122. **Michigan Biostatistics presents a seminar with Konrad Körding, PhD** | Konrad Kording | 2021 | 52:03 | https://www.youtube.com/watch?v=2mRJrXKUT1M — Causality in neuroscience and ML.
123. **DLRLSS 2019 - Biological DL - Blake Richards** | Blake Richards (McGill/Mila), Amii | 2019 | 1:20:56 | https://www.youtube.com/watch?v=yqQe_Qcamwo — The full tutorial on biologically plausible credit assignment. Paper: Richards et al., *A deep learning framework for neuroscience* (Nat Neuro 2019).
124. **Fundamentals of deep learning in neuroscience** | Blake Richards, BrainHack School | 2020 | 1:35:12 | https://www.youtube.com/watch?v=kpNI6or-qJs — Inductive-bias framing; a good lecture-style entry point.
125. **Deep Learning with Ensembles of Neocortical Microcircuits - Dr. Blake Richards** | Blake Richards | 2018 | 50:14 | https://www.youtube.com/watch?v=YUVLgccVi54 — Paper: Guerguiev, Lillicrap & Richards, *Towards deep learning with segregated dendrites* (eLife 2017).
126. **Backpropagation and Deep Learning in the Brain** | Timothy Lillicrap (DeepMind), Simons Institute | 2018 | 59:43 | https://www.youtube.com/watch?v=-kHLKLLxIF4 — Paper: Lillicrap, Santoro, Marris, Akerman & Hinton, *Backpropagation and the brain* (Nat Rev Neuro 2020). The central reference for this debate.
127. **Stanford Seminar - Can the brain do back-propagation? Geoffrey Hinton** | Geoffrey Hinton (Toronto/Google) | 2016 | 1:25:13 | https://www.youtube.com/watch?v=VIRCybGgHts — Hinton's own early framing of the problem.
128. **Does the brain do backpropagation? CAN Public Lecture - Geoffrey Hinton - May 21, 2019** | Canadian Association for Neuroscience | 2019 | 1:22:03 | https://www.youtube.com/watch?v=qIEfJ6OBGj8 — Updated version with temporal derivatives as error signals.
129. **MoroccoAI Conference 2022 Honorary Keynote Prof. Geoffrey Hinton - The Forward-Forward Algorithm** | Geoffrey Hinton | talk Dec 2022, posted 2023 | 49:48 | https://www.youtube.com/watch?v=_5W5BvKe_6Y — Paper: Hinton, *The Forward-Forward Algorithm: Some Preliminary Investigations* (2022).
130. **Geoffrey Hinton Unpacks The Forward-Forward Algorithm** | Eye on AI | 2023 | 58:55 | https://www.youtube.com/watch?v=NWqy_b1OvwQ — Interview; covers mortal computation, which the paper only gestures at.
131. **Nobel Prize lecture: John J. Hopfield, Nobel Prize in Physics 2024** | John Hopfield (Princeton) | lecture Dec 2024, posted 2025 | 40:01 | https://www.youtube.com/watch?v=8SffhDk4mdU — Paper: Hopfield, PNAS 1982.
132. **Nobel Prize lecture: Geoffrey Hinton, Nobel Prize in Physics** | Geoffrey Hinton | lecture Dec 2024, posted 2025 | 31:53 | https://www.youtube.com/watch?v=XDE9DjpcSdI — Papers: Ackley, Hinton & Sejnowski, *A Learning Algorithm for Boltzmann Machines* (1985).
133. **2024 Nobel Prize lectures in physics | John Hopfield and Geoffrey Hinton** | Nobel Prize | 2024 | 1:18:57 | https://www.youtube.com/watch?v=lPIVl5eBPh8 — Both lectures in one stream, with the laudatio.
134. **Modern Hopfield Networks - Dr Sepp Hochreiter** | Sepp Hochreiter (JKU Linz), IARAI | 2020 | 1:26:33 | https://www.youtube.com/watch?v=bsdPZJKOlQs — Paper: Ramsauer et al., *Hopfield Networks is All You Need* (ICLR 2021) — the attention/associative-memory equivalence.
135. **Hopfield Networks in 2021 - Fireside chat between Sepp Hochreiter and Dmitry Krotov | NeurIPS 2020** | IARAI | 2020 | 1:15:53 | https://www.youtube.com/watch?v=k3YmWrK6wxo — Two of the principals arguing it out.
136. **Dmitry Krotov | Modern Hopfield Networks for Novel Transformer Architectures** | Dmitry Krotov (IBM/MIT-IBM), Harvard CMSA | 2023 | 1:05:07 | https://www.youtube.com/watch?v=5LXiQUsnHrI — Paper: Krotov & Hopfield, *Dense Associative Memory for Pattern Recognition* (NeurIPS 2016).
137. **Dmitry Krotov - Generative AI models through the lens of Dense Associative Memory - IPAM at UCLA** | IPAM | 2024 | 1:10:15 | https://www.youtube.com/watch?v=lzYwzIkO89Q — Energy-based reading of modern generative models.
138. **Energy-based Approaches to Representation Learning - Yann LeCun** | Yann LeCun (NYU/Meta), Institute for Advanced Study | 2019 | 39:54 | https://www.youtube.com/watch?v=m17B-cXcZFI — Paper: LeCun et al., *A Tutorial on Energy-Based Learning* (2006).
139. **Yann LeCun | May 18, 2021 | The Energy-Based Learning Model** | Harvard Mathematical Picture Language | 2021 | 1:15:52 | https://www.youtube.com/watch?v=4lthJd3DNTM — Longer; leads into the JEPA line.
140. **Debate: "Does Hierarchical Predictive Coding Explain Perception?" (Clark, Heeger, Melloni, Rescorla)** | NYU Center for Mind, Brain and Consciousness | 2018 | 2:00:33 | https://www.youtube.com/watch?v=CvAbPtbjxhw — A real adversarial debate, which is rarer and more useful than another sympathetic overview. Paper: Rao & Ballard, Nat Neuro 1999; Heeger, PNAS 2017.
141. **The Predictive Brain: Michael Pollan, Celeste Kidd, Christos Papadimitriou, and Bruno Olshausen** | Simons Institute | 2019 | 1:25:39 | https://www.youtube.com/watch?v=ItU0HeFmsrY — Olshausen on sparse coding, which is the direct ancestor of dictionary learning in Section 1. Paper: Olshausen & Field, Nature 1996.
142. **A New Framework for Modeling Brain Information Processing - Nikolaus Kriegeskorte** | Nikolaus Kriegeskorte (Columbia), Stanford | 2015 | 49:50 | https://www.youtube.com/watch?v=tyYIuvbV2po — RSA, the method ML later rediscovered as CKA. Paper: Kriegeskorte, Mur & Bandettini (2008).
143. **BI 163 Ellie Pavlick: The Mind of a Language Model** | Ellie Pavlick (Brown/DeepMind), Brain Inspired | 2023 | 1:21:35 | https://www.youtube.com/watch?v=o8_lZbQ0PEs — The cognitive-science-meets-interpretability perspective.
144. **Ellie Pavlick, (How) Does AI Think?** | Ellie Pavlick, Remarque Institute NYU | 2026 | 1:33:50 | https://www.youtube.com/watch?v=etWMRit98sA — Current and unusually careful about what interpretability claims actually establish.

## 7. Technical AI safety research

145. **Can We Get Asymptotic Safety Guarantees Based On Scalable Oversight?** | Geoffrey Irving (UK AI Safety Institute), Simons Institute | 2025 | 59:10 | https://www.youtube.com/watch?v=cJ0YPyP-I_o — Complexity-theoretic treatment of debate. The most technical scalable-oversight talk available. Papers: Irving, Christiano & Amodei, *AI Safety via Debate* (2018); *Prover-Estimator Debate* (2025).
146. **Sam Bowman - Adversarial Scalable Oversight for Truthfulness: Work in Progress** | Sam Bowman (NYU/Anthropic), FAR.AI | 2024 | 29:11 | https://www.youtube.com/watch?v=bkZsjmyF00k — Paper: Michael et al., *Debate Helps Supervise Unreliable Experts* (2023); Bowman et al., *Measuring Progress on Scalable Oversight* (2022).
147. **Collin Burns - Weak-to-Strong Generalization** | Collin Burns (OpenAI Superalignment), FAR.AI | 2024 | 26:54 | https://www.youtube.com/watch?v=wBPZNhw1LV4 — From the first author. Paper: Burns et al., *Weak-to-Strong Generalization* (ICML 2024).
148. **Transfer learning for weak-to-strong generalization** | Yuekai Sun (Michigan), Simons Institute | 2024 | 42:10 | https://www.youtube.com/watch?v=q68VtFoWmFI — The theory side; when W2S provably works.
149. **Aligning ML objectives with human values** | Paul Christiano (OpenAI), Simons Institute | 2019 | 47:00 | https://www.youtube.com/watch?v=3fZvahTlPaQ — Christiano's framing of the problem that ELK later formalized. Paper: Christiano, Cotra & Xu, *Eliciting Latent Knowledge* (ARC 2021).
150. **23 - Mechanistic Anomaly Detection with Mark Xu** | AXRP, Mark Xu (ARC) | 2023 | 2:05:53 | https://www.youtube.com/watch?v=sEWei02m7qk — The most substantive public explanation of ELK and the ARC heuristic-arguments agenda.
151. **Dangerous Capability Evals: Basis for Frontier Safety | Mary Phuong (Google DeepMind)** | FAR.AI | 2024 | 15:15 | https://www.youtube.com/watch?v=pO8IcIqhHuk — Paper: Phuong et al., *Evaluating Frontier Models for Dangerous Capabilities* (2024).
152. **David Duvenaud | The big picture of LLM dangerous capability evals** | David Duvenaud (Toronto/Anthropic), Schwartz Reisman Institute | 2025 | 1:19:50 | https://www.youtube.com/watch?v=zvIN7PnVuy4 — Methodologically critical about what these evals can and cannot establish.
153. **Alignment faking in large language models** | Ryan Greenblatt, Monte MacDiarmid, Benjamin Wright, Evan Hubinger (Anthropic/Redwood) | 2024 | 1:30:19 | https://www.youtube.com/watch?v=9eXV64O2Xp8 — Authors walking through the full experimental design. Paper: Greenblatt et al. (2024).
154. **27 - AI Control with Buck Shlegeris and Ryan Greenblatt** | AXRP | 2024 | 2:56:04 | https://www.youtube.com/watch?v=gQbCO6zGRiI — The control agenda as an alternative to alignment. Paper: Greenblatt et al., *AI Control: Improving Safety Despite Intentional Subversion* (ICML 2024).
155. **Interpretability Agents** | Sarah Schwettmann (MIT/Transluce), Simons Institute | 2024 | 42:07 | https://www.youtube.com/watch?v=9q9deK7RfII — Automating interpretability with agents. Paper: Shaham, Schwettmann et al., *A Multimodal Automated Interpretability Agent (MAIA)* (ICML 2024).
156. **Sarah Schwettmann - Scalable Oversight and Understanding [Alignment Workshop]** | FAR.AI | posted 2026 | 5:41 | https://www.youtube.com/watch?v=8oJW7hdbc2I — Short; the argument that understanding must scale with capability.
157. **Neel Nanda - Our Pivot To Pragmatic Interpretability [Alignment Workshop]** | Neel Nanda (DeepMind), FAR.AI | posted Dec 2025 | 10:20 | https://www.youtube.com/watch?v=k93o4R145Os — An important strategic update: the DeepMind team stepping back from ambitious reverse-engineering.
158. **"AI Safety Through Interpretable and Controllable Language Models" - Peter Hase, YRSS** | Peter Hase (UNC/Anthropic), TTIC | 2024 | 59:18 | https://www.youtube.com/watch?v=Ao8Gprp9mC0 — Model editing, belief localization, and why localization does not imply editability. Paper: Hase et al., *Does Localization Inform Editing?* (NeurIPS 2023).
159. **Yoshua Bengio - Disentangling Agency & Predictive Power Without Solving ELK [Alignment Workshop]** | Yoshua Bengio (Mila), FAR.AI | posted 2026 | 30:56 | https://www.youtube.com/watch?v=ZndiBDmss-w — The Scientist AI proposal, framed explicitly against ELK.
160. **42 - Owain Evans on LLM Psychology** | AXRP, Owain Evans (Truthful AI/Berkeley) | 2025 | 2:14:26 | https://www.youtube.com/watch?v=3D4pgIKR4cQ — Introspection, out-of-context reasoning, emergent misalignment. Papers: *Looking Inward*; *Emergent Misalignment* (2025).
161. **An Observation on Generalization** | Ilya Sutskever (OpenAI), Simons Institute | 2023 | 57:21 | https://www.youtube.com/watch?v=AKMuA_TVz3A — Compression-theoretic account of unsupervised learning. Bonus framing talk for the whole curriculum.

---

**Flagged as unverifiable — I could not find a real recording and will not invent one:**

- A dedicated recorded talk by **Julius Adebayo** on *Sanity Checks for Saliency Maps* — UNVERIFIED. Search terms: `Julius Adebayo sanity checks saliency maps NeurIPS 2018 spotlight`, `Adebayo debugging tests for model explanations MIT`. Entry #63 (Been Kim, Simons 2019) covers the same results. The paper is Adebayo, Gilmer, Muelly, Goodfellow, Hardt & Kim (NeurIPS 2018).
- A dedicated recorded talk by **Mukund Sundararajan** on integrated gradients — UNVERIFIED. Search terms: `Mukund Sundararajan integrated gradients talk Google`, `axiomatic attribution for deep networks ICML 2017 oral`. Entry #67 covers the method.
- A dedicated **TRAK** talk by Sung Min Park or Kristian Georgiev — UNVERIFIED. Search terms: `Sung Min Park TRAK attributing model behavior at scale ICML 2023 oral`, `Kristian Georgiev data attribution MIT talk`. Entry #79 (Andrew Ilyas, MLST 2024) covers TRAK within the broader data-attribution program.
- A dedicated **model stitching** talk (Bansal, Nakkiran & Barak, or Lenc & Vedaldi) — UNVERIFIED. Search terms: `Yamini Bansal revisiting model stitching NeurIPS 2021`, `Lenc Vedaldi understanding image representations equivariance equivalence`. Entries #57 and #58 cover the adjacent representational-similarity literature.

Two notes on using this list. First, Neel Nanda's paper walkthroughs (#6, #7, #31, #32, #39, #40, #44) are the closest thing to a graduate seminar in the field, but they are long and assume you have the paper open; budget real time for them rather than treating them as lectures. Second, I deliberately paired several talks with their own rebuttals — #55 with #56 on the platonic representation hypothesis, #11 and #12 with #14 on sparse autoencoders, #24 with #157 on whether ambitious mech interp is tractable. For someone aiming at original contributions, those disagreements are where the open problems actually live.

I did not write any files to the project directory, and since the working directory is not a git repository, there was nothing to commit or push. All search and verification scratch files are in the session scratchpad.
