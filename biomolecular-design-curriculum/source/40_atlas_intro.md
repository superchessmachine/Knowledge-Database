# Part II — The Method Atlas

## A.0 What this part is

Every computational method for understanding proteins, DNA and RNA, organized by
the problem it solves.

The organizing claim is that the field looks fragmented but is not. Underneath
the hundreds of named tools there are perhaps nineteen genuine families of
method, and almost every tool is one family's answer to one question. Once you
can see the families, three things become possible that are not possible
otherwise: you can place a new paper within an hour of it appearing, you can
tell whether a claimed advance is a new family or a refinement within one, and —
the point of this document — you can notice which exchanges between families
have not yet happened.

A caution about the organization. Methods are grouped by *what they compute*,
not by who built them or which software implements them. That means Rosetta
appears in five places and AlphaFold in four. This is deliberate. Organizing by
software teaches you tools; organizing by problem teaches you the field.

---

## A.1 The nineteen families

| | Family | The question it answers |
|---|---|---|
| **A** | Potential energy functions | What is the energy of this arrangement of atoms? |
| **B** | Molecular dynamics | How does this system move in time? |
| **C** | Monte Carlo | How do I sample this distribution without dynamics? |
| **D** | Enhanced sampling and rare events | How do I reach states that are too rare to see? |
| **E** | Free energy calculation | What is the free energy difference between two states? |
| **F** | Coarse-graining and reduced models | What can I throw away and still be right? |
| **G** | Continuum and mesoscale methods | What if I treat solvent, membrane or chromatin as a continuum? |
| **H** | Polymer theory and minimal models | What does a chain do, independent of chemistry? |
| **I** | Normal modes, networks and dynamics analysis | What are the meaningful motions, and what do they couple? |
| **J** | Structure determination algorithms | How does experimental data become coordinates? |
| **K** | Integrative and hybrid modeling | How do I combine data of different kinds and resolutions? |
| **L** | Classical structure prediction | How do I get a structure from a sequence without a network? |
| **M** | Docking and virtual screening | What binds where, and how tightly? |
| **N** | Sequence analysis and evolution | What does the evolutionary record say about this molecule? |
| **O** | Deep learning foundations for molecules | What architectures respect molecular structure? |
| **P** | Learned structure prediction | How do I get a structure from a sequence with a network? |
| **Q** | Sequence and biological language models | What is learnable from sequence alone, at scale? |
| **R** | Generative design | How do I produce a molecule that does not yet exist? |
| **S** | Benchmarking and assessment | How would I know if any of this were true? |

Families A through I are the physics-first culture. J and K are the experimental
interface. L through N are the classical computational-biology tradition. O
through R are the learning-first culture. S is the discipline that keeps all of
them honest, and it is the one most often skipped.

---

## A.2 Reading an Atlas entry

Each family entry has a fixed shape so you can navigate without re-reading.

> **Problem.** The question stated precisely, including what is being
> approximated and what is assumed.
>
> **Theory.** Lectures that derive the method. Tier A or B. These are where the
> derivation checkpoints live.
>
> **Practice.** Lectures and tutorials that run it. Tier B.
>
> **Talks.** Research-level talks on the frontier of this family. Tier C.
>
> **Papers.** The canonical references, with the one-or-two marked **[landmark]**
> that you should read twice.
>
> **Software.** What actually implements this, so you can read source.
>
> **Open.** What is unsolved in this family, as its own practitioners state it.
> These feed the open-problems file and are where contributions come from.

The **Open** sections are the most valuable part of this document and the part
most likely to be wrong within two years. Treat them as a snapshot of October
2026 and update them as you watch.

---

## A.3 The dependency structure

Families are not independent. The practical order of study is roughly:

```
            H (polymer theory)
                    |
     A (energy) --> B (MD) --> D (enhanced sampling) --> E (free energy)
         |           |                |
         |           v                v
         |          C (Monte Carlo)   I (dynamics analysis)
         |           |
         v           v
     F (coarse-graining)  <-->  G (continuum/mesoscale)

     J (structure determination) --> K (integrative modeling)
                                            ^
     N (sequence/evolution) --> L (classical prediction)
                |                       |
                v                       v
            Q (language models)     P (learned prediction)
                      \                /
                       \              /
                        v            v
                     O (DL foundations)
                              |
                              v
                        R (generative design)
                              |
                              v
                        S (assessment)  <-- applies to everything
```

Three dependencies are worth stating explicitly because they are commonly
violated:

**You cannot understand E without D, and you cannot understand D without B and
C.** People routinely run free energy calculations without understanding the
sampling underneath, which is why so many published ΔΔG values are confidently
wrong.

**You cannot evaluate P or R without S.** A structure predictor or a design
method is a claim about generalization, and claims about generalization are
meaningless without a defensible split. This is the single most common failure
in the current literature.

**You cannot usefully contribute to R without A.** Generative design models
produce molecules that must obey physics they were never told about. The groups
producing the highest experimental success rates are the ones that kept a
physical energy function somewhere in the loop.

---

## A.4 Where the unexchanged ideas are

A working list, as of compilation, of exchanges between families that have not
happened or have barely started. These are not predictions that they will work;
they are observations that nobody has seriously tried. Each is a candidate
project and each maps to a capstone in Part III.

| From | To | The unexchanged idea |
|---|---|---|
| D, E | R | Convergence and error estimation for generative design. The physics culture's single greatest export; the learning culture has essentially not imported it. |
| D | R | Treat reverse-diffusion sampling as a rare-event problem and apply weighted ensemble or path sampling to it, rather than to a physical trajectory. |
| F | O | Learned coarse-graining as an architectural prior for structure models, rather than as a separate simulation technique. |
| H | R | Polymer-theoretic constraints as a design objective — designing for chain statistics rather than for a single backbone. |
| I | R | Design against an ensemble objective or a normal-mode spectrum rather than a static structure. |
| J, K | P | Chemical probing, HDX and crosslinking data as differentiable likelihood terms inside a learned structure model, the way MSA depth is used now. |
| B, D | Q | Simulation-generated training data off the PDB manifold, to teach models about the region where design actually operates. |
| N | S | Homology-aware and epistasis-aware splits as a standard, rather than per-paper improvisation. |
| C | R | Proper MCMC over design space with a defined stationary distribution, instead of greedy or temperature-sampled decoding. |
| G | R | Continuum electrostatics as a differentiable layer, so designs can be optimized for solubility and pKa directly. |
| A (ML potentials) | B, E | Machine-learned potentials at biomolecular scale, which would collapse the force-field accuracy ceiling that bounds every number in families B through E. |
| S | R | A blind, adversarial, CASP-style assessment for de novo design. It does not exist. |

The last row is the largest single piece of missing infrastructure in this
field, and it is the one most likely to make a career.
