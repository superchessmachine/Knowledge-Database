# Part V — From Consumption to Contribution

## C.1 The derivation checkpoints

Sixty things you must be able to produce on a blank sheet of paper, unaided, by
the end of this program. They are chosen because each is load-bearing: a person
who can derive all sixty can read any paper in this field and immediately see
what is new, what is borrowed, and what is hidden.

This is the real examination. The lectures are support material.

### From potential energy functions (Family A)

1. Write down every term in a modern molecular mechanics force field and name
   the physical effect each stands in for — including the ones standing in for
   nothing.
2. Derive the Lennard-Jones potential's relationship to dispersion and Pauli
   repulsion, and explain why the r⁻¹² term is chosen for convenience rather
   than physics.
3. Explain Ewald summation and why particle-mesh Ewald is O(N log N). State what
   artifact periodic boundary conditions introduce for a charged solute and how
   large it is.
4. Explain what a polarizable force field adds, and why the added cost has not
   been worth it for most biomolecular applications.
5. Derive the functional form of a machine-learned interatomic potential's
   energy as a sum of local atomic contributions, and state precisely what that
   locality assumption forbids.

### From molecular dynamics (Family B)

6. Show that velocity Verlet is symplectic and time-reversible, and explain what
   that buys over a higher-order non-symplectic scheme.
7. Derive the Langevin equation's fluctuation-dissipation relation and explain
   why violating it gives wrong kinetics but can still give right thermodynamics.
8. Explain why constraining bonds to hydrogen permits a larger timestep, and
   derive what hydrogen mass repartitioning does to the fastest vibrational mode.
9. Show why the Berendsen thermostat does not sample the canonical ensemble, and
   state what distribution it does sample.
10. Derive the pressure estimator from the virial, and explain why it is noisy.

### From Monte Carlo (Family C)

11. State the Metropolis-Hastings acceptance criterion and prove it satisfies
    detailed balance for an arbitrary symmetric or asymmetric proposal.
12. Explain why detailed balance is sufficient but not necessary for correct
    sampling, and give one method that is correct without it.
13. Derive Hamiltonian Monte Carlo and explain where the Metropolis correction
    enters and why it is needed despite the dynamics being deterministic.
14. Explain configurational bias Monte Carlo and derive its acceptance ratio.
15. Derive the Gillespie stochastic simulation algorithm from the chemical
    master equation.
16. Explain Wang-Landau sampling and state what it converges to.

### From enhanced sampling (Family D)

17. Derive the weighted histogram analysis method from maximum likelihood.
18. Explain why well-tempered metadynamics converges where the original did not,
    and write the asymptotic form of the bias.
19. Derive the scaling of the required replica count with system size in
    temperature replica exchange, and explain why it is fatal for large systems.
20. Derive the weighted ensemble resampling scheme and show it is unbiased.
21. Explain transition path sampling's shooting move and why it preserves the
    path ensemble.
22. State and derive the Jarzynski equality, and explain why it is nearly
    useless in practice without careful attention to the tails.

### From free energy (Family E)

23. Derive the free energy perturbation identity and state the overlap condition
    under which it fails.
24. Derive the Bennett acceptance ratio estimator and show it is the
    minimum-variance estimator in its class.
25. Explain thermodynamic integration and the endpoint singularity problem, and
    state the standard fix.
26. Write the thermodynamic cycle for absolute binding free energy and name
    every correction term.
27. Explain what MM-GBSA actually computes and why its entropy treatment is
    usually wrong.

### From coarse-graining and polymer theory (Families F, H)

28. Derive the multiscale coarse-graining / force-matching objective and state
    what it is a projection of.
29. Explain the Mori-Zwanzig decomposition and identify which term coarse-grained
    models normally discard.
30. Explain why coarse-grained models systematically get entropy and dynamics
    wrong even when they get structure right.
31. Derive the end-to-end distance distribution of an ideal chain and the
    worm-like chain's force-extension relation.
32. Derive the Flory scaling exponent and explain what it predicts for a
    disordered protein versus a folded one.
