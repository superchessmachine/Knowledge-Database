# D.8 Deep Learning Theory

### The "why does any of this work" layer

## Why this module exists

Everything else in an AI curriculum teaches you to *build*. This module is the
only one that teaches you to *explain*, and explanation is where original
contributions to artificial intelligence itself actually come from. The field
has a large and embarrassing gap between what works and what anyone can justify:
networks with more parameters than data points generalize, gradient descent on a
wildly nonconvex loss finds good minima, test error goes down after it has
already gone up, and abilities appear at scale that nobody predicted. Each of
those is an open problem with a recorded literature of people arguing about it on
stage.

A warning specific to this module. **Deep learning theory is the one area where
the recorded talks are strictly better than the papers for learning purposes.**
The papers compress away the failed attempts; the talks keep them in. Nati Srebro
telling you which capacity measure he tried first and why it did not work is
worth more than the theorem. Peter Bartlett saying out loud that uniform
convergence cannot be the answer is a thing he writes much more carefully in
print. This is why the module is built almost entirely out of the Simons
Institute and IAS archives rather than out of survey papers.

**A structural note on sources.** Two institutions have, between them, recorded
essentially the entire modern history of this field: the **Simons Institute for
the Theory of Computing** at Berkeley and the **Institute for Advanced Study** at
Princeton. The Simons programs are listed in §DLT-9 as coherent archives, because
watching one program end to end is a different and better experience than
watching ten talks from ten places. Individual talks are pulled forward into the
topic sections where they belong.

### Conventions

Every entry below is an **individual video**, verified to exist and play, with
its real duration and the year the talk was given or posted. All 291 video links
in this document were checked programmatically against YouTube; nothing here is
a bare playlist, and where a playlist is named it is also enumerated into
individual lectures. Where a talk has a canonical paper, it is paired. Where I
could not confirm something, it is flagged `UNVERIFIED` with the search term that
would find it, rather than guessed at.

Durations are given as H:MM:SS. Years are the year the talk was delivered where
the hosting institution publishes a schedule, and the upload year otherwise; the
two differ by a few months in some Simons entries, where the talk date is used.

Entries marked **[CORE]** are the ones to watch if you only do a third of this.

---

## DLT-1 Generalization theory for deep networks

The founding question: a network with 60 million parameters trained on 50,000
images, which can fit random labels perfectly, nevertheless generalizes. Every
classical bound is vacuous by many orders of magnitude. What is the real
explanation?

### 1.1 The canonical lecture series

This four-part sequence from the Simons Deep Learning Boot Camp is the single
best structured introduction that exists, and it is taught by the two people who
wrote most of the relevant theorems.

**1. Generalization I** **[CORE]**
Peter Bartlett (UC Berkeley) + Sasha Rakhlin (MIT) · 2019 · 1:16:56 · https://www.youtube.com/watch?v=Ntl_WNW8yGc
Sets up the classical uniform-convergence and VC machinery, then shows precisely where it breaks for overparameterized networks. Start here; everything downstream is a reaction to this lecture.
*Paper:* Bartlett, Harvey, Liaw, Mehrabian, "Nearly-tight VC-dimension bounds for piecewise linear neural networks" (arXiv:1703.02930)

**2. Generalization II** **[CORE]**
Peter Bartlett + Sasha Rakhlin · 2019 · 1:23:06 · https://www.youtube.com/watch?v=QO8HOqQ_6BQ
Builds Rademacher complexity and the norm-based route to capacity control — the first serious attempt to replace parameter counting with something that tracks reality.
*Paper:* Bartlett, Foster, Telgarsky, "Spectrally-normalized margin bounds for neural networks" (arXiv:1706.08498)

**3. Generalization III**
Peter Bartlett + Sasha Rakhlin · 2019 · 1:18:23 · https://www.youtube.com/watch?v=8hZD5bMBbY4
Margin-based bounds in full detail. This is the technical core of spectrally-normalized margin theory.
*Paper:* same as above (arXiv:1706.08498)

**4. Generalization IV** **[CORE]**
Peter Bartlett + Sasha Rakhlin · 2019 · 1:22:14 · https://www.youtube.com/watch?v=n5Zxi22801Q
Closes on interpolation and benign overfitting, which is the bridge from this section to §DLT-2.
*Paper:* Bartlett, Montanari, Rakhlin, "Deep learning: a statistical viewpoint" (arXiv:2103.09177)

### 1.2 Implicit regularization and the implicit bias of gradient descent

The most important single idea in this module: the hypothesis class does not
constrain the solution, **the optimizer does**. Gradient descent silently picks a
minimum-norm or maximum-margin solution out of the infinite set of zero-training-
error solutions, and that choice is the whole explanation.

**5. Implicit Regularization I** **[CORE]**
Nati Srebro (TTIC) · 2019 · 1:16:51 · https://www.youtube.com/watch?v=7uRVR9hsF0g
The canonical lecture on why the algorithm, not the loss, picks the solution. If you watch one hour of this module, make it this one.
*Paper:* Neyshabur, Tomioka, Srebro, "In search of the real inductive bias" (arXiv:1412.6614)

**6. Implicit Regularization II**
Nati Srebro (TTIC) · 2019 · 1:22:54 · https://www.youtube.com/watch?v=IkuOmf7ey14
Characterizes the implicit bias concretely for matrix factorization and linear convolutional networks — where it can actually be computed.
*Paper:* Gunasekar, Lee, Soudry, Srebro, "Implicit bias of gradient descent on linear convolutional networks" (arXiv:1806.00468)

**7. Tutorial: Implicit Bias I** **[CORE]**
Nati Srebro (TTIC), Simons Deep Learning Theory Workshop & Summer School · 2022 · 1:20:40 · https://www.youtube.com/watch?v=NeTUt5TJOiY
The rebuilt, three-years-wiser version of #5. If you only do one Srebro tutorial in 2026, do this pair instead of the 2019 pair.
*Paper:* Gunasekar et al., "Characterizing implicit bias in terms of optimization geometry" (arXiv:1802.08246)

**8. Tutorial: Implicit Bias II**
Nati Srebro (TTIC) · 2022 · 1:36:30 · https://www.youtube.com/watch?v=8mO1CFfpbRE
Extends to homogeneous networks, max-margin convergence, and the rich-versus-kernel transition that §DLT-3 depends on.
*Paper:* Lyu & Li, "Gradient descent maximizes the margin of homogeneous neural networks" (arXiv:1906.05890)

**9. Optimization's Untold Gift to Learning: Implicit Regularization**
Nati Srebro (TTIC), Simons · 2017 · 1:01:19 · https://www.youtube.com/watch?v=YwX44phI_gc
The original talk that put "norm, not size, controls capacity" on the map. Historically the most important entry in this subsection.
*Paper:* Neyshabur, Tomioka, Srebro, "Norm-based capacity control in neural networks" (arXiv:1503.00036)

**10. Implications of the implicit bias in neural networks**
Gal Vardi (Weizmann/TTIC), One World Theoretical ML Seminar · 2022 · 0:58:28 · https://www.youtube.com/watch?v=t9ZRPpVKt4c
The consequences nobody wanted: the same implicit bias that gives you generalization also gives you training-data reconstruction attacks and adversarial non-robustness.
*Paper:* Vardi, "On the implicit bias in deep-learning algorithms" (arXiv:2208.12591)

### 1.3 Uniform convergence and its limits

This is a genuine live argument, and the two sides are both on video. Watch them
back to back as one session.

**11. Uniform convergence may be unable to explain generalization in deep learning** (NeurIPS 2019 oral)
Vaishnavh Nagarajan & Zico Kolter (CMU) · 2019 · 0:02:52 · https://www.youtube.com/watch?v=o3GfnEjTdIQ
Three minutes, by the authors. The claim: *no* uniform-convergence bound, however clever, can explain this — the proof technique itself is the problem.
*Paper:* Nagarajan & Kolter (arXiv:1902.04742)

**12. In Defense of Uniform Convergence** **[CORE]**
Daniel M. Roy (Toronto), IAS · 2020 · 1:21:46 · https://www.youtube.com/watch?v=6mdFQR0-WT0
The full-length rebuttal: derandomization recovers meaningful uniform-convergence bounds, and the impossibility result is narrower than it sounds. The best hour on YouTube for learning how theorists actually argue.
*Paper:* Negrea, Dziugaite, Roy, "In defense of uniform convergence" (arXiv:1912.04265)

### 1.4 Margin theory

**13. Margins, perceptrons, and deep networks** **[CORE]**
Matus Telgarsky (UIUC / Courant), IAS Theoretical ML Seminar · 2020 · 1:22:27 · https://www.youtube.com/watch?v=yfk-IPlr6M0
Telgarsky's own account, from the perceptron through to spectrally-normalized margin bounds. The cleanest single narrative of the margin thread.
*Papers:* Bartlett, Foster, Telgarsky (arXiv:1706.08498); Ji & Telgarsky, "Gradient descent aligns the layers of deep linear networks" (arXiv:1810.02032)

**14. A Primal-dual Analysis of Margin Maximization by Steepest Descent Methods**
Matus Telgarsky (NYU), Simons "Frontiers of Deep Learning" · 2019 · 0:41:42 · https://www.youtube.com/watch?v=Rc76ZBP6fHM
The technical follow-through: *why* steepest descent maximizes margin, in duality language.
*Paper:* Ji, Telgarsky, "Directional convergence and alignment in deep learning" (arXiv:2006.06657)

**15. Optimisation and Generalization of deep networks**
Matus Telgarsky (UIUC), SMILES Summer School · 2019 · 1:17:16 · https://www.youtube.com/watch?v=rv-vzl5-oIs
Summer-school pacing, covering optimization and generalization jointly. Good if the IAS talk moves too fast.
*Paper:* Soudry et al., "The implicit bias of gradient descent on separable data" (arXiv:1710.10345)

**16. A Perceptron Trio**
Matus Telgarsky (Courant/NYU), IPAM · 2024 · 0:50:45 · https://www.youtube.com/watch?v=b5bYObH8rKs
The most current Telgarsky entry: margin/perceptron arguments reframed for shallow ReLU feature learning.
*Paper:* Telgarsky, "Feature selection and low test error in shallow low-rotation ReLU networks" (arXiv:2208.02789)

**17. Feature Selection with Gradient Descent on Two-layer Networks in Low-rotation Regimes**
Matus Telgarsky (NYU), Simons Deep Learning Theory Summer School · 2022 · 0:57:45 · https://www.youtube.com/watch?v=bSJZQVNiLP0
The research-talk version of #16, with more proof detail.
*Paper:* arXiv:2208.02789

### 1.5 PAC-Bayes for neural networks

The only framework that has produced **non-vacuous** generalization bounds for
real networks on real data. That is a low bar and it is still the record.

**18. Studying Generalization in Deep Learning via PAC-Bayes** **[CORE]**
Gintare Karolina Dziugaite (Element AI), Simons "Frontiers of Deep Learning" · 2019 · 0:44:39 · https://www.youtube.com/watch?v=_bYT2VOOxU0
The author on the first bounds for real deep networks that were not vacuous. This is the entry point.
*Paper:* Dziugaite & Roy, "Computing nonvacuous generalization bounds for deep (stochastic) neural networks with many more parameters than training data" (arXiv:1703.11008)

**19. Nonvacuous Generalization Bounds for Deep Neural Networks via PAC-Bayes**
Gintare Karolina Dziugaite, Borealis AI · 2018 · 0:26:02 · https://www.youtube.com/watch?v=dHUH0hmKvs8
The earliest recorded version, closest to the paper. Use as a 26-minute primer.
*Paper:* arXiv:1703.11008

**20. PAC-Bayesian approaches to understanding generalization in deep learning**
Gintare Karolina Dziugaite, IAS · 2019 · 0:31:34 · https://www.youtube.com/watch?v=MrUqeSj9Pgk
Condensed overview of the whole PAC-Bayes programme.
*Paper:* arXiv:1703.11008

**21. Distribution-dependent generalization bounds for noisy, iterative learning algorithms**
Gintare Karolina Dziugaite, MTL MLOpt Seminar · 2021 · 1:05:17 · https://www.youtube.com/watch?v=iZC5H9dYVeI
The information-theoretic / SGLD line that succeeds naive PAC-Bayes. This is where the field actually went next.
*Paper:* Negrea, Haghifam, Dziugaite, Khisti, Roy (arXiv:1911.02151)

**22. Size of Teachers as a Measure of Data Complexity: PAC-Bayes Excess Risk Bounds and Scaling Laws**
Dan Roy (Toronto), IPAM · 2024 · 0:56:32 · https://www.youtube.com/watch?v=pJqV2YNlkWc
The newest item here, and the one that connects PAC-Bayes directly to §DLT-5 scaling laws. An underexplored seam.
*Paper:* Roy et al., NeurIPS 2024

### 1.6 Overparameterization, compression, and reality checks

**23. Toward Theoretical Understanding of Deep Learning** (ICML 2018 tutorial) **[CORE]**
Sanjeev Arora (Princeton/IAS) · 2018 · 2:13:56 · https://www.youtube.com/watch?v=rcR6P5O8CpU
The two-hour tutorial that frames generalization, optimization and expressivity as one problem. Best single survey assignment in the module.
*Paper:* Zhang, Bengio, Hardt, Recht, Vinyals, "Understanding deep learning requires rethinking generalization" (arXiv:1611.03530)

**24. Why do deep nets generalize, that is, predict well on unseen data**
Sanjeev Arora (Princeton/IAS), DeepMath · 2018 · 0:56:16 · https://www.youtube.com/watch?v=xscvWCC-y6U
The compression-based route to bounds — a genuinely distinct third approach alongside margins and PAC-Bayes.
*Paper:* Arora, Ge, Neyshabur, Zhang, "Stronger generalization bounds for deep nets via a compression approach" (arXiv:1802.05296)

**25. Is Optimization the Right Language to Understand Deep Learning?**
Sanjeev Arora (Princeton), DeepMath · 2020 · 1:03:01 · https://www.youtube.com/watch?v=HMdJd2minAI
Arora arguing that the trajectory, not the endpoint, is the object of study. A useful corrective to the whole "find the minimum" framing.
*Paper:* Arora, Cohen, Hazan, "On the optimization of deep networks: implicit acceleration by overparameterization" (arXiv:1802.06509)

**26. Opening the black box: Toward mathematical understanding of deep learning**
Sanjeev Arora (Princeton), Harvard CMSA · 2020 · 0:57:58 · https://www.youtube.com/watch?v=DbpJ6wTM5vQ
A broader, better-paced survey than #25 for a first pass.

**27. Toward a Causal Analysis of Generalization in Deep Learning** **[CORE]**
Behnam Neyshabur (Google), IAS · 2019 · 0:33:17 · https://www.youtube.com/watch?v=HAfQ-Q8pn0g
The empirical reality check that should be watched immediately after any theory talk here: most proposed generalization measures fail when tested causally at scale.
*Paper:* Jiang, Neyshabur, Mobahi, Krishnan, Bengio, "Fantastic generalization measures and where to find them" (arXiv:1912.02178)

**28. The mystery of over-parametrization in neural networks**
Behnam Neyshabur, IAS · 2017 · 0:17:33 · https://www.youtube.com/watch?v=4Mga1cERS34
Seventeen minutes stating the puzzle cleanly. Good pre-reading before the Srebro tutorials.
*Paper:* Neyshabur et al., "Towards understanding the role of over-parametrization in generalization" (arXiv:1805.12076)

**29. Learning and Generalization in Over-parametrized Neural Networks, Going Beyond Kernels**
Yuanzhi Li (Stanford), Simons · 2019 · 0:49:42 · https://www.youtube.com/watch?v=NNPCk2gvTnI
The first serious results showing networks provably beat their own tangent kernel. The technical bridge to §DLT-3.
*Paper:* Allen-Zhu, Li, Liang, "Learning and generalization in overparameterized neural networks, going beyond two layers" (arXiv:1811.04918)

