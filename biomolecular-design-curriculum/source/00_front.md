# The Biomolecular Design Curriculum

### Third Edition — every computational method for proteins, DNA and RNA, the AI research upstream of it, and the engineering that makes it fast

**A self-study curriculum** · Compiled October 2026

---

## 0.1 What changed, and why

### From the first edition to the second

The first edition was a six-month survey, and it was too coarse in three ways.

**It pointed at playlists instead of lectures.** A link to a 71-video course is
not a curriculum; it is a deferral of the actual work of deciding what to watch
and in what order. The second edition enumerates individual lectures with titles
and runtimes, so that every study session has a specific named target.

**It was thin on applications.** It named the major design methods but did not
treat them individually. Most significant methods now get their own entry with a
recorded talk — preferably by a first author — paired with the exact paper that
talk narrates.

**It was missing entire method families.** Coarse-graining, Monte Carlo in all
its forms, Brownian and Langevin dynamics, polymer theory, normal modes and
elastic networks, continuum electrostatics, docking, QM/MM, machine-learned
interatomic potentials, the reconstruction algorithms behind cryo-EM and
crystallography, integrative modeling, sequence and evolutionary algorithms.
These are now organized as a **Method Atlas** aimed at the whole space rather
than the fashionable corner of it.

### From the second edition to this one

The second edition was audited against its own claims, and it failed several.
This edition is the repair.

**It had, in about ten places, done the exact thing it criticized.** Jeffrey
Gray's course, the PLUMED Masterclass, the forty-three-talk free energy
workshop, the geometric deep learning courses — all referenced as important and
all left as bare playlist links. They are enumerated now.

**Three Atlas families were reading lists rather than video sections.**
Continuum and mesoscale methods had zero lectures, integrative modeling had
four, free energy had six. Those are filled.

**RNA was badly under-served** despite Rhiju Das being one of the ten scientists
the document is built around. The secondary-structure algorithms, chemical
probing, ribozymes, riboswitches and RNA design now get proper treatment, along
with an evidence-based answer to why RNA structure prediction trails protein
structure prediction.

**The cross-references were broken.** Capstone numbers cited throughout Parts II
and III pointed at projects that did not match what Part V defined, and one
referenced a capstone that did not exist. All eleven are now named, specified,
and reachable from the family that cites them.

**Performance engineering was absent entirely** — and that was the largest gap.
Part IV is new, and it exists because making molecular computation faster is a
genuine source of original contribution, not plumbing. Anton was an ASIC.
FlashAttention introduced no new mathematics. ColabFold's speedup came from
replacing the sequence search, not the network. The open problems in this area
are unusually tractable for one person with a few GPUs.

**Two things are now generated rather than written**, so they cannot drift out
of date: the runtime budget in Section 0.9 and the index in Appendix D, both
rebuilt from the assembled text on every build.

**On what is deliberately not here.** There is no wet-lab or experimental
protocol module. The measurement side appears only where it changes how you read
a number — what a deep mutational scan actually reports, what an SEC trace
means, why a stability dataset is skewed toward destabilizing mutations. That is
a scoping decision, not an oversight.

---

## 0.2 The central thesis, unchanged

The ten scientists this curriculum is built around — David Baker, Possu Huang,
Tanja Kortemme, Phil Bradley, John Jumper, David E. Shaw, Greg Bowman, Pranam
Chatterjee, Daniel Zuckerman, Rhiju Das — do not practice a single discipline.
They practice three that share a subject matter and disagree, quietly and
politely, about what counts as truth.

**Culture One — Physics-first.** *Shaw, Zuckerman, Bowman; historically Karplus
and Levitt.* The ground truth is the Boltzmann distribution. A molecule is a
high-dimensional energy landscape and the problem is sampling it correctly. A
method is judged on whether it is **statistically correct**: does it converge, is
it unbiased, what is the error bar. The cardinal sin is an unconverged result.
The weakness is that a perfectly converged simulation of a slightly wrong
Hamiltonian is a perfectly converged wrong answer.

**Culture Two — Engineering-first.** *Baker, Kortemme, Huang, Bradley, and the
Rosetta community.* The ground truth is the tube. A method is judged on whether
the thing it designs **folds, binds or catalyzes when made**. Energy functions are
empirical scoring devices with free parameters fit to whatever makes designs
work. Success rate is the metric; the cardinal sin is a beautiful method with no
experimental validation. The weakness is that a function fit to successes
explains very little about the failures.

