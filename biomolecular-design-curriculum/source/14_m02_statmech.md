# B.2 — Statistical Mechanics

## B.2.0 Why this module differentiates you

The field has a large surplus of people who understand transformers and a
shortage of people who understand the Boltzmann distribution well enough to
derive things with it.

Every quantity you care about — a binding affinity, a stability, a population,
a rate — is an ensemble average or a free energy difference. Scoring functions
approximate free energies. Diffusion models learn score functions that are, up
to temperature, forces. Normalizing flows trained to sample equilibrium are the
explicit bridge between the two fields. If you can derive statistical mechanics
rather than recall it, the entire generative-model literature reads differently:
you see the physics hiding inside machine learning papers, which is exactly the
vantage point from which the cross-cultural carries become visible.

Roughly 100 hours if you do all three courses. Worth every one.

---

## B.2.1 MIT 8.333 — Statistical Mechanics of Particles
**Mehran Kardar (MIT)** · 26 lectures · ~36 hours · Tier A

The canonical graduate course, and the exact language in which partition
functions, free energies and every MD and Monte Carlo estimator are written.
**Do the problem sets** — OCW has them with solutions, and a statistical
mechanics course without problem sets is entertainment rather than training.

### Unit I — Thermodynamics
| # | Lecture | Length | Link |
|---|---|---|---|
| 1 | Thermodynamics Part 1 | 1:26:25 | [▶](https://www.youtube.com/watch?v=4RX_lpoGRBg) |
| 2 | Thermodynamics Part 2 | 1:23:38 | [▶](https://www.youtube.com/watch?v=EQB2Pw0lWRU) |
| 3 | Thermodynamics Part 3 | 1:23:44 | [▶](https://www.youtube.com/watch?v=JaEqS1ozlHY) |
| 4 | Thermodynamics Part 4 | 1:18:53 | [▶](https://www.youtube.com/watch?v=__tGxUu5BTc) |

### Unit II — Probability
| # | Lecture | Length | Link |
|---|---|---|---|
| 5 | Probability Part 1 | 1:21:30 | [▶](https://www.youtube.com/watch?v=w_I0AkvbWFc) |
| 6 | Probability Part 2 | 1:24:53 | [▶](https://www.youtube.com/watch?v=I_LcUur7quE) |

### Unit III — Kinetic Theory of Gases
| # | Lecture | Length | Link |
|---|---|---|---|
| 7 | Kinetic Theory of Gases Part 1 | 1:18:39 | [▶](https://www.youtube.com/watch?v=BhVyiU_dWps) |
| 8 | Kinetic Theory of Gases Part 2 | 1:15:56 | [▶](https://www.youtube.com/watch?v=8woIHrY6eM0) |
| 9 | Kinetic Theory of Gases Part 3 | 1:25:36 | [▶](https://www.youtube.com/watch?v=t7pTpwMjQ5I) |
| 10 | Kinetic Theory of Gases Part 4 | 1:25:18 | [▶](https://www.youtube.com/watch?v=ybCsMYk5xMg) |
| 11 | Kinetic Theory of Gases Part 5 | 1:22:23 | [▶](https://www.youtube.com/watch?v=QmV7FOXijMo) |

### Unit IV — Classical Statistical Mechanics
| # | Lecture | Length | Link |
|---|---|---|---|
| 12 | Classical Statistical Mechanics Part 1 | 1:25:38 | [▶](https://www.youtube.com/watch?v=ckUyxmwaC5E) |
| 13 | Classical Statistical Mechanics Part 2 | 1:22:35 | [▶](https://www.youtube.com/watch?v=Lt8FtWsq0q0) |
| 14 | Classical Statistical Mechanics Part 3 | 1:25:17 | [▶](https://www.youtube.com/watch?v=tCxonq5r-O8) |

### Unit V — Interacting Particles
| # | Lecture | Length | Link |
|---|---|---|---|
| 15 | Interacting Particles Part 1 | 1:25:42 | [▶](https://www.youtube.com/watch?v=Y59FgktB4uQ) |
| 16 | Interacting Particles Part 2 | 1:22:06 | [▶](https://www.youtube.com/watch?v=TDnfhpAZBqs) |
| 17 | Interacting Particles Part 3 | 1:23:18 | [▶](https://www.youtube.com/watch?v=TSjJlJJ2aoI) |
| 18 | Interacting Particles Part 4 | 1:24:22 | [▶](https://www.youtube.com/watch?v=l2Q31eoy_rY) |
| 19 | Interacting Particles Part 5 | 1:19:18 | [▶](https://www.youtube.com/watch?v=hl4c1P9D8IY) |

### Units VI–VII — Quantum Statistical Mechanics and Ideal Quantum Gases
*Optional for biomolecular work; included for completeness.*

| # | Lecture | Length | Link |
|---|---|---|---|
| 20 | Quantum Statistical Mechanics Part 1 | 1:23:32 | [▶](https://www.youtube.com/watch?v=b1P0hurY6UE) |
| 21 | Quantum Statistical Mechanics Part 2 | 1:23:48 | [▶](https://www.youtube.com/watch?v=34lmLIYpkYQ) |
| 22 | Ideal Quantum Gases Part 1 | 1:20:31 | [▶](https://www.youtube.com/watch?v=hRHzPaDpgu0) |
| 23 | Ideal Quantum Gases Part 2 | 1:23:42 | [▶](https://www.youtube.com/watch?v=8kNP_VWmfFs) |
| 24 | Ideal Quantum Gases Part 3 | 1:23:42 | [▶](https://www.youtube.com/watch?v=FmylhZqFXNk) |
| 25 | Ideal Quantum Gases Part 4 | 1:22:55 | [▶](https://www.youtube.com/watch?v=6rn4q9mv4jQ) |
| 26 | Ideal Quantum Gases Part 5 | 1:21:05 | [▶](https://www.youtube.com/watch?v=6gMgNriK1Nk) |

**The protein-relevant core is lectures 1–19.** Units VI and VII matter only if
you move toward QM/MM or electronic structure. Unit V (interacting particles) is
where the cluster expansion and the mean-field approximation appear, and those
are the ancestors of every implicit-solvent and mean-field DCA method you will
meet later.

---

## B.2.2 V. Balakrishnan — Physical Applications of Stochastic Processes
**NPTEL / IIT Madras** · 29 lectures · ~28 hours · Tier A

**This is the course nobody tells you to watch and the one that pays off most.**
Langevin dynamics, Fokker-Planck and first-passage times derived in full — the
machinery directly beneath thermostats, diffusion coefficients, enhanced-sampling
estimators, *and* the stochastic differential equation formulation of diffusion
models. Watching it before Atlas family N makes that material roughly twice as
legible.

| # | Lecture | Length | Link |
|---|---|---|---|
| 1 | Discrete probability distributions (Part 1) | 1:02:41 | [▶](https://www.youtube.com/watch?v=6x1pL9Yov1k) |
| 2 | Discrete probability distributions (Part 2) | 54:54 | [▶](https://www.youtube.com/watch?v=aK_RZxARlYo) |
| 3 | Continuous random variables | 56:50 | [▶](https://www.youtube.com/watch?v=P6dOawFYLVA) |
| 4 | Central Limit Theorem | 1:00:54 | [▶](https://www.youtube.com/watch?v=3gTBvpppkVc) |
| 5 | Stable distributions | 1:08:37 | [▶](https://www.youtube.com/watch?v=-BzaVD93akQ) |
| 6 | Stochastic processes | 1:00:20 | [▶](https://www.youtube.com/watch?v=FWe5uk5NA5I) |
| 7 | Markov processes (Part 1) | 54:12 | [▶](https://www.youtube.com/watch?v=l4FKjOfF8qs) |
| 8 | Markov processes (Part 2) | 1:02:21 | [▶](https://www.youtube.com/watch?v=YlLiRv18Css) |
| 9 | Markov processes (Part 3) | 52:22 | [▶](https://www.youtube.com/watch?v=CtyVQJ358aU) |
| 10 | Birth-and-death processes | 51:20 | [▶](https://www.youtube.com/watch?v=jkctXp4x43U) |
| 11 | Continuous Markov processes | 57:36 | [▶](https://www.youtube.com/watch?v=hXRMX76V0nM) |
| 12 | **Langevin dynamics (Part 1)** | 57:53 | [▶](https://www.youtube.com/watch?v=IlwG0ZLB2fU) |
| 13 | **Langevin dynamics (Part 2)** | 51:46 | [▶](https://www.youtube.com/watch?v=J-nH26vbgug) |
| 14 | **Langevin dynamics (Part 3)** | 58:39 | [▶](https://www.youtube.com/watch?v=TLjDHHXF6Os) |
| 15 | **Langevin dynamics (Part 4)** | 57:15 | [▶](https://www.youtube.com/watch?v=Zb-7xXmJq3U) |
| 16 | **Itô and Fokker-Planck equations for diffusion processes** | 47:42 | [▶](https://www.youtube.com/watch?v=qnJ4Yt8ku7s) |
| 17 | Level-crossing statistics of a continuous random process | 54:33 | [▶](https://www.youtube.com/watch?v=TG1Jjp8eyvs) |
| 18 | Diffusion of a charged particle in a magnetic field | 59:56 | [▶](https://www.youtube.com/watch?v=GxrLQ2AEhwI) |
| 19 | Power spectrum of noise | 53:38 | [▶](https://www.youtube.com/watch?v=xD3rbUprXrA) |
| 20 | Elements of linear response theory | 1:01:50 | [▶](https://www.youtube.com/watch?v=LQfIiff7A6E) |
| 21 | Random pulse sequences | 57:33 | [▶](https://www.youtube.com/watch?v=e6l_Wq0CMeM) |
| 22 | Dichotomous diffusion | 1:07:31 | [▶](https://www.youtube.com/watch?v=kRbh3Dvi1l4) |
| 23 | **First passage time (Part 1)** | 59:50 | [▶](https://www.youtube.com/watch?v=c_KV_KAEdvY) |
| 24 | **First passage time (Part 2)** | 1:03:14 | [▶](https://www.youtube.com/watch?v=6OZu2S1nEA8) |
| 25 | First passage and recurrence in Markov chains | 1:06:21 | [▶](https://www.youtube.com/watch?v=Tz26OMwyCYw) |
| 26 | Recurrent and transient random walks | 1:11:49 | [▶](https://www.youtube.com/watch?v=JQ2zbhCR4GY) |
| 27 | Non-Markovian random walks | 51:31 | [▶](https://www.youtube.com/watch?v=IFIHGSDMwjE) |
| 28 | Statistical aspects of deterministic dynamics (Part 1) | 54:36 | [▶](https://www.youtube.com/watch?v=qckJgCLHZl4) |
| 29 | Statistical aspects of deterministic dynamics (Part 2) | 1:01:54 | [▶](https://www.youtube.com/watch?v=dqVp2G-rHnI) |

**If you watch only six lectures from this course, watch 12 through 16 and 23.**
Lectures 12–16 give you Langevin through Fokker-Planck in sequence, which is the
derivation that makes thermostats, Brownian dynamics and score-based diffusion
all one subject. Lecture 23 on first-passage time is the theory of rates, and
therefore of every kinetics claim in Atlas family I.

---

## B.2.3 V. Balakrishnan — Nonequilibrium Statistical Mechanics
**NPTEL / IIT Madras** · 36 lectures · ~33 hours · Tier A

The deeper treatment. Fluctuation-dissipation and response theory let you prove
whether a biased simulation still reports equilibrium observables — which is the
question underneath every enhanced-sampling method in Atlas family D.

| # | Lecture | Length | Link |
|---|---|---|---|
| 1 | Recapitulation of equilibrium statistical mechanics | 50:36 | [▶](https://www.youtube.com/watch?v=SjTfNFso4mE) |
| 2 | The Langevin model (Part 1) | 52:25 | [▶](https://www.youtube.com/watch?v=kkqTPl0S4iU) |
| 3 | The Langevin model (Part 2) | 51:20 | [▶](https://www.youtube.com/watch?v=IjCjpoGZG78) |
| 4 | The Langevin model (Part 3) | 57:12 | [▶](https://www.youtube.com/watch?v=RHQB9W5Mxiw) |
| 5 | The Langevin model (Part 4) | 49:57 | [▶](https://www.youtube.com/watch?v=9A1vTwd4LO4) |
| 6 | **Linear response theory (Part 1)** | 47:55 | [▶](https://www.youtube.com/watch?v=iAhb8CeKwnc) |
| 7 | Linear response theory (Part 2) | 51:08 | [▶](https://www.youtube.com/watch?v=6MwuElZDFpQ) |
| 8 | Linear response (Part 3) | 50:24 | [▶](https://www.youtube.com/watch?v=grerei081MA) |
| 9 | Linear response (Part 4) | 49:40 | [▶](https://www.youtube.com/watch?v=yE3ZrcD6is4) |
| 10 | Linear response (Part 5) | 49:05 | [▶](https://www.youtube.com/watch?v=1ERJq_CpYQE) |
| 11 | Linear response (Part 6) | 49:19 | [▶](https://www.youtube.com/watch?v=4z5gdFntl_Y) |
| 12 | Linear response theory (Part 7) | 52:16 | [▶](https://www.youtube.com/watch?v=Cokmqm96DIs) |
| 13 | Quiz 1 — questions and answers | 51:17 | [▶](https://www.youtube.com/watch?v=Dw2hcTtrVuQ) |
| 14 | Linear response theory (Part 8) | 48:23 | [▶](https://www.youtube.com/watch?v=Vnw5ENxCp7Y) |
| 15 | Linear response theory (Part 9) | 56:45 | [▶](https://www.youtube.com/watch?v=Yg-5OVG5Mcw) |
| 16 | The dynamic mobility | 52:21 | [▶](https://www.youtube.com/watch?v=qV25XtQ1Ivc) |
| 17 | **Fokker-Planck equations (Part 1)** | 50:22 | [▶](https://www.youtube.com/watch?v=o5iwZpvtpiE) |
| 18 | Fokker-Planck equations (Part 2) | 52:36 | [▶](https://www.youtube.com/watch?v=d7gzALqU95Y) |
| 19 | Fokker-Planck equations (Part 3) | 1:00:26 | [▶](https://www.youtube.com/watch?v=Be7lHQ90hFM) |
| 20 | **The generalized Langevin equation (Part 1)** | 1:00:14 | [▶](https://www.youtube.com/watch?v=6tmby1Dv4aU) |
| 21 | The generalized Langevin equation (Part 2) | 56:27 | [▶](https://www.youtube.com/watch?v=CI7blNtcqME) |
| 22 | Diffusion in a magnetic field | 51:17 | [▶](https://www.youtube.com/watch?v=mgyJnMhFxns) |
| 23 | The Boltzmann equation for a dilute gas (Part 1) | 57:24 | [▶](https://www.youtube.com/watch?v=hJt9VWTSSyM) |
| 24 | The Boltzmann equation for a dilute gas (Part 2) | 54:58 | [▶](https://www.youtube.com/watch?v=eQ2yXWkKks0) |
| 25 | The Boltzmann equation for a dilute gas (Part 3) | 52:12 | [▶](https://www.youtube.com/watch?v=kmY8lecGJq8) |
| 26 | The Boltzmann equation for a dilute gas (Part 4) | 56:23 | [▶](https://www.youtube.com/watch?v=cSBwopamRMM) |
| 27 | The Boltzmann equation for a dilute gas (Part 5) | 53:51 | [▶](https://www.youtube.com/watch?v=rWztVWNVeeg) |
| 28 | Quiz 2 — questions and answers | 59:06 | [▶](https://www.youtube.com/watch?v=s0-Oyj7rhuc) |
| 29 | Critical phenomena (Part 1) | 1:06:56 | [▶](https://www.youtube.com/watch?v=1XBKV1pU-mA) |
| 30 | Critical phenomena (Part 2) | 1:03:44 | [▶](https://www.youtube.com/watch?v=9R0tR6DC6Z0) |
| 31 | Critical phenomena (Part 3) | 1:04:57 | [▶](https://www.youtube.com/watch?v=hLoneUTGi28) |
| 32 | Critical phenomena (Part 4) | 57:26 | [▶](https://www.youtube.com/watch?v=83AmY13yvWY) |
| 33 | Critical phenomena (Part 5) | 1:00:27 | [▶](https://www.youtube.com/watch?v=RFKb4uJj4LE) |
| 34 | Critical phenomena (Part 6) | 51:11 | [▶](https://www.youtube.com/watch?v=QFKeDcy_z8w) |
| 35 | Critical phenomena (Part 7) | 53:47 | [▶](https://www.youtube.com/watch?v=SL3jyu_FFMI) |
| 36 | **The Wiener process (standard Brownian motion)** | 1:03:10 | [▶](https://www.youtube.com/watch?v=tdgnWgTfZnQ) |

**Lecture 20, the generalized Langevin equation, is the one to mark.** It
contains the memory kernel — the term that coarse-grained models almost always
discard, and whose discarding is why coarse-grained dynamics is wrong even when
coarse-grained structure is right. That is derivation checkpoint 29 and it is
the theoretical heart of Atlas family F.

---

## B.2.4 Supporting courses

| Course | Instructor | Scale | Link |
|---|---|---|---|
| Statistical Mechanics (Theoretical Minimum) | Leonard Susskind (Stanford) | 10 × ~2 hr | [Playlist](https://www.youtube.com/playlist?list=PL177B242D4104DCC5) |
| MIT 5.60 Thermodynamics & Kinetics | Nelson & Bawendi (MIT) | 36 × 50 min | [OCW](https://ocw.mit.edu/courses/5-60-thermodynamics-kinetics-spring-2008/video_galleries/video-lectures/) |
| MIT 8.334 Statistical Mechanics II: Fields | Mehran Kardar | 26 lectures, 35 hr | [Playlist](https://www.youtube.com/playlist?list=PLUl4u3cNGP63HkEHvYaNJiO0UCUmY0Ts7) |
| Statistical Mechanics: Algorithms and Computations | Werner Krauth (ENS Paris) | 10 modules | [Coursera, free audit](https://www.coursera.org/learn/statistical-mechanics) |
| Physical Biology of the Cell | Rob Phillips (Caltech) | 100 videos | [Playlist](https://www.youtube.com/playlist?list=PLVA3Onuu1UMAzuqbD5PiCZ3tKUDtxqTab) |
| Statistical Mechanics of Soft Matter | Jonathan Selinger (Kent State) | 41 videos | [Playlist](https://www.youtube.com/playlist?list=PL7B_29ynGKv3v81zK9C9AcTNtGDCvbojV) |
| Nonequilibrium Physics: Stochastic Dynamics & Field Theories | LMU Munich, SS 2025 | 40 videos, 30 hr | [Playlist](https://www.youtube.com/playlist?list=PL2IEUF-u3gRdSbgtuqH5RNTuT798s0GqX) |
| Brownian Motion and Stochastic Differential Equations | K. Hlyniana | 10 lectures, 13 hr | [Playlist](https://www.youtube.com/playlist?list=PL0LYPHnhlRgcQ7IP7APWI50U8BiPe3_Xt) |
| Large Deviation Theory in Statistical Physics | ICTS program (Touchette, Mallick, Lelièvre) | 66 talks, 57 hr | [Playlist](https://www.youtube.com/playlist?list=PL04QVxpjcnjjs7dEO4LY_GZ48peTG1drT) |

**Krauth is the one to do if you only do one computational item** — Monte Carlo,
detailed balance and sampling implemented in downloadable Python by someone who
thinks carefully about correctness. **The LMU nonequilibrium course is the
modern path-integral treatment** and is the right language for score-based and
flow-matching generative models of conformations; it is the most direct bridge
in this module to Atlas family N.

---

## B.2.5 Statistical honesty: the Zuckerman thread

Daniel Zuckerman is the field's conscience on convergence and error estimation.
His best material is **text rather than video**, which is unusual in this
curriculum and worth accommodating rather than working around.

| Resource | Type | Link |
|---|---|---|
| Introduction to Weighted Ensemble Simulation | video, 31 min | [▶](https://www.youtube.com/watch?v=EMZu-n4WCH0) |
| Recent Advances in Weighted Ensemble Simulation | video, 36 min | [▶](https://www.youtube.com/watch?v=ICQWQDBz87g) |
| Simple trajectory physics for path sampling and improving Markov models | video, 33 min | [▶](https://youtu.be/zIMX8NotwQg) |
| **Physical Lens on the Cell** | free online book | [physicallensonthecell.org](https://www.physicallensonthecell.org/) |
| **Basic Nonequilibrium Physics** | free online book | [OSF](https://osf.io/9yq2n/) |
| Statistical Biophysics Blog | articles with exercises | [statisticalbiophysicsblog.org](http://statisticalbiophysicsblog.org/) |

---

## B.2.6 BUILD — Module B.2

1. **Derive the Boltzmann distribution** from maximum entropy under a mean-energy
   constraint. State precisely what temperature is in that derivation.
2. **Implement Metropolis Monte Carlo** for a 2D Ising model. Verify detailed
   balance numerically. Measure the heat capacity and locate the transition.
3. **Implement a Langevin integrator** for a 1D double well. Measure populations
   against analytic Boltzmann weights. Then deliberately break the
   fluctuation-dissipation relation — change friction without changing noise —
   and watch the thermodynamics go wrong.
4. **Error estimation.** For item 3, implement block averaging and compute a
   correlation time. Produce an honest error bar. Then answer Zuckerman's
   question: how would you know if this were not converged?
5. **The bridge exercise.** Write the Fokker-Planck equation for your Langevin
   system. Then write the reverse-time SDE of a diffusion model. Identify every
   corresponding term. Keep this page; you will need it in Atlas family N.

**Derivation checkpoints due: 7, 29, 36, 37.**

---

## B.2.7 Paired reading — Module B.2

| Watch this | Then read this | Hold this question |
|---|---|---|
| Kardar Units I–II | Any text on ensemble equivalence | When do canonical and microcanonical disagree, and does it ever matter for a protein? |
| Kardar Unit IV | Zwanzig 1954 | FEP is exact. Why does it fail in practice, and what quantity governs the failure? |
| Kardar Unit V (interacting particles) | Any implicit-solvent or mean-field DCA paper | Both are mean-field approximations. What exactly is being averaged over? |
| Balakrishnan SP 12–16 | Any Langevin thermostat paper | Which thermostats preserve correct dynamics, and which only the correct distribution? |
| Balakrishnan SP 23–24 | Kramers 1940 | Derive the rate from first-passage theory. Where does the barrier height enter? |
| Balakrishnan NESM 6–12 | Any Green-Kubo derivation | Transport coefficients from equilibrium fluctuations — what is the protein analogue? |
| **Balakrishnan NESM 20–21** | Mori-Zwanzig formalism; any coarse-graining paper | The memory kernel is what CG models discard. What does discarding it cost? |
| Balakrishnan NESM 36 | Any SDE text on Wiener processes | Write the Wiener process. Now write the forward diffusion of a DDPM. Compare. |
| Krauth, *Algorithms and Computations* | Metropolis et al. 1953 | Detailed balance is sufficient but not necessary. What is necessary? |
| LMU nonequilibrium course | Song et al. 2021, *Score-based generative modeling through SDEs* | The field theory and the generative model use the same formalism. Map the terms. |
| Zuckerman, weighted ensemble | Zuckerman & Chong 2017 | WE is unbiased. What exactly does that mean, and what is still not guaranteed? |
| Zuckerman, any talk | **Grossfield & Zuckerman 2009** | Read before publishing any simulation. Which of its tests does your workflow pass? |
| Phillips, *Physical Biology of the Cell* | Any MWC allostery paper | Allostery as a two-state model — could a design method target that directly? |
