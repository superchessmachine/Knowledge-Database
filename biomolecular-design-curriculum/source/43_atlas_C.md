# Atlas C — Monte Carlo and Stochastic Sampling

> **Problem.** You want expectations under a distribution you can evaluate up to
> a constant but cannot sample from directly. Molecular dynamics is one answer —
> follow a trajectory and hope it is ergodic. Monte Carlo is the other, and it
> is more general: construct a Markov chain whose stationary distribution is the
> one you want, and let it run. **Almost every method in this document is a
> Monte Carlo method wearing different clothes**, including Rosetta's design
> protocol, simulated annealing in NMR refinement, and the reverse process of a
> diffusion model.

This family is badly underrepresented in biomolecular curricula, which is why
so many practitioners can run a Metropolis move but cannot say what would make
it incorrect.

---

## C.1 Fundamentals

### Werner Krauth — Statistical Mechanics: Algorithms and Computations
**ENS Paris** · Tier A

The spine of this family. Krauth builds Metropolis from a pebble game, so
detailed balance and rejection arrive as consequences rather than incantations.

> **Fragility note.** These individual videos sit on a third-party re-upload
> channel rather than an institutional one, so they could disappear. The durable
> route is the free-to-audit [Coursera course](https://www.coursera.org/learn/statistical-mechanics);
> the ICTP lectures below are the institutionally-hosted fallback.

| # | Lecture | Length | Link |
|---|---|---|---|
| 1 | Introduction to Monte Carlo algorithms | 28:08 | [▶](https://www.youtube.com/watch?v=L7nsVrt41Rg) |
| 2 | Hard disks: from Classical to Statistical Mechanics | 35:59 | [▶](https://www.youtube.com/watch?v=ameqTFF7Q9g) |
| 4 | Sampling and Integration: from Gaussians to Maxwell and Boltzmann | 32:20 | [▶](https://www.youtube.com/watch?v=Z_VomhU7XH8) |
| 8 | **Ising model: from enumeration to Cluster Monte Carlo** | 28:49 | [▶](https://www.youtube.com/watch?v=kvf7aUPZCWk) |
| 9 | Dynamical Monte Carlo and the Faster-than-the-Clock approach | 25:07 | [▶](https://www.youtube.com/watch?v=QHCBSk_XH5I) |
| 10 | **The Alpha and the Omega of Monte Carlo** (convergence, error bars) | 32:28 | [▶](https://www.youtube.com/watch?v=8b5C75P8Vxs) |
| T1 | Tutorial: Exponential convergence and the 3×3 pebble game | 32:39 | [▶](https://www.youtube.com/watch?v=D8DZjLPlWd0) |
| T8 | Tutorial: Heat bath algorithm, coupling of Markov chains | 19:21 | [▶](https://www.youtube.com/watch?v=jNdNs266AK0) |

Tutorial 8's coupling-of-Markov-chains material is the cleanest free explanation
of exact sampling anywhere — Propp-Wilson coupling from the past, which
terminates with a sample guaranteed to be from the stationary distribution
rather than approximately so.

**Krauth at ICTP** — same material, graduate pace, roughly double the time, with
autocorrelation and error analysis done more rigorously:
[I](https://www.youtube.com/watch?v=iWiWjuNthi8) (1:33:56) ·
[II](https://www.youtube.com/watch?v=hCQ8HDsdJo4) (2:05:19) ·
[III](https://www.youtube.com/watch?v=vh70bDyUfpU) (2:03:39)

### Why high-dimensional sampling needs MCMC at all

| Title | Speaker | Length | Link |
|---|---|---|---|
| MacKay Lec 12: Monte Carlo Methods I | David MacKay (Cambridge) | 1:23:48 | [▶](https://www.youtube.com/watch?v=sN_0iGWcyLI) |
| MacKay Lec 13: Monte Carlo Methods II, Slice Sampling | David MacKay | 1:47:57 | [▶](https://www.youtube.com/watch?v=Qr6tg9oLGTA) |
| **Markov Chain Monte Carlo** | Iain Murray (Edinburgh, MLSS Africa) | 1:17:50 | [▶](https://www.youtube.com/watch?v=_v4Eb09qp7Q) |
| Introduction to MCMC for Deep Learning | Iain Murray (IPAM) | 1:01:50 | [▶](https://www.youtube.com/watch?v=Em6mQQy4wYA) |
| Pseudo-Marginal Slice Sampling | Iain Murray | 32:08 | [▶](https://www.youtube.com/watch?v=HhGJZmn-5SU) |
| A Gentle Introduction to Markov chain Monte Carlo | Dootika Vats (IIT Kanpur) | 1:08:45 | [▶](https://www.youtube.com/watch?v=yOeJwWnOpmg) |

MacKay gives the best motivation anywhere for *why* importance sampling and
rejection sampling die in high dimension — the fact that makes MCMC necessary
rather than merely convenient. **Murray is the clearest living explainer of why
detailed balance is sufficient but not necessary**, and of what burn-in does and
does not fix.

**Vats is the authority on honest MCMC standard errors.** Her lecture is where
effective sample size stops being a number a library prints and becomes
something you can defend in a referee reply.

### Course modules

| Title | Instructor | Length | Link |
|---|---|---|---|
| Lec 34: Markov chain algorithm, equilibrium and detailed balance | NPTEL / IIT Roorkee | 38:04 | [▶](https://www.youtube.com/watch?v=PmQNLhxoPZA) |
| Lec 35: Metropolis algorithm, periodic boundary conditions | NPTEL / IIT Roorkee | 45:46 | [▶](https://www.youtube.com/watch?v=AyfZuJ7oDjE) |
| MIT 3.320 Lec 17: Monte Carlo Simulations | Ceder & Marzari (MIT) | 1:14:31 | [▶](https://www.youtube.com/watch?v=3FumIu7Qito) |
| MIT 3.320 Lec 18: Monte Carlo Simulation II | Ceder & Marzari | 1:15:27 | [▶](https://www.youtube.com/watch?v=ZsqPyPe7B5w) |
| Lec 30: Introduction to Markov Chain Monte Carlo | NPTEL / IIT Kanpur | 24:30 | [▶](https://www.youtube.com/watch?v=LhCIqbZqgDM) |
| Computational Physics: Monte Carlo methods | Morten Hjorth-Jensen (Oslo/MSU) | 1:28:30 | [▶](https://www.youtube.com/watch?v=ThTzc8LZlA4) |

*Sokal's Cargèse lectures on autocorrelation and critical slowing down are the
canonical treatment and have no video. His recorded Newton Institute lectures
are on combinatorics, not MC algorithms — do not substitute them. Read the
written notes.*

---

## C.2 Advanced MCMC

### Hamiltonian Monte Carlo

| Title | Speaker | Length | Link |
|---|---|---|---|
| **New Monte Carlo Methods Based on Hamiltonian Dynamics** | Radford Neal (Toronto) | 1:05:31 | [▶](https://www.youtube.com/watch?v=KFq7LB1nDTw) |
| Efficient Bayesian inference with HMC, Part 1 | Michael Betancourt (MLSS Iceland) | 1:29:43 | [▶](https://www.youtube.com/watch?v=pHsuIaPbNbY) |
| HMC and Stan, Part 2 | Michael Betancourt | 42:26 | [▶](https://www.youtube.com/watch?v=xWQpEAyI5s8) |
| Unravelling A Geometric Conspiracy | Michael Betancourt (LOGML) | 58:06 | [▶](https://www.youtube.com/watch?v=7qeB25OFfvA) |
| Scalable Bayesian Inference with HMC | Michael Betancourt | 53:20 | [▶](https://www.youtube.com/watch?v=jUSZboSq1zg) |
| No-U-Turn Sampler (NIPS 2011) | Matthew D. Hoffman | 20:51 | [▶](https://www.youtube.com/watch?v=oMNXRYRNj_M) |
| The No-U-Turn Sampler (2024) | Nawaf Bou-Rabee (Rutgers) | 58:31 | [▶](https://www.youtube.com/watch?v=eAVXROsyT9Y) |
| An Introduction to HMC for Sampling | Simons Institute | 1:10:16 | [▶](https://www.youtube.com/watch?v=efqGwPDnlQY) |
| Lec 36: Hamiltonian Monte Carlo | NPTEL / IIT Kanpur | 40:29 | [▶](https://www.youtube.com/watch?v=eFvK6_sQMdI) |

**Neal presenting his own method is the highest-value item here.** And note what
HMC actually is: a molecular dynamics integrator used as an MCMC proposal, with
a Metropolis correction for integration error. The physics culture invented the
dynamics; the statistics culture noticed it was a proposal distribution. That is
a completed cross-cultural carry, and knowing it happened once makes the next
one easier to see.

### Nested sampling, Wang-Landau, tempering

| Title | Speaker | Length | Link |
|---|---|---|---|
| Computing Bayes in Big Spaces | John Skilling (MaxEnt 2011) | 43:23 | [▶](https://www.youtube.com/watch?v=kqB4Wcvj0Pk) |
| Big spaces: Quantification | John Skilling (MLSS Africa) | 1:33:17 | [▶](https://www.youtube.com/watch?v=WLDDLCHnDPw) |
| A Brief Introduction to Nested Sampling | Joshua Speagle (Toronto) | 38:02 | [▶](https://www.youtube.com/watch?v=5Gh2FvEPr60) |
| Nested Sampling from scratch | Johannes Buchner (MPE Garching) | 1:00:00 | [▶](https://www.youtube.com/watch?v=baLFl_4ZwXw) |
| State of the art in nested sampling and MCMC | Johannes Buchner | 1:46:52 | [▶](https://www.youtube.com/watch?v=HFaqcB_H6MA) |
| **Replica-Exchange Wang-Landau Sampling, Lec 1** | David P. Landau (Georgia) | 45:00 | [▶](https://www.youtube.com/watch?v=_ilTEy_w8h8) |
| Replica-Exchange Wang-Landau Sampling, Lec 2 | Ying-Wai Li (LANL) | 55:44 | [▶](https://www.youtube.com/watch?v=4-4zJh_RPqU) |
| Replica-Exchange Wang-Landau Sampling, Lec 3 | Ying-Wai Li | 53:20 | [▶](https://www.youtube.com/watch?v=dFAaOcOH9dU) |
| Recent advances in accelerated Monte Carlo algorithms | Ying-Wai Li | 54:55 | [▶](https://www.youtube.com/watch?v=g042Y2668go) |
| Theory of simulated tempering and replica exchange | Massimiliano Bonomi (PASI 2012) | 1:02:31 | [▶](https://www.youtube.com/watch?v=5upvgbp_elI) |
| Non-Reversible Parallel Tempering | Alexandre Bouchard-Côté (UBC) | 33:35 | [▶](https://www.youtube.com/watch?v=bRZ1kXYEfh8) |
| Non-Reversible Parallel Tempering: a Scalable Scheme | Saifuddin Syed (Oxford) | 58:21 | [▶](https://www.youtube.com/watch?v=9gOssrhN3EA) |

Landau presenting Wang-Landau is the draw. Nested sampling is the one method
here that computes the *evidence* — the normalizing constant — which is exactly
the partition function. A physicist and a Bayesian statistician are computing
the same object and almost never say so to each other.

### Cluster algorithms, non-reversible MCMC, sequential MC

| Title | Speaker | Length | Link |
|---|---|---|---|
| Reversible and irreversible Markov chains in statistical physics, Lec 1 | Werner Krauth | 1:04:16 | [▶](https://www.youtube.com/watch?v=lZw7Zs3bWzw) |
| Reversible and irreversible Markov chains, Lec 2 | Werner Krauth | 51:55 | [▶](https://www.youtube.com/watch?v=W9fFhOuJQ1I) |
| **Fast irreversible Markov chains in statistical physics** | Werner Krauth | 1:10:34 | [▶](https://www.youtube.com/watch?v=BZKN6ZoFOcQ) |
| Swendsen-Wang on the Mean-Field Potts Model | Simons Institute | 45:49 | [▶](https://www.youtube.com/watch?v=7nogiBu1yxE) |
| Asymmetric momentum sampling in event-chain Monte Carlo | Michael Faulkner (Bristol) | 53:03 | [▶](https://www.youtube.com/watch?v=BTxgAyLQirc) |
| The coordinate sampler: a non-reversible Gibbs-like MCMC | Christian P. Robert (Paris-Dauphine) | 32:45 | [▶](https://www.youtube.com/watch?v=TfhrC_lghwg) |
| Tutorial on Sequential Monte Carlo methods | Anthony Lee (Bristol) | 1:02:58 | [▶](https://www.youtube.com/watch?v=E8Jxaq81mso) |
| Particle Markov chain Monte Carlo, Part 1 | Fredrik Lindsten (Linköping) | 1:16:17 | [▶](https://www.youtube.com/watch?v=BxHNcXv54ow) |

**The event-chain and lifted-MCMC thread is the one nobody teaches and the one
most likely to transfer.** These chains violate detailed balance deliberately —
they satisfy the weaker global balance condition — and get order-of-magnitude
speedups on hard-particle and polymer systems as a result. If you ever wondered
what "sufficient but not necessary" buys you, this is the answer, in production.

---

## C.3 Monte Carlo in molecular systems

| Title | Speaker | Length | Link |
|---|---|---|---|
| Lec 52: Extension of canonical MC to other ensembles (GCMC) | NPTEL / IIT Roorkee | 33:55 | [▶](https://www.youtube.com/watch?v=r5qOSxEYIus) |
| Lec 53: Monte Carlo in Gibbs and semi-grand canonical ensembles | NPTEL / IIT Roorkee | 24:37 | [▶](https://www.youtube.com/watch?v=8LqVN8a7MOY) |
| ChEn 513: Gibbs Ensemble Monte Carlo | Thomas Knotts (BYU) | 1:27:50 | [▶](https://www.youtube.com/watch?v=Y1eMPT1DoBI) |
| Lec 23: Monte Carlo simulations of polymer chains | NPTEL / IIT Roorkee | 46:58 | [▶](https://www.youtube.com/watch?v=GhR9xBZZF6g) |
| Introduction to Atomic Simulations by Metropolis Monte Carlo | Mathieu Bauchy (UCLA) | 2:36:28 | [▶](https://www.youtube.com/watch?v=GMCFVEfupDA) |
| **L21: Kinetic Monte Carlo** | Peter Kratzer (Duisburg-Essen) | 53:16 | [▶](https://www.youtube.com/watch?v=AQJPrUxxSpk) |
| MIT 10.34 Lec 34: Stochastic Chemical Kinetics 1 | Green & Swan (MIT) | 53:57 | [▶](https://www.youtube.com/watch?v=42TkHA__6bk) |
| MIT 10.34 Lec 35: Stochastic Chemical Kinetics 2 (tau-leaping) | Green & Swan | 47:32 | [▶](https://www.youtube.com/watch?v=geVT3JYHeqI) |
| **Dan Gillespie presenting the Gillespie Algorithm** | Daniel T. Gillespie | 39:37 | [▶](https://www.youtube.com/watch?v=atOc2v8Wtcw) |
| **Refining biomolecular structures with minimization and Monte Carlo** | RosettaCommons | 39:13 | [▶](https://www.youtube.com/watch?v=X_pLpIjEpas) |
| **Rotamer Libraries and Side-chain Packing** | Brian Weitzner (Gray course, JHU) | 1:05:04 | [▶](https://www.youtube.com/watch?v=fvtnEv4x6sQ) |
| StepWise Monte Carlo for modeling and design of RNA and protein | Rhiju Das (Stanford) | 28:20 | [▶](https://www.youtube.com/watch?v=WtbTh9rFznY) |
| Cryo-BIFE: Bayesian Inference of Free Energy profiles | Pilar Cossio (Flatiron) | 37:34 | [▶](https://www.youtube.com/watch?v=MpL5VY9BmJs) |

**The two Rosetta items are the ones to study hardest.** The first is the
Monte-Carlo-plus-Minimization protocol; the second is the simulated-annealing
side-chain packer underneath every design run you have ever launched. Then ask
the question that Atlas R's open problems hinge on: *what is the stationary
distribution of Rosetta's design protocol?* It is not the Boltzmann distribution
of the energy function, because the annealing schedule and the minimization
steps break detailed balance. Nobody has characterized it properly.

Gillespie explaining why his algorithm is *exact* rather than an ODE
approximation has unusual primary-source value.

*Configurational bias Monte Carlo has no dedicated free video. The polymer-chain
and Gibbs-ensemble lectures set up the Rosenbluth chain-growth logic; read
Siepmann & Frenkel 1992 and Frenkel & Smit ch. 13.*

---

## C.4 Rare-event and path sampling

| Title | Speaker | Length | Link |
|---|---|---|---|
| **Transition path sampling of complex activated processes** | Peter Bolhuis (Amsterdam, ICTP) | 1:21:36 | [▶](https://www.youtube.com/watch?v=XjboE1opv8k) |
| Understanding emergent rare event behaviour in high-dimensional systems | Peter Bolhuis | 1:09:02 | [▶](https://www.youtube.com/watch?v=uQ2M6ZVzOb8) |
| TPS and quantitative mechanistic hypothesis testing | Baron Peters (IPAM) | 1:09:37 | [▶](https://www.youtube.com/watch?v=_B4ngJdMAzY) |
| Path Sampling and OpenPathSampling | David W. H. Swenson (ENS Lyon) | 1:37:43 | [▶](https://www.youtube.com/watch?v=ys26j1YnERk) |
| ∞RETIS: exchanging replicas with unequal cost | Titus S. van Erp (NTNU) | 36:21 | [▶](https://www.youtube.com/watch?v=7wqzFTQCiYI) |
| Forward Flux Sampling | Sapna Sarupria (Minnesota) | 23:08 | [▶](https://www.youtube.com/watch?v=SOwMzq7um8I) |
| Introduction to Weighted Ensemble Simulation | Daniel M. Zuckerman (OHSU) | 31:14 | [▶](https://www.youtube.com/watch?v=EMZu-n4WCH0) |
| Recent Advances in Weighted Ensemble Simulation | Daniel M. Zuckerman | 35:59 | [▶](https://www.youtube.com/watch?v=ICQWQDBz87g) |
| Weighted ensemble simulations of long-timescale dynamics | Lillian T. Chong (Pittsburgh) | 56:39 | [▶](https://www.youtube.com/watch?v=jdECtI1KTEo) |
| Introduction to WESTPA | Matthew C. Zwier | 48:44 | [▶](https://www.youtube.com/watch?v=YpltPzpcmLY) |
| **Rare Events: Theory** | Eric Vanden-Eijnden (Courant/NYU) | 59:53 | [▶](https://www.youtube.com/watch?v=spKvY1rKT9I) |
| **Rare Events: Numerical Implementation (string method)** | Eric Vanden-Eijnden | 1:08:10 | [▶](https://www.youtube.com/watch?v=66JqXJv2u0E) |
| Exploring Complex Reaction Pathways I (string with swarms) | Mahmoud Moradi (Arkansas) | 1:24:20 | [▶](https://www.youtube.com/watch?v=68qbwQyz5WY) |
| Adaptive multilevel splitting for molecular dynamics | Arnaud Guyader (Sorbonne) | 1:05:08 | [▶](https://www.youtube.com/watch?v=TcnWEFupXPw) |
| Modeling Transition States (NEB / CI-NEB) | Shyue Ping Ong (UCSD) | 37:10 | [▶](https://www.youtube.com/watch?v=YFNqq3XUGB4) |
| Lecture 14: The Committor Function | Pietro Faccioli (Milano-Bicocca) | 37:29 | [▶](https://www.youtube.com/watch?v=FPlzOpl_R4c) |

The committor is the exact reaction coordinate — the probability of reaching
the product before the reactant — and every collective variable anyone has ever
hand-picked is an approximation to it. Faccioli's lecture is short and it
reframes the entire enhanced-sampling enterprise.

*Milestoning has no free video lecture. Read Faradjian & Elber 2004 and Elber
2020.*

---

## C.5 Monte Carlo meets machine learning — the live frontier

**This is the most important subsection in Atlas C for someone trying to make a
contribution**, because the exchange is happening right now and is incomplete.

| Title | Speaker | Length | Link |
|---|---|---|---|
| ML for Sampling Probability Distributions in Lattice Field Theory | Phiala Shanahan (MIT) | 1:05:34 | [▶](https://www.youtube.com/watch?v=9kLxWTVwShQ) |
| Building symmetries into generative flow models | Phiala Shanahan | 1:11:50 | [▶](https://www.youtube.com/watch?v=CafVsQ7yodY) |
| Normalizing Flows for Lattice Gauge Theory, Part 1 | Gurtej Kanwar (Bern) | 1:32:03 | [▶](https://www.youtube.com/watch?v=Twod0mnNTQI) |
| Towards Flow-based MCMC for Lattice Gauge Theory with Fermions | Danilo Rezende (DeepMind) | 1:16:22 | [▶](https://www.youtube.com/watch?v=n9jyJr6gBo8) |
| **Boltzmann Generators** | Frank Noé (FU Berlin / MSR) | 22:39 | [▶](https://www.youtube.com/watch?v=WuXJRswYIaA) |
| Deep Generative Learning for Physics Many-Body Systems | Frank Noé (IPAM) | 1:01:56 | [▶](https://www.youtube.com/watch?v=XhAP2VNPVhg) |
| Stochastic Normalizing Flows | Frank Noé | 15:58 | [▶](https://www.youtube.com/watch?v=B2XT0Yyt_JA) |
| Equivariant flow matching | Leon Klein (FU Berlin) | 1:08:07 | [▶](https://www.youtube.com/watch?v=xaisDpCof9I) |
| **Flow Annealed Importance Sampling Bootstrap** | Midgley & Stimper | 1:33:26 | [▶](https://www.youtube.com/watch?v=xQQXvOWu9nE) |
| Generalizing HMC with Neural Networks (L2HMC) | Jascha Sohl-Dickstein (Google Brain) | 46:55 | [▶](https://www.youtube.com/watch?v=H1o6SJ1ovUw) |
| Enhancing MCMC with Deep Learning | Eric Vanden-Eijnden (Courant) | 46:05 | [▶](https://www.youtube.com/watch?v=J8oSJkYvRHU) |
| **Adaptive Monte Carlo with Normalizing Flows** | Marylou Gabrié (NYU/Flatiron) | 1:00:37 | [▶](https://www.youtube.com/watch?v=urYu8M_6W38) |
| Diffusion models for sampling | Arnaud Doucet (Oxford/DeepMind) | 42:43 | [▶](https://www.youtube.com/watch?v=AUjzhfPdrVM) |
| Non-equilibrium transport and tilt matching for sampling | Michael Albergo (Harvard/NYU) | 38:53 | [▶](https://www.youtube.com/watch?v=0hxaendCWLc) |

**Watch Gabrié and Vanden-Eijnden as a pair.** They explain why a learned global
proposal plus a local MCMC kernel beats either alone, and — crucially — they
name the mode-collapse failure mode honestly. The lattice field theory community
(Shanahan, Kanwar, Rezende) has been doing flow-based sampling with exactness
guarantees for years, largely unread by the biomolecular community.

**FAB is the one to study for a design application.** It trains a flow on a
Boltzmann target *with no samples, only an energy function* — which is precisely
the situation for any designed protein that does not exist yet.

---

## C.6 Quantum and Bayesian Monte Carlo

| Title | Speaker | Length | Link |
|---|---|---|---|
| Introduction to Monte Carlo | David Ceperley (UIUC) | 1:03:42 | [▶](https://www.youtube.com/watch?v=V7JaQXDnKWw) |
| Variational Monte Carlo | David Ceperley | 57:17 | [▶](https://www.youtube.com/watch?v=9qP_sYHnHzQ) |
| Diffusion Monte Carlo, Part 1 | David Ceperley | 54:54 | [▶](https://www.youtube.com/watch?v=ktXWE8TF3OI) |
| Natural QMC Computation of Excited States (FermiNet) | David Pfau (DeepMind) | 25:39 | [▶](https://www.youtube.com/watch?v=LejqfvskG2g) |
| Neural-network wave functions for quantum chemistry (PauliNet) | Jan Hermann (FU Berlin/MSR) | 50:41 | [▶](https://www.youtube.com/watch?v=O-wWPtpk5Jg) |
| Approximating Many-Electron Wave Functions using Neural Networks | Matthew Foulkes (Imperial) | 50:02 | [▶](https://www.youtube.com/watch?v=h-byFNFq4vw) |

### Bayesian computation and diagnostics

| Title | Speaker | Length | Link |
|---|---|---|---|
| Statistical Rethinking 2023 Lec 08: MCMC | Richard McElreath (MPI-EVA) | 1:16:17 | [▶](https://www.youtube.com/watch?v=rZk2FqX2XnY) |
| **BDA Lec 5.2: Convergence diagnostics, R-hat and ESS** | Aki Vehtari (Aalto) | 37:39 | [▶](https://www.youtube.com/watch?v=BsjhKYFH1ms) |
| BDA Lec 6.1: HMC, NUTS, dynamic HMC and diagnostics | Aki Vehtari | 49:59 | [▶](https://www.youtube.com/watch?v=FYliDjeYuXg) |
| A Few of My Favorite Diagnostics | Aki Vehtari (PyMCon) | 58:54 | [▶](https://www.youtube.com/watch?v=HKPm6txxxQM) |
| Practical pre-asymptotic diagnostic of Monte Carlo estimates | Aki Vehtari | 50:14 | [▶](https://www.youtube.com/watch?v=uIojz7lOz9w) |
| PSIS-LOO and K-fold cross-validation | Aki Vehtari | 50:50 | [▶](https://www.youtube.com/watch?v=D0kVMie93Yk) |
| **Bayesian Workflow** | Andrew Gelman (Columbia) | 1:02:48 | [▶](https://www.youtube.com/watch?v=hLeYPhgiuzg) |
| Problems I'd like to solve in Stan | Andrew Gelman | 36:14 | [▶](https://www.youtube.com/watch?v=_RTHFTDJImg) |
| How does Stan work? | Bob Carpenter (Flatiron) | 55:47 | [▶](https://www.youtube.com/watch?v=CAdX2PNz1iM) |
| Debugging Bayesian Inference | PyMC Labs | 54:41 | [▶](https://www.youtube.com/watch?v=HCyVOs0Z2vA) |
| The state of Bayesian workflows in JAX | Colin Carroll (Google) | 31:14 | [▶](https://www.youtube.com/watch?v=b0_D0BxPYLo) |

**Vehtari's two BDA lectures are the ones that justify the R-hat and ESS numbers
you will otherwise copy blindly.** The molecular simulation community has no
equivalent of rank-normalized R-hat, and importing it is a small, concrete,
immediately useful contribution available to anyone who watches these two hours.

---

## C.7 BUILD — Atlas C

1. **Implement Metropolis for a 2D Ising model.** Verify detailed balance
   numerically. Measure the autocorrelation time as you approach the critical
   temperature and watch critical slowing down happen.
2. **Implement the Wolff cluster algorithm** on the same system. Measure the
   autocorrelation time again. The speedup is the lesson.
3. **Implement HMC** for a 2D Gaussian with strong correlation. Tune the step
   size and trajectory length. Then implement NUTS and observe what the
   automatic tuning buys you.
4. **Compute R-hat and effective sample size** for one of your own production MD
   trajectories, treating independent replicas as chains. Most MD papers would
   fail this test. See whether yours does.
5. **The research exercise.** Characterize the stationary distribution of a
   Rosetta fixed-backbone design run empirically: run it many times from the same
   input, histogram the sequences, and compare to the Boltzmann distribution of
   the score function at the annealing temperature. Write up the discrepancy.
   Nobody has published this carefully.

**Derivation checkpoints due: 11, 12, 13, 14, 15, 16.**

---

## C.8 Paired reading — Atlas C

| Watch this | Then read this | Hold this question |
|---|---|---|
| Krauth Lec 1 | Metropolis et al. 1953 | Derive the acceptance ratio. Where does the normalizing constant cancel? |
| Krauth Lec 8 | Swendsen & Wang 1987; Wolff 1989 | Why does a cluster move beat a single-spin flip near criticality? |
| Krauth Lec 9 | Bortz, Kalos & Lebowitz 1975 | Rejection-free MC changes the time variable. What is the new clock? |
| Krauth Tutorial 8 | Propp & Wilson 1996 | Coupling from the past terminates with an exact sample. How? |
| Krauth, *Irreversible Markov chains* | Bernard, Krauth & Wilson 2009; Michel et al. 2014 | These violate detailed balance deliberately. What replaces it? |
| MacKay Lec 12 | MacKay, *Information Theory*, ch. 29–30 | Why do importance and rejection sampling fail in high dimension? |
| Murray, *MCMC* | Neal 1993, *Probabilistic Inference Using MCMC* | What exactly does burn-in fix, and what does it not? |
| Vats, *Gentle Introduction* | **Vats, Flegal & Jones 2019, *Biometrika* 106:321** | Compute a defensible ESS for your own trajectory. |
| **Neal, *HMC*** | **Neal 2011, *Handbook of MCMC* ch. 5** | HMC is MD as a proposal. What does the Metropolis step correct for? |
| Betancourt, Part 1 | Betancourt 2017, arXiv:1701.02434 | Why does HMC work geometrically, and when does it fail? |
| Hoffman, *NUTS* | Hoffman & Gelman 2014, *JMLR* 15:1593 | What does the no-U-turn criterion detect? |
| Skilling, *Computing Bayes* | Skilling 2006, *Bayesian Analysis* 1:833 | Nested sampling computes the evidence. That is a partition function. Why does nobody say so? |
| Landau, *Wang-Landau* | Wang & Landau 2001, *PRL* 86:2050 | It converges to the density of states. What is the protein-design analogue? |
| Bonomi, *Tempering and REX* | Sugita & Okamoto 1999; Marinari & Parisi 1992 | Derive the replica-count scaling. Why is it fatal for large systems? |
| Weitzner, *Side-chain packing* | Desmet et al. 1992; Dunbrack & Karplus 1993 | DEE is exact; annealing is not. Why does production use annealing? |
| RosettaCommons, *MC with minimization* | Li & Scheraga 1987; Rohl et al. 2004 | Minimization inside a MC move breaks detailed balance. What is sampled instead? |
| Gillespie, his own algorithm | **Gillespie 1977, *J Phys Chem* 81:2340** | Why is SSA exact where an ODE is not? |
| Kratzer, *Kinetic Monte Carlo* | Voter 2007 | kMC needs a rate catalogue. Who supplies it, and what if it is incomplete? |
| Bolhuis, *TPS* | **Dellago, Bolhuis, Csajka & Chandler 1998, *JCP* 108:1964** | TPS samples trajectory space. What is the measure on that space? |
| Faccioli, *Committor* | Bolhuis et al. 2002, *Annu Rev Phys Chem* 53:291 | The committor is the exact reaction coordinate. Why can we never compute it? |
| Vanden-Eijnden, *Rare Events: Theory* | E & Vanden-Eijnden 2006, *J Stat Phys* 123:503 | What does transition path theory add beyond sampling paths? |
| Sarupria, *Forward Flux Sampling* | Allen, Warren & ten Wolde 2005, *PRL* 94:018104 | FFS needs no equilibrium. When is that decisive? |
| **Noé, *Boltzmann Generators*** | **Noé, Olsson, Köhler & Wu 2019, *Science* 365:eaaw1147** | Where does exactness come from, and what is the catch? |
| Noé, *Stochastic Normalizing Flows* | Wu, Köhler & Noé 2020, NeurIPS | Interleaving flow layers and MCMC steps. Why does that help? |
| Midgley & Stimper, *FAB* | Midgley et al. 2023, ICLR | Training on an energy with no samples. Apply this to a designed protein. |
| Gabrié, *Adaptive MC with flows* | **Gabrié, Rotskoff & Vanden-Eijnden 2022, *PNAS* 119:e2109420119** | Global proposal plus local kernel. Why does neither suffice alone? |
| Sohl-Dickstein, *L2HMC* | Levy, Hoffman & Sohl-Dickstein 2018, ICLR | A learned MCMC kernel that stays correct. What constrains the learning? |
| Vehtari, BDA 5.2 | **Vehtari et al. 2021, *Bayesian Analysis* 16(2)** | Apply rank-normalized R-hat to replica MD. Does your ensemble pass? |
| Gelman, *Bayesian Workflow* | Gelman et al. 2020, arXiv:2011.01808 | What would a "simulation workflow" paper look like, by analogy? |
| Carpenter, *How does Stan work?* | Carpenter et al. 2017, *JSS* 76(1) | Constrained-to-unconstrained transforms and log-Jacobians. Where do these appear in molecular sampling? |