**Culture Three — Learning-first.** *Jumper, Chatterjee, modern Das, and nearly
every group founded after 2020.* The ground truth is the data distribution. The
PDB is a sample and the problem is to learn it well enough to generalize. A
method is judged on **held-out benchmark performance**; the cardinal sin is test
set leakage. The weakness is that a model which interpolates the PDB has no
defined behavior off the manifold of natural proteins — which is exactly where
design lives.

A fourth culture supplies the ground truth all three depend on: **the
experimentalists**, whose deep mutational scanning, display technologies,
cryo-EM and high-throughput biochemistry turn design into data.

### Why this is the organizing principle

Nearly every major methodological advance of the last fifteen years came from
someone **carrying an idea across one of these boundaries.**

| Advance | Imported from | Into | What the carry accomplished |
|---|---|---|---|
| Markov state models | Learning (clustering, Markov chains) | Physics | Short trajectories became long-timescale kinetics |
| Replica exchange | Physics (tempering) | Engineering (Rosetta sampling) | Escaped local minima in design search |
| Rosetta energy refits (REF15) | Physics (explicit solvation, electrostatics) | Engineering | A more transferable empirical function |
| AlphaFold2 triangle attention | Physics (geometric consistency) | Learning | The right inductive bias for distances |
| Boltzmann generators | Learning (normalizing flows) | Physics | Equilibrium sampling with no trajectory |
| ProteinMPNN | Learning (graph neural networks) | Engineering | A learned packer replacing a hand-tuned one |
| RFdiffusion | Learning (denoising diffusion) | Engineering | Backbone generation became a sampling problem |
| Deep mutational scanning as supervision | Experiment (high-throughput assays) | Learning | A non-PDB training signal |
| Cryptic pocket discovery | Physics (enhanced sampling) | Engineering (drug design) | Druggable sites no structure showed |
| cryoDRGN / 3DFlex | Learning (latent variable models) | Experiment (cryo-EM) | Continuous ensembles from particle stacks |
| Machine-learned force fields | Learning (equivariant networks) | Physics | Near-QM accuracy at MM cost |
| AlphaFold-derived ensembles | Learning | Physics | Conformational states without simulation |
| GFlowNets | Learning (RL/flow networks) | Design | Sampling diverse high-reward sequences |

Read that table as a job description. **Your contribution, when it comes, will
most likely be an unexchanged idea** — something routine in one of these cultures
that nobody has yet carried into another. The Method Atlas in Part II exists to
give you the complete inventory of what each culture already knows, because you
cannot notice a missing exchange between fields you have only surveyed.

---

## 0.3 How this document is organized

**Part I — Foundations.** The mathematics, physics, computer science, chemistry
and experimental grounding. Enumerated lecture by lecture. This is the part that
does not go out of date.

**Part II — The Method Atlas.** The core of this edition. Every family of
computational method for proteins, DNA and RNA, organized by what problem it
solves rather than by who invented it. Each family gets: the problem statement,
theory lectures, practical lectures, canonical papers, the software that
implements it, and the open problems in it.

**Part III — Upstream AI Research.** Vision, architecture research, training
at scale, post-training and reinforcement learning, reasoning, deep learning
theory, and interpretability — the literature that produces the ideas Part II
inherits two years later. It closes with fourteen specific transfers between the
two fields, in both directions.

**Part IV — Performance Engineering.** How molecular computation actually gets
fast: GPU and kernel programming, accelerators and compilers, the internals of
simulation engines, and the systems engineering of structure-prediction models.
This part exists because making something ten times faster is a real
contribution and is treated in most curricula as if it were plumbing. It is not.
Anton is a hardware-software codesign result; FlashAttention is an algorithm
with no new mathematics; ColabFold's speedup came from replacing the search, not
the network. **The open problems here are unusually tractable for one person
with a few GPUs.**

**Part V — Contribution.** Sixty-three derivation checkpoints, ten capstone
projects, the five generators by which new methods actually get invented, and
the permanent seminar diet.

**Part VI — Appendices.** The standing archives enumerated talk by talk
(Appendix A), the ten named courses enumerated lecture by lecture (B), an honest
register of what is missing from the public record (C), the progress tracker (D),
and a generated index of every method, model and package in the document (E).

---

## 0.4 Conventions

Every entry gives what it can verify and flags what it cannot.

- **Lecture tables** list individual videos: number, exact title, runtime, link.
  Where a course has natural units, that structure is preserved.
- **Tier tags** indicate how to watch: **A** foundation (work it, with problem
  sets), **B** method (reimplement it), **C** talk (interrogate it, watch the
  Q&A), **D** cultural (context and taste, 2x, no notes).
- **Atlas entries** follow a fixed shape: *Problem · Theory · Practice · Papers ·
  Software · Open*.
