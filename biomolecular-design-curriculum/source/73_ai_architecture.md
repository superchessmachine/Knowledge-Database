# D.4 Architecture Research

> **Why this comes first in Part III.** Every model in Atlas P, Q and R is an
> architecture decision stack: what the attention does, how position is encoded,
> where the normalization goes, what the tokens are. Those decisions were made
> in the language-modeling literature and inherited wholesale, usually without
> re-examination for the molecular setting.
>
> **The opportunity is specific.** Most of the architecture choices in protein
> models were imported from text, where the sequence is one-dimensional,
> causally ordered, and discretely tokenized. None of those three things is true
> of a protein in 3D. **Every place where that mismatch is unexamined is a
> paper.**

---

## D.4.1 State space models — the strongest single thread here

Watch these in order. The claims change visibly across the five years, and
seeing a researcher become *more modest* as the evidence comes in is itself the
lesson.

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| **Efficiently Modeling Long Sequences with Structured State Spaces** (S4) | Albert Gu (Stanford MLSys #46) | 2021 | 57:18 | [▶](https://www.youtube.com/watch?v=EvQ3ncuriCM) |
| Structured State Space Models for Deep Sequence Modeling | Albert Gu (CMU) | 2023 | 1:04:27 | [▶](https://www.youtube.com/watch?v=OpJMn8T7Z34) |
| Structured State Space Models (the long version) | Albert Gu (LxMLS Lisbon) | 2024 | 1:34:12 | [▶](https://www.youtube.com/watch?v=WC9tqkCpq4s) |
| EPFL AI Center — SSMs for Deep Sequence Modeling | Albert Gu (EPFL) | 2024 | 1:01:10 | [▶](https://www.youtube.com/watch?v=Fo4mOOXYyIQ) |
| **On the Tradeoffs of State Space Models** | Albert Gu (Simons Institute) | 2024 | 49:05 | [▶](https://www.youtube.com/watch?v=ksRp_DIHWj4) |
| **CS25 V6 — On the Tradeoffs of SSMs and Transformers** | Albert Gu (CMU, Cartesia) | **2026** | 1:17:07 | [▶](https://www.youtube.com/watch?v=OyimE74UMF8) |
| Computational Benefits and Limitations of Transformers and SSMs | Eran Malach (Kempner, Simons) | 2024 | 50:52 | [▶](https://www.youtube.com/watch?v=sbViSPM3lVE) |
| **Hardware-aware Algorithms for Sequence Modeling** | Tri Dao (Stanford MLSys #87) | 2024 | 1:19:06 | [▶](https://www.youtube.com/watch?v=foG0ebzuw34) |
| Model Architecture Design for Modern Hardware | Tri Dao (Kempner, Harvard) | 2025 | 1:08:38 | [▶](https://www.youtube.com/watch?v=aFQetsW4NFA) |

**Papers:** Gu et al. 2021, arXiv:2111.00396 (S4) · Fu et al. 2022,
arXiv:2212.14052 (H3) · **Gu & Dao 2023, arXiv:2312.00752 (Mamba)** ·
**Dao & Gu 2024, arXiv:2405.21060 (Mamba-2, state space duality)**.

> **The molecular connection is direct and it is already being made.** Evo and
> Evo 2 (Atlas Q.5) are built on this line — StripedHyena, then a Mamba-adjacent
> architecture — precisely because genomes are long and attention is quadratic.
> If you want to understand *why* genomic language models have a different
> architecture from protein language models, this subsection is the answer.
>
> **Watch the 2021 talk and the 2026 talk back to back.** The 2021 talk claims
> SSMs are a general replacement for attention. The 2026 talk, by the same
> person, is careful about what a fixed-size state loses relative to a KV cache
> and argues for hybrids. That is what intellectual honesty looks like across
> five years, and it is a better lesson than either talk alone.

---

## D.4.2 Linear attention and efficient attention

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| **Linear Attention and Beyond (interactive tutorial)** | Songlin Yang (MIT), hosted by Sasha Rush | 2025 | 1:27:08 | [▶](https://www.youtube.com/watch?v=d0HJvGSWw8A) |
| Understanding and Improving Efficient Language Models | Simran Arora (Stanford, Simons) | 2024 | 46:36 | [▶](https://www.youtube.com/watch?v=DmuZ3ckl8rs) |
| Monarch Mixer: Making Foundation Models More Efficient | Dan Fu (Stanford MLSys #86) | 2023 | 56:32 | [▶](https://www.youtube.com/watch?v=IS59IwGLvVs) |
| Dynamic Short Convolutions Improve Transformers | Oliver Sieberling (Cohere Labs) | 2026 | 43:33 | [▶](https://www.youtube.com/watch?v=DnlXx8DXR5I) |
| ML Perf Reading Group 18: Kimi Delta Attention | EleutherAI | 2025 | 1:22:27 | [▶](https://www.youtube.com/watch?v=HEFM4NXsWpQ) |

**Papers:** Yang et al. 2023, arXiv:2312.06635 (Gated Linear Attention) ·
Yang et al. 2024, arXiv:2406.06484 (DeltaNet, parallelized delta rule) ·
Katharopoulos et al. 2020, ICML (transformers are RNNs) · Arora et al. 2024
(Based: the recall-throughput tradeoff).

> **Arora's recall-throughput tradeoff is the one to internalize.** Linear
> attention buys throughput and pays in associative recall. For a protein MSA —
> where the model must retrieve the homologous residue in a distant sequence —
> recall is exactly the operation that matters. **Nobody has carefully measured
> what linear attention costs an MSA-based model.** That is a clean, tractable
> experiment and nobody has run it.

---

## D.4.3 Positional encoding, normalization, tokenization

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| **ALiBi enables transformers to handle longer inputs** | Ofir Press (author) | 2022 | 46:57 | [▶](https://www.youtube.com/watch?v=Pp61ShI9VGc) |
| **CS336 2026 Lecture 3: Architectures** | Liang / Hashimoto (Stanford) | 2026 | 1:29:14 | [▶](https://www.youtube.com/watch?v=lVynu4bo1rY) |
| **CS336 2026 Lecture 4: Attention Alternatives** | Stanford | 2026 | 1:26:20 | [▶](https://www.youtube.com/watch?v=cKSwj_qZ8Jg) |
| **CS336 2026 Lecture 1: Overview, Tokenization** | Stanford | 2026 | 1:19:22 | [▶](https://www.youtube.com/watch?v=JuoVZkPBiKk) |
| Meta's MEGABYTE with Lili Yu | Lili Yu (author, Cognitive Revolution) | 2023 | 1:32:22 | [▶](https://www.youtube.com/watch?v=8EIqHFFdccA) |

**Papers:** **Su et al. 2021, arXiv:2104.09864 (RoPE)** · **Press et al. 2021,
arXiv:2108.12409 (ALiBi)** · Peng et al. 2023, arXiv:2309.00071 (YaRN) ·
Zhang & Sennrich 2019, NeurIPS (RMSNorm) · Xiong et al. 2020, ICML
(**pre-LN vs post-LN**) · Yu et al. 2023, arXiv:2305.07185 (MEGABYTE).

> **Honest gap, reported as found.** There is no author talk for RoPE, for YaRN,
> or for normalization placement. The CS336 2026 Lecture 3 is the substitute and
> it is a good one — a research-grade treatment of exactly these choices with the
> ablations. **CS336 Lectures 3 and 4 together are the single best "what actually
> matters in an architecture" resource that exists**, and they are current.
>
> **The molecular question this raises.** RoPE encodes relative position along a
> 1D sequence. A protein's relevant "position" is a position in 3D space, which
> is why AlphaFold uses pair representations and invariant point attention
> instead. **What is the right relative positional encoding for a structure?**
> Nobody has a clean answer, and the question is well-posed.

---

## D.4.4 Mixture of experts

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| **Switch Transformers: Scaling to Trillion Parameter Models** | Barret Zoph (KUIS AI) | 2021 | 55:54 | [▶](https://www.youtube.com/watch?v=2pbvnxdaKaw) |
| **Sparse Expert Models — with the authors** | Zoph & Fedus | 2022 | 58:22 | [▶](https://www.youtube.com/watch?v=ccBMRryxGog) |
| MIAI Deeptails Seminar | Zoph & Fedus (Google Brain) | 2022 | 1:11:39 | [▶](https://www.youtube.com/watch?v=77mK3gtWK28) |
| CS25 V1 — MoE and the Switch Transformer | Stanford (speaker not in metadata) | 2022 | 1:05:44 | [▶](https://www.youtube.com/watch?v=U8J32Z3qV8s) |
| CS25 V4 — Demystifying Mixtral of Experts | Albert Jiang (Mistral/Cambridge) | 2024 | 1:04:31 | [▶](https://www.youtube.com/watch?v=RcJ1YXHLv5o) |
| **CS336 2025 Lecture 4: Mixture of experts** | Stanford | 2025 | 1:22:04 | [▶](https://www.youtube.com/watch?v=LPv1KfUXLCo) |
| ML Perf Reading Group 15: Megablocks | EleutherAI | 2025 | 1:00:30 | [▶](https://www.youtube.com/watch?v=tWkMj6lUp1c) |
| ML Perf Reading Group 17: MXFP8 Training for MoEs | EleutherAI | 2025 | 37:12 | [▶](https://www.youtube.com/watch?v=MlLofYn8Ae0) |

**Papers:** **Fedus et al. 2022, JMLR 23:120 (Switch Transformer)** ·
Zoph et al. 2022, arXiv:2202.08906 (ST-MoE) · Jiang et al. 2024,
arXiv:2401.04088 (Mixtral) · Shazeer et al. 2017, ICLR (the original
sparsely-gated MoE) · Gale et al. 2023, MLSys (MegaBlocks).

> **The Zoph & Fedus author interview is the valuable one**, because they
> describe the fine-tuning instabilities that are not in the papers. A field's
> oral tradition — what reviewers never see — is most accessible in exactly this
> format.
>
> **Why a protein person should care.** A protein model is asked to handle
> enzymes, membrane proteins, antibodies and IDPs with one set of weights. That
> is the textbook case for conditional computation, and essentially nobody has
> tried routing by structural class. **The experiment is sitting there.**

---

## D.4.5 Long context

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| **The Frontier between Retrieval-augmented and Long-context LMs** | Danqi Chen (Princeton, Simons) | 2025 | 59:30 | [▶](https://www.youtube.com/watch?v=p4-I1LfYK9A) |
| ML Perf Reading Group 4: Ring Attention | EleutherAI | 2025 | 48:20 | [▶](https://www.youtube.com/watch?v=fC9L8J7dVFI) |
| GPU MODE Lecture 13: Ring Attention | GPU MODE | 2024 | 1:15:35 | [▶](https://www.youtube.com/watch?v=ws7angQYIxI) |
| ML Perf Reading Group 20: Native Sparse Attention | EleutherAI | 2026 | 59:24 | [▶](https://www.youtube.com/watch?v=HS5FJbif5A0) |
| CMU Advanced NLP (13): Long Sequence Models | Graham Neubig | 2024 | 57:11 | [▶](https://www.youtube.com/watch?v=t_FZAGUjbks) |

**Papers:** Liu et al. 2023, arXiv:2310.01889 (Ring Attention) ·
Yuan et al. 2025, arXiv:2502.11089 (Native Sparse Attention) ·
Beltagy et al. 2020 (Longformer) · Child et al. 2019 (sparse transformers).

> **Ring attention is directly relevant here.** AF3-style models hit
> memory walls on large complexes — which is the entire reason the chromatin
> work needed chunked triangle multiplication. Ring attention solves the same
> class of problem by sharding the sequence across devices with overlapped
> communication. **Whether the triangle operations admit a ring decomposition is
> an open engineering question with a real payoff.**

---

## D.4.6 Diffusion language models

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| **How to Build a Modern Diffusion Language Model** | Volodymyr Kuleshov (Cornell, Simons) | 2026 | 48:40 | [▶](https://www.youtube.com/watch?v=1fUSw9Jgvog) |
| Advancing Diffusion Models for Text Generation | Kilian Weinberger (Cornell, Simons) | 2025 | 1:01:50 | [▶](https://www.youtube.com/watch?v=klW65MWJ1PY) |
| Unlocking Lossless Speedups via Discrete Diffusion | Subham Sahoo (Cohere Labs) | 2026 | 1:09:04 | [▶](https://www.youtube.com/watch?v=lZmgfPMyWg8) |
| Diffusion LLM & Why the Future Won't Be Autoregressive | Stefano Ermon (Stanford/Inception) | 2026 | 49:18 | [▶](https://www.youtube.com/watch?v=CYYroZkqu-I) |
| Discrete diffusion by estimating ratios of the data distribution | Generative Memory Lab | 2024 | 1:20:34 | [▶](https://www.youtube.com/watch?v=_1qv_LNjH9U) |

**Papers:** **Lou et al. 2024, ICML, arXiv:2310.16834 (SEDD — score entropy)** ·
Sahoo et al. 2024, NeurIPS (MDLM) · Austin et al. 2021, NeurIPS (D3PM) ·
Campbell et al. 2022, NeurIPS (continuous-time discrete diffusion).

> **This subsection is the clearest two-way bridge in Part III.** EvoDiff, DPLM
> and the discrete-diffusion half of Multiflow (Atlas Q.2, R.2) are the *same
> mathematics* applied to amino acids instead of word pieces. The molecular
> field adopted it early and in some respects pushed it further, because protein
> sequences are short, the vocabulary is 20 symbols, and there is no left-to-right
> causality to give up.
>
> **The idea that has not been carried back:** molecular diffusion models
> routinely condition on a 3D structure. Text diffusion has no equivalent of a
> structural conditioner. What would it mean to condition a language diffusion
> model on a *plan* in the way RFdiffusion conditions on a motif? That question
> is open in both directions.

---

## D.4.7 RWKV, Hyena, xLSTM — the other attention alternatives

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| How RWKV-7 "Goose" and Its Linear Inference Work | Eugene Cheah (author, Oxen AI) | 2025 | 1:11:16 | [▶](https://www.youtube.com/watch?v=4Bdty7GOrbw) |
| Beyond Transformers — Intro to RWKV | Cheah & Vanderbyl (Linux Foundation) | 2023 | 34:16 | [▶](https://www.youtube.com/watch?v=I-HMKky7Qsw) |
| **xLSTM: New Architectures for LLMs** | **Sepp Hochreiter** (SCIoI) | 2024 | 1:25:38 | [▶](https://www.youtube.com/watch?v=-OwYtltMeXY) |
| LSTM: The Comeback Story? | Hochreiter (MLST) | 2025 | 1:07:02 | [▶](https://www.youtube.com/watch?v=8u2pW2zZLCs) |
| **HyenaDNA: Long-Range Genomic Sequence Modeling** | Eric Nguyen (Valence) | 2023 | 1:20:38 | [▶](https://www.youtube.com/watch?v=zGPPG6insm8) |
| Tri Dao and Michael Poli on the future of LLM architectures | Interconnects | 2023 | 36:51 | [▶](https://www.youtube.com/watch?v=OFFHiJzPpCQ) |

**Papers:** Peng et al. 2023, arXiv:2305.13048 (RWKV) · Peng et al. 2025,
arXiv:2503.14456 (RWKV-7) · Beck et al. 2024, arXiv:2405.04517 (xLSTM) ·
Poli et al. 2023, ICML (Hyena) · **Nguyen et al. 2023, NeurIPS,
arXiv:2306.15794 (HyenaDNA)**.

**HyenaDNA is the single entry in this subsection that is already biology.**
Watch it to see an architecture idea cross from language to genomics in under a
year, and note what had to change: single-nucleotide resolution, no tokenizer,
and a context length chosen by the biology rather than by the benchmark.

---

## D.4.8 Paired reading — D.4

| Watch this | Then read this | Hold this question |
|---|---|---|
| Gu 2021, *S4* | **arXiv:2111.00396** | HiPPO gives the initialization. What is being approximated? |
| **Gu 2026, *Tradeoffs of SSMs*** | **arXiv:2405.21060 (Mamba-2)** | What exactly does a fixed-size state lose? Name the task class. |
| Dao, *Hardware-aware algorithms* | **arXiv:2312.00752 (Mamba)** | Selectivity breaks the convolution. How is the scan made fast anyway? |
| Yang, *Linear Attention and Beyond* | arXiv:2312.06635; arXiv:2406.06484 | Write the delta rule as a linear attention update. |
| Arora, *Efficient LMs* | The Based papers | Measure the recall-throughput tradeoff. Then ask what it costs an MSA model. |
| Press, *ALiBi* | **arXiv:2108.12409** then **arXiv:2104.09864 (RoPE)** | What is the right relative position for a 3D structure? |
| **CS336 2026 L3 + L4** | The ablation tables in each | Which architecture choices survive controlled comparison? |
| Zoph & Fedus, *Sparse Expert Models* | **Fedus et al. 2022, JMLR 23:120** | Design an MoE routed by structural class. What is the auxiliary loss? |
| Danqi Chen, *Retrieval vs long context* | Her paper | When does long context subsume retrieval? Apply the answer to MSAs. |
| **Kuleshov, *Modern diffusion LM*** | **Lou et al. 2024 (SEDD)** | Compare the loss to EvoDiff's. What is the same and what differs? |
| Nguyen, *HyenaDNA* | **arXiv:2306.15794** | An architecture crossed domains in a year. What had to change? |
| Hochreiter, *xLSTM* | arXiv:2405.04517 | The person who invented LSTM is still working on it. What is the claim? |