**30. Size-free Generalization Bounds for Convolutional Neural Networks**
Hanie Sedghi (Google Brain), Simons · 2019 · 0:34:34 · https://www.youtube.com/watch?v=jRK3W48cO90
Norm-based bounds for convnets that do not grow with parameter count.
*Paper:* Long & Sedghi, "Generalization bounds for deep convolutional neural networks" (arXiv:1905.12600)

**31. Understanding Generalization from Pre-training Loss to Downstream Tasks**
Tengyu Ma (Stanford), Simons Modern Paradigms in Generalization Boot Camp · 2024 · 1:17:51 · https://www.youtube.com/watch?v=rFp0tVQW_q0
The modern reframing: in the foundation-model era the quantity to bound is downstream transfer, not in-distribution test error. This is where the open problems now are.

**32. Training on the Test Set and Other Heresies**
Benjamin Recht (UC Berkeley), Simons · 2019 · 0:49:37 · https://www.youtube.com/watch?v=NTz4rJS9BAI
The adaptive-overfitting reality check — do the benchmarks we measure generalization *on* still mean anything after a decade of reuse?
*Paper:* Recht, Roelofs, Schmidt, Shankar, "Do ImageNet classifiers generalize to ImageNet?" (arXiv:1902.10811)

**33. An Observation on Generalization**
Ilya Sutskever (OpenAI), Simons · 2023 · 0:57:21 · https://www.youtube.com/watch?v=AKMuA_TVz3A
Compression-as-generalization argued from the practitioner side by someone who built the systems. Worth watching precisely because it does not sound like the rest of this section.

---

## DLT-2 Double descent, benign overfitting, interpolation

The empirical discovery that broke the bias-variance picture, and the theory that
grew up to explain it. The short version: past the interpolation threshold, more
capacity makes test error go **down** again, and interpolating noisy data is not
always fatal.

**34. From Classical Statistics to Modern Machine Learning** **[CORE]**
Misha Belkin (UC San Diego), Simons "Frontiers of Deep Learning" · 2019 · 0:49:47 · https://www.youtube.com/watch?v=OBCciGnOJVs
Belkin presenting double descent close to its original publication. The founding talk of this section.
*Paper:* Belkin, Hsu, Ma, Mandal, "Reconciling modern machine learning practice and the bias-variance trade-off" (arXiv:1812.11118)

**35. From Classical Statistics to Modern ML: the Lessons of Deep Learning**
Mikhail Belkin, IAS · 2019 · 0:37:29 · https://www.youtube.com/watch?v=5-Kqb80h9rk
Shorter companion to #34, same period.

**36. Mikhail Belkin: From classical statistics to modern deep learning**
Mikhail Belkin (UCSD), Oxford ML and Physics Seminars · 2022 · 0:58:00 · https://www.youtube.com/watch?v=5-QjjOYfeSI
Three years on, with the interpolation story matured and transparent-kernel results included.
*Paper:* Belkin, "Fit without fear: remarkable mathematical phenomena of deep learning through the prism of interpolation" (arXiv:2105.14368)

**37. The elusive generalization: classical bounds to double descent to grokking** **[CORE]**
Misha Belkin (UCSD), Simons Modern Paradigms in Generalization Boot Camp · 2024 · 1:19:56 · https://www.youtube.com/watch?v=h2I0Hs2K2KI
The best single arc in this module: VC bounds → interpolation → double descent → grokking, as one continuous story by the person who started it. If you watch one Belkin talk, this is it.
*Paper:* arXiv:1812.11118

**38. Benign Overfitting in Linear Prediction** **[CORE]**
Peter Bartlett (UC Berkeley), Simons · 2019 · 0:47:40 · https://www.youtube.com/watch?v=GXpP-rXEDpk
The theorem that made "interpolating noise is sometimes harmless" a provable statement rather than an observation. Requires overparameterized linear regression with a specific eigenvalue decay — knowing *which* condition is the real content.
*Paper:* Bartlett, Long, Lugosi, Tsigler, "Benign overfitting in linear regression" (arXiv:1906.11300)

**39. Benign Overfitting**
Peter Bartlett (UC Berkeley), TOPML Workshop · 2021 · 1:01:04 · https://www.youtube.com/watch?v=o0tzfayJfVg
Longer and more self-contained than #38, two years later.
*Paper:* arXiv:1906.11300

**40. Benign Overfitting** (NeurIPS 2021 invited talk)
Peter Bartlett (UC Berkeley) · 2021 · 1:30:04 · https://www.youtube.com/watch?v=zNGm0iXWxYE
The plenary version — broadest framing, aimed at a general ML audience.
*Paper:* Bartlett, Montanari, Rakhlin, "Deep learning: a statistical viewpoint" (arXiv:2103.09177)

**41. Peter Bartlett: Benign overfitting — Lecture 1**
Peter Bartlett (UC Berkeley), CIRM · 2022 · 1:08:15 · https://www.youtube.com/watch?v=MZFXVGGB11E
Mathematics-institute pacing with the proofs actually done. Use this one if you intend to work in the area rather than just know about it.

**42. Benign, Tempered, or Catastrophic: A Taxonomy of Overfitting** **[CORE]**
Neil Mallinar (UCSD) & Preetum Nakkiran, Simons Deep Learning Theory Summer School · 2022 · 0:57:45 · https://www.youtube.com/watch?v=cg9s7jpWgck
The necessary correction to #38: most real networks are not benign, they are *tempered*, and the three-way taxonomy is more useful than the binary.
*Paper:* Mallinar, Simon, Abedsoltan, Pandit, Belkin, Nakkiran, "Benign, tempered, or catastrophic: a taxonomy of overfitting" (arXiv:2207.06569)

**43. Is Overfitting Actually Benign? On the Consistency of Interpolating Methods**
Simons · 2021 · 0:26:25 · https://www.youtube.com/watch?v=aZL4mIvuYd4
Short, sharp skeptical take. Pairs with #42.

**44. The Devil is in the Tails and Other Stories of Interpolation**
Niladri Chatterji (OpenAI), Simons Deep Learning Theory Summer School · 2022 · 0:54:40 · https://www.youtube.com/watch?v=e7Y3hgQlaaE
Where the benign-overfitting conditions come from and how fragile they are.

**45. Reconsidering Overfitting in the Age of Overparameterized Models**
Fanny Yang (ETH Zurich), Simons Modern Paradigms in Generalization Boot Camp · 2024 · 1:18:05 · https://www.youtube.com/watch?v=g1Gb3UEgpOk
The current state of the question, including the robustness-vs-interpolation tension that is now the live part.

**46. The Deep Bootstrap Framework: A New Lens to Understand Generalization**
Preetum Nakkiran (Harvard), ICTP · 2021 · 0:19:54 · https://www.youtube.com/watch?v=3hDWN7Ka23I
Twenty minutes that reframe generalization as a statement about *optimization speed* online versus offline. One of the genuinely original reframings of the last decade.
*Papers:* "The Deep Bootstrap Framework" (arXiv:2010.08127); "Deep Double Descent" (arXiv:1912.02292)

**47. An Empirical Theory of Deep Learning** (Gradient Podcast)
Preetum Nakkiran · 2022 · 1:37:29 · https://www.youtube.com/watch?v=EBSLLOJJJuc
Long-form interview. The only place Nakkiran lays out the methodological argument — that deep learning needs an empirical science, not just theorems — at length.

**48. The Interpolation Phase Transition in Neural Networks: Memorization and Generalization under Lazy Training**
Simons · 2020 · 1:06:39 · https://www.youtube.com/watch?v=FNG8yTnZuOY
Connects interpolation directly to the lazy/NTK regime of §DLT-3 with precise asymptotics.
*Paper:* Montanari, Zhong (arXiv:2007.12826)

**49. Kernel and Deep Regimes in Overparameterized Learning**
Suriya Gunasekar (Microsoft Research), Simons · 2019 · 0:46:15 · https://www.youtube.com/watch?v=fUQCJNSdskA
Separates the kernel regime from the genuinely rich feature-learning regime — which determines which of the above bounds even apply.
*Paper:* Woodworth et al., "Kernel and rich regimes in overparametrized models" (arXiv:2002.09277)

**50. Kernel and Rich Regimes in Deep Learning**
Nati Srebro (TTIC), IAS · 2019 · 0:37:01 · https://www.youtube.com/watch?v=ZjTMiYhW4XY
Srebro's short version of the same distinction.
*Paper:* arXiv:2002.09277

---

## DLT-3 Neural tangent kernel and infinite-width limits

The one place deep learning becomes exactly solvable. Take width to infinity
under the standard parametrization and the network becomes a linear model in a
fixed kernel — trainable, analyzable, and **unable to learn features**. That last
clause is the whole drama of this section: the tractable limit is the wrong
limit, and finding a different scaling that keeps feature learning (muP) turned
out to have enormous practical consequences.

### 3.1 The NTK and the wide limit

**78. Neural Tangent Kernel: Convergence and Generalization in Neural Networks** (STOC 2021)
Arthur Jacot, Franck Gabriel, Clément Hongler (EPFL) · 2021 · 0:22:25 · https://www.youtube.com/watch?v=Yc5EMw3wDwg
The original authors on the founding paper. Twenty-two minutes, and it is the primary source — watch it first, then go to the longer lectures.
*Paper:* Jacot, Gabriel, Hongler (arXiv:1806.07572)

**79. The Wide limit of Neural Networks: NNGP and NTK** **[CORE]**
Jascha Sohl-Dickstein (Google Brain), Understanding Deep Learning lecture series · 2021 · 1:16:51 · https://www.youtube.com/watch?v=fcpI5z9q91A
The best self-contained lecture on both correspondences — infinite-width networks at initialization are Gaussian processes, and under gradient descent they evolve as linear models. If you learn NTK from one video, learn it from this one.
*Papers:* Lee et al., "Deep neural networks as Gaussian processes" (arXiv:1711.00165); Lee et al., "Wide neural networks of any depth evolve as linear models under gradient descent" (arXiv:1902.06720)

**80. Understanding overparameterized neural networks**
Jascha Sohl-Dickstein (Google Brain), Oxford ML and Physics · 2021 · 1:18:22 · https://www.youtube.com/watch?v=6C1hKqLe2Tc
Same material with more emphasis on *why* width makes networks analytically tractable at all.
*Paper:* arXiv:1902.06720

**81. Towards an Understanding of Wide Neural Networks**
Yasaman Bahri (Google Brain), DeepMath · 2020 · 1:11:37 · https://www.youtube.com/watch?v=tECNnHxJH_M
Frames the wide-network programme as a statistical-mechanics research agenda rather than a single theorem. Good for seeing where the open problems are.

**82. Computation in Very Wide Neural Networks**
Yasaman Bahri (Google Brain), Simons · 2019 · 0:48:40 · https://www.youtube.com/watch?v=EWLQoO0SGvI
The compact research-talk version.

**83. Neural Tangent Kernel** (Stanford CS229M Lecture 13)
Tengyu Ma (Stanford) · 2022 · 1:29:30 · https://www.youtube.com/watch?v=btphvvnad0A
The derivation done properly at blackboard pace, inside a graduate course. Use this if you want to be able to *reproduce* the result rather than cite it.

**84. On the Connection between Neural Networks and Kernels: a Modern Perspective**
Simon Du (University of Washington), IAS · 2019 · 0:30:46 · https://www.youtube.com/watch?v=HvEGJUwQEO8
Thirty minutes on the optimization consequence: NTK is why gradient descent provably converges.

**85. The Catapult phase of Neural Networks**
Guy Gur-Ari (Google), Understanding Deep Learning lecture series · 2021 · 1:07:20 · https://www.youtube.com/watch?v=aPY-M4epEz4
Where the lazy/NTK picture visibly breaks: at large learning rate the loss spikes and the network lands somewhere the kernel theory cannot describe. The cleanest empirical wedge into the rich regime.
*Paper:* Lewkowycz, Bahri, Dyer, Sohl-Dickstein, Gur-Ari (arXiv:2003.02218)

### 3.2 Lazy training versus feature learning, and mean-field limits

**86. Analysis of Gradient Descent on Wide Two-Layer ReLU Neural Networks** **[CORE]**
Lénaïc Chizat (CNRS / Paris-Saclay), One World Theoretical ML · 2020 · 1:07:29 · https://www.youtube.com/watch?v=cE-Q5jPRRik
The definitive treatment of the lazy-versus-rich dichotomy, by the person who named lazy training. This is the hinge of the whole section.
*Papers:* Chizat, Oyallon, Bach, "On lazy training in differentiable programming" (arXiv:1812.07956); Chizat & Bach (arXiv:2002.04486)

**87. Analysis of Gradient Descent on Wide Two-Layer Neural Networks** (IHES)
Lénaïc Chizat · 2021 · 0:38:55 · https://www.youtube.com/watch?v=jV0TGfqfFKw
Tighter 39-minute version of #86. Use as the assigned short form.

**88. On the Global Convergence of Gradient Descent for Over-parameterized Models using Optimal Transport**
Francis Bach (INRIA / ENS), Institut Henri Poincaré · 2019 · 1:00:51 · https://www.youtube.com/watch?v=rQM5uh2EsHA
The optimal-transport formulation that launched the mean-field line in machine learning: training a wide two-layer net is Wasserstein gradient flow on a measure.
*Paper:* Chizat & Bach (arXiv:1805.09545)

**89. Mean Field Descriptions of Two Layers Neural Networks**
Andrea Montanari (Stanford), FODSI · 2019 · 1:05:39 · https://www.youtube.com/watch?v=eMFqg-B0oPE
The distributional-dynamics / PDE view of SGD, from the author of the other founding mean-field paper.
*Paper:* Mei, Montanari, Nguyen (arXiv:1804.06561)

**90. Self-induced regularization from linear regression to neural networks** **[CORE]**
Andrea Montanari (Stanford), Harvard CMSA · 2020 · 1:06:11 · https://www.youtube.com/watch?v=bjRqmlI_SFs
Connects random-feature asymptotics to benign overfitting and answers directly *when kernels do and do not match real networks*. The bridge between §DLT-2 and §DLT-3.
*Papers:* "When do neural networks outperform kernel methods?" (arXiv:2006.13409); "The generalization error of random features regression" (arXiv:1908.05355)

**91. A mean-field theory of lazy training in two-layer neural nets**
Maxim Raginsky (UIUC) · 2020 · 0:49:38 · https://www.youtube.com/watch?v=oWE9jFIEwUw
Casts lazy training as entropic-regularized stochastic control — the sharpest formal statement of what "lazy" actually means.
*Paper:* arXiv:2002.01987

**92. Trainability and accuracy of artificial neural networks**
Eric Vanden-Eijnden (NYU Courant) · 2020 · 1:11:07 · https://www.youtube.com/watch?v=tcrt9y7ypQc
The interacting-particle-system formulation — the Rotskoff–Vanden-Eijnden half of the mean-field literature.
*Paper:* arXiv:1805.00915

**93. Mean-Field Theory of Two-Layers Neural Networks: Dimension Free Bounds and Kernel Limit**
Theodor Misiakiewicz (Stanford), Simons · 2021 · 0:49:55 · https://www.youtube.com/watch?v=BMnxZaFeWNA
The quantitative, dimension-free version of the mean-field approximation.
*Paper:* arXiv:1902.06015

**94. A general framework for the mean field limit of multilayer neural networks**
Huy Tuan Pham (Stanford) · 2020 · 0:56:38 · https://www.youtube.com/watch?v=3gxDiTEE-bM
Extends mean-field theory past two layers — the gap everyone notices immediately.
*Paper:* arXiv:2001.11443