- **Talk+paper pairs** give the recorded talk and the exact paper it narrates.
- Items that could not be verified are marked **[unverified]** with a search
  string rather than given a possibly-dead link. Known absences are recorded in
  Appendix D rather than silently omitted — a gap in the public record is
  information too.

Runtimes and lecture counts were read from live pages at compile time, not
estimated. They drift; the titles are the durable identifier.

---

## 0.5 The pairing principle

The organizing device of this curriculum is that **no talk stands alone.** Each
significant video is paired with the specific paper it narrates, consumed as a
unit, in a fixed order, with a specific question held in mind.

Video and text fail in opposite directions and the failures cancel. A **talk**
gives you the author's own sense of which part was hard — almost never what the
paper's structure suggests — the motivation that was true at the time rather
than the one reverse-engineered for publication, and the Q&A, where objections
are voiced by people under no obligation to be diplomatic. A **paper** gives you
the precise claim with its conditions and error bars, and the methods section,
where the thirty undocumented decisions that make it work are hiding.

> **Watch first, read second, then write the gap.**
>
> 1. Watch at the tier-appropriate speed. Take the three-line note: claim,
>    evidence, what-would-make-this-wrong.
> 2. Read the paper properly, methods section included.
> 3. Write two or three sentences on **what the paper contains that the talk
>    omitted, and what the talk said that the paper does not.**

Step three takes five minutes and is the entire point. That delta is composed of
things that are true, known to practitioners, and unpublishable: failure modes,
the hyperparameter that matters more than the architecture, the dataset quirk,
the reviewer who demanded a figure that obscured the result. After forty of
these you will notice the same gaps recurring within a research group, which is
what it feels like to understand a culture from the inside.

---

## 0.6 How to watch, by tier

**Tier A — foundations.** Watch at 1x with a notebook. Pause before every
derivation and attempt the next step. Afterward, close everything and write the
central result from memory. Do the problem sets; a statistical mechanics course
without them is entertainment. One lecture per sitting.

**Tier B — methods.** Watch once at 1.25x for the shape of the idea. Write one
paragraph on what problem it solves and what it assumes — if you cannot state the
assumption you did not understand it. Implement the smallest possible version
from scratch before looking at the real code. Then read the real implementation
and catalog every difference; the differences are the accumulated scar tissue of
what does not work.

**Tier C — talks.** Watch at 1.5x. Three lines: claim, evidence, falsifier.
**Watch the Q&A, always** — it is where real disagreements surface and the part
everyone skips. Log every open problem a speaker names as unsolved.

**Tier D — cultural.** 2x, no notes. The purpose is knowing who the field is and
what it has already tried and abandoned, which is what stops you spending a year
reinventing something that failed in 2009 for reasons nobody published.

### The three numbers

Monthly, record: **lines added to the open-problems file** (should grow 20–40 a
month), **derivation checkpoints completed unaided**, and **things you built that
run**. If video hours are high and these are flat, stop watching and start
building.

---

## 0.7 Suggested orderings

There is no single correct path through a multi-year reference. Four that work:

**The physics-deficit path** (likeliest fit given your background). Part I
mathematics and statistical mechanics at full depth, then Atlas families A
through I in order, then Part III. You already run the tools; this makes you
able to derive them.

**The learning-first path.** Part I mathematics and CS, Atlas N (deep learning
for molecules), then O, P, Q, then back-fill A through I as each becomes
necessary. Faster to the frontier, weaker foundations, and you will feel the gap
the first time a reviewer asks about convergence.

**The atlas-sweep path.** Read every Atlas entry's *Problem* and *Open* sections
first — perhaps forty pages — before watching anything. This gives you the map of
the whole field in a week and lets you choose where to go deep. **This is the
recommended first move regardless of which path you then take.**

**The depth-first path.** Pick one Atlas family, watch everything in it, read
every paper, do every derivation, build the tool. Then move. Slower, but it
produces genuine expertise in a sub-area rather than uniform competence — and
genuine expertise in one sub-area is what gets you taken seriously.

---

## 0.8 Prerequisites, honestly assessed

This assumes undergraduate chemistry and biology, fluency in Python, the ability
to read a structural biology paper, and practical experience running molecular
dynamics and structure prediction. Based on your project history you have all of
this, and much of the practical content in Atlas families B, E and O will be
review you can accelerate past.

It does not assume, and therefore teaches: measure-theoretic probability at a
working level, statistical mechanics derived rather than recalled, the
mathematics of equivariance, the internals of the deep learning methods you
currently use as tools, and the algorithmic computer science that makes any of
it fast. Those are the gaps between someone who can run RFdiffusion and someone
who could have invented it.