33. Explain the random energy model of protein folding and derive the condition
    for a funnel-shaped landscape.

### From continuum and mesoscale methods (Family G)

34. Write the Poisson-Boltzmann equation and derive the Debye length. State what
    the linearized form assumes and when it breaks.
35. Explain the generalized Born approximation and what it approximates.
36. Explain the hydrophobic effect in terms of entropy, and explain why implicit
    solvent models get the enthalpy-entropy decomposition wrong even when the
    total free energy is approximately right.
37. Derive the Ermak-McCammon Brownian dynamics propagator and state when the
    overdamped approximation is valid.
38. Explain why hydrodynamic interactions change association rates and write the
    Rotne-Prager tensor's role.

### From dynamics analysis (Family I)

39. Derive the Gaussian network model and show its connection to the contact
    matrix's pseudo-inverse.
40. Explain why TICA finds slow coordinates where PCA finds high-variance ones.
41. Write the transfer operator for a molecular system, explain the relationship
    between its eigenvalues and implied timescales, and derive why a Markov state
    model's lag time must exceed the fastest resolved process.
42. Explain what a Chapman-Kolmogorov test checks and what passing it does not
    guarantee.

### From structure determination (Families J, K)

43. Explain the crystallographic phase problem and how molecular replacement
    solves it.
44. State the relationship between a B-factor, a cryo-EM local resolution, and a
    conformational ensemble — and why treating any as a per-atom uncertainty is
    wrong.
45. Derive the maximum-likelihood objective for single-particle cryo-EM
    reconstruction and explain what the marginalization is over.
46. Explain Fourier shell correlation and why the 0.143 threshold is a convention
    rather than a theorem.
47. Write the Bayesian formulation of integrative modeling and state where the
    forward model for each data type enters.
48. Explain maximum-entropy reweighting of a simulated ensemble against
    experimental data, and state what it assumes about the prior.

### From classical prediction and docking (Families L, M)

49. Derive why side-chain packing with a rotamer library is NP-hard, and explain
    what dead-end elimination actually eliminates.
50. Explain what a Ramachandran plot is a projection of, and what a
    backbone-dependent rotamer library encodes that an independent one does not.
51. Explain the loop closure problem and why it has an analytic solution while
    loop modeling remains unsolved.
52. Explain why docking scoring functions rank poses better than they rank
    affinities, and what that implies about their functional form.

### From sequence and evolution (Family N)

53. Derive the Needleman-Wunsch recursion and state its complexity. Then explain
    what affine gap penalties change.
54. Derive the forward algorithm for a profile HMM and explain the relationship
    between HMM emission probabilities and a substitution matrix.
55. Formalize direct coupling analysis as inference in a Potts model, and state
    precisely what mean-field DCA approximates and what it costs.

### From machine learning (Families O, P, Q, R)

56. Derive backpropagation for an arbitrary computational graph; then derive the
    adjoint method for differentiating through an ODE solver.
57. Derive the evidence lower bound and show where the reparameterization trick
    enters and why it is necessary.
58. Derive the denoising diffusion objective from the variational bound, show its
    equivalence to score matching, and state the relationship between the
    probability-flow ODE and the reverse SDE. Then show that the learned score is
    a force up to temperature.
59. Define equivariance and invariance formally for SE(3), prove that a network
    built from scalar products of relative position vectors is SE(3)-invariant,
    and explain what is lost by taking invariance instead of equivariance.
60. Derive the triangle inequality constraint on a distance matrix and explain
    precisely what AlphaFold's triangle multiplicative update enforces — and the
    sense in which it is only a soft enforcement.

### From RNA (Family T)

71. **Derive the Nussinov recursion** and prove that the non-crossing condition
    is exactly what makes the interval decomposition valid. Then state what the
    Zuker loop model adds, and explain why the partition function requires a
    *different* recursion rather than the same one with max replaced by sum.
