# Atlas O — Geometric Deep Learning for Molecules

> **Problem.** A molecule is a set of atoms in R³. Rotate it and it is the same
> molecule. Build a network for which that is true by construction rather than by
> training, and understand what you paid for it.
>
> **This family is the hinge between Part III and Part III.** The mathematics
> comes from the machine learning literature; the constraints come from physics.
> It is also where the field's current orthodoxy — equivariance is necessary —
> is being seriously challenged, which makes it an unusually good place to have
> an opinion.

---

## O.1 The framework

| Resource | Instructors | Scale | Link |
|---|---|---|---|
| **AMMI Geometric Deep Learning, 2nd ed.** (enumerated in **Appendix B.5**) | Bronstein, Bruna, Cohen, Veličković | 18 videos, ~1:15 each | [▶](https://www.youtube.com/playlist?list=PLn2-dEmQeTfSLXW8yXP4q_Ii58wFdxb3C) |
| AMMI Geometric Deep Learning, 1st ed. (2021) | same four | 13 lectures | [▶](https://www.youtube.com/playlist?list=PLn2-dEmQeTfQ8YVuHBOvAhUlnIPYxkeu3) |
| Course hub with slides | — | — | [geometricdeeplearning.com](https://geometricdeeplearning.com/lectures/) |
| **Group Equivariant Deep Learning** (all 21 lectures in **Appendix B.6**) | Erik Bekkers | 21 videos, 10–50 min | [▶](https://www.youtube.com/playlist?list=PL8FnQMH2k7jzPrxqdYufoiYVHim8PyZWd) |
| Stanford CS224W: ML with Graphs | Jure Leskovec | 60 videos | [▶](https://www.youtube.com/playlist?list=PLoROMvodv4rPLKxIpqhjhPgdQy7imNkDn) |
| **A Gentle Introduction to Graph Neural Networks** | Sanchez-Lengeling (Broad MIA) | 44:53 | [▶](https://youtu.be/r5TB1d_rUxg) |
| Geometric deep learning for functional protein design | Michael Bronstein (Broad MIA) | 1:09:06 | [▶](https://youtu.be/pDp-uxR4JDI) |
| Harnessing Geometric ML for Molecular Design | Bronstein (ML4DD Day 3) | 1:08:23 | [▶](https://youtu.be/zsIyzLtwAHY) |
| Learning Geometry & 3D Symmetries | Mario Geiger, NVIDIA (ML4DD Day 1) | 45:18 | [▶](https://youtu.be/SXVtHu5ZnN4) |

**Papers:** **Bronstein et al. 2021, arXiv:2104.13478 (Geometric Deep Learning:
Grids, Groups, Graphs, Geodesics, and Gauges)** · Gilmer et al. 2017, ICML
(message passing neural networks) · Battaglia et al. 2018, arXiv:1806.01261
(relational inductive biases).

> **The Erlangen-programme framing is the one to carry.** Every architecture is
> characterized by the symmetry group it respects: CNNs are translation
> equivariant on grids, GNNs are permutation equivariant on graphs, and E(3)-
> equivariant networks are rotation-translation equivariant in space.
> **Once you see architectures as choices of symmetry group, designing a new one
> becomes a question about your problem's symmetries rather than about taste.**
>
> **Derivation checkpoint 50.** State precisely the difference between
> *invariance* and *equivariance*, and say which one you want at which layer of a
> structure predictor. Getting this backwards — invariant intermediate features
> in a network that must output coordinates — is a real and common bug.

---

## O.2 Equivariant architectures for atoms

| Talk | Speaker / host | Length | Link |
|---|---|---|---|
| **An Orientation in Symmetry-Aware ML Methods** | **Tess Smidt (MIT)** | 1:01 | [▶](https://www.youtube.com/watch?v=R3N6BocbknM) |
| **Euclidean neural networks to understand and design atomistic systems** | Tess Smidt (Harvard CMSA) | 55:00 | [▶](https://www.youtube.com/watch?v=Iah-YIFdmbs) |
| Symmetry-Aware Neural Networks with e3nn (MRS tutorial) | Smidt, Geiger et al. | 6 parts | [▶](https://www.youtube.com/watch?v=q9EwZsHY1sk) |
| **Symmetries in Inference and Learning** | **Max Welling** (TUM AI) | 57:00 | [▶](https://www.youtube.com/watch?v=YihnfamwA_s) |
| Equivariant Networks (NeurIPS 2020 tutorial) | Taco Cohen & Risi Kondor | ~2:00 | [▶](https://neurips.cc/virtual/2020/tutorial/16650) |
| **NequIP / Allegro** | Batzner & Musaelian (Valence) | 1:26:43 / 1:09:17 | [▶](https://youtu.be/ZR1NTBPBDOo) [▶](https://youtu.be/-mRl5Uk8IWk) |
| MACE | Valence | 1:22:55 | [▶](https://youtu.be/I9Y2le9e74A) |
| Is Distance Matrix Enough for Geometric Deep Learning? | Zian Li (Valence) | 1:04:15 | [▶](https://youtu.be/Qom83crI4NE) |
| Learning 3D Representations of Molecular Chirality | Keir Adams (MIT, Valence) | 1:09:59 | [▶](https://youtu.be/-CfhsOT983w) |
| ChiENN: Molecular Chirality with Graph Neural Networks | Gaiński (Valence) | 50:33 | [▶](https://youtu.be/Oil_yd-AR0U) |
| Torsional Diffusion for Molecular Conformer Generation | Corso & Jing (Valence) | 1:36:42 | [▶](https://youtu.be/29veWh5Ls5s) |
| Protein Representation Learning by Geometric Structure Pretraining | Zhang (Valence) | 53:20 | [▶](https://youtu.be/N99M9_YF9vA) |

**Papers:** **Thomas et al. 2018, arXiv:1802.08219 (tensor field networks)** ·
**Fuchs et al. 2020, NeurIPS (SE(3)-Transformers)** · Satorras et al. 2021, ICML
(**EGNN — equivariance without spherical harmonics**) · **Batzner et al. 2022,
*Nat Commun* 13:2453 (NequIP)** · Batatia et al. 2022, NeurIPS (MACE) ·
**Jumper et al. 2021 supplement, Algorithm 22 (Invariant Point Attention)** ·
Köhler et al. 2020, ICML (equivariant flows).

> **Read the IPA algorithm box in the AlphaFold supplement next to the
> SE(3)-Transformer paper.** They solve the same problem differently: IPA
> predicts points in a local frame and transforms them, avoiding spherical
> harmonics entirely. **Derivation checkpoint 51: show that IPA is equivariant,
> and identify where the equivariance would break if you changed the frame
> construction.**
>
> **Chirality is the sharp edge of this family.** A fully E(3)-equivariant
> network cannot distinguish a molecule from its mirror image, because reflection
> is in E(3). Biology is chiral everywhere — L-amino acids, D-sugars, and the
> D-residues in your own cyclic peptides. **SE(3) is the group you want, not
> E(3)**, and a surprising number of published models get this wrong or leave it
> ambiguous. The two chirality talks above are the ones that take it seriously.

---

## O.3 The challenge to the orthodoxy

**This subsection exists because the consensus is actively under attack and you
should know it before you build your next model.**

| Talk | Speaker / host | Length | Link |
|---|---|---|---|
| **Does equivariance matter at scale?** | Johann Brehmer (Valence) | — | [▶](https://www.youtube.com/@valence_labs) |
| **Transformers Discover Molecular Structure Without Graph Priors** | Tobias Kreiman (Berkeley, Valence) | 1:04:09 | [▶](https://youtu.be/k9IbNCKJc-c) |
| UMA: A Family of Universal Models for Atoms | Brandon Wood (Valence) | — | [▶](https://www.youtube.com/@valence_labs) |
| AlphaFold3 review (note the architecture change) | Ovchinnikov (BPDMC) | 1:12:58 | [▶](https://youtu.be/qjFgthkKxcA) |

**Papers:** Brehmer et al. 2024, arXiv:2410.23179 (**Does equivariance matter at
scale?**) · **Abramson et al. 2024, *Nature* 630:493 (AlphaFold3 — which
*dropped* the equivariant frame machinery for a diffusion module with data
augmentation)** · Wang et al. 2024 (**on the surprising effectiveness of
non-equivariant models given enough data**).

> **The argument, stated plainly.** Equivariance is a hard constraint that buys
> data efficiency. With enough data and augmentation, an unconstrained model can
> learn the symmetry and is often faster and more expressive. **AlphaFold3 is the
> highest-profile piece of evidence for this position**: it replaced AF2's
> explicitly equivariant structure module with a diffusion module trained with
> augmentation, and it got better.
>
> **The counter-argument.** Low-data regimes are the normal case in biology.
> Your cyclic-peptide dataset is not going to have a million examples. Where data
> is scarce, equivariance is not a stylistic preference — it is the difference
> between learning and not learning.
>
> **Derivation checkpoint 52.** Design the experiment that would settle this for
> *your* problem: train equivariant and non-equivariant versions of the same
> architecture across a data-size sweep, and find the crossover. **Nobody has
> published that curve for protein structure, and it would be cited constantly.**
> That is Capstone II.

---

## O.4 BUILD — Atlas O

1. **Implement an E(3)-equivariant message-passing layer from scratch** — EGNN
   is about forty lines and does not need spherical harmonics. Verify
   equivariance numerically by rotating the input and checking the output
   transforms correctly to machine precision.
2. **Break it deliberately.** Add a term that uses absolute coordinates. Watch
   the equivariance test fail. This is how you will debug every geometric model
   you ever write.
3. **Run the data-scaling sweep.** Same task, equivariant and non-equivariant,
   at 100, 1,000, 10,000 and 100,000 examples. Plot the crossover.
4. **Write the one page.** At what dataset size does the inductive bias stop
   paying for itself on your task?

**Derivation checkpoints due: 50, 51, 52.**

---

## O.5 Paired reading — Atlas O

| Watch this | Then read this | Hold this question |
|---|---|---|
| AMMI GDL lectures 1–4 | **Bronstein et al. 2021, arXiv:2104.13478** | Name the symmetry group of every architecture you use. |
| Bekkers, *Group Equivariant DL* | Cohen & Welling 2016, ICML (G-CNNs) | Build a G-CNN for a finite group by hand. |
| **Smidt, *Orientation in Symmetry-Aware ML*** | **Thomas et al. 2018, arXiv:1802.08219** | Invariant, equivariant, or augmented? Choose for your problem and defend it. |
| Smidt, *Euclidean NNs for atomistic systems* | Batzner et al. 2022, *Nat Commun* 13:2453 | Spherical harmonics as a basis. What does order ℓ buy? |
| Geiger, *Learning Geometry & 3D Symmetries* | Satorras et al. 2021, ICML (EGNN) | EGNN has no spherical harmonics. What is traded? |
| Welling, *Symmetries in Inference and Learning* | His argument for data efficiency | Quantify: how many examples is a symmetry worth? |
| — | **AlphaFold2 supplement, Algorithm 22 (IPA)** | Prove IPA is equivariant. Where would it break? |
| Adams, *Molecular Chirality* | Adams et al. 2022, ICLR | E(3) cannot see chirality. Check your own model. |
| **Kreiman, *Transformers without graph priors*** | **Brehmer et al. 2024, arXiv:2410.23179** | Run the data-scaling sweep. Where is the crossover? |
| Ovchinnikov, *AlphaFold3 review* | **Abramson et al. 2024, *Nature* 630:493** | AF3 dropped the equivariant module. Was that a concession or a result? |
