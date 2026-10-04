# D.7 Reasoning, Inference-Time Compute, In-Context Learning

> **Why this matters to a methods researcher in biology.** Two ideas here are
> directly transferable and one argument is directly instructive.
>
> The first idea is **inference-time compute as a second scaling axis**. You
> already do this — generating a thousand backbones and filtering is
> inference-time search — but nobody in design has framed it as a compute
> allocation problem with an optimal policy. The language field has.
>
> The second is **verification**. A design pipeline is generate-then-verify, and
> so is every reasoning system here. The literature on when verification works,
> when it is gamed, and how to allocate budget between generation and
> verification is directly importable.
>
> The argument is **whether reasoning is real**, and it is instructive because it
> is the same argument as "do protein language models learn biology." Watching a
> neighboring field have it carefully will sharpen how you have yours.

---

## D.7.1 Chain-of-thought and the theory behind it

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| **CS25 V5 — Large Language Model Reasoning** | **Denny Zhou (DeepMind)** | 2025 | 1:06:07 | [▶](https://www.youtube.com/watch?v=ebnX5Ur1hBk) |
| LLM Reasoning (earlier version) | Denny Zhou (Berkeley MOOC) | 2024 | 1:04:02 | [▶](https://www.youtube.com/watch?v=QL-FS_Zcmyo) |
| **Chain of Thought Empowers Transformers to Solve Inherently Serial Problems** | Zhiyuan Li (first author) | 2024 | 55:19 | [▶](https://www.youtube.com/watch?v=_tmzV4ZRwVs) |
| Iterated Models: Expressive Power, Learning, and Chain of Thought | Nati Srebro (TTIC, Simons) | 2024 | 54:08 | [▶](https://www.youtube.com/watch?v=NRyIPyO_IWY) |
| Towards Revealing the Mystery behind Chain of Thought | — | 2023 | 47:38 | [▶](https://www.youtube.com/watch?v=nOIRuVluCyE) |
| **Implicit Chain-of-Thought: Internalizing Reasoning** | Yuntian Deng (Cohere Labs) | 2025 | 1:21:38 | [▶](https://www.youtube.com/watch?v=_I2yEhxRJlc) |
| Do Large Language Models Perform Latent Reasoning? | Mor Geva (Tel Aviv, Simons) | 2024 | 32:15 | [▶](https://www.youtube.com/watch?v=cVjgMVYkxbg) |
| **LLMs Cannot Self-Correct Reasoning Yet** | Jie Huang (UIUC, Cohere) | 2024 | 49:01 | [▶](https://www.youtube.com/watch?v=_pY8YwQ2gF8) |
| Transformers can learn compositional functions | Simons Institute | 2025 | 1:03:56 | [▶](https://www.youtube.com/watch?v=70-ugtkvqe8) |

**Papers:** **Wei et al. 2022, NeurIPS (chain-of-thought prompting)** ·
Wang et al. 2023, ICLR (self-consistency) · **Li et al. 2024, arXiv:2402.12875
(CoT empowers transformers — the circuit-complexity result)** ·
Feng et al. 2023, arXiv:2305.15408 · Deng et al. 2024, arXiv:2405.14838
(implicit CoT) · Huang et al. 2024, ICLR, arXiv:2310.01798.

> **Li et al. 2024 is the theoretical result that makes this subsection
> respectable.** A fixed-depth transformer is in a bounded circuit class and
> cannot compute certain serial functions. Chain-of-thought lets it use the
> output as working memory, which provably escapes that bound. **This is not a
> prompting trick, it is a complexity-theoretic statement about architecture.**
>
> **Derivation checkpoint 56.** State the circuit class a fixed-depth transformer
> falls in, and the class CoT reaches. Then ask the molecular version: a structure
> predictor recycles its output three times. **Is recycling chain-of-thought?**
> What serial computation does it enable that a single pass cannot do? Nobody has
> written this down, and it is exactly the kind of question that makes a theory
> paper.

---

## D.7.2 Test-time scaling

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| **Scaling LLM Test-Time Compute** | Charlie Snell (first author, Berkeley) | 2024 | 53:31 | [▶](https://www.youtube.com/watch?v=OXwGp9YeuBg) |
| Optimally Scaling Test-Time Compute & Predicting Emergence | Charlie Snell | 2025 | 36:45 | [▶](https://www.youtube.com/watch?v=4xT_6NtC3oo) |
| **From Decoding to Meta-Generation: Inference Time Algorithms** | Sean Welleck (CMU) | 2024 | 1:14:44 | [▶](https://www.youtube.com/watch?v=0s1gZe_BcQ0) |
| Beyond Decoding: Meta-Generation Algorithms | Sean Welleck (Simons) | 2024 | 1:21:55 | [▶](https://www.youtube.com/watch?v=oqOBYOx3sHE) |
| The Key Ingredients of Optimizing Test-Time Compute | Aviral Kumar (CMU, Simons) | 2025 | 1:02:15 | [▶](https://www.youtube.com/watch?v=5hJhPxKFaus) |
| Inference Scaling: A New Frontier for AI Capability | Azalia Mirhoseini (Stanford, Simons) | 2025 | 1:07:45 | [▶](https://www.youtube.com/watch?v=-pi4lI6FnT4) |
| Inference-Time Techniques for LLM Reasoning | Xinyun Chen (DeepMind, Berkeley) | 2025 | 1:21:32 | [▶](https://www.youtube.com/watch?v=g0Dwtf3BH-0) |
| Test Time Scaling Small LMs to o1 level | Isha Puri (Cohere Labs) | 2025 | 53:55 | [▶](https://www.youtube.com/watch?v=gaRyGLFI2YA) |
| **Inverse Scaling in Test-Time Compute** | EleutherAI PRA Reading Group | 2026 | 51:06 | [▶](https://www.youtube.com/watch?v=nIsSN-nujGQ) |

**Papers:** **Snell et al. 2024, arXiv:2408.03314** · **Welleck et al. 2024,
arXiv:2406.16838 (the survey)** · Puri et al. 2025, arXiv:2502.01618
(particle-based Monte Carlo with a PRM) · Brown et al. 2024 (large language
monkeys — repeated sampling).

> **Welleck's survey is the one that reframes design as search.** It treats
> generation as a search problem with a budget, and catalogues the algorithms:
> best-of-N, beam search over reasoning steps, MCTS, particle filtering. **Every
> one of these has a protein design analogue and most have not been tried.**
>
> Best-of-N with a learned verifier is what every design pipeline already does.
> **Particle filtering with a process reward model is not** — but it is exactly
> what you would want for a sequential generation process like diffusion, where
> you could reweight partially-denoised structures by a partial-quality estimate
> rather than waiting until the end to filter. **Capstone III lives here.**
>
> And watch the *Inverse Scaling* session as the corrective: more inference
> compute sometimes makes things worse. In design, more aggressive filtering
> sometimes selects for filter-gaming rather than quality. Same phenomenon.

---

## D.7.3 The o1/R1 line

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| **Learning to Reason with LLMs** | **Noam Brown (OpenAI, Simons)** | 2024 | 52:03 | [▶](https://www.youtube.com/watch?v=Gr_eYXdHFis) |
| Learning to Reason with LLMs | Jason Weston (Meta, Berkeley MOOC) | 2025 | 1:16:47 | [▶](https://www.youtube.com/watch?v=_MNlLhU33H0) |
| **Speculations on Test-Time Scaling (o1)** | Sasha Rush (Cornell) | 2024 | 47:55 | [▶](https://www.youtube.com/watch?v=6PEJ96k1kiw) |
| How DeepSeek changes the LLM story | Sasha Rush (Simons) | 2025 | 1:11:09 | [▶](https://www.youtube.com/watch?v=KtBcIDtS13M) |
| DeepSeek-R1 Thoughtology | Siva Reddy (Mila/McGill, Simons) | 2025 | 59:41 | [▶](https://www.youtube.com/watch?v=IeCS6hsnOXs) |
| **s1: Simple test-time scaling** | Niklas Muennighoff (first author) | 2025 | 50:59 | [▶](https://www.youtube.com/watch?v=EEkxuqlvCss) |
| s1 (TWIML interview) | Muennighoff | 2025 | 48:59 | [▶](https://www.youtube.com/watch?v=kEfUaLBlSHc) |
| Scaling Test Time Compute to Multi-Agent Civilizations | Noam Brown (Latent Space) | 2025 | 1:17:47 | [▶](https://www.youtube.com/watch?v=ddd4xjuJTyg) |
| ML Perf Reading Group 7: DeepSeek V3 | EleutherAI | 2025 | 53:54 | [▶](https://www.youtube.com/watch?v=hPXTRZ9A-9M) |

**Papers:** DeepSeek-AI 2025, arXiv:2501.12948 (R1) · Muennighoff et al. 2025,
arXiv:2501.19393 (s1) · OpenAI o1 system card.

> **Rush's *Speculations on Test-Time Scaling* is a masterclass in a skill you
> need**: reconstructing how a closed system probably works from public papers
> alone. He is explicit about what is inference and what is evidence. That is
> exactly the discipline required when you read an industrial structure-prediction
> paper with no code and no weights.
>
> **s1 is the result that should change what you attempt.** A thousand curated
> examples and a simple budget-forcing trick reproduced much of the reasoning
> behavior. **The lesson for a small lab: careful data and a simple inference-time
> idea can substitute for enormous training compute.** That is directly
> applicable to your situation and it is the most encouraging single finding in
> Part III.

---

## D.7.4 Process versus outcome supervision

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| **Mathematical Reasoning in Language Models** | Karl Cobbe (OpenAI) | 2023 | 51:17 | [▶](https://www.youtube.com/watch?v=0rfgyQ-wAQM) |
| Noam Brown, Ilge Akkaya and Hunter Lightman on o1 | Sequoia Training Data | 2024 | 45:22 | [▶](https://www.youtube.com/watch?v=jPluSXJpdrA) |

**Papers:** Cobbe et al. 2021, arXiv:2110.14168 (GSM8K and verifiers) ·
**Lightman et al. 2024, ICLR, arXiv:2305.20050 (Let's Verify Step by Step)**.

> **This is the subsection with the most under-exploited protein analogue in the
> entire curriculum.** Outcome supervision scores the final answer; process
> supervision scores each intermediate step, and Lightman et al. show process
> wins decisively.
>
> **A diffusion trajectory is a process.** RFdiffusion takes 50 steps and is
> scored only at the end. Nobody has built a process reward model for
> intermediate denoising states — a model that says "this partially-denoised
> backbone is on a bad trajectory, resample now." The data to train it is
> obtainable: run the pipeline, record intermediate states, label by final
> outcome. **This is a concrete, fundable, novel project and it is stated here in
> three sentences.**

---

## D.7.5 In-context learning and induction heads

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| **Induction Heads** (BlackboxNLP keynote) | **Catherine Olsson (Anthropic)** | 2022 | 37:57 | [▶](https://www.youtube.com/watch?v=yMGG2OENyu0) |
| CS25 V1 — Transformer Circuits, Induction Heads, ICL | Anthropic | 2022 | 59:34 | [▶](https://www.youtube.com/watch?v=pC4zRb_5noQ) |
| A Walkthrough of In-Context Learning and Induction Heads | Neel Nanda w/ Charles Frye | 2022 | 1:03:51 | [▶](https://www.youtube.com/watch?v=dCkQQYwPxdM) |
| Induction Heads and Phase Transitions | Rohan Hitchcock (SLT Summit) | 2023 | 58:06 | [▶](https://www.youtube.com/watch?v=0Dwimu1q5yk) |
| In-context Language Learning and N-gram Heads | Ekin Akyürek (MIT) | 2024 | 53:47 | [▶](https://www.youtube.com/watch?v=CXLL_-UFZsQ) |
| **What Learning Algorithm is In-Context Learning?** | Jacob Andreas (MIT, Harvard CMSA) | 2023 | 50:16 | [▶](https://www.youtube.com/watch?v=UNVl64G3BzA) |
| Toward Understanding In-context Learning | Tengyu Ma (Stanford, Simons) | 2024 | 1:29:35 | [▶](https://www.youtube.com/watch?v=hxrR39mAlR4) |
| In-Context Learning: Simple Function Classes | Gregory Valiant (Stanford, Simons) | 2023 | 1:03:40 | [▶](https://www.youtube.com/watch?v=DiJsg93zQDc) |
| **Pretraining Task Diversity and Non-Bayesian ICL** | Surya Ganguli (Stanford, Simons) | 2023 | 1:05:52 | [▶](https://www.youtube.com/watch?v=Gag7H4M-GdQ) |
| Uncovering Mesa-Optimization Algorithms in Transformers | Nino Scherrer (IVADO) | 2026 | 37:33 | [▶](https://www.youtube.com/watch?v=zpsJgG7rosE) |
| Associative memories as a building block in Transformers | Alberto Bietti (Flatiron, Simons) | 2024 | 38:37 | [▶](https://www.youtube.com/watch?v=ncAhx70jTIc) |
| Using Algorithms to Understand Transformers | Vatsal Sharan (USC, Simons) | 2024 | 48:04 | [▶](https://www.youtube.com/watch?v=qHWBk5ewYwI) |

**Papers:** **Olsson et al. 2022, Transformer Circuits (induction heads)** ·
**Akyürek et al. 2023, ICLR, arXiv:2211.15661 (ICL implements gradient descent)**
· Garg et al. 2022, NeurIPS, arXiv:2208.01066 · Xie et al. 2022, ICLR,
arXiv:2111.02080 (ICL as implicit Bayesian inference) · von Oswald et al. 2023,
ICML.

> **The direct molecular connection, and it is not a stretch.** An MSA
> Transformer attends across sequences in an alignment to find the residue at the
> corresponding position in a homolog. **That is an induction head doing
> structural biology.** Olsson's prefix-matching + copying description is a
> mechanistic account of exactly the operation the MSA axis performs.
>
> **Nobody has looked for induction heads in an MSA Transformer.** The
> methodology exists, the model is open, and the hypothesis is sharp. **That is
> Capstone VIII**, and it is the single most tractable bridge project in this
> entire document.

---

## D.7.6 Emergence — and the argument about it

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| **CS25 V2 — Emergent Abilities and Scaling in LLMs** | Jason Wei (author) | 2023 | 1:07:48 | [▶](https://www.youtube.com/watch?v=tVtOevLrt5U) |
| Emergence and reasoning in large language models | Jason Wei (JHU CLSP) | 2022 | 52:04 | [▶](https://www.youtube.com/watch?v=0Z1ZwY2K2-M) |
| **Investigating emergent abilities and challenging dominant research ideas** | **Rylan Schaeffer** (Imbue) | 2024 | 1:03:16 | [▶](https://www.youtube.com/watch?v=blX2RzZYeJo) |
| A Theory for Emergence of Complex Skills in Language Models | Sanjeev Arora (Princeton, Simons) | 2023 | 1:04:45 | [▶](https://www.youtube.com/watch?v=0D23NeBjCeQ) |
| Emergence of Complex Skills in LLMs | Sanjeev Arora (FAR.AI) | 2024 | 6:05 | [▶](https://www.youtube.com/watch?v=LYqqHLaW30w) |
| Progress Measures for Grokking via Mechanistic Interpretability | Neel Nanda w/ Lawrence Chan | 2023 | 43:10 | [▶](https://www.youtube.com/watch?v=IHikLL8ULa4) |
| **CS25 V6 — Distinct Modes of Generalization from Parameters and Context** | Andrew Lampinen (Anthropic) | 2026 | 1:12:30 | [▶](https://www.youtube.com/watch?v=dJtHauhRasc) |
| You Know It Or You Don't: Compositionality and Phase Transitions | Simons Institute | 2025 | 57:00 | [▶](https://www.youtube.com/watch?v=WJ89r5x5hDA) |
| **ICML 2024 Tutorial: Physics of Language Models** | **Zeyuan Allen-Zhu** | 2024 | 1:53:43 | [▶](https://www.youtube.com/watch?v=yBL7J0kgldU) |

**Papers:** **Wei et al. 2022, TMLR (emergent abilities)** · **Schaeffer et al.
2023, NeurIPS, arXiv:2304.15004 (Are Emergent Abilities a Mirage?)** ·
Arora & Goyal 2023, arXiv:2307.15936 · Nanda et al. 2023, ICLR,
arXiv:2301.05217 (grokking).

> **Watch Wei and then Schaeffer, in that order, in one sitting.** This is the
> best-constructed disagreement in Part III. Wei documents capabilities appearing
> abruptly with scale. Schaeffer argues the abruptness is manufactured by
> discontinuous metrics — exact-match accuracy is a step function over a
> continuously improving quantity — and that smooth metrics show smooth
> improvement.
>
> **Then apply it to yourself.** "Success rate above 4 Å RMSD" is a thresholded
> metric. "Fraction of designs that express" is a thresholded metric. **Every
> apparent discontinuity in a protein benchmark should be checked against
> Schaeffer's argument before it is believed**, and most never are.
>
> **Allen-Zhu's *Physics of Language Models* tutorial is the methodology lesson
> of this whole Part.** Controlled synthetic data, clean ablations, falsifiable
> claims — doing science on models rather than reporting benchmark numbers. If
> you want a template for how to run a rigorous empirical study of a model, this
> two-hour tutorial is it.

---

## D.7.7 Is reasoning real? — the standing debate

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| **Debate: Sparks versus Embers** | Bubeck, McCoy, Izmailov, Moitra (Simons) | 2024 | 1:22:10 | [▶](https://www.youtube.com/watch?v=H3TnTxVKIOQ) |
| **LLMs can't plan (..but they can help you in planning)** | Subbarao Kambhampati (ICAPS keynote) | 2023 | 1:12:44 | [▶](https://www.youtube.com/watch?v=qPhbh9fQ7tI) |
| LLM-Modulo Frameworks | Kambhampati (ICRA workshop) | 2024 | 30:51 | [▶](https://www.youtube.com/watch?v=oC1PESU0xN4) |
| Do you think that ChatGPT can reason? | Kambhampati (MLST) | 2024 | 1:42:28 | [▶](https://www.youtube.com/watch?v=y1WnHpedi2A) |
| **Pattern Recognition vs True Intelligence** | François Chollet (MLST) | 2024 | 2:42:55 | [▶](https://www.youtube.com/watch?v=JTU8Ha4Jyfc) |
| **Chollet on OpenAI o-models and ARC** | François Chollet (MLST) | 2025 | 1:26:47 | [▶](https://www.youtube.com/watch?v=w9WE1aOPjHc) |
| Investigating Abstract Reasoning in Humans and Machines | Melanie Mitchell (SFI) | 2026 | 56:59 | [▶](https://www.youtube.com/watch?v=X9M4HKotADo) |
| **Six Principles for Evaluating Cognitive Capabilities in AI Models** | Melanie Mitchell (SFI) | 2026 | 48:41 | [▶](https://www.youtube.com/watch?v=0DpJJFH9jvY) |
| Failures in Reasoning Models | EleutherAI PRA Reading Group | 2025 | 1:03:03 | [▶](https://www.youtube.com/watch?v=GWYdAMGQh1s) |

**Papers:** **McCoy et al. 2024, *PNAS* 121:e2322420121 (Embers of
Autoregression)** · Bubeck et al. 2023, arXiv:2303.12712 (Sparks of AGI) ·
Valmeekam et al. 2023, NeurIPS (planbench) · Kambhampati et al. 2024,
arXiv:2402.01817 (LLM-Modulo) · Chollet 2019, arXiv:1911.01547 (ARC).

> **The Sparks-versus-Embers debate is the single most useful thing in this
> section**, because it is two careful people disagreeing in public with the
> evidence on the table. McCoy's position — that LLM failures are predicted by
> the *probability of the task under the pretraining distribution*, not by its
> logical difficulty — is a falsifiable, mechanistic claim, and it has an exact
> protein analogue: **protein model failures should be predicted by the rarity of
> the fold in the PDB, not by the protein's biophysical difficulty.** Someone
> should test that. It is a one-figure paper and it would settle a lot of
> arguments.
>
> **Mitchell's *Six Principles* is the methodology talk to keep.** It is about
> how to design an evaluation that measures a capability rather than a
> correlate — which is the question behind every benchmark in Atlas S.
>
> **Watch the two Chollet talks in order**, before and after o3's ARC result. He
> updates in public. That is rarer and more valuable than being right the first
> time.