72. **Write down what a SHAPE reactivity profile determines and what it does
    not.** Construct a synthetic two-state mixture, compute its
    population-averaged reactivity, and attempt to recover the components. The
    recovery is ill-posed; characterize how ill-posed.
73. **Quantify the RNA-versus-protein data gap** from the PDB directly, then
    decompose the performance gap into the six causes in Atlas T.10 and argue,
    with evidence, which are contingent and which are structural.

### The design-specific trio

61. Formalize inverse folding as a conditional distribution and explain why
    maximizing sequence likelihood given a backbone is not the same as maximizing
    the probability that the sequence folds to that backbone.
62. Explain designability: why some backbone folds admit many sequences and
    others none, and how that relates to the density of states.
63. Explain what self-consistency validation does and does not establish, and
    construct a concrete case where a design passes with high confidence and
    still fails experimentally.

If you can do all sixty-three unaided, you are no longer a user of this field's
methods.

---

### From performance engineering (Part IV)

**These seven are the cheapest checkpoints in the document to attempt and the
ones most likely to change what you do next week.** Every one is answerable on
hardware you already own, in an afternoon, and each has a number as its answer.

64. Compute the **arithmetic intensity of the triangle multiplicative update** in
    an AlphaFold-class model — floating-point operations per byte of memory
    traffic — and place it on a roofline for a card you own. Do the same for the
    pairwise non-bonded force kernel in MD. Explain why the two land in such
    different places and what that implies about how each community optimizes.
65. **Derive the FlashAttention tiling** and prove it computes exactly the same
    function as standard attention. Then state precisely which term in the memory
    traffic it eliminates and why the online-softmax trick is what makes it
    possible.
66. Write down the **memory required to store the pair representation** as a
    function of sequence length, for a given precision and number of channels.
    Find the length at which it exceeds each card in your fleet. Then find how
    much chunking and activation recomputation buy you, and at what cost in time.
67. Explain why GPU molecular dynamics uses **cluster pair lists rather than
    per-atom Verlet neighbor lists.** The answer is about warps and memory
    coalescing, not about algorithmic complexity — and it is the clearest example
    in this document of hardware dictating an algorithm.
68. Derive the **communication cost of the PME FFT** across ranks, and explain
    the scaling wall it creates. Then explain why separate PME ranks exist and
    how you would choose their number for a given system and node count.
69. Work out **why reduced precision is safe in attention but dangerous in force
    accumulation.** Write the error analysis. This is the single most useful
    numerics question in computational biology and almost nobody can answer it
    cleanly.
70. For one AlphaFold-class prediction on your own hardware, **measure what
    fraction of wall-clock time is MSA search versus network inference.** Most
    people assume the network dominates. Measure it before you believe it, then
    decide which one is worth optimizing.

---

## C.2 The capstone projects

**Eleven projects, each named and cross-referenced from the family it belongs to.**
Where a section elsewhere in this document says "that is Capstone VII," this is
the list it means. Begin each as soon as its prerequisite families are done; do
not wait until the end.

Every one of these is scoped to the multi-machine GPU fleet you already run, and
every one is stated specifically enough that you could write the methods section
before you start. That is deliberate: a capstone you cannot specify is a wish.

### I — The reimplementation *(after Families B, C, I)*
**Build a Markov state model pipeline from scratch.** Featurization, TICA,
clustering, transition matrix estimation with reversibility, implied timescales,
Chapman-Kolmogorov. Validate against PyEMMA on data you already have.
*Why:* it forces you to confront, in code, every place the statistics can
silently fail. After this you will never trust an MSM figure without asking
about the lag time.

### II — The equivariance crossover *(after Family O)*
**Find the dataset size at which an architectural symmetry constraint stops
paying for itself.** Train equivariant and non-equivariant versions of one
architecture on one task across a data-size sweep, and plot the crossover.
*Why:* AlphaFold3 dropped AF2's explicitly equivariant structure module and got
better, while low-data molecular problems clearly still benefit. **Nobody has
published that curve for protein structure**, and it would be cited constantly.
See Atlas O.3 and O.4.

