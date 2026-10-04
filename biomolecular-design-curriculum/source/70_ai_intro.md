# Part III — Upstream AI Research

## D.0 Why this part exists

The rest of this document trains you to be excellent at applying artificial
intelligence to molecules. This part is about contributing to artificial
intelligence itself.

These are different ambitions with different reward structures, and it is worth
being honest about the tension before describing the bridge. The AI research
community rewards generality, benchmark movement on tasks many people care
about, and speed. The molecular community rewards domain insight, experimental
validation, and correctness. A person who splits attention evenly between them
tends to be out-competed in both: the AI people have read more papers this month
than you have, and the biology people have a better wet-lab collaborator.

So the goal here is not to be a part-time AI researcher. It is something more
specific and more defensible.

---

## D.1 The bridge thesis

**Molecular problems are an unusually good forcing function for genuine AI
contributions, because they break assumptions that language and vision let you
keep.**

This is not a consolation prize. It is the observation that a surprising
fraction of core machine learning advances came out of scientific domains, and
they came out of those domains precisely because the domain refused to let the
researcher take the usual shortcut.

| AI contribution | Came from | The assumption the domain refused to allow |
|---|---|---|
| Graph neural networks | Chemistry (molecular property prediction) | That inputs have a grid or sequence structure |
| Equivariant networks, tensor field networks, e3nn | Physics and chemistry | That you can augment your way out of a symmetry |
| Neural ODEs, continuous-depth models | Dynamical systems | That depth is discrete |
| Riemannian and discrete flow matching | Geometry and molecular structure | That your data lives in Euclidean space |
| GFlowNets | Molecule and drug design | That you want the mode rather than a diverse sample from the reward |
| Boltzmann generators, flow-based samplers | Statistical physics | That generation and sampling a known distribution are different problems |
| Machine-learned interatomic potentials | Quantum chemistry | That approximate function fitting is good enough |
| Triangle attention and geometric consistency layers | Structural biology | That attention needs no structural prior |
| Conformal prediction uptake in science | High-stakes prediction | That a softmax output is a probability |
| Active learning at scale, closed-loop experimentation | Experimental science | That data is free and i.i.d. |

Read that table alongside the one in Section 0.2. The same move appears in both:
a constraint that one community treats as an obstacle turns out, carried
elsewhere, to be a research program.

### The five assumptions molecular work forces you to drop

These are the specific places where your domain hands you an AI research problem
that the mainstream does not have to solve.

**1. Data is not abundant.** Language and vision research operates in a regime
where more data is usually available. Protein design operates in a regime where
the relevant labeled data is a few thousand examples, expensive, and biased
toward what was easy to measure. Everything about low-data learning —
inductive bias, transfer, meta-learning, active learning, uncertainty — is
*load-bearing* here and merely interesting there.

**2. Symmetry is not optional.** You cannot augment your way out of SE(3). A
model that assigns different energies to the same molecule in two orientations
is not slightly worse; it is wrong. This makes molecular work one of the few
areas where equivariant architecture research is forced rather than fashionable.

**3. The test distribution is deliberately different from the training
distribution.** This is the deepest one. In most of machine learning,
distribution shift is a nuisance to be minimized. In design it is *the goal* —
you are explicitly asking the model to score molecules that do not exist and
were therefore not in training. Almost no mainstream ML method is built for
this, and the theory of it is thin. If you want one durable AI research question
to own, this is the best candidate in the document.

**4. Errors are expensive and uncertainty must be calibrated.** A wrong
recommendation costs months of wet-lab time. That makes uncertainty
quantification a first-class requirement rather than a reviewer's afterthought,
and it is why conformal prediction and proper calibration matter more in your
setting than in most.

**5. There is a ground truth that is not the dataset.** Physics exists
independently of the PDB. This is a luxury other ML fields do not have, and it
enables a whole class of method — physics-informed losses, differentiable
simulation, hybrid energy-and-learning models, generative models constrained to
be physically normalized — that has no analogue in a domain where the only
arbiter is held-out data.

---

## D.2 What to actually do with this part

Three honest postures, and you should pick one rather than drifting.

**Posture A — Informed consumer, deep in one AI sub-area.** Follow the field
broadly through Section D.5 and the standing archives, but go genuinely deep in
exactly one technical area that your molecular work needs: most plausibly
generative modeling, equivariant architectures, or uncertainty quantification.
Publish AI-venue papers occasionally, molecular papers mainly. This is the
highest expected value for most people and the lowest risk.

**Posture B — Dual-track researcher.** Treat molecular problems as a source of
AI research questions and publish into both communities deliberately, with the
same work framed differently for each. Requires more time and a tolerance for
being slightly foreign in both rooms. The people who pull it off — the
geometric deep learning community is full of them — tend to have outsized
influence because they are the translation layer.

**Posture C — Switch.** Decide that core AI is the real interest and molecules
were the entry point. Legitimate, common, and worth naming so that you choose it
deliberately rather than by drift. If this is the path, the biology becomes a
domain you understand unusually well rather than your subject.

The material below serves all three. What differs is depth: Posture A takes
Sections D.3 and D.6 seriously and skims the rest; Posture B does all of it;
Posture C inverts the weighting of this document.

---

## D.3 How this part is organized

**D.4 Vision and perception research.** The field where most modern architecture
ideas were first tested, and the source of the 3D and generative machinery that
molecular work now runs on.

**D.5 Deep learning theory.** Why any of this works. Generalization, implicit
bias, infinite-width limits, scaling laws, and the phenomena — grokking, double
descent, edge of stability — that current theory only partly explains.

**D.6 Architecture, training and language model research.** What actually
matters inside a model, how training at scale really works, and the live
architecture arguments.

**D.7 Interpretability and the science of models.** Treating a trained network
as an object of empirical study. The fastest-moving area in AI with the most
room for a careful newcomer.

**D.8 Foundational arguments and research taste.** The field's live
disagreements, stated by the people having them — scaling versus architecture,
whether language models reason, world models, embodiment, the bitter lesson and
its critics.

**D.9 The bridge, concretely.** Specific open AI research problems that your
molecular work is unusually well positioned to attack.

---

## D.4 A warning about this part specifically

AI research video has a worse signal-to-noise ratio than anything else in this
document. There is an enormous volume of talks that are repackaged press
releases, and a genre of confident explainer content that is wrong in ways that
are hard to detect without reading the paper.

Three defenses, and they matter more here than in Part II.

**Prefer first-author talks at academic venues over keynotes at industry
events.** The former are accountable to an audience that has read the paper.

**Apply the pairing principle without exception.** In the molecular sections you
can occasionally get away with watching a talk alone. Here you cannot — the gap
between what a talk claims and what the paper establishes is systematically
wider, because the incentive to overclaim is stronger.

**Date everything.** A talk from 2021 about what transformers can and cannot do
may describe a settled question or a long-refuted guess, and nothing in the
video will tell you which. Each entry below carries its date for this reason.
