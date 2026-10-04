# D.10 The Bridge, Concretely

> Part III has been a long argument that the AI literature is worth your time.
> This section makes the argument specific. Below are **fourteen transfers**:
> seven ideas from AI that have a stated, unexploited application in molecular
> modeling, and seven places where the molecular setting has something the AI
> field lacks.
>
> None of these are gestures. Each names the source talk, the source paper, the
> target problem, and what the first experiment would be. **If you want a thesis
> topic, it is in this table.**

---

## D.10.1 Seven ideas to carry into molecules

### 1. μP — hyperparameter transfer across scale

**From:** Greg Yang, *Tuning Large Neural Networks via Zero-Shot Hyperparameter
Transfer* (D.5.3) · Yang et al. 2022, arXiv:2203.03466.
**To:** Every structure-prediction and design model retunes hyperparameters at
every scale, by hand, at enormous cost.
**First experiment:** Derive the μP parameterization for a pair-representation
network. The non-obvious part is the triangle operations, which have no analogue
in a standard transformer. Verify coordinate-scale stability across widths, then
tune a small model and transfer.
**Why it is a contribution and not an application:** the derivation is genuinely
new, because the architecture is.

### 2. Process reward models over generation trajectories

**From:** Lightman et al., *Let's Verify Step by Step* (D.7.4), arXiv:2305.20050.
**To:** Diffusion-based design scores only the final backbone after 50 denoising
steps. There is no intermediate signal.
**First experiment:** Run RFdiffusion, record intermediate states, label them by
the final design's self-consistency outcome, train a model to score partial
trajectories, then resample from bad trajectories early.
**Why it matters:** it converts a fixed-cost generator into one where compute is
allocated adaptively, and it is the exact structure that made reasoning models
work.

### 3. Over-optimization curves for design filters

**From:** Gao, Schulman & Hilton (D.6.1), arXiv:2210.10760.
**To:** Design pipelines optimize against learned proxies — pLDDT, interface
pAE, self-consistency RMSD — with no measurement of where the proxy stops
tracking reality.
**First experiment:** Take a target with experimental data at several
optimization strengths. Plot wet-lab success against filter stringency. Find the
peak.
**Why it matters:** the curve has a maximum, and nobody knows where it is.
Publishing it would immediately change how campaigns are run.

### 4. Ring attention and IO-aware kernels for triangle operations

**From:** Dao, *FlashAttention* (D.5.1); Liu et al., *Ring Attention* (D.4.5).
**To:** Triangle multiplication is the memory bottleneck in every AF3-class
model and the reason large complexes do not fit.
**First experiment:** Write a tiled, recomputation-based triangle-multiplicative
update, then a ring-sharded version across devices. Measure peak memory against
sequence length.
**Why it matters:** this is what makes megabase-scale and large-assembly
modeling feasible on hardware anyone owns.

### 5. DoReMi-style data mixture optimization over protein families

**From:** Sang Michael Xie, *Data-distributional Approaches* (D.5.5),
arXiv:2305.10429.
**To:** Protein models train on whatever UniRef gives them, with mixture weights
nobody chose.
**First experiment:** Train small proxy models, run the DoReMi minimax
reweighting over Pfam clans, and compare downstream performance against uniform
and against size-proportional sampling.
**Why it matters:** it is a reimplementation, but on data where nobody has done
it, and the answer is directly actionable.

### 6. Sparse autoencoders with real ground truth

**From:** D.9 (interpretability) and InterPLM (Atlas Q.4).
**To:** Protein models have thousands of independently-established labels —
catalytic residues, domain boundaries, binding sites, transmembrane spans — that
language has no equivalent of.
**First experiment:** Train SAEs on an MSA Transformer and evaluate recovered
features against Pfam, CATH and catalytic-site annotations. **Report precision
and recall of features against real labels**, which is a thing language
interpretability literally cannot do.
**Why it matters:** this is Capstone VIII and it benefits the AI field more than
the biology field.

### 7. Scaling laws for structure prediction

**From:** Kaplan, Hoffmann, Bahri, Kudugunta (D.5.4).
**To:** Nobody knows the functional form of structure-prediction performance in
data, parameters or compute, which means nobody can say what another 10,000
structures would be worth.
**First experiment:** Subsample the PDB at many fractions, train a fixed
architecture at several sizes, fit the surface. Use Kudugunta's methodology
critique as the checklist.
**Why it matters:** it is the quantitative answer to "should we fund more
structure determination or more compute," and that question is currently decided
by opinion.

---

## D.10.2 Seven things molecules have that AI wants

### 1. Ground truth for interpretability
As above, in reverse: the molecular domain is the best available testbed for
validating interpretability methods, and the AI community does not know it.

### 2. A real distribution shift, with a physical ground truth
Design is extrapolation (Listgarten, Atlas R.10). Unlike most benchmark
distribution shifts, this one can be *checked in the wet lab*. **Conformal
prediction methods have no better evaluation setting anywhere.**

### 3. A hard constraint that cannot be learned away
Physical validity — bond lengths, stereochemistry, clashes — is checkable,
objective and not negotiable. PoseBusters is a model for the kind of validity
check that language generation lacks entirely.

### 4. Symmetry that is genuinely exact
SE(3) equivariance is not an approximation or a modeling convenience. The
equivariance-versus-scale debate (Atlas O.3) can be settled empirically here in
a way it cannot be in vision.

### 5. A blind benchmark with a thirty-year record
CASP. The AI field keeps rediscovering that held-out test sets leak and that
benchmarks saturate. **Structural biology solved this in 1994** and almost no one
outside it knows how, or why the specific design choices mattered.

### 6. Long sequences with real long-range dependencies
A genome's regulatory elements act over megabases. A protein contact can span
the whole chain. These are not synthetic long-context benchmarks — the
dependencies are physical, labeled and verifiable.

### 7. A culture of negative results, in one corner
Enzyme design publishes its failures (Blomberg 2013; Rocklin's *Why designs
fail*). The AI field's analogous literature is thin and recent. **The norm is
transferable and the transfer is free.**

---

## D.10.3 How to actually work the bridge

Three practical habits, in descending order of importance.

**First, keep a standing diet.** One talk a week from Part III, permanently.
Simons Institute, Stanford CS25, EleutherAI reading groups, Valence, ML4PE —
listed in the archives appendix. The point is not to keep up; it is to keep the
vocabulary live so that when a transfer is available you recognize it. **Most
transfers are recognized, not derived.**

**Second, when you read an AI paper, ask the three questions.** What is the
object being modeled? What is the symmetry or constraint being exploited? What is
the metric, and is it the quantity anyone cares about? **The third question is
where most of the transfers in D.10.1 came from**, because the answer in both
fields is usually no.

**Third, publish in both directions.** A protein result submitted to a
biology venue reaches biologists. The same result framed as an interpretability
or benchmarking contribution, submitted to NeurIPS or ICML, reaches the people
who will build on the method. **The people doing the most interesting work in
this curriculum — Ovchinnikov, AlQuraishi, Zhong, Noé, Bowman — publish in
both**, and that is not an accident of productivity. It is the mechanism.