### III — The over-optimization curve *(after Families P, R, S)*
**Measure where your design filters stop tracking reality.** Take a target with
experimental data at several optimization strengths and plot wet-lab success
against filter stringency. The curve has a maximum. Find it.
*Why:* Gao, Schulman & Hilton did exactly this for learned reward models in
language and found true performance peaks and then falls while the proxy keeps
climbing. Design pipelines optimize against pLDDT and interface pAE with no
equivalent measurement. See D.6.1 and Atlas R.10.

### IV — The Boltzmann-generator audit *(after Family D)*
**Test whether a learned sampler actually samples the target distribution.**
Take a system where you can afford converged reference sampling, generate from a
flow or diffusion emulator, compute importance weights, and report the effective
sample size and the free energy difference against the reference.
*Why:* the claim these methods make is Boltzmann sampling, not plausible
structures, and the distinction is checkable. See Atlas D.6.

### V — The learned prior meets sparse data *(after Family K)*
**Work out the correct way to combine a learned structural prior with averaged
experimental restraints without double-counting.** Hummer and Köfinger solved
this for simulation ensembles; nobody has solved it for AlphaFold-class priors,
which is what every crosslink-guided and density-guided prediction now does
informally.
*Why:* it is a well-posed inference question with immediate practical payoff,
and it sits directly on top of any restraint-guided prediction work. See Atlas K.3.

### VI — The whole-cell parameter gap *(after Family G)*
**Take the minimal-cell whole-cell model and ask what it would take to put a
designed protein into it.** Enumerate every parameter the model needs, mark
which are computable today, and quantify how wrong the computable ones are.
*Why:* it is the clearest statement of the distance between design and cell
biology, and nobody in design has written it down. See Atlas G.2.

### VII — The standing assessment *(ambitious)*
**Build the blind assessment for de novo design that does not exist.** Target
set, held out by a third party, experimental readout, published protocol, annual
cadence. Adaptyv is the proof it can work; it is not yet CASP.
*Why:* this is the single largest piece of missing infrastructure in the field.
It is hard because it needs wet-lab partners, which is exactly why nobody has
done it. See Atlas R.4 and S.1.

### VIII — Interpretability with ground truth *(after Family Q and D.9)*
**Train sparse autoencoders on an MSA Transformer and evaluate the recovered
features against Pfam domains, CATH folds, catalytic-site annotations and
transmembrane spans.** Report precision and recall of features against real
labels — which language interpretability literally cannot do.
*Why:* an MSA Transformer attending across an alignment to find the
corresponding residue in a homolog is an induction head doing structural
biology, and nobody has looked. **This is the most tractable bridge project in
this document, and it benefits the AI field more than the biology field.**
See Atlas Q.4, D.7.5, D.9 and D.10.1.

### IX — The RNA gap *(after Family Q)*
**Characterize, quantitatively, why RNA structure prediction is behind protein
structure prediction.** Is it data volume, conformational heterogeneity, the
ion atmosphere, or the absence of a CASP-grade assessment? Decompose it.
*Why:* this is the Rhiju Das question, it is stated honestly nowhere, and the
answer determines where effort should go. See Atlas Q.5.

### X — Scaling laws for structure prediction *(after D.5)*
**Fit the functional form of structure-prediction performance in data,
parameters and compute.** Subsample the PDB at many fractions, train a fixed
architecture at several sizes, fit the surface, and use Kudugunta's methodology
critique as the checklist.
*Why:* it is the quantitative answer to "should we fund more structure
determination or more compute," and that question is currently decided by
opinion. See D.5.4.

### XI — The speedup *(after Part IV)*
**Make one real tool measurably faster and get the change merged.** Not a fork,
not a benchmark script — an upstream contribution to something people run:
GROMACS, OpenMM, OpenFold, Boltz, ColabFold, e3nn, MDAnalysis. Profile it, find
the actual bottleneck, fix it, show the number, defend it in review.
*Why:* it is the single most verifiable contribution in this entire document —
a speedup either reproduces on someone else's machine or it does not — and it is
how you become known to the people who maintain the tools you depend on. It is
also the one capstone where the field's gatekeeping is purely technical. **See
Part IV, especially E.8.**