**95. Learning Over-parameterized Neural Networks: From Neural Tangent Kernel to Mean-field Analysis**
Quanquan Gu (UCLA) · 2020 · 0:44:06 · https://www.youtube.com/watch?v=zlqQ7VRba2Y
Explicitly bridges the two regimes in one lecture. Watch this as the synthesis session after the NTK and mean-field blocks.
*Paper:* arXiv:1902.01384

### 3.3 Tensor Programs, muP, and the parametrization that actually matters

The highest practical payoff in this entire module. The argument is that NTK
parametrization provably kills feature learning at infinite width, that a
different scaling (maximal update parametrization) preserves it, and that under
muP the optimal hyperparameters stop moving with width — so you can tune a small
model and transfer to a huge one.

**96. Feature Learning in Infinite-Width Neural Networks** **[CORE]**
Greg Yang (Microsoft Research), ELLIS UCL CSML Seminar · 2021 · 0:47:37 · https://www.youtube.com/watch?v=DuBQCBWcq4M
The core theoretical argument, stated cleanly: NTK parametrization cannot learn features, muP can. Watch before the muTransfer talk.
*Paper:* Yang & Hu, "Tensor Programs IV: Feature learning in infinite-width neural networks" (arXiv:2011.14522)

**97. Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer** **[CORE]**
Greg Yang (Microsoft Research), AutoML Seminars · 2022 · 1:12:52 · https://www.youtube.com/watch?v=XpU3mDKJOak
muTransfer: the clearest case in the field of infinite-width theory producing a practice-changing engineering recipe. Tune on a 40M-parameter proxy, transfer to 6.7B.
*Paper:* Yang, Hu, Babuschkin et al., "Tensor Programs V" (arXiv:2203.03466)

**98. The unreasonable effectiveness of mathematics in large scale deep learning**
Greg Yang (xAI), Sydney Mathematical Research Institute · 2023 · 1:08:48 · https://www.youtube.com/watch?v=_p0S_zZd4NQ
The mature overview of the whole Tensor Programs arc, after it had been deployed at scale.

**99. Large N Limits: Random Matrices & Neural Networks** (Cartesian Cafe)
Greg Yang with Timothy Nguyen · 2023 · 3:01:27 · https://www.youtube.com/watch?v=1aXOXHA7Jcw
Three hours, blackboard-style, going through the actual mathematics with an interlocutor who pushes back. The deepest available treatment, and the only long-form one.

**100. Infinite limits and scaling laws of neural networks** **[CORE]**
Blake Bordelon (Harvard), IPAM · 2024 · 0:59:29 · https://www.youtube.com/watch?v=WcWFFiPRslM
The best single bridge from §DLT-3 to §DLT-5: dynamical mean field theory used to *derive* scaling-law exponents rather than fit them.
*Papers:* Bordelon, Atanasov, Pehlevan, "A dynamical model of neural scaling laws" (arXiv:2402.01092); "Self-consistent dynamical field theory of kernel evolution in wide neural networks" (arXiv:2205.09653)

**101. Infinite Limits and Scaling Laws for Deep Neural Networks**
Blake Bordelon (Harvard), Harvard CMSA · 2024 · 1:05:38 · https://www.youtube.com/watch?v=0998FJhPdj8
Longer version of #100 with the depth-scaling and residual-network material included.
*Paper:* Bordelon, Noci, Li, Hanin, Pehlevan, "Depthwise hyperparameter transfer in residual networks" (arXiv:2309.16620)

**102. Scaling Insights from Infinite-Width Theory for Next Gen Architectures & Learning**
Leena Vankadara (Amazon Research), IPAM · 2024 · 0:51:06 · https://www.youtube.com/watch?v=2QwdaGIOjcw
"Beyond muP" — carries the parametrization analysis into state-space models and newer architectures. The open frontier.
*Paper:* "On feature learning in structured state space models" (arXiv:2406.03529)

### 3.4 Finite-width corrections — the effective-theory programme

**103. The Principles of Deep Learning Theory** **[CORE]**
Dan Roberts (MIT / Salesforce), IAS · 2021 · 1:20:17 · https://www.youtube.com/watch?v=YzR2gZrsdJc
The 1/width perturbative expansion: infinite width is the free theory, and real networks are that plus corrections. A genuinely different intellectual approach, imported wholesale from theoretical physics.
*Paper:* Roberts, Yaida, Hanin, "The Principles of Deep Learning Theory" (arXiv:2106.10165)

**104. The Principles of Deep Learning Theory** (Harvard CMSA version)
Dan Roberts, Harvard CMSA · 2021 · 1:15:33 · https://www.youtube.com/watch?v=wXZKoHEzASg
Same content, mathematics-department audience. Pick whichever framing suits you.

**105. Random Neural Networks at Finite Width and Large Depth**
Boris Hanin (Princeton), Rocky Mountain Mathematical Physics Seminar · 2021 · 0:58:43 · https://www.youtube.com/watch?v=QLz_Lu9pOnQ
The depth-to-width ratio as the real control parameter, showing the infinite-width Gaussian picture is only a perturbative first term.
*Paper:* arXiv:2204.01058

**106. Effective Theory of Transformers at Initialization**
Sho Yaida (Meta FAIR), IAIFI Summer Workshop · 2023 · 0:46:04 · https://www.youtube.com/watch?v=BhpMsDbOI2c
Applies the effective theory specifically to transformers and derives initialization and hyperparameter scaling rules from it.
*Paper:* arXiv:2304.02034

**107. Statistical mechanics of deep learning**
Surya Ganguli (Stanford), IAS · 2019 · 0:29:55 · https://www.youtube.com/watch?v=-QF_jX8L0nw
Thirty minutes placing this whole section in the physics tradition it came from.

**108. Signal Propagation and Dynamical Isometry in Deep Neural Networks**
Understanding Deep Learning lecture series · 2021 · 1:06:50 · https://www.youtube.com/watch?v=IwrpOhfhj9o
Why very deep networks are trainable at all — the random-matrix condition on the input-output Jacobian. *(Speaker is not listed in the video description.)*
*Paper:* Pennington, Schoenholz, Ganguli, "Resurrecting the sigmoid in deep learning through dynamical isometry" (arXiv:1711.04735)

**109. Disentangling Trainability and Generalization in Deep Neural Networks**
Lechao Xiao (Google Brain), Understanding Deep Learning lecture series · 2021 · 0:52:09 · https://www.youtube.com/watch?v=4wiFeJOdro4
Shows the two properties are controlled by *different* spectral quantities — architectures can be trainable and not generalize, or the reverse.
*Paper:* arXiv:1912.13053

---

## DLT-4 Optimization theory for deep learning

Gradient descent on a nonconvex, non-smooth, million-dimensional loss should not
work. This section is about the three reasons it does anyway: the landscape is
not as bad as it looks, the dynamics are not what the textbook describes, and the
step size is doing something the theory never modeled.

### 4.1 Edge of stability — the most important recent result

The textbook says you need a step size below 2/L for stability. Real training
sits *exactly at* 2/η with sharpness pinned there, oscillating, and still
converging. Every classical convergence proof is therefore inapplicable to actual
deep learning. This is the cleanest "the theory is simply wrong" result in the
field.

**51. Jeremy Cohen (CMU AI Seminar) — Gradient Descent on Neural Networks Typically Occurs at the Edge of Stability** **[CORE]**
Jeremy Cohen (Carnegie Mellon) · 2021 · 0:58:18 · https://www.youtube.com/watch?v=6xeh6gfESuc
The founding empirical paper, presented by its author. Sharpness rises until it hits 2/η and then hovers there — "progressive sharpening" followed by stability at the edge.
*Paper:* Cohen, Kaur, Li, Kolter, Talwalkar (arXiv:2103.00065)

