# D.6 Post-Training and Reinforcement Learning

> **Why a protein designer should care about RLHF.** Because design *is* a
> post-training problem and nobody says so.
>
> A protein language model is pretrained on evolution. Then you want it to
> produce sequences that are stable, soluble, expressible and active — properties
> no pretraining objective contains. That is exactly the structure of RLHF: a
> pretrained distribution, a separately learned reward, and an optimization that
> moves the policy toward the reward while staying near the prior.
>
> **Every pathology the RLHF literature documents therefore applies to you.**
> Reward hacking is a design filter being gamed. KL regularization is the
> stay-near-natural-sequences constraint. Over-optimization is your 1% hit rate.
> This subsection is a vocabulary for problems you already have.

---

## D.6.1 The mechanics, and the over-optimization result

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| **Proxy Objectives in RLHF** (ICML 2023 invited talk) | **John Schulman** | 2023 | 1:01:06 | [▶](https://www.youtube.com/watch?v=e2Dp90pi6Fg) |
| **RLHF: Progress and Challenges** | John Schulman (Berkeley EECS Colloquium) | 2023 | 1:03:32 | [▶](https://www.youtube.com/watch?v=hhiLw5Q_UFg) |
| Reinforcement Learning from Human Feedback | Nathan Lambert (UCL DARK) | 2023 | 47:15 | [▶](https://www.youtube.com/watch?v=8SgKDSX-Me0) |
| AI Safety, RLHF, and Self-Supervision | Jared Kaplan (MLSys #79) | 2023 | 1:02:37 | [▶](https://www.youtube.com/watch?v=fqC3D-zNJUM) |
| CS25 V4 — Aligning Open Language Models | Nathan Lambert (AI2) | 2024 | 1:16:21 | [▶](https://www.youtube.com/watch?v=AdLgPmcrXwQ) |

**Papers:** **Ouyang et al. 2022, NeurIPS, arXiv:2203.02155 (InstructGPT)** ·
**Gao, Schulman & Hilton 2023, ICML, arXiv:2210.10760 (Scaling Laws for Reward
Model Overoptimization)** · Christiano et al. 2017, NeurIPS · Stiennon et al.
2020, NeurIPS · Bai et al. 2022, arXiv:2204.05862.

> **Gao, Schulman & Hilton is the paper to read twice.** It measures what happens
> as you optimize harder against a learned reward: true performance rises, peaks,
> and then *falls*, while the proxy reward keeps climbing. They fit the curve.
>
> **Now map it.** Your learned reward is pLDDT, or interface pAE, or a
> self-consistency RMSD threshold. Your optimization is the design loop. The
> paper predicts that past some point, pushing harder on your filters makes your
> designs *worse* in the tube while looking better on screen. **Nobody in protein
> design has measured that curve.** Measuring it is Capstone III, and it would be
> among the most useful things anyone could publish about design pipelines.

---

## D.6.2 The Post-Training Course — Nathan Lambert, AI2, 2026

A complete 14-lecture course, released alongside *The RLHF Book*, and the
best-organized systematic treatment of post-training that exists. **It is current
to 2026**, which matters in a subfield that reorganizes annually.

| # | Lecture | Len | Link |
|---|---|---|---|
| 0 | ML Foundations (prerequisites) for Post-Training | 23:53 | [▶](https://www.youtube.com/watch?v=MMDNaeIFVy8) |
| 1 | Post-Training and RLHF Overview | 46:10 | [▶](https://www.youtube.com/watch?v=o6l6tJQgUg4) |
| 2 | RLHF Foundations, IFT, Reward Modeling, Rejection Sampling | 49:49 | [▶](https://www.youtube.com/watch?v=4gIwiSPmQkU) |
| 3 | **Understanding Policy Gradient Algorithms for RL on LLMs** | 57:35 | [▶](https://www.youtube.com/watch?v=K_Sj_-1BUMM) |
| 4 | Implementing RL Algorithms for LLMs | 53:36 | [▶](https://www.youtube.com/watch?v=i-AIMpZHgeg) |
| 5 | The Rise of Reasoning Models | 45:20 | [▶](https://www.youtube.com/watch?v=o4AB5xHIDdM) |
| 6 | **Direct Preference Optimization (DPO) and Friends** | 42:44 | [▶](https://www.youtube.com/watch?v=6g6b4gvO-y0) |
| 7 | On-Policy Distillation & Synthetic Data in Post-Training | 49:40 | [▶](https://www.youtube.com/watch?v=6nyJ8y8ghsE) |
| 8 | **Preference Data: The Most Opaque Part of Post-Training** | 35:53 | [▶](https://www.youtube.com/watch?v=Y2tv5vuaxFs) |
| 9 | **Over-Optimization and RLHF's Bad Reputation** | 23:34 | [▶](https://www.youtube.com/watch?v=y04JhXpiI4s) |
| 10 | **Regularization in RL, Why RL Generalizes, and Why SFT Forgets** | 31:33 | [▶](https://www.youtube.com/watch?v=IwpYxANrpUs) |
| 11 | How Language Models Use Tools and the Path to Agents | 37:47 | [▶](https://www.youtube.com/watch?v=GMry2DzC304) |
| 12 | How Evaluation Has Evolved with Frontier Model Progress | 32:11 | [▶](https://www.youtube.com/watch?v=dFafQmClYq4) |
| 13 | An Introduction to Character Training | 32:56 | [▶](https://www.youtube.com/watch?v=xECWRYBxq1E) |
| — | From Academic Research to a Frontier LLM: A Case Study in DPO | 1:06:30 | [▶](https://www.youtube.com/watch?v=rhA7pLVt4E0) |

**Lectures 9 and 10 are the two to watch first** if you are short on time.
Lecture 10 in particular — why RL generalizes and SFT forgets — is a claim with
a direct protein analogue that nobody has tested: does fine-tuning a PLM on a
narrow family cause catastrophic forgetting of the broader distribution, and
would a KL-regularized RL objective avoid it?

---

## D.6.3 DPO, PPO and the algorithmic debate

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| **CS234 Guest Lecture on DPO — all three co-authors** | Rafailov, Sharma & Mitchell (Stanford) | 2024 | 1:18:44 | [▶](https://www.youtube.com/watch?v=Q7rl8ovBWwQ) |
| CS224N Lecture 10 — Post-training | Archit Sharma (Stanford) | 2025 | 1:19:42 | [▶](https://www.youtube.com/watch?v=35X6zlhoCy4) |
| DPO has given us alignment without the overhead | Sharma & Rafailov | 2024 | 20:19 | [▶](https://www.youtube.com/watch?v=wSva87OcaS4) |
| An update on DPO vs PPO for LLM alignment | Nathan Lambert | 2024 | 13:23 | [▶](https://www.youtube.com/watch?v=rDF7eFPeVto) |
| DPO Debate: Is RL needed for RLHF? | Nathan Lambert | — | 26:55 | [▶](https://www.youtube.com/watch?v=YJMCSVLRUNs) |
| Asynchronous RLHF: Faster Off-Policy RL for LMs | Michael Noukhovitch (Mila, Cohere) | 2025 | 51:11 | [▶](https://www.youtube.com/watch?v=3Tr5rS3uDDs) |
| Efficient Policy Optimization Techniques for LLMs | Kianté Brantley (Harvard, Simons) | 2025 | 45:35 | [▶](https://www.youtube.com/watch?v=JudHG3tiln4) |
| **Coherence in RLHF Preference Data** | Shuo Li Liu (Cohere Labs) | 2026 | 48:39 | [▶](https://www.youtube.com/watch?v=V_l4vOL_1Ms) |

**Papers:** **Rafailov et al. 2023, NeurIPS, arXiv:2305.18290 (DPO)** ·
Schulman et al. 2017, arXiv:1707.06347 (PPO) · Ethayarajh et al. 2024 (KTO) ·
Meng et al. 2024 (SimPO) · Xu et al. 2024, ICML (**Is DPO superior to PPO?**).

> **The DPO derivation is the most elegant result in this whole Part and you
> should be able to reproduce it.** The claim: the optimal KL-regularized policy
> has a closed form in terms of the reward, so the reward can be *eliminated* and
> the preference likelihood written directly in terms of the policy. No reward
> model, no RL loop.
>
> **Derivation checkpoint 58.** Derive it. Then answer the protein question:
> your preference data is a pair of designs where one expressed and one did not.
> Can you DPO a protein language model on that? **What is the Bradley-Terry
> assumption buying, and is it true for wet-lab outcomes?** The Cohere talk on
> preference-data coherence is the right companion — it asks exactly when the
> Bradley-Terry model is valid, and the answer for noisy assay data is not
> obviously yes.

---

## D.6.4 RLVR — reinforcement learning with verifiable rewards

**This is the subsection with the most direct protein analogue**, because a
verifier is exactly what design pipelines have: a structure predictor that says
whether the sequence folds back.

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| Tulu 3: Frontiers in Open Language Model Post-Training | Nathan Lambert (AI2) | 2024 | 1:01:45 | [▶](https://www.youtube.com/watch?v=ltSzUIJ9m6s) |
| Open Training Recipes: LLM Reasoning | Hanna Hajishirzi (UW/AI2, Berkeley MOOC) | 2025 | 1:20:53 | [▶](https://www.youtube.com/watch?v=cMiu3A7YBks) |
| Open Training Recipes for Reasoning | Hajishirzi | 2025 | 46:35 | [▶](https://www.youtube.com/watch?v=i591a2Pv390) |
| Experimenting with RLVR | Nathan Lambert (USC ISI) | 2025 | 47:13 | [▶](https://www.youtube.com/watch?v=zYeIqzULzr0) |
| **Spurious Rewards: Rethinking Training Signals in RLVR** | Stella Li (Cohere Labs) | 2025 | 1:02:11 | [▶](https://www.youtube.com/watch?v=xXXdea-i5ic) |
| Early stages of the RL era of language models | Nathan Lambert (UCSC) | 2025 | 59:31 | [▶](https://www.youtube.com/watch?v=J1APR8Bo9dE) |
| GRPO's new variants and implementation secrets | Nathan Lambert | 2025 | 22:23 | [▶](https://www.youtube.com/watch?v=amrJDwMUFNs) |
| Random Sparse Subnetworks suffice for RLVR | EleutherAI PRA Reading Group | 2026 | 41:24 | [▶](https://www.youtube.com/watch?v=BaAaD0JH6BE) |
| **CS336 2026 Lecture 16: Post-Training — RLVR** | Stanford | 2026 | 1:15:50 | [▶](https://www.youtube.com/watch?v=dIFAi87Ws4E) |

**Papers:** Lambert et al. 2024, arXiv:2411.15124 (Tulu 3) · Shao et al. 2024
(GRPO / DeepSeekMath) · DeepSeek-AI 2025 (R1).

> **Assign the *Spurious Rewards* talk as a critical-reading exercise.** The
> finding: some models improve on math under *random or incorrect* reward
> signals. If that holds, RLVR is sometimes eliciting a capability that was
> already in the pretrained model rather than teaching anything. **That is the
> sharpest open question in post-training**, and its protein analogue is sharp
> too: when a design pipeline's filters "improve" results, is the generator
> getting better or is the filter just selecting from what was already there?
>
> **Derivation checkpoint 59** asks you to design the experiment that
> distinguishes elicitation from learning, in both settings.

---

## D.6.5 Reward modeling, reward hacking and supervision

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| Introducing RewardBench | Nathan Lambert (AI2) | 2024 | 16:50 | [▶](https://www.youtube.com/watch?v=CAaHAfCqrBA) |
| **Supervising AI on hard tasks** | Jan Leike (Anthropic) | 2024 | 33:34 | [▶](https://www.youtube.com/watch?v=PuESFNSh_Qo) |
| Forecasting and Aligning AI | Jacob Steinhardt (Berkeley) | 2022 | 54:35 | [▶](https://www.youtube.com/watch?v=ZOc_SqEhKVM) |
| Understanding and Steering Generative AI Systems | Jacob Steinhardt (Simons) | 2024 | 1:03:30 | [▶](https://www.youtube.com/watch?v=gh7tff8roKw) |
| Oversight of Foundation Models | Jacob Steinhardt (IPAM/UCLA) | 2026 | 56:33 | [▶](https://www.youtube.com/watch?v=L9Vnd9-CV5U) |
| **Prover-Verifier Games Improve Legibility of LLM Outputs** | Yining Chen (OpenAI, Simons) | 2024 | 40:49 | [▶](https://www.youtube.com/watch?v=jIvMB0dbpiI) |
| Interactive Proofs, Debate, and AI Safety | Jonah Brown-Cohen (DeepMind, Simons) | 2024 | 53:35 | [▶](https://www.youtube.com/watch?v=b1hdi7jMdxU) |

**Papers:** Lambert et al. 2024, arXiv:2403.13787 (RewardBench) ·
**Burns et al. 2023, arXiv:2312.09390 (weak-to-strong generalization)** ·
**Pan, Bhatia & Steinhardt 2022, ICLR, arXiv:2201.03544 (the effects of reward
misspecification)** · Kirchner et al. 2024, arXiv:2407.13692.

> **Pan, Bhatia & Steinhardt is the reward-hacking paper with the cleanest
> experiments**, and it generalizes immediately: a misspecified proxy produces
> *phase transitions* in behavior as capability increases, not gradual
> degradation. A more capable design model does not game your filters slightly
> more — it games them suddenly and completely. If you have ever seen a design
> campaign produce a cluster of nearly identical, high-scoring, useless
> sequences, you have seen this.

---

## D.6.6 Distillation and synthetic data

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| Distilling the Knowledge in a Neural Network | Geoffrey Hinton | — | 54:41 | [▶](https://www.youtube.com/watch?v=kfR6Jq-51x0) |
| Learning by Distilling Context | Charlie Snell (Berkeley, Cohere) | 2022 | 53:16 | [▶](https://www.youtube.com/watch?v=IKtAFLUAYvM) |
| CMU Advanced NLP (11): Distillation, Quantization, Pruning | Graham Neubig | 2024 | 1:04:21 | [▶](https://www.youtube.com/watch?v=DvVGkj4zhVU) |
| **Instruction Tuning of LLMs (Self-Instruct)** | Yizhong Wang (UW, JHU CLSP) | 2023 | 48:22 | [▶](https://www.youtube.com/watch?v=jpbt3IZgbcc) |
| Lessons from the Alpaca Project | Tatsu Hashimoto (Stanford) | 2024 | 23:36 | [▶](https://www.youtube.com/watch?v=wqJH7EMOHrg) |
| Textbooks Are All You Need | Sébastien Bubeck | 2023 | 37:15 | [▶](https://www.youtube.com/watch?v=24O1KcIO3FM) |
| Small Language Models | Sébastien Bubeck | 2024 | 1:04:03 | [▶](https://www.youtube.com/watch?v=DqIhGQWzjSo) |
| Synthetic Data / Smol Models | Loubna Ben Allal (HF) | 2024 | 28:07 | [▶](https://www.youtube.com/watch?v=AjmdDy7Rzx0) |
| Self-Play Fine-Tuning (SPIN) | Zixiang Chen (UCLA, first author) | 2024 | 1:02:31 | [▶](https://www.youtube.com/watch?v=Fg4C6YZcqQ4) |
| Self-Play for LMs on Programming Puzzles | Adam Tauman Kalai (MSR, Simons) | 2023 | 1:03:54 | [▶](https://www.youtube.com/watch?v=_b0Y_Oj7id4) |

**Papers:** Hinton et al. 2015, arXiv:1503.02531 · **Wang et al. 2023, ACL,
arXiv:2212.10560 (Self-Instruct)** · Gunasekar et al. 2023, arXiv:2306.11644
(Textbooks Are All You Need) · Chen et al. 2024, arXiv:2401.01335 (SPIN) ·
**Shumailov et al. 2024, *Nature* 631:755 (model collapse)**.

> **Model collapse is the one to think hardest about**, because biology is
> already doing it. The AFDB contains 200 million *predicted* structures. Models
> are now trained on them. Shumailov et al. show that recursive training on
> generated data degrades the distribution's tails — which, in a structural
> context, means the unusual folds. **Nobody has measured whether AFDB-trained
> models have lost tail diversity.** That is a well-defined, important, and
> currently unanswered question.

---

## D.6.7 Paired reading — D.6

| Watch this | Then read this | Hold this question |
|---|---|---|
| **Schulman, *Proxy Objectives in RLHF*** | **Gao et al. 2023, arXiv:2210.10760** | Plot the over-optimization curve for pLDDT as a design reward. |
| Lambert, Post-Training L9–10 | The RLHF Book, corresponding chapters | Why does RL generalize where SFT forgets? Does that hold for PLMs? |
| **CS234, *DPO with all three authors*** | **Rafailov et al. 2023, arXiv:2305.18290** | Derive DPO. Then ask whether Bradley-Terry fits wet-lab outcomes. |
| Liu, *Coherence in RLHF Preference Data* | The paper | When is pairwise preference learning valid? Check your assay. |
| **Li, *Spurious Rewards in RLVR*** | The paper | Design the experiment separating elicitation from learning. |
| Lambert, *Experimenting with RLVR* | Shao et al. 2024 (GRPO) | A verifier-based reward. What is your verifier, and is it gameable? |
| **Steinhardt, *Forecasting and Aligning AI*** | **Pan et al. 2022, arXiv:2201.03544** | Reward hacking is a phase transition. Have you seen one? |
| Leike, *Supervising AI on hard tasks* | **Burns et al. 2023, arXiv:2312.09390** | Can a weak verifier supervise a strong generator? What is the protein version? |
| Wang, *Self-Instruct* | **arXiv:2212.10560** | Bootstrapping data from the model. What is the protein analogue, and its risk? |
| Ben Allal, *Synthetic data* | **Shumailov et al. 2024, *Nature* 631:755** | Measure whether AFDB-trained models lost tail fold diversity. |