---

### C.2b — Four standing commitments, not projects

These were capstones in the first edition. They are better understood as things
you do permanently, starting now, rather than things you finish.

**The hard target.** Pick one biological system nobody has solved and that you
already have a head start on. Know it better than anyone. Domain depth
is what makes a methods person's benchmarks credible; it is the Phil Bradley
lesson.

**The infrastructure.** Build and release one tool other people use. The Baker
and Das lesson is that infrastructure compounds. A narrow, correct,
well-documented tool with ten real users is worth more to a methods career than
three papers nobody runs.

**The negative result.** Publish one thing that did not work, properly
characterized. The field has almost no record of its failures, which is why
people keep repeating them — see Appendix B.3 for how badly the record is
skewed. A careful negative result on a method that sounds like it should work is
a real contribution and is far easier to get right than a positive one.

**The review nobody has written.** Write the survey that connects two families
in Section A.4 that have never been connected in print. A good review is a
research contribution — it creates the frame other people then work inside — and
it is the cheapest way to establish that you see the whole field.


---

## C.3 The five generators

Having watched several hundred hours of people describing their own work, the
same small number of move-types recur. Named, they can be applied deliberately.

**1 — The cross-cultural carry.** The highest-yield move, and the reason to be
trilingual. Ask continuously: what is routine in one family that another has
never heard of? Section A.4 is the current inventory.

**2 — Attack the invisible assumption.** Every field has a simplifying
assumption so universal it has stopped being visible. Live candidates here: that
a protein has *a* structure; that the PDB is a representative sample of protein
space; that sequence recovery is a meaningful design metric; that a confidence
score estimates accuracy rather than training-set density; that a pairwise
decomposable energy is adequate; that static backbone design suffices for
anything involving function. Each is false in an interesting way.

**3 — Change the level of the stack.** The Shaw move. When the limit is the
hardware, build hardware. When it is the data, build an assay. When it is the
benchmark, build a benchmark. Most people accept the level they were handed.

**4 — Take a method where it should not work.** RNA is the obvious target —
roughly where proteins were twenty years ago, thinner data, harder physics,
and the protein methods have not been properly adapted. Disordered proteins are
the second. Both are large territories adjacent to your existing skills.

**5 — Make it fast enough to change the question.** When a calculation goes from
a week to a second, people do not do the same science faster; they do different
science. A thousandfold speedup is a methods contribution even with no new
mathematics in it.

---

## C.4 The permanent seminar diet

After the program ends the practice begins. Roughly three to four hours a week
keeps you current in a field that turns over its state of the art about every
eighteen months.

- **Weekly:** one ML4PE or Institute for Protein Design seminar.
- **Weekly:** scan new preprints in the relevant bioRxiv and arXiv categories;
  read two properly, skim twenty.
- **Monthly:** one full conference session from the archives — MLSB, Simons,
  IPAM, KITP, a CASP meeting, or a Free Energy Workshop.
- **Quarterly:** one historical dive. Pick a method you use daily and watch or
  read its original presentation. The gap between how a method was originally
  motivated and how it is now used is reliably instructive and is where a
  surprising number of new ideas hide in plain sight.
- **Annually:** CASP and CAPRI assessments when they appear. Still the field's
  only genuinely adversarial evaluation and therefore its most honest few hours.

And the habit that matters most: **maintain the open-problems file.** Every time
a speaker says "we don't know how to do X," or "that's still open," or "this is
the part that doesn't work" — write it down with the date and the speaker.
Review it monthly. After a year that file is a more valuable research asset than
anything else this curriculum produces, because it is a list of problems that
senior people have personally confirmed are both unsolved and worth solving.

That is Hamming's list, and his whole argument is that keeping one is what
separates the people who do important work from the people who do competent
work.