**52. Understanding Optimization in Deep Learning with Central Flows** **[CORE]**
Alex Damian (Princeton), One World Theoretical ML · 2026 · 0:55:15 · https://www.youtube.com/watch?v=WopNCEVk5BQ
The current best quantitative theory of edge-of-stability: a deterministic ODE ("central flow") that actually predicts real training curves and the effect of learning-rate schedules. This is the state of the art as of 2026.
*Paper:* Damian, Nichani, Lee et al. (arXiv:2410.24206)
*(Harvard CMSA version of the same talk, 2025, 0:50:55: https://www.youtube.com/watch?v=04E8r76TetQ)*

**53. Gradient Optimization Methods: The Benefits of a Large Step-size**
Peter Bartlett (UC Berkeley / Google DeepMind), University of Waterloo Distinguished Lecture · 2026 · 1:11:23 · https://www.youtube.com/watch?v=o7BdY9Qd6_g
Proves the oscillatory non-monotone phase is a *feature*: large step sizes reach low loss faster and induce a specific implicit bias.
*Paper:* Wu, Braverman, Bartlett et al., "Large stepsize gradient descent for logistic loss" (arXiv:2402.15926)

**54. Learning threshold neurons via the Edge of Stability**
Kwangjun Ahn & Felipe Suarez (MIT), hosted by Sébastien Bubeck · 2023 · 0:32:50 · https://www.youtube.com/watch?v=_TpSDM8jG-Y
A solvable toy model where edge-of-stability instability is the *mechanism* that creates useful features. Instability is not noise to be suppressed.
*Paper:* Ahn, Bubeck, Chewi, Lee, Suarez, Zhang (arXiv:2212.07469)

### 4.2 Loss landscape geometry and mode connectivity

**55. Loss Surfaces, fast ensembling and weight averaging of DNNs**
Timur Garipov · 2018 · 1:06:00 · https://www.youtube.com/watch?v=GU2sQgLrTx8
The original mode-connectivity result by its first author: independently trained minima are connected by simple low-loss curves, which means the landscape is not a set of isolated basins.
*Papers:* "Loss surfaces, mode connectivity, and fast ensembling of DNNs" (arXiv:1802.10026); SWA (arXiv:1803.05407)

**56. Explaining Landscape Connectivity of Low-cost Solutions for Multilayer Nets** **[CORE]**
Rong Ge (Duke), Simons · 2019 · 0:45:11 · https://www.youtube.com/watch?v=0kXDqS2OmeI
The theory behind #55 — dropout stability and noise stability as the conditions that *force* connectivity. Watch these two in order.
*Paper:* Kuditipudi, Wang, Lee, Zhang, Li, Hu, Ge, Arora (arXiv:1906.06247)

**57. Loss Landscape of Neural Networks**
Andrew Gordon Wilson (NYU), EPFL Virtual Symposium · 2022 · 0:40:26 · https://www.youtube.com/watch?v=XHZvLeMkgDM
Mode connectivity and flat-basin averaging recast as a Bayesian statement about generalization.
*Paper:* Wilson & Izmailov, "Bayesian deep learning and a probabilistic perspective of generalization" (arXiv:2002.08791)

**58. Towards the Science of Deep Learning — The Loss Landscape Geometry**
Stanislav Fort (Stanford), GoodAI · 2020 · 0:38:53 · https://www.youtube.com/watch?v=VOPviJBNVpw
The high-dimensional wedge/radial picture, and why deep ensembles explore genuinely different functions while SWA-style averaging does not.
*Paper:* Fort, Hu, Lakshminarayanan, "Deep ensembles: a loss landscape perspective" (arXiv:1912.02757)

**59. Optimization Landscape and Two-Layer Neural Networks**
Rong Ge (Duke), IAS · 2019 · 0:58:27 · https://www.youtube.com/watch?v=dmfyYXl0xUY
Where the landscape *is* provably benign — all local minima global, strict saddles — and exactly how far that extends.

**60. Toward a theory of optimization for deep learning**
Misha Belkin (UCSD), DeepMath · 2020 · 1:04:55 · https://www.youtube.com/watch?v=gM-FLiBNg5A
The PL-condition / transition-to-linearity argument: overparameterization makes the landscape effectively convex-like along the trajectory, which is why optimization is easy at all.
*Paper:* Liu, Zhu, Belkin, "Loss landscapes and optimization in over-parameterized non-linear systems" (arXiv:2003.00307)

### 4.3 Sharpness, flat minima, and implicit bias of SGD

**61. Sharpness-Aware Minimization (SAM): Current Method and Future Directions**
Hossein Mobahi (Google Research), ELLIS UCL CSML Seminar · 2022 · 0:53:56 · https://www.youtube.com/watch?v=QBiLph-r5Hw
From a SAM co-author: why minimizing a neighborhood-maximum rather than the loss itself buys generalization, and what remains unexplained about it.
*Paper:* Foret, Kleiner, Mobahi, Neyshabur (arXiv:2010.01412)

**62. Implicit Bias of SGD for Diagonal Linear Networks: a Provable Benefit of Stochasticity**
Nicolas Flammarion (EPFL) · 2022 · 1:04:30 · https://www.youtube.com/watch?v=FQ7w3ubKDoU
A clean separation theorem: SGD noise provably biases toward sparser solutions than gradient flow. One of the few places stochasticity is shown to help rather than merely be tolerated.
*Paper:* Pesme, Pillaud-Vivien, Flammarion (arXiv:2106.09524)

**63. Implicit Regularization effect of the noise** (Stanford CS229M Lecture 17)
Tengyu Ma (Stanford) · 2022 · 1:32:15 · https://www.youtube.com/watch?v=60GqpISCtCU
The lecture-course treatment of SGD noise as an implicit regularizer, derived rather than asserted.

### 4.4 Why Adam works, and the preconditioned-optimizer wave

The most practically consequential open question in optimization theory right
now. Adam has worked for a decade with no satisfying explanation; Shampoo, SOAP
and Muon have reopened the question.

**64. Understanding Adam Optimizer via Online Learning of Updates: Adam is FTRL in Disguise** **[CORE]**
Kwangjun Ahn (MIT), ICML 2024 · 2024 · 0:14:16 · https://www.youtube.com/watch?v=AU39SNkkIsA
Fourteen minutes containing the sharpest current answer: Adam's update rule is exactly Follow-The-Regularized-Leader applied to the sequence of updates. Short — pair with #65.
*Paper:* Ahn, Zhang, Singh, Sra (arXiv:2402.01567)

**65. Making sense of training large AI models** (MIT EECS thesis defense)
Kwangjun Ahn (MIT) · 2024 · 0:40:33 · https://www.youtube.com/watch?v=5rgrB7TGPdc
A single coherent pass over edge-of-stability, SAM, and Adam-as-FTRL from one of the most active people in this area.

**66. Scalable second order optimization for deep learning** (JAX Meetup)
Rohan Anil (Google Brain) · 2022 · 1:28:15 · https://www.youtube.com/watch?v=YDL8NXlS8hA
The Distributed Shampoo author on making a full-matrix preconditioner run at scale. The direct engineering ancestor of SOAP and Muon.
*Paper:* Anil, Gupta, Koren, Regan, Singer (arXiv:2002.09018)

**67. Depths of First Order Optimization** **[CORE]**
Jeremy Bernstein (MIT CSAIL), Cohere Labs · 2025 · 0:47:31 · https://www.youtube.com/watch?v=4OAiakkmKQs
Reframes Shampoo, muP and Muon as one idea — steepest descent under a well-chosen norm — and introduces modular duality. This is the conceptual core of the entire modern optimizer wave, and the most intellectually satisfying talk in §DLT-4.
*Papers:* "Old optimizer, new norm" (arXiv:2409.20325); "Modular duality in deep learning" (arXiv:2410.21265)

**68. Metrized Deep Learning** (MIT 6.7960, Lecture 23)
Jeremy Bernstein (MIT), MIT OpenCourseWare · course Fall 2024, posted 2026 · 1:07:50 · https://www.youtube.com/watch?v=zBvsoxC6tAo
The same material at lecture pace with derivations. Use this if #67 moves too fast.

**69. Why Muon Is Good but May Not Be Optimal**
Weijie Su (University of Pennsylvania), CRUNCH Group · 2026 · 1:00:45 · https://www.youtube.com/watch?v=GBsPpmh1vo4
Separates curvature-anisotropy preconditioning (Adam) from gradient-anisotropy preconditioning (Muon), and argues orthogonalization is directionally right but not optimal. The most current word on Muon theory.
*Papers:* arXiv:2505.21799, arXiv:2511.00674

**70. The Muon Optimizer and Non-Euclidean gradient descent**
Robert Gower (Flatiron Institute), IMPA · 2026 · 0:59:45 · https://www.youtube.com/watch?v=phM8GzT7ZV4
The convergence-theory view of Muon from the optimization-theory side rather than the deep-learning side.

**71. Memory-Efficient Adaptive Optimization**
Yoram Singer (Princeton/Google), FODSI · 2019 · 0:52:43 · https://www.youtube.com/watch?v=kN5KMiIqpEw
The SM3 work, and useful historical context for why full preconditioners were abandoned and then revived.
*Paper:* Anil, Gupta, Koren, Singer (arXiv:1901.11150)

### 4.5 Convergence theory for overparameterized networks

**72. Recent Developments in Over-parametrized Neural Networks, Part I** **[CORE]**
Jason Lee (USC), Simons Deep Learning Boot Camp · 2019 · 1:14:29 · https://www.youtube.com/watch?v=uC2IGoTE2u4
The tutorial on why gradient descent provably finds global minima in the overparameterized regime. The companion lecture to Srebro's implicit-bias pair.
*Paper:* Du, Lee, Li, Wang, Zhai, "Gradient descent finds global minima of deep neural networks" (arXiv:1811.03804)

**73. Recent Developments in Over-parametrized Neural Networks, Part II**
Jason Lee (USC), Simons · 2019 · 1:13:57 · https://www.youtube.com/watch?v=NGon2JyjO6Y
Continues into the limits of the kernel argument and what lies beyond it.

**74. On the Foundations of Deep Learning: SGD, Overparametrization, and Generalization**
Jason Lee (USC), Simons · 2019 · 0:45:38 · https://www.youtube.com/watch?v=l0im8AJAMco
The research-talk condensation of #72–73.

**75. Analyzing Optimization and Generalization in Deep Learning via Trajectories of Gradient Descent**
Nadav Cohen (IAS / Tel Aviv), Simons · 2019 · 0:46:27 · https://www.youtube.com/watch?v=Lmj2bU9MdwM
The trajectory-based alternative to landscape analysis — and the implicit acceleration result for deep linear networks.
*Paper:* Arora, Cohen, Hazan (arXiv:1802.06509)

**76. How Over-Parameterization Slows Down Gradient Descent**
Simon Du (University of Washington) · 2024 · 0:48:34 · https://www.youtube.com/watch?v=W8mVZzWI5gM
The counterweight: overparameterization is not free, and the rate degradation is quantifiable.

**77. The Large Learning Rate Phase of Deep Learning**
Yasaman Bahri (Google Brain) · 2020 · 0:36:06 · https://www.youtube.com/watch?v=gBFmS8qyuFQ
Identifies a sharp phase boundary in learning-rate space with qualitatively different training behavior on each side. The link between §DLT-4 and §DLT-3.
*Paper:* Lewkowycz, Bahri, Dyer, Sohl-Dickstein, Gur-Ari, "The large learning rate phase of deep learning: the catapult mechanism" (arXiv:2003.02218)

---

## DLT-5 Scaling laws

Loss falls as a power law in parameters, data, and compute, over many orders of
magnitude, with exponents that are stable across architectures. Nobody fully
knows why. This is simultaneously the most economically consequential empirical
regularity in the field and one of its least explained.

Watch this section in the order given: the empirical result, then the compute-
optimal correction, then the theory, then the emergence argument — because the
emergence debate only makes sense once you know what a scaling law actually
claims.

### 5.1 The empirical result and compute-optimal training

**110. Neural Scaling Laws and GPT-3** **[CORE]**
Jared Kaplan (Johns Hopkins / Anthropic), Initiative for the Theoretical Sciences · 2020 · 1:15:20 · https://www.youtube.com/watch?v=sNfkZFVm_xs
The original scaling-laws paper by its lead author, with the physicist's framing of why power laws should be expected at all. Start here.
*Paper:* Kaplan, McCandlish et al., "Scaling laws for neural language models" (arXiv:2001.08361)

**111. Neural Scaling Laws and GPT-3** (Physics Meets ML)
Jared Kaplan (Johns Hopkins) · 2020 · 1:35:49 · https://www.youtube.com/watch?v=QMqPAM_knrE
The longest version, with extended Q&A covering the data-manifold-dimension derivation — an attempt at an actual mechanism for the exponent.
*Paper:* Sharma & Kaplan, "A neural scaling law from the dimension of the data manifold" (arXiv:2004.10802)

**112. Scaling Language Models** (Stanford CS224N guest lecture)
Jared Kaplan (Anthropic) · 2022 · 1:14:49 · https://www.youtube.com/watch?v=UFem7xa3Q2Q
The best-paced classroom version, post-Chinchilla. If you only assign one Kaplan lecture, assign this one.

**113. Scaling laws** (Stanford CS336, Lecture 9) **[CORE]**
Stanford CS336 "Language Modeling from Scratch" · 2025 · 1:05:18 · https://www.youtube.com/watch?v=6Q-ESEmDf4Q
The most rigorous available treatment of Chinchilla — all three of its estimation approaches, and the places where the fits disagree with each other. This is the Chinchilla lecture, since no DeepMind author talk exists on video.
*Paper:* Hoffmann, Borgeaud, Mensch et al., "Training compute-optimal large language models" (arXiv:2203.15556)

**114. How to train an LLM**
Samuel L. Smith (Google DeepMind), IPAM · 2024 · 0:53:16 · https://www.youtube.com/watch?v=GfAT2zkB6-U
A Chinchilla co-author on how compute-optimal reasoning is actually used inside a frontier lab, as opposed to how it reads in the paper.
*Paper:* arXiv:2203.15556

**115. (Mis)Fitting: A Survey of Scaling Laws** **[CORE]**
Sneha Kudugunta (Google DeepMind), Cohere For AI · 2026 · 0:54:55 · https://www.youtube.com/watch?v=ggz4iaQpzcY
A methodological audit showing how much published scaling-law practice is underspecified or irreproducible. The necessary skeptical companion to everything above, and the most current item in this section.
*Paper:* "(Mis)Fitting: A survey of scaling laws" (ICLR 2025)

**116. Scaling Data-Constrained Language Models**
Niklas Muennighoff (Stanford / Contextual AI), Cohere For AI · 2024 · 1:00:01 · https://www.youtube.com/watch?v=lLV-g-rGPhk
Extends Chinchilla into the repeated-data regime — the constraint that actually binds now that high-quality web text is exhausted.
*Paper:* arXiv:2305.16264

**117. Scaling LLM Test-Time Compute**
Charlie Snell (UC Berkeley / Google DeepMind) · 2024 · 0:53:31 · https://www.youtube.com/watch?v=OXwGp9YeuBg
The inference-compute scaling law, and its tradeoff against pretraining compute. The newest axis in the field and the one underlying reasoning models.
*Paper:* Snell, Lee, Xu, Kumar (arXiv:2408.03314)

### 5.2 Deriving the exponents

**118. Explaining Neural Scaling Laws** **[CORE]**
Jaehoon Lee (Google Brain), Understanding Deep Learning lecture series · 2021 · 0:56:12 · https://www.youtube.com/watch?v=A8F4Qga3NaM
The variance-limited versus resolution-limited taxonomy — the foundational theory talk for this section, and the first serious derivation rather than fit.
*Paper:* Bahri, Dyer, Kaplan, Lee, Sharma, "Explaining neural scaling laws" (arXiv:2102.06701)

**119. Understanding the Origins and Taxonomy of Neural Scaling Laws** **[CORE]**
Yasaman Bahri (Google Brain / Stanford), Simons Institute · 2023 · 1:05:24 · https://www.youtube.com/watch?v=MUvFuZpxLU8
The updated and most complete presentation of the four-regime taxonomy, by the paper's first author.
*Paper:* arXiv:2102.06701

**120. Dynamics and scaling laws in deep learning**
Yasaman Bahri (Google Brain), Yale Institute for Network Science · 2021 · 1:07:08 · https://www.youtube.com/watch?v=WbHfM774bKc
Pairs the scaling-law derivation directly with the wide-network dynamics of §DLT-3.

**121. Toward a Theory of Neural Scaling Laws** **[CORE]**
Cengiz Pehlevan (Harvard / Kempner Institute), KUIS AI · 2026 · 0:58:59 · https://www.youtube.com/watch?v=8kax6scOskM
The most current first-principles derivation of scaling exponents from solvable random-feature and kernel models. This is the state of the art as of 2026.
*Papers:* Atanasov, Zavatone-Veth, Pehlevan, "Scaling and renormalization in high-dimensional regression" (arXiv:2405.00592); Bordelon, Atanasov, Pehlevan (arXiv:2402.01092)

**122. Scaling Neural Networks: Laws and Limits**
Cengiz Pehlevan (Harvard / Kempner), Principles of Intelligence · 2026 · 0:53:03 · https://www.youtube.com/watch?v=PC-eaqv5EnI
Companion to #121, extending the solvable-model programme to the emergence of in-context learning.

**123. The Quantization Model of Neural Scaling** **[CORE]**
Eric Michaud (MIT), SLT Summit · 2023 · 0:45:19 · https://www.youtube.com/watch?v=qSw75ix83r4
The discrete "quanta" account: smooth aggregate power laws and sharp per-task jumps come out of the *same* mechanism. This single talk unifies §5.1 and §5.3, and it is the most intellectually satisfying item in §DLT-5.
*Paper:* Michaud, Liu, Girit, Tegmark (arXiv:2303.13506)

**124. The Mathematics of Scaling Laws and Model Collapse in AI**
Elvis Dohmatob (Meta FAIR), IPAM · 2024 · 1:03:19 · https://www.youtube.com/watch?v=qZVJuFv-wyw
Derives how scaling laws deform when training on synthetic data. A genuinely new theoretical regime, and increasingly the practical one.
*Paper:* Dohmatob, Feng, Yang, Charton, Kempe, "A tale of tails: model collapse as a change of scaling laws" (arXiv:2402.07043)

**125. When is Scale Enough?**
Ethan Dyer (Google Research, Blueshift), Simons Deep Learning Theory Summer School · 2022 · 1:12:25 · https://www.youtube.com/watch?v=Jpu3kQv39L4
The question posed directly, from inside the group that produced the scaling-law theory papers.

### 5.3 Emergence — and whether it is real

A clean, well-documented scientific dispute with both sides on video. Watch #126
then #128 back to back; it is the best available case study in how an empirical
claim in ML gets contested.

**126. Emergence in Large Language Models** **[CORE]**
Jason Wei (Google Brain / OpenAI), Generative AI at MIT · 2023 · 0:57:32 · https://www.youtube.com/watch?v=0SuyDLjNR9g
The canonical statement of the emergent-abilities claim by its first author: some capabilities appear abruptly at scale and are unpredictable from smaller models.
*Paper:* Wei, Tay, Bommasani et al., "Emergent abilities of large language models" (arXiv:2206.07682)

**127. Scaling unlocks emergent abilities in language models**
Jason Wei (Google Brain), USC ISI · 2023 · 1:00:11 · https://www.youtube.com/watch?v=Z_Qt737HG-0
Alternative version with more chain-of-thought and instruction-tuning material.

**128. Investigating emergent abilities and challenging dominant research ideas** **[CORE]**
Rylan Schaeffer (Stanford), Imbue · 2024 · 1:03:16 · https://www.youtube.com/watch?v=blX2RzZYeJo
The rebuttal by its first author: emergence is largely an artifact of choosing discontinuous metrics, and switching to continuous ones makes the jumps disappear. Teach immediately after Wei.
*Paper:* Schaeffer, Miranda, Koyejo, "Are emergent abilities of large language models a mirage?" (arXiv:2304.15004)

**129. Are Emergent Behaviors in LLMs an Illusion?** (TWIML podcast)
Sanmi Koyejo (Stanford) · 2024 · 1:05:25 · https://www.youtube.com/watch?v=3BQ9_b8JAMU
The senior author's framing of the metric critique and what it implies for capability forecasting and AI safety. Podcast format, but substantive.
*Paper:* arXiv:2304.15004

---

## DLT-6 Science-of-deep-learning phenomena

This section is different in kind from the rest. These are not theorems but
**reproducible empirical phenomena** that any correct theory will have to
explain, and several of them were found by people who were simply looking
carefully. That is a useful thing to notice if you intend to contribute: the
highest-impact results here came from measurement, not proof.

### 6.1 Grokking and phase transitions in training

**130. Progress Measures for Grokking via Mechanistic Interpretability** **[CORE]**
Neel Nanda (DeepMind) · 2023 · 0:43:10 · https://www.youtube.com/watch?v=IHikLL8ULa4
The author reverse-engineering the actual Fourier-multiplication algorithm a grokked network learns, and showing that the apparently sudden generalization is gradual underneath once you measure the right thing.
*Paper:* Nanda, Chan, Lieberum, Smith, Steinhardt (arXiv:2301.05217)

**131. A solvable model of the grokking transition in neural networks** (Part 1)
Andrey Gromov (UMD), Leinweber Institute for Theoretical Physics · 2023 · 1:11:10 · https://www.youtube.com/watch?v=-EJn3xnmJXY
A physicist's analytically solvable two-layer model where the transition can be *computed* rather than observed.
*Paper:* Gromov, "Grokking modular arithmetic" (arXiv:2301.02679)

**132. A solvable model of the grokking transition** (Part 2)
Andrey Gromov · 2023 · 1:06:35 · https://www.youtube.com/watch?v=fCE55iC-HaY
Continues the derivation.

**133. Emergence and grokking in "simple" architectures**
Misha Belkin (UCSD), Simons "Transformers as a Computational Model" · 2024 · 0:52:40 · https://www.youtube.com/watch?v=dzpA30qZxYw
Grokking in architectures simple enough to analyze, which strongly suggests it is not a transformer-specific phenomenon.

**134. You Know It Or You Don't: Compositionality and Phase Transitions in LMs** **[CORE]**
Naomi Saphra (Kempner Institute, Harvard), Simons · 2025 · 0:57:00 · https://www.youtube.com/watch?v=WJ89r5x5hDA
Training is not smooth. Abilities arrive in discrete breakthroughs, and this talk gives methods for detecting them rather than just noticing them afterward.
*Paper:* Chen, Saphra et al., "Sudden drops in the loss: syntax acquisition, phase transitions, and simplicity bias in MLMs" (arXiv:2309.07311)

**135. Interpreting Training** (MIT EI Seminar)
Naomi Saphra · 2024 · 1:04:20 · https://www.youtube.com/watch?v=J0tHAZlFGSc
The broader argument that the training *trajectory*, not the final checkpoint, is the right object of interpretability study.

**136. The Structure and Development of Neural Networks**
Jesse Hoogland (Timaeus), TAIS 2024 · 2024 · 0:32:40 · https://www.youtube.com/watch?v=lbHDbV53-sk
The developmental-interpretability programme: singular learning theory used to detect discrete developmental stages during transformer training. A genuinely different mathematical toolkit.
*Paper:* Hoogland, Wang, Farrugia-Roberts et al., "The developmental landscape of in-context learning" (arXiv:2402.02364)

**137. Dynamics of Concept Learning and Emergent Abilities in Neural Networks**
Ekdeep Singh Lubana (Harvard), TTIC · 2025 · 1:03:31 · https://www.youtube.com/watch?v=nYGyeJRHqEA
Formal models of how data scaling produces sudden emergence, with in-context learning treated as competition between algorithms the model could run.
*Paper:* "Competition dynamics shape algorithmic phases of in-context learning" (arXiv:2412.01003)

### 6.2 Induction heads and in-context learning theory

**138. Transformer Circuits, Induction Heads, In-Context Learning** (Stanford CS25) **[CORE]**
Chris Olah (Anthropic) · 2022 · 0:59:34 · https://www.youtube.com/watch?v=pC4zRb_5noQ
The primary-source lecture on induction heads and the sharp, visible bump in the loss curve their formation creates. One of the few places where a specific circuit has been tied to a specific capability.
*Paper:* Olsson, Elhage, Nanda, Olah et al., "In-context learning and induction heads" (arXiv:2209.11895)

**139. A Walkthrough of In-Context Learning and Induction Heads** (Part 1 of 2)
Neel Nanda, with Charles Frye · 2022 · 1:03:51 · https://www.youtube.com/watch?v=dCkQQYwPxdM
A line-by-line technical walkthrough of the same paper by a co-author. The ideal companion to #138 if you want to actually understand the evidence rather than the conclusion.

**140. What Learning Algorithm is In-Context Learning?** **[CORE]**
Jacob Andreas (MIT), Harvard CMSA · 2023 · 0:50:16 · https://www.youtube.com/watch?v=UNVl64G3BzA
Evidence that in-context learning on linear tasks implements something close to gradient descent or ridge regression *inside the forward pass*. If true, the forward pass is running a learning algorithm.
*Paper:* Akyürek, Schuurmans, Andreas, Ma, Zhou (arXiv:2211.15661)

**141. In-Context Learning: A Case Study of Simple Function Classes**
Gregory Valiant (Stanford), Simons · 2023 · 1:03:40 · https://www.youtube.com/watch?v=DiJsg93zQDc
The controlled-function-class methodology that turned in-context learning from anecdote into measurement.
*Paper:* Garg, Tsipras, Liang, Valiant (arXiv:2208.01066)

**142. Toward Understanding In-context Learning**
Tengyu Ma (Stanford), Simons LLM Boot Camp · 2024 · 1:29:35 · https://www.youtube.com/watch?v=hxrR39mAlR4
The ninety-minute tutorial version, with the theory laid out systematically.

**143. Learning Theory of Transformers: Generalization and Optimization of In-Context Learning**
Taiji Suzuki (University of Tokyo), Simons · 2024 · 0:45:35 · https://www.youtube.com/watch?v=WyeomuU2vQw
Actual generalization bounds for in-context learning — the formal end of this thread.

**144. Associative memories as a building block in Transformers**
Alberto Bietti (Flatiron Institute), Simons · 2024 · 0:38:37 · https://www.youtube.com/watch?v=ncAhx70jTIc
A mechanistic account of what transformer weights are *storing*, which underwrites the induction-head picture.
*Paper:* Bietti, Cabannes, Bouchacourt, Jegou, Bottou, "Birth of a transformer: a memory viewpoint" (arXiv:2306.00802)

### 6.3 Memorization versus generalization

**145. Chasing the Long Tail: What Neural Networks Memorize and Why** **[CORE]**
Vitaly Feldman (Apple ML Research), Simons · 2022 · 0:51:40 · https://www.youtube.com/watch?v=w_BUN5tPiuA
Proves that memorizing outliers is *necessary* for near-optimal generalization on long-tailed data. Memorization is not a failure mode; it is part of the mechanism. This result should change how you read every privacy and copyright argument in ML.
*Papers:* "Does learning require memorization? A short tale about a long tail" (arXiv:1906.05271); Feldman & Zhang, "What neural networks memorize and why" (arXiv:2008.03703)

**146. Does Learning Require Memorization? A Short Tale about a Long Tail**
Vitaly Feldman (Google Research), FODSI · 2019 · 0:49:53 · https://www.youtube.com/watch?v=YWy2Iwn-1S8
The earlier version, closer to the original theorem.

**147. On Memorization of Large Language Models in Logical Reasoning**
Chiyuan Zhang (Google Research), Simons · 2024 · 0:48:05 · https://www.youtube.com/watch?v=eULIf02frIw
From the author of "Understanding deep learning requires rethinking generalization," now asking the same question about reasoning benchmarks. Directly relevant to whether any reasoning evaluation means what it claims.

**148. Understanding the abilities of AI systems: Memorization, generalization, and points in between**
Tom McCoy (Yale), Simons · 2024 · 0:44:25 · https://www.youtube.com/watch?v=3c9TiKryTtA
The "embers of autoregression" argument: apparent reasoning ability is strongly modulated by training-distribution probability.

**149. Threat Models for Memorization: Privacy, Copyright, and Everything In-Between**
Michael Aerni (ETH Zürich), Google TechTalks · recorded 2025, posted 2026 · 0:49:30 · https://www.youtube.com/watch?v=MdZjXUHJIq4
The measurement side: how much verbatim training text appears in ordinary, non-adversarial model output. The numbers are higher than most people assume.
*Paper:* Aerni, Rando, Carlini, Tramèr (arXiv:2411.10242)

**150. Generalization in the representations and computations of frontier language models**
Joshua Batson (Anthropic), Simons · 2024 · 0:52:05 · https://www.youtube.com/watch?v=2xb3mhIqjLw
What generalization looks like when you can open the model up and look — the interpretability perspective on this section's question.

**151. Weak-to-Strong Generalization**
Pavel Izmailov (Anthropic), Simons · 2024 · 0:43:25 · https://www.youtube.com/watch?v=VViyQRGxSKo
A strong model supervised by a weak one outperforms its supervisor. Nobody has a satisfying theory for this, and it is load-bearing for alignment plans.
*Paper:* Burns, Izmailov, Kirchner et al. (arXiv:2312.09390)

### 6.4 Lottery tickets, neural collapse, loss of plasticity

**152. The Lottery Ticket Hypothesis: On Sparse, Trainable Neural Networks** **[CORE]**
Jonathan Frankle (MIT), ELLIS UCL CSML Seminar · 2020 · 0:54:19 · https://www.youtube.com/watch?v=dYKiDwUEbCM
The author's own full account of winning tickets, rewinding, and what sparsity reveals about what training actually requires. The best single version.
*Paper:* Frankle & Carbin (arXiv:1803.03635)

**153. The Lottery Ticket Hypothesis** (MIT EI Seminar)
Michael Carbin (MIT) · 2020 · 1:05:47 · https://www.youtube.com/watch?v=0cU8r6dgD_A
The co-author's version, with more on the stability-and-rewinding follow-up work.

**154. Neural Collapse** (MIT 9.520, Class 25) **[CORE]**
Vardan Papyan, X. Y. Han, David Donoho · 2020 · 1:44:55 · https://www.youtube.com/watch?v=D5eP0CWta8k
All three original authors presenting the simplex-equiangular-tight-frame collapse of last-layer features in the terminal phase of training. The definitive source, and a strikingly clean empirical regularity.
*Paper:* Papyan, Han, Donoho, PNAS 2020 (arXiv:2008.08186)

**155. Principles of Deep Representation Learning via Neural Collapse**
Qing Qu (Michigan) · 2022 · 1:09:28 · https://www.youtube.com/watch?v=IxzRVhQr3kI
The landscape-analysis follow-up that explains *why* collapse occurs, via the unconstrained-features model.

**156. Maintaining Plasticity in Deep Continual Learning** **[CORE]**
Richard Sutton (Alberta / DeepMind), CoLLAs · 2022 · 1:11:20 · https://www.youtube.com/watch?v=p_zknyfV9fY
Backpropagation demonstrably loses the ability to learn over long training runs — networks go dead. This is one of the most under-appreciated results in the field and directly limits continual and online learning.
*Paper:* Dohare, Hernandez-Garcia, Rahman, Mahmood, Sutton, "Loss of plasticity in deep continual learning" (arXiv:2306.13812; Nature 2024)

**157. Maintaining Plasticity in Deep Continual Learning** (Amii seminar)
Shibhansh Dohare (Alberta) · 2023 · 0:54:25 · https://www.youtube.com/watch?v=oA_XLqh4Das
The first author's version, with more experimental detail and the continual-backprop algorithm.

**158. Why do neural networks lose plasticity?**
Clare Lyle (DeepMind), CoLLAs · 2023 · 1:01:29 · https://www.youtube.com/watch?v=1EwKYesnKAA
The mechanistic diagnosis — curvature collapse, dead units, and which interventions actually restore plasticity.
*Paper:* Lyle, Zheng, Nikishin et al., "Understanding plasticity in neural networks" (arXiv:2303.01486)

---

## DLT-7 Expressivity and architecture theory

What a given architecture *can* represent, independent of whether training finds
it. This is the oldest and most mathematically settled part of the module, and
also the one that has recently become urgent again: the question "can a
transformer do this at all?" turns out to have crisp answers in circuit
complexity, and those answers explain real failures.

**A channel worth knowing about.** Most of the transformer-expressivity entries
below come from the **Formal Languages and Neural Networks Seminar**
(https://www.youtube.com/channel/UCrp8k-nSuMKHM4sSUvlPdAw), which holds roughly
120 hour-long talks, nearly all given by the first author of the paper. It is the
single best-concentrated archive for this subfield and is largely unknown outside
it.

### 7.1 Universal approximation and approximation rates

**159. Deep Neural Networks: From Approximation to Expressivity** **[CORE]**
Gitta Kutyniok (LMU Munich), Isaac Newton Institute · 2025 · 0:58:10 · https://www.youtube.com/watch?v=Co5jT2FME6g
The cleanest modern survey: classical universal approximation, then optimal approximation rates with sparse connectivity, then where expressivity stops being the binding constraint.
*Papers:* Bölcskei, Grohs, Kutyniok, Petersen (arXiv:1705.01714); "The modern mathematics of deep learning" (arXiv:2105.04026)

**160. Approximation with neural networks of minimal size**
Dmitry Yarotsky (Skoltech), HSE Computer Science Colloquium · 2022 · 1:17:46 · https://www.youtube.com/watch?v=xkYd411hdCs
The definitive long-form treatment of how many weights a ReLU network actually needs, including the strange super-expressive regimes.
*Paper:* Yarotsky, "Error bounds for approximations with deep ReLU networks" (arXiv:1610.01145)

**161. Optimal approximation of continuous functions by very deep ReLU networks** (COLT 2018)
Dmitry Yarotsky · 2018 · 0:10:33 · https://www.youtube.com/watch?v=Rsw1lQdCs1o
Ten minutes stating the depth-versus-width rate tradeoff precisely. Watch before #160.
*Paper:* arXiv:1802.03620

**162. Expressive Power of Narrow Networks**
Sejun Park (KAIST), DeepMath · 2020 · 0:17:03 · https://www.youtube.com/watch?v=NHCfKFz3IeU
Closes the *width* side of universality: the exact minimum width for universal approximation.
*Paper:* Park, Yun, Lee, Shin, "Minimum width for universal approximation" (arXiv:2006.08859)

**163. Approximation Power** **[CORE]**
Matus Telgarsky (NYU), Simons Deep Learning Boot Camp · 2019 · 1:13:54 · https://www.youtube.com/watch?v=KU6IaE37B9o
The boot-camp tutorial tying approximation theory to everything else in this module. The best single lecture if you want one.

**164. Approximation power of deep networks**
Matus Telgarsky, SMILES Summer School · 2019 · 1:22:56 · https://www.youtube.com/watch?v=6Ss9kFTUS-Y
Longer, slower version of #163.

### 7.2 Depth separation

**165. Benefits of depth in neural networks** (COLT 2016) **[CORE]**
Matus Telgarsky · 2016 · 0:09:06 · https://www.youtube.com/watch?v=ssaXJqG9Dz4
Nine minutes, by the author, on the sawtooth construction — the canonical proof that depth buys exponential expressive power. One of the highest insight-per-minute items in the whole module.
*Paper:* Telgarsky, "Benefits of depth in neural networks" (arXiv:1602.04485)

**166. The Power of Depth for Feedforward Neural Networks** (COLT 2016)
Ronen Eldan & Ohad Shamir · 2016 · 0:12:37 · https://www.youtube.com/watch?v=Ue_hR6x0B-U
The radial-function three-versus-two-layer separation — the complementary half of the depth story.
*Paper:* arXiv:1512.03965

**167. On the benefits of deep and narrow neural networks**
Gilad Yehudai (Weizmann), HUJI Machine Learning Club · 2022 · 1:01:17 · https://www.youtube.com/watch?v=NzmDUI3gNFo
Modern synthesis on when width can and cannot substitute for depth.
*Paper:* Vardi, Yehudai, Shamir, "Width is less important than depth in ReLU neural networks" (arXiv:2202.03841)

**168. Is Deeper Better Only When Shallow Is Good?**
Shai Shalev-Shwartz (Hebrew University of Jerusalem), Simons "Emerging Challenges in Deep Learning" · 2019 · 0:44:48 · https://www.youtube.com/watch?v=I8KOeXuCLm4
The uncomfortable caveat: many depth-separation constructions only separate on functions a shallow network was never going to learn anyway.

**169. On Expressiveness and Optimization in Deep Learning**
Nadav Cohen (IAS), IAS · 2018 · 1:03:26 · https://www.youtube.com/watch?v=F079b2dwcAg
The tensor-decomposition view of expressivity for convolutional architectures, and why expressivity and optimization interact.

### 7.3 What transformers can and cannot compute

This is the most active area in this section, and the results are sharp enough to
be predictive. The headline: a fixed-depth transformer lives in **TC⁰**, a very
small complexity class, and therefore provably cannot do certain serial
computations — which is exactly what chain-of-thought buys back.

**170. Transformers are Uniform Constant Depth Threshold Circuits** **[CORE]**
William Merrill (NYU), FLaNN Seminar · 2022 · 0:34:32 · https://www.youtube.com/watch?v=WU9RSiTw4R8
The foundational TC⁰ upper bound. Start the transformer unit here.
*Paper:* Merrill, Sabharwal, Smith, "Saturated transformers are constant-depth threshold circuits" (arXiv:2106.16213)

**171. The Parallelism Tradeoff: Understanding Transformer Expressivity Through Circuit Complexity** **[CORE]**
Will Merrill (NYU), Simons · 2024 · 0:45:13 · https://www.youtube.com/watch?v=7GVesfXD6_Q
The polished Simons version of the whole log-precision circuit-complexity programme. The argument that parallelizability — the thing that made transformers trainable — is exactly what limits them.
*Paper:* Merrill & Sabharwal (arXiv:2207.00729)

**172. Transformers, parallel computation, and logarithmic depth**
Daniel Hsu (Columbia), Simons · 2024 · 0:57:21 · https://www.youtube.com/watch?v=spxJnEhs1qI
The positive direction: logarithmic depth suffices to simulate substantial parallel computation.
*Paper:* Sanford, Hsu, Telgarsky (arXiv:2402.09268)

**173. Transformer Expressivity and Formal Logic**
David Chiang (Notre Dame), Simons · 2024 · 0:45:34 · https://www.youtube.com/watch?v=hR3G5jsuOHs
The logic side: first-order logic with counting as an *exact* characterization, not just an upper bound.
*Paper:* Chiang, Cholak, Pillay (arXiv:2301.10743)

**174. Thinking Like Transformers** **[CORE]**
Gail Weiss (Technion), FLaNN Seminar · 2022 · 1:07:11 · https://www.youtube.com/watch?v=t5LjgczaS80
RASP, by its author, at full length: a small programming language whose programs compile to transformers. The constructive counterpart to all the impossibility results, and the thing to read before trying to prove a transformer can't do something.
*Paper:* Weiss, Goldberg, Yahav (arXiv:2106.06981)

**175. Masked Hard-Attention Transformers and B-RASP Recognize Exactly the Star-Free Languages**
Andy Yang (Notre Dame), FLaNN Seminar · 2024 · 0:35:08 · https://www.youtube.com/watch?v=gKzyfqrZvkI
A clean three-way exact equivalence between an architecture, a programming language, and a language class.
*Paper:* arXiv:2310.13897

**176. The Expressive Power of Transformers with Chain of Thought** **[CORE]**
Will Merrill (NYU), FLaNN Seminar · 2024 · 0:39:40 · https://www.youtube.com/watch?v=30MhUdapqc8
Exactly how many chain-of-thought steps buy how much additional computational power. This is the theoretical explanation for why reasoning models work.
*Paper:* Merrill & Sabharwal (arXiv:2310.07923)

**177. Chain of Thought Empowers Transformers to Solve Inherently Serial Problems**
Zhiyuan Li (TTIC), FLaNN Seminar · 2024 · 0:55:19 · https://www.youtube.com/watch?v=_tmzV4ZRwVs
The complementary result: constant depth plus chain of thought escapes TC⁰ into P/poly.
*Paper:* Li, Liu, Zhou, Ma (arXiv:2402.12875)

**178. Iterated Models: Expressive Power, Learning, and Chain of Thought**
Nati Srebro (TTIC), Simons · 2024 · 0:54:08 · https://www.youtube.com/watch?v=NRyIPyO_IWY
Learning-theoretic framing of iteration and chain of thought, rather than the complexity-theoretic one.

**179. Representational Strengths and Limitations of Transformers**
Clayton Sanford (Columbia), FLaNN Seminar · 2023 · 0:51:27 · https://www.youtube.com/watch?v=7hYIN7Q-YRQ
Communication-complexity lower bounds — a different and quite powerful proof technique from circuits.
*Paper:* Sanford, Hsu, Telgarsky (arXiv:2306.02896)

**180. Transformers Learn Shortcuts to Automata** **[CORE]**
Bingbin Liu (CMU), FLaNN Seminar · 2023 · 0:48:49 · https://www.youtube.com/watch?v=ni9jCjhRUyY
Shallow transformers simulate long automaton runs via Krohn–Rhodes shortcuts. The key bridge from "what is representable" to "what training actually finds."
*Paper:* Liu, Ash, Goel, Krishnamurthy, Zhang (arXiv:2210.10749)

**181. What Algorithms can Transformers Learn? A Study in Length Generalization**
Hattie Zhou (Mila), FLaNN Seminar · 2024 · 0:53:49 · https://www.youtube.com/watch?v=koo5Bo0k9Wc
The RASP-L conjecture: length generalization happens roughly when a short RASP program for the task exists. A rare *predictive* theory of a training outcome.
*Paper:* arXiv:2310.16028

**182. A Formal Framework for Understanding Length Generalization in Transformers**
Xinting Huang (ETH / Saarland), FLaNN Seminar · 2025 · 0:38:23 · https://www.youtube.com/watch?v=3G_4VYGhgvQ
The current state of the art on predicting which tasks length-generalize.
*Paper:* arXiv:2410.02140

**183. The emergence of clusters in self-attention dynamics**
Philippe Rigollet (MIT), Simons · 2024 · 0:48:48 · https://www.youtube.com/watch?v=ZrsQGhG0su0
Attention as an interacting-particle system; tokens provably cluster as depth increases. A completely different mathematical lens on the same architecture.
*Paper:* Geshkovski, Letrouit, Polyanskiy, Rigollet (arXiv:2305.05465)

**184. Exact solutions to the geometric dynamics of signal propagation through transformers predict their trainability**
Surya Ganguli (Stanford), Simons · 2024 · 0:44:20 · https://www.youtube.com/watch?v=_THXU94rarw
Signal-propagation theory specialized to transformers, with trainability predictions that hold up.

### 7.4 Weisfeiler–Leman hierarchy and GNN expressivity

**185. Theoretical Foundations of Graph Neural Networks** **[CORE]**
Petar Veličković (DeepMind) · 2021 · 1:12:20 · https://www.youtube.com/watch?v=uF53xsT7mjc
The best single lecture deriving message passing from permutation invariance as a first principle. Start here even if you know GNNs.
*Paper:* Bronstein, Bruna, Cohen, Veličković, "Geometric deep learning" (arXiv:2104.13478)

**186. Representation and Learning in Graph Neural Networks** **[CORE]**
Stefanie Jegelka (MIT), Tübingen Machine Learning · 2020 · 0:41:38 · https://www.youtube.com/watch?v=Rr0pBFGcnjw
GIN and the 1-WL upper bound, by a co-author of the paper that established the result. This is the "message-passing GNNs are exactly as powerful as 1-WL" talk.
*Paper:* Xu, Hu, Leskovec, Jegelka, "How powerful are graph neural networks?" (arXiv:1810.00826)

**187. A Deep Dive into the Weisfeiler-Leman Algorithm**
Martin Grohe (RWTH Aachen) · 2023 · 0:56:28 · https://www.youtube.com/watch?v=ymRBPnDVw0I
The algorithm itself, in depth, from the logic-and-combinatorics side. Essential if you want to understand *why* the hierarchy is the right yardstick.

**188. The Descriptive Complexity of Graph Neural Networks**
Martin Grohe (RWTH Aachen), FLaNN Seminar · 2023 · 0:52:41 · https://www.youtube.com/watch?v=1VHIMszFGnk
GNN expressivity restated in logic and circuit terms rather than as "equals 1-WL."
*Paper:* arXiv:2303.04613

**189. Subgraph-based networks for expressive, efficient, and domain-independent graph learning**
Haggai Maron (Technion / NVIDIA), CIRM · 2022 · 0:49:41 · https://www.youtube.com/watch?v=QlCDaP2RU9A
How subgraph GNNs climb above 1-WL, and the symmetry group that explains why they work.
*Paper:* Frasca, Bevilacqua, Bronstein, Maron (arXiv:2206.11140)

**190. On Computational Hardness with Graph Neural Networks**
Joan Bruna (NYU), IPAM · 2018 · 0:55:31 · https://www.youtube.com/watch?v=ZSIZSVRvd4Q
The hardness side — what GNNs cannot do for reasons other than WL.

**191. Boot camp on generalization theory for graph learning**
Simons "Graph Learning Meets TCS" · 2025 · 1:39:50 · https://www.youtube.com/watch?v=AhgY4ErqXDo
Current tutorial-level treatment of generalization specifically for graph models, which has its own subtleties.

### 7.5 State space model theory

**192. On the Tradeoffs of State Space Models** **[CORE]**
Albert Gu (CMU), Simons · 2024 · 0:49:05 · https://www.youtube.com/watch?v=ksRp_DIHWj4
Gu's own framing of the SSM-versus-transformer tradeoff, delivered to a theory audience rather than a systems one.
*Paper:* Gu & Dao, "Mamba" (arXiv:2312.00752)

**193. Structured State Space Models for Deep Sequence Modeling** (LxMLS tutorial)
Albert Gu (CMU) · 2024 · 1:34:12 · https://www.youtube.com/watch?v=WC9tqkCpq4s
The full ninety-minute tutorial from S4 through Mamba and the SSD duality with linear attention.
*Paper:* Dao & Gu, "Transformers are SSMs" (arXiv:2405.21060)

**194. The Illusion of State in State-Space Models** **[CORE]**
Will Merrill (NYU), FLaNN Seminar · 2024 · 0:45:42 · https://www.youtube.com/watch?v=4-VXe1yPDjk
The negative result that matters: despite the name, SSMs are no more expressive than transformers for state tracking — both are stuck in TC⁰. Recurrence in form is not recurrence in power.
*Paper:* Merrill, Petty, Sabharwal (arXiv:2404.08819)

**195. The Expressive Capacity of State Space Models: A Formal Language Perspective**
Yash Sarrof (Saarland), FLaNN Seminar · 2024 · 0:48:38 · https://www.youtube.com/watch?v=-CBUWqvmVVU
The formal-language counterpart to #194.
*Paper:* arXiv:2405.17394

**196. Computational Benefits and Limitations of Transformers and State-Space Models**
Eran Malach (Kempner Institute, Harvard), Simons · 2024 · 0:50:52 · https://www.youtube.com/watch?v=sbViSPM3lVE
Direct head-to-head comparison of the two architectures' computational classes.

**197. Scaling Insights from Infinite-Width Theory for Next Gen Architectures**
Leena Vankadara (Amazon Research), IPAM · 2024 · 0:51:06 · https://www.youtube.com/watch?v=2QwdaGIOjcw
muP-style parametrization analysis carried into state-space models — where §DLT-3 and §DLT-7 meet.
*Paper:* arXiv:2406.03529

---

## DLT-8 Full courses with complete recordings

Four complete graduate courses, enumerated lecture by lecture. These are the
spine of the module — the talks above are commentary on material that gets taught
properly here.

If you do only one, do **CS229M**. It is the only course that goes all the way
from Hoeffding's inequality to the neural tangent kernel and implicit
regularization in a single coherent sequence, taught by someone actively
publishing in it.

### 8.1 Stanford CS229M / STATS214 — Machine Learning Theory

**Tengyu Ma (Stanford)** · recorded Fall 2021, posted 2022 · 19 lectures, ≈27 hours
Course notes: https://web.stanford.edu/class/stats214/

| # | Lecture | Link | Length |
|---|---|---|---|
| 1 | Overview, supervised learning, empirical risk minimization | https://www.youtube.com/watch?v=I-tmjGFaaBg | 1:04:07 |
| 2 | Asymptotic analysis, uniform convergence, Hoeffding inequality | https://www.youtube.com/watch?v=Fx3xldCEfsM | 1:20:14 |
| 3 | Finite hypothesis class, discretizing infinite hypothesis space | https://www.youtube.com/watch?v=io-YFfXbIXk | 1:14:13 |
| 4 | Advanced concentration inequalities | https://www.youtube.com/watch?v=fKM6fcOkXuk | 1:31:16 |
| 5 | Rademacher complexity, empirical Rademacher complexity | https://www.youtube.com/watch?v=tkJd2B98hII | 1:23:58 |
| 6 | Margin theory and Rademacher complexity for linear models | https://www.youtube.com/watch?v=echF7IWE05c | 1:22:41 |
| 7 | Challenges in DL theory, generalization bounds for neural nets | https://www.youtube.com/watch?v=kVkMRDZ5fcU | 1:25:43 |
| 8 | Refined generalization bounds for neural nets, kernel methods | https://www.youtube.com/watch?v=gwKfeDRCvSg | 1:27:11 |
| 9 | Covering number approach, Dudley's theorem | https://www.youtube.com/watch?v=wDfardbL50I | 1:26:23 |
| 10 | Generalization bounds for deep nets | https://www.youtube.com/watch?v=P5-VVI1qLxA | 1:23:35 |
| 11 | All-layer margin | https://www.youtube.com/watch?v=GeXBfyrKfM4 | 1:29:24 |
| 13 | Neural tangent kernel | https://www.youtube.com/watch?v=btphvvnad0A | 1:29:29 |
| 14 | NTK, implicit regularization of gradient descent | https://www.youtube.com/watch?v=xpT1ymwCk9w | 1:33:00 |
| 15 | Implicit regularization effect of initialization | https://www.youtube.com/watch?v=l-CR_TLihdg | 1:24:13 |
| 16 | Implicit regularization in classification problems | https://www.youtube.com/watch?v=mham4hHpo7A | 1:29:51 |
| 17 | Implicit regularization effect of the noise | https://www.youtube.com/watch?v=60GqpISCtCU | 1:32:14 |
| 18 | Unsupervised learning, mixture of Gaussians, moment methods | https://www.youtube.com/watch?v=4xDEsLUkdG4 | 1:22:08 |
| 19 | Mixture of Gaussians, spectral clustering | https://www.youtube.com/watch?v=E6rZeGIKdRY | 1:30:30 |
| 20 | Spectral clustering | https://www.youtube.com/watch?v=UYBRLG64oSQ | 1:28:25 |

*Lecture 12 was never posted — the sequence runs 11 → 13 on YouTube. The gap is covered in the course notes.*

**Lectures 7–17 are the heart of this entire module.** Lectures 1–6 are standard
statistical learning theory you can get in many places; lectures 7 onward are
Tengyu Ma deriving the deep-learning-specific results at blackboard pace, and
there is no substitute for them anywhere else on video.

### 8.2 MIT 9.520 / 6.860 — Statistical Learning Theory and Applications

**Tomaso Poggio & Lorenzo Rosasco (MIT)** · Fall 2019 · 25 classes, ≈33 hours
Channel: MITCBMM · no playlist exists; URLs below are the Fall 2019 set specifically

A caution worth stating up front: **the MITCBMM channel hosts several years of
this course with identical generic titles** ("Class 1", "Class 2", …). Mixing
years gives you a scrambled course. Every link below was date-checked to fall
between 2019-09-05 and 2019-12-10, so this is one coherent offering.

| Class | Link | Length |
|---|---|---|
| 1 | https://www.youtube.com/watch?v=4nPABKIuYKo | 1:21:55 |
| 2 | https://www.youtube.com/watch?v=kNWONiLbfVs | 1:18:18 |
| 3 | https://www.youtube.com/watch?v=MiypgGqEPpQ | 1:20:06 |
| 4 | https://www.youtube.com/watch?v=_hOZw7SsTXc | 1:17:27 |
| 5 | https://www.youtube.com/watch?v=blSZ605iJ8Q | 1:15:46 |
| 6 | https://www.youtube.com/watch?v=WvscTPTEqow | 1:18:45 |
| 7 | https://www.youtube.com/watch?v=k8hUi6xYgtQ | 1:14:16 |
| 8 | https://www.youtube.com/watch?v=0Tw036csfhI | 1:20:25 |
| 9 | https://www.youtube.com/watch?v=M3lTpmTjZ0Q | 1:19:54 |
| 10 | https://www.youtube.com/watch?v=emnYADN_73o | 1:21:20 |
| 11 | https://www.youtube.com/watch?v=KU5cSQpPP5Y | 1:15:51 |
| 12 | https://www.youtube.com/watch?v=BKemj2t5HRU | 1:16:44 |
| 13 | https://www.youtube.com/watch?v=4leS-ga_B3w | 1:19:51 |
| 14 | https://www.youtube.com/watch?v=awkA8oQxxog | 1:20:53 |
| 15 | https://www.youtube.com/watch?v=LLTyPRWPtjE | 1:20:17 |
| 16 | https://www.youtube.com/watch?v=UJK1O01UyMc | 1:21:18 |
| 17 | https://www.youtube.com/watch?v=8wjQIZ8bm1o | 1:23:49 |
| 18 | https://www.youtube.com/watch?v=u7dRrT5HX1w | 1:22:33 |
| 19 | https://www.youtube.com/watch?v=WX3oIjupleo | 1:25:31 |
| 20 | https://www.youtube.com/watch?v=CTzRZGMgGIE | 1:24:17 |
| 21 | https://www.youtube.com/watch?v=sgwcKA6ej6Q | 1:25:57 |
| 22 | https://www.youtube.com/watch?v=UAE9JgBm5Yo | 1:24:17 |
| 23 | https://www.youtube.com/watch?v=fqVQ48_G1-8 | 1:15:59 |
| 25 | https://www.youtube.com/watch?v=I4JJYnkUQ80 | 1:15:12 |
| 26 | https://www.youtube.com/watch?v=iiFynQczYiM | 1:13:17 |

*Class 24 from Fall 2019 was never uploaded. The Fall 2018 Class 24 (https://www.youtube.com/watch?v=-v992r3IiyY, 1:11:42) is a reasonable substitute.*

Use 9.520 as the **kernel-methods and RKHS foundation** that CS229M assumes.
Poggio's own deep-learning-theory material appears in the later classes.

### 8.3 Mathematics of Deep Learning (minicourse)

**Boris Hanin (Princeton)** · April 2026 · 5 lectures, ≈4.9 hours
University of Chicago Department of Mathematics
Playlist: https://www.youtube.com/playlist?list=PLXOaY9trlJU0E1u1Ru7nxu87qFrXuIlDJ

| # | Link | Length |
|---|---|---|
| 1 | https://www.youtube.com/watch?v=4SVWo5kspR8 | 1:08:52 |
| 2 | https://www.youtube.com/watch?v=nz5I9Nze6CM | 0:56:22 |
| 3 | https://www.youtube.com/watch?v=2rSi7iYuhRU | 0:57:29 |
| 4 | https://www.youtube.com/watch?v=PlQs3IdWBmg | 1:10:55 |
| 5 | https://www.youtube.com/watch?v=4mtlk_HnwV8 | 1:01:16 |

**The most current complete treatment available**, posted April 2026. Five hours
rather than thirty, aimed at mathematicians, and it reflects what the field
believes now rather than in 2019. If your time is short, this plus CS229M
lectures 7–17 is a defensible minimum.

### 8.4 Neural Network Theory (APS 2025 Summer School)

**Matus Telgarsky (NYU Courant)** · 2025 · 3 lectures, ≈4.4 hours
Playlist: https://www.youtube.com/playlist?list=PLVsDasYggo92OhNlmfKjjR196uVLh1dLZ

| # | Link | Length |
|---|---|---|
| 1 | https://www.youtube.com/watch?v=OjyPVFX-fAY | 1:26:20 |
| 2 | https://www.youtube.com/watch?v=rLFNU9c1hr4 | 1:29:48 |
| 3 | https://www.youtube.com/watch?v=Tp8XV_u1vxw | 1:27:44 |

Telgarsky's own course-length treatment of approximation, optimization and
generalization together, updated to 2025. His earlier SMILES 2019 pair splits the
same material differently: "Approximation power of deep networks"
(https://www.youtube.com/watch?v=6Ss9kFTUS-Y, 1:22:56) and "Optimisation and
Generalization of deep networks" (https://www.youtube.com/watch?v=rv-vzl5-oIs,
1:17:16).

### 8.5 Understanding Deep Learning lecture series

**Data ICMC (University of São Paulo)** · 2021 · 10 lectures + panel, ≈11 hours

A genuinely underknown gem: a lecture series where Google Brain and academic
researchers each taught one full hour on their own result. Several lectures cited
elsewhere in this module live here.

| # | Lecture | Speaker | Link | Length |
|---|---|---|---|---|
| 1 | Understanding Generalization Requires Rethinking Deep Learning | Boaz Barak & Gal Kaplun (Harvard) | https://www.youtube.com/watch?v=wi9mjnDfS7Y | 1:15:41 |
| 2 | The Wide Limit of Neural Networks: NNGP and NTK | Jascha Sohl-Dickstein (Google Brain) | https://www.youtube.com/watch?v=fcpI5z9q91A | 1:16:51 |
| 3 | The Catapult Phase of Neural Networks | Guy Gur-Ari (Google) | https://www.youtube.com/watch?v=aPY-M4epEz4 | 1:07:20 |
| 4 | Signal Propagation and Dynamical Isometry | *not listed* | https://www.youtube.com/watch?v=IwrpOhfhj9o | 1:06:50 |
| 5 | Neural Network Loss Landscape in High Dimensions | Stanislav Fort (Stanford/Google) | https://www.youtube.com/watch?v=stTzg8iUaXM | 1:02:22 |
| 6 | Disentangling Trainability and Generalization | Lechao Xiao (Google Brain) | https://www.youtube.com/watch?v=4wiFeJOdro4 | 0:52:09 |
| 7 | Explaining Neural Scaling Laws | Jaehoon Lee (Google Brain) | https://www.youtube.com/watch?v=A8F4Qga3NaM | 0:56:12 |
| 8 | Progress Towards Understanding Generalization | Gintare Karolina Dziugaite (Element AI) | https://www.youtube.com/watch?v=Et_v-EIxqUs | 1:02:25 |
| 9 | Information-Theoretic Generalization Bounds for SGD | Gergely Neu (UPF) | https://www.youtube.com/watch?v=jJrOLPZJxSI | 1:05:37 |
| 10 | Backprop as a Functor | Brendan Fong (MIT / Topos Institute) | https://www.youtube.com/watch?v=N9zZeACcV98 | 1:08:41 |
| — | Panel: The Many Paths to Understanding Deep Learning | — | https://www.youtube.com/watch?v=NfvYufQwA_o | 1:02:40 |

### 8.6 Francis Bach — optimization for machine learning

**Francis Bach (INRIA / ENS)** · no single recorded course, but three verified multi-part series:

*Large-scale Machine Learning and Convex Optimization* (Hausdorff Center, 2016, 4 lectures)
https://www.youtube.com/watch?v=V7lBkV9-kgc (1:07:34) ·
https://www.youtube.com/watch?v=4C65WnxoWPg (1:22:01) ·
https://www.youtube.com/watch?v=naXDNOMNazo (1:04:38) ·
https://www.youtube.com/watch?v=KGx23IxC_Fk (1:15:59)

*MLSS 2020 Tübingen — Optimization* (2 parts)
https://www.youtube.com/watch?v=0MeNygohD6c (1:38:50) ·
https://www.youtube.com/watch?v=hg2h53bU5ic (1:42:35)

*CIRM — Large-scale machine learning and convex optimization* (2 parts)
https://www.youtube.com/watch?v=RPIfP00emcs (1:22:17) ·
https://www.youtube.com/watch?v=nM4lK9ORQx8 (1:28:41)

`UNVERIFIED — search term: "Francis Bach learning theory from first principles lecture"` — that
title appears to exist only as his book (free PDF on his INRIA page), not as a
recorded course. The MLSS 2020 pair is the closest video equivalent.

### 8.7 Princeton ORFE Deep Learning Theory Summer School

**Organized by Boris Hanin (Princeton)** · 2021 · 7 full days, ≈30 hours
Posted as whole unsegmented days on Hanin's own channel, which makes it harder to
assign but it is the largest single block of deep-learning-theory lecture content
freely available.

Day 1 https://www.youtube.com/watch?v=PHcodnoOlgI (5:22:38) ·
Day 2 https://www.youtube.com/watch?v=PRyEApLxcSQ (2:42:47) ·
Day 3 https://www.youtube.com/watch?v=OBrjyorRCxo (5:50:04) ·
Day 4 https://www.youtube.com/watch?v=sS4vvt4dp5U (2:57:17) ·
Day 5 https://www.youtube.com/watch?v=0BUl_5cMilM (4:17:27) ·
Day 6 https://www.youtube.com/watch?v=2rRUfmo4Ays (3:13:55) ·
Day 7 https://www.youtube.com/watch?v=dM1PDZ8Bgkw (5:58:25)

---

## DLT-9 The archives: Simons Institute and IAS programs

Both institutions post complete video archives of multi-month programs. Watching
one program end to end is a different experience from watching scattered talks:
you see the same people disagree across a week, and you see which questions the
community considered open at that moment. For a would-be contributor that
situational knowledge is worth as much as the technical content.

Below, each program is named with its playlist, then **the specific talks worth
watching** with individual URLs.

### 9.1 Simons: Foundations of Deep Learning (Summer 2019)

The program that organized this field. Two archives.

**Deep Learning Boot Camp** · May 28–31, 2019 · tutorial-level, four lecturers
Already enumerated in §DLT-1 and §DLT-4; the full set is:

| Talk | Speaker | Link | Length |
|---|---|---|---|
| Generalization I | Bartlett & Rakhlin | https://www.youtube.com/watch?v=Ntl_WNW8yGc | 1:16:56 |
| Generalization II | Bartlett & Rakhlin | https://www.youtube.com/watch?v=QO8HOqQ_6BQ | 1:23:06 |
| Generalization III | Bartlett & Rakhlin | https://www.youtube.com/watch?v=8hZD5bMBbY4 | 1:18:23 |
| Generalization IV | Bartlett & Rakhlin | https://www.youtube.com/watch?v=n5Zxi22801Q | 1:22:14 |
| Approximation Power | Matus Telgarsky (NYU) | https://www.youtube.com/watch?v=KU6IaE37B9o | 1:13:54 |
| Over-parametrized Neural Networks I | Jason Lee (USC) | https://www.youtube.com/watch?v=uC2IGoTE2u4 | 1:14:29 |
| Over-parametrized Neural Networks II | Jason Lee (USC) | https://www.youtube.com/watch?v=NGon2JyjO6Y | 1:13:57 |
| Implicit Regularization I | Nati Srebro (TTIC) | https://www.youtube.com/watch?v=7uRVR9hsF0g | 1:16:51 |
| Implicit Regularization II | Nati Srebro (TTIC) | https://www.youtube.com/watch?v=IkuOmf7ey14 | 1:22:54 |

**This nine-lecture set is effectively a short course and is the best single
entry point to the entire module.**

**Frontiers of Deep Learning** · July 15–18, 2019 · research talks
Playlist: https://www.youtube.com/playlist?list=PLgKuh-lKre11ekU7g-Z_qsvjDD8cT-hi9

Must-watch eight:

1. **Benign Overfitting in Linear Prediction** — Peter Bartlett (UC Berkeley) · 0:47:40 · https://www.youtube.com/watch?v=GXpP-rXEDpk
2. **From Classical Statistics to Modern Machine Learning** — Misha Belkin (UCSD) · 0:49:47 · https://www.youtube.com/watch?v=OBCciGnOJVs
3. **Learning and Generalization in Over-parametrized Neural Networks, Going Beyond Kernels** — Yuanzhi Li (Stanford) · 0:49:42 · https://www.youtube.com/watch?v=NNPCk2gvTnI
4. **Analyzing Optimization and Generalization in Deep Learning via Trajectories of Gradient Descent** — Nadav Cohen (IAS) · 0:46:27 · https://www.youtube.com/watch?v=Lmj2bU9MdwM
5. **Explaining Landscape Connectivity of Low-cost Solutions for Multilayer Nets** — Rong Ge (Duke) · 0:45:11 · https://www.youtube.com/watch?v=0kXDqS2OmeI
6. **Computation in Very Wide Neural Networks** — Yasaman Bahri (Google Brain) · 0:48:40 · https://www.youtube.com/watch?v=EWLQoO0SGvI
7. **Studying Generalization in Deep Learning via PAC-Bayes** — Gintare Karolina Dziugaite (Element AI) · 0:44:39 · https://www.youtube.com/watch?v=_bYT2VOOxU0
8. **Kernel and Deep Regimes in Overparameterized Learning** — Suriya Gunasekar (MSR) · 0:46:15 · https://www.youtube.com/watch?v=fUQCJNSdskA

Also strong: **Training on the Test Set and Other Heresies** — Ben Recht ·
0:49:37 · https://www.youtube.com/watch?v=NTz4rJS9BAI ·
**A Primal-dual Analysis of Margin Maximization** — Telgarsky · 0:41:42 ·
https://www.youtube.com/watch?v=Rc76ZBP6fHM ·
**Size-free Generalization Bounds for CNNs** — Hanie Sedghi · 0:34:34 ·
https://www.youtube.com/watch?v=jRK3W48cO90

**Emerging Challenges in Deep Learning** · 2019–2020
Playlist: https://www.youtube.com/playlist?list=PLgKuh-lKre10BpafDrv0fg2VNUweWXWVd
Mostly RL, robustness and fairness; the one theory item worth pulling out is
**Is Deeper Better Only When Shallow Is Good?** — Shai Shalev-Shwartz (Hebrew University) ·
0:44:48 · https://www.youtube.com/watch?v=I8KOeXuCLm4

### 9.2 Simons: Deep Learning Theory Workshop and Summer School (August 1–5, 2022)

The best-balanced single week in the archive — tutorials in the morning,
research talks in the afternoon, and the first serious airing of the "benign
overfitting is not what usually happens" correction.

Must-watch seven:

1. **Tutorial: Statistical Learning Theory and Neural Networks I** — Spencer Frei (UC Davis) · 0:59:25 · https://www.youtube.com/watch?v=pb9LQV3fytE
2. **Tutorial: Statistical Learning Theory and Neural Networks II** — Spencer Frei · 1:02:20 · https://www.youtube.com/watch?v=PqentqYpUXk
3. **Tutorial: Implicit Bias I** — Nati Srebro (TTIC) · 1:20:40 · https://www.youtube.com/watch?v=NeTUt5TJOiY
4. **Tutorial: Implicit Bias II** — Nati Srebro · 1:36:30 · https://www.youtube.com/watch?v=8mO1CFfpbRE
5. **Benign, Tempered, or Catastrophic: A Taxonomy of Overfitting** — Neil Mallinar (UCSD) & Preetum Nakkiran · 0:57:45 · https://www.youtube.com/watch?v=cg9s7jpWgck
6. **Feature Selection with Gradient Descent on Two-layer Networks in Low-rotation Regimes** — Matus Telgarsky (NYU) · 0:57:45 · https://www.youtube.com/watch?v=bSJZQVNiLP0
7. **When is Scale Enough?** — Ethan Dyer (Google Research) · 1:12:25 · https://www.youtube.com/watch?v=Jpu3kQv39L4

Also: **The Devil is in the Tails and Other Stories of Interpolation** — Niladri
Chatterji (OpenAI) · 0:54:40 · https://www.youtube.com/watch?v=e7Y3hgQlaaE ·
**A Theoretical Framework of Convolutional Kernels on Image Datasets** — Song Mei
(UC Berkeley) · 1:00:05 · https://www.youtube.com/watch?v=DD0RBODEE78 ·
**Understanding the Robustness of Deep Learning** — Aditi Raghunathan (Stanford) ·
1:00:23 · https://www.youtube.com/watch?v=pToDHIS2kcE

### 9.3 Simons: Modern Paradigms in Generalization (Fall 2024)

The 2024 restatement of the whole question, five years after the 2019 program.
Useful precisely as a before-and-after comparison: watch a 2019 talk and its 2024
counterpart to see what actually got settled.

**Modern Paradigms in Generalization Boot Camp** · August 27–30, 2024
Playlist: https://www.youtube.com/playlist?list=PLgKuh-lKre10_AXZufHVP1qZRfnDt5RFD

Must-watch six:

1. **Overview of Statistical Learning Theory, Part 1** — Nati Srebro (TTIC) · 1:16:40 · https://www.youtube.com/watch?v=BxQxsuRjoR8
2. **Overview of Statistical Learning Theory, Part 2** — Nati Srebro · 1:02:44 · https://www.youtube.com/watch?v=Mntd78eCrgk
3. **Modern paradigms of generalization, the heliocentric model of Aristarchus, gradient descent is a lazy scientist, and other stories** — Matus Telgarsky (Courant, NYU) · 1:09:38 · https://www.youtube.com/watch?v=-TIZPe_YaiU
4. **The elusive generalization: classical bounds to double descent to grokking** — Misha Belkin (UCSD) · 1:19:56 · https://www.youtube.com/watch?v=h2I0Hs2K2KI
5. **Understanding Generalization from Pre-training Loss to Downstream Tasks** — Tengyu Ma (Stanford) · 1:17:51 · https://www.youtube.com/watch?v=rFp0tVQW_q0
6. **Reconsidering Overfitting in the Age of Overparameterized Models** — Fanny Yang (ETH Zurich) · 1:18:05 · https://www.youtube.com/watch?v=g1Gb3UEgpOk

Also: **Prediction, Generalization, Complexity: Revisiting the Classical View
from Statistics, Part 1 / Part 2** — Ryan Tibshirani (UC Berkeley) · 1:18:06 /
1:01:38 · https://www.youtube.com/watch?v=mwnoEZgsZpA ·
https://www.youtube.com/watch?v=-PWYupkL6Kg

**Unknown Futures of Generalization** · December 2–6, 2024
Playlist: https://www.youtube.com/playlist?list=PLgKuh-lKre10arpoJoYeh2B0QIB3OjuLe

Must-watch five:

1. **Learning Theory of Transformers: Generalization and Optimization of In-Context Learning** — Taiji Suzuki (University of Tokyo) · 0:45:35 · https://www.youtube.com/watch?v=WyeomuU2vQw
2. **Weak-to-Strong Generalization** — Pavel Izmailov (Anthropic) · 0:43:25 · https://www.youtube.com/watch?v=VViyQRGxSKo
3. **On Memorization of Large Language Models in Logical Reasoning** — Chiyuan Zhang (Google Research) · 0:48:05 · https://www.youtube.com/watch?v=eULIf02frIw
4. **Generalization in the representations and computations of frontier language models** — Joshua Batson (Anthropic) · 0:52:05 · https://www.youtube.com/watch?v=2xb3mhIqjLw
5. **Understanding the abilities of AI systems: Memorization, generalization, and points in between** — Tom McCoy (Yale) · 0:44:25 · https://www.youtube.com/watch?v=3c9TiKryTtA

*Also in this program:* **Emerging Generalization Settings** playlist —
https://www.youtube.com/playlist?list=PLgKuh-lKre12gP84pKqe_1n4FLk6JD-Eo

### 9.4 Simons: Special Year on Large Language Models and Transformers (2023–2024)

Where theory met the actual systems. Three archives.

**Part 1 Boot Camp** · September 4–6, 2024
Playlist: https://www.youtube.com/playlist?list=PLgKuh-lKre13qQH5G4jpudE3_TYcqySVE

1. **Introduction to Transformers (How Do Transformers Work, Part 1)** — Ankur Moitra (MIT) · 1:10:24 · https://www.youtube.com/watch?v=9L3i4rqcGG8
2. **How Do Transformers Work? (Part 2)** — Daniel Hsu (Columbia) · 1:15:41 · https://www.youtube.com/watch?v=uIsej_SIIQU
3. **Toward Understanding In-context Learning** — Tengyu Ma (Stanford) · 1:29:35 · https://www.youtube.com/watch?v=hxrR39mAlR4
4. **On large language models and transformers: perspectives from physics, neuroscience, and theory** — Surya Ganguli (Stanford) · 1:32:41 · https://www.youtube.com/watch?v=qXEuY6qLISE

**Transformers as a Computational Model** · September 23–27, 2024
Playlist: https://www.youtube.com/playlist?list=PLgKuh-lKre11RuxGM038u0OSxVdCicIMF

**This workshop is the single densest source of expressivity theory that exists.**
Must-watch eight:

1. **Transformers, parallel computation, and logarithmic depth** — Daniel Hsu (Columbia) · 0:57:21 · https://www.youtube.com/watch?v=spxJnEhs1qI
2. **The Parallelism Tradeoff: Understanding Transformer Expressivity Through Circuit Complexity** — Will Merrill (NYU) · 0:45:13 · https://www.youtube.com/watch?v=7GVesfXD6_Q
3. **Transformer Expressivity and Formal Logic** — David Chiang (Notre Dame) · 0:45:34 · https://www.youtube.com/watch?v=hR3G5jsuOHs
4. **Iterated Models: Expressive Power, Learning, and Chain of Thought** — Nati Srebro (TTIC) · 0:54:08 · https://www.youtube.com/watch?v=NRyIPyO_IWY
5. **Computational Benefits and Limitations of Transformers and State-Space Models** — Eran Malach (Kempner, Harvard) · 0:50:52 · https://www.youtube.com/watch?v=sbViSPM3lVE
6. **On the Tradeoffs of State Space Models** — Albert Gu (CMU) · 0:49:05 · https://www.youtube.com/watch?v=ksRp_DIHWj4
7. **The emergence of clusters in self-attention dynamics** — Philippe Rigollet (MIT) · 0:48:48 · https://www.youtube.com/watch?v=ZrsQGhG0su0
8. **Emergence and grokking in "simple" architectures** — Misha Belkin (UCSD) · 0:52:40 · https://www.youtube.com/watch?v=dzpA30qZxYw

Also: **Associative memories as a building block in Transformers** — Alberto
Bietti (Flatiron) · 0:38:37 · https://www.youtube.com/watch?v=ncAhx70jTIc ·
**Exact solutions to the geometric dynamics of signal propagation through
transformers** — Surya Ganguli (Stanford) · 0:44:20 ·
https://www.youtube.com/watch?v=_THXU94rarw

**Large Language Models and Transformers** (Aug 2023 workshop)
Playlist: https://www.youtube.com/playlist?list=PLgKuh-lKre12qVTl88k2n2N37tT-BpmHT
Pull out: **Understanding the Origins and Taxonomy of Neural Scaling Laws** —
Yasaman Bahri · 1:05:24 · https://www.youtube.com/watch?v=MUvFuZpxLU8 ·
**In-Context Learning: A Case Study of Simple Function Classes** — Gregory
Valiant (Stanford) · 1:03:40 · https://www.youtube.com/watch?v=DiJsg93zQDc ·
**An Observation on Generalization** — Ilya Sutskever (OpenAI) · 0:57:21 ·
https://www.youtube.com/watch?v=AKMuA_TVz3A

*Also:* **The Future of Transformers and LLMs** —
https://www.youtube.com/playlist?list=PLgKuh-lKre13F6duXbU7e8dJqXnRpJuxy

### 9.5 Simons: Graph Learning Meets Theoretical Computer Science (2025)

Playlist: https://www.youtube.com/playlist?list=PLgKuh-lKre13j2lBO8AeVUCu0TQrY9GhE
The current reference archive for GNN theory. Four to start with:

1. **Boot Camp on Graph Learning** · 1:38:30 · https://www.youtube.com/watch?v=ENW8T59-_eE
2. **Boot camp on generalization theory for graph learning** · 1:39:50 · https://www.youtube.com/watch?v=AhgY4ErqXDo
3. **Boot camp on logic and graph learning** · 1:30:19 · https://www.youtube.com/watch?v=G_8csFlLabM
4. **Boot camp on invariances in graph learning** · 1:29:00 · https://www.youtube.com/watch?v=jeXwv0ClIzY

Plus **Homomorphism Indistinguishability** · 0:57:40 ·
https://www.youtube.com/watch?v=8spy7FJgOjc — the sharpest modern restatement of
what the Weisfeiler–Leman hierarchy is actually measuring.

### 9.6 Simons: Theoretical Foundations — From the Early Days of Neural Networks to the Modern Deep Learning Era

Playlist: https://www.youtube.com/playlist?list=PLgKuh-lKre13Qgeo9Yf4pMIqwpLRPa1Lk
Short historical talks from the people who were there. Of particular value:
**Talk by Matus Telgarsky (Courant, NYU)** · 0:31:06 ·
https://www.youtube.com/watch?v=2QmxsxlEjLU ·
**Talk by Nati Srebro (TTIC)** · 0:23:09 ·
https://www.youtube.com/watch?v=-A6LFTLmnYg ·
**Talk by Misha Belkin (UC San Diego)** · 0:15:46 ·
https://www.youtube.com/watch?v=xgaZPTG7hVo

### 9.7 IAS: Special Year on Optimization, Statistics, and Theoretical Machine Learning (2019–2020)

The Institute for Advanced Study ran a full special year on this subject under
Sanjeev Arora, and posted the seminar series. The talks are shorter than Simons'
(25–45 minutes is typical) and more sharply focused on a single result, which
makes them good for sampling breadth.

Must-watch eight:

1. **In Defense of Uniform Convergence** — Daniel M. Roy (Toronto) · 2020 · 1:21:46 · https://www.youtube.com/watch?v=6mdFQR0-WT0
2. **The Principles of Deep Learning Theory** — Dan Roberts (MIT/Salesforce) · 2021 · 1:20:17 · https://www.youtube.com/watch?v=YzR2gZrsdJc
3. **Margins, perceptrons, and deep networks** — Matus Telgarsky · 2020 · 1:22:27 · https://www.youtube.com/watch?v=yfk-IPlr6M0
4. **Toward a Causal Analysis of Generalization in Deep Learning** — Behnam Neyshabur (Google) · 2019 · 0:33:17 · https://www.youtube.com/watch?v=HAfQ-Q8pn0g
5. **Kernel and Rich Regimes in Deep Learning** — Nati Srebro (TTIC) · 2019 · 0:37:01 · https://www.youtube.com/watch?v=ZjTMiYhW4XY
6. **From Classical Statistics to Modern ML: the Lessons of Deep Learning** — Mikhail Belkin · 2019 · 0:37:29 · https://www.youtube.com/watch?v=5-Kqb80h9rk
7. **Optimization Landscape and Two-Layer Neural Networks** — Rong Ge (Duke) · 2019 · 0:58:27 · https://www.youtube.com/watch?v=dmfyYXl0xUY
8. **Statistical mechanics of deep learning** — Surya Ganguli (Stanford) · 2019 · 0:29:55 · https://www.youtube.com/watch?v=-QF_jX8L0nw

Also worth it: **On the Connection between Neural Networks and Kernels: a Modern
Perspective** — Simon Du · 2019 · 0:30:46 ·
https://www.youtube.com/watch?v=HvEGJUwQEO8 ·
**Towards a theoretical foundation of neural networks** — Jason Lee · 2019 ·
0:24:39 · https://www.youtube.com/watch?v=vQsuF21tGQk ·
**PAC-Bayesian approaches to understanding generalization** — Gintare Karolina
Dziugaite · 2019 · 0:31:34 · https://www.youtube.com/watch?v=MrUqeSj9Pgk ·
**Designing explicit regularizers for deep models?** — Tengyu Ma · 2019 ·
0:33:55 · https://www.youtube.com/watch?v=QjxzY8W-caY ·
**The mystery of over-parametrization in neural networks** — Behnam Neyshabur ·
2017 · 0:17:33 · https://www.youtube.com/watch?v=4Mga1cERS34 ·
**On Expressiveness and Optimization in Deep Learning** — Nadav Cohen · 2018 ·
1:03:26 · https://www.youtube.com/watch?v=F079b2dwcAg ·
**Understanding Deep Neural Networks: From Generalization to Interpretability** —
Gitta Kutyniok · 2020 · 1:02:04 · https://www.youtube.com/watch?v=qVZksJt1WQo

### 9.8 Formal Languages and Neural Networks Seminar

https://www.youtube.com/channel/UCrp8k-nSuMKHM4sSUvlPdAw

Not an institute program, but functionally an archive: roughly 120 hour-long
talks on transformer and SSM expressivity, nearly all delivered by the first
author of the paper being discussed. Ten of §DLT-7's entries come from here. If
you intend to work on architecture theory, this is the channel to subscribe to.

---

## DLT-10 How to sequence this

There are 197 numbered entries above. Counting the enumerated course lectures and
the archive listings in §DLT-9, the module contains **291 distinct videos, 330
hours in total**. Nobody should watch all of it linearly. Three paths.

**The twelve-week path (≈10 hrs/week).** Weeks 1–3: the Simons Deep Learning Boot
Camp nine-lecture set (§9.1) plus CS229M lectures 1–6. Week 4: double descent and
benign overfitting (§DLT-2, items 34, 37, 38, 42, 46). Weeks 5–6: NTK and the
lazy/rich distinction (§DLT-3, items 78, 79, 85, 86, 90) plus CS229M 13–14. Week
7: muP and Tensor Programs (items 96, 97, 100). Week 8: optimization (§DLT-4,
items 51, 52, 56, 64, 67). Week 9: scaling laws (§DLT-5, items 110, 113, 118,
121, 123). Week 10: emergence debate and phenomena (items 126, 128, 130, 138,
145). Week 11: expressivity (§DLT-7, items 165, 170, 171, 174, 176, 186). Week
12: the 2024 restatement — watch §9.3 and compare against week 1.

**The six-week compressed path.** Boris Hanin's five-lecture minicourse (§8.3),
then CS229M lectures 7–17, then every item marked **[CORE]** in §DLT-2 through
§DLT-7. That is roughly 60 hours and covers the live questions without the
historical build-up.

**The research-entry path.** If you already know the material and want to find a
problem: watch §9.3 and §9.4 end to end, both from 2024, and write down every
sentence beginning "we don't know" or "it's open whether." Then watch items 115
((Mis)Fitting), 27 (Neyshabur's causal analysis), 42 (the overfitting taxonomy)
and 194 (The Illusion of State), which are the four talks in this module that
most directly say *the published consensus is wrong about something specific*.
Those four are where contributions are currently cheapest.

### Where the open problems actually are

Based on what the 2024–2026 talks say out loud rather than what the 2019 talks
hoped:

- **Generalization bounds remain vacuous for real models.** PAC-Bayes is still
  the only approach that has produced non-vacuous bounds, and only for small
  stochastic networks (items 18, 22). Nobody has a bound for a frontier model.
- **The feature-learning regime has no clean theory.** NTK is solved and wrong;
  mean-field works for two layers; muP is an empirical scaling prescription with
  partial theory. The gap between items 86 and 97 is the gap in the field.
- **Why Adam works is genuinely unsettled** and has become urgent again because
  Muon and SOAP changed the practical landscape (items 64, 67, 69).
- **Scaling-law methodology is weaker than it looks** (item 115), and the
  theoretical derivations (items 118, 121, 123) do not yet reproduce the measured
  exponents from first principles.
- **Loss of plasticity** (items 156–158) is a hard obstacle to continual learning
  that has attracted far less theoretical attention than it deserves.
- **Expressivity theory is now ahead of learning theory for transformers.** We
  know what they can compute (§7.3); we have much less idea what gradient descent
  on them will find. Item 180 is one of the few bridges.

### Flagged as unverifiable

Everything listed above was confirmed to exist and play, with its real title,
duration and year. These are the items I looked for and could **not** confirm:

- `UNVERIFIED — search term: "Nitish Keskar large batch training generalization gap talk"` — no recorded talk by Keskar on the large-batch/sharp-minima result appears to exist.
- `UNVERIFIED — search term: "Ziming Liu grokking Omnigrok MIT talk"` — no standalone talk found; Gromov (items 131–132) covers the physics-of-grokking angle.
- `UNVERIFIED — search term: "Jordan Hoffmann training compute optimal large language models talk"` — no DeepMind-author Chinchilla talk on video. Items 113 and 114 are the substitutes.
- `UNVERIFIED — search term: "Utkarsh Sharma Jared Kaplan scaling laws data manifold dimension"` — no dedicated talk; the result is covered inside item 111.
- `UNVERIFIED — search term: "Alexander Maloney random feature model scaling laws"` — no dedicated talk; Pehlevan (items 121–122) covers the same mathematics.
- `UNVERIFIED — search term: "Christopher Morris Weisfeiler Leman graph neural networks talk"` — Morris appears only inside the Simons 2025 graph boot camp, not as a standalone lecture.
- `UNVERIFIED — search term: "Denny Zhou chain of thought expressivity talk"` — no standalone talk; item 177 (Zhiyuan Li) covers the same theorem.
- `UNVERIFIED — search term: "Francis Bach learning theory from first principles lecture"` — appears to exist only as his book, not as a recorded course. §8.6 lists the closest recorded equivalents.
- **Stanford CS229M Lecture 12** was never posted to YouTube; the course notes cover it.
- **MIT 9.520 Fall 2019 Class 24** was never uploaded; the Fall 2018 recording is the only version.

### A closing note on how to use the talks

The single highest-value habit in this module is to **watch pairs that disagree**.
The field's real content lives in the disagreements, and this module is
deliberately stocked with them:

- Nagarajan & Kolter (item 11) against Roy (item 12) on uniform convergence.
- Bartlett's benign overfitting (item 38) against Mallinar & Nakkiran's taxonomy
  (item 42) on whether interpolation is actually harmless.
- Wei (item 126) against Schaeffer (item 128) on whether emergence is real.
- Arora (item 25) against the entire landscape-analysis literature on whether
  optimization is even the right language.
- Gu's SSM tradeoffs (item 192) against Merrill's illusion-of-state (item 194) on
  whether recurrence buys anything.

Watch each pair back to back in one sitting and write down which argument you
find stronger and why. That exercise — not the lecture count — is what converts
this module into the ability to produce an original result.
