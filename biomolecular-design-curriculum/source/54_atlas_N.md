# Atlas N — Sequence, Evolution and Phylogeny

> **Problem.** Every learned model in Part III is trained on a database that is
> a biased, non-independent sample of one evolutionary history. This family is
> about what that means.
>
> **Skip this family and you will misinterpret every benchmark you run.** The
> training examples are related by descent, which breaks the i.i.d. assumption
> underlying every statistical guarantee you will cite.

---

## N.1 Alignment and search

| Topic | Resource | Link |
|---|---|---|
| **Computational Genomics — full course** | Ben Langmead (JHU) | → Module B.3 |
| Dynamic programming, BLAST, profile HMMs | Langmead's lectures | [▶](https://www.youtube.com/@BenLangmead) |
| MMseqs2 and Foldseek | **Exploring the Protein Universe**, Steinegger (Broad MIA), 1:17:41 | [▶](https://youtu.be/lHNeBIGkroM) |
| End-to-end learning of MSAs with differentiable Smith-Waterman | Samantha Petti (ML4PE), 50:41 | [▶](https://youtu.be/BJdRvODiDnk) |

**Papers:** Needleman & Wunsch 1970; Smith & Waterman 1981 · **Eddy 1998,
*Bioinformatics* 14:755 (profile HMMs) and Eddy 2011, *PLoS Comput Biol*
7:e1002195 (HMMER3)** · **Söding 2005, *Bioinformatics* 21:951** ·
**Steinegger & Söding 2017, *Nat Biotechnol* 35:1026 (MMseqs2)** ·
van Kempen et al. 2024, *Nat Biotechnol* 42:243 (Foldseek) ·
Mirdita et al. 2022, *Nat Methods* 19:679 (**ColabFold — the MSA is the
bottleneck**).

> **Petti's talk is the quiet gem here.** Making alignment differentiable means
> the MSA stops being a fixed preprocessing step and becomes part of the model.
> Almost nobody has followed up. That is an opening.

---

## N.2 Phylogenetics and the non-independence problem

| Topic | Resource | Link |
|---|---|---|
| **Learning, using, and extending variational distributions for phylogenetics** | Erik Matsen (MLCB 2019), 14:07 | [▶](https://youtu.be/0QWfV3aOTVI) |
| Phylogenetic inference methods | Matsen group materials; RevBayes tutorials | [revbayes.github.io](https://revbayes.github.io) |
| Ancestral sequence reconstruction | GRASP talk, Gabriel Foley (ML4PE), 1:03:40 | [▶](https://youtu.be/vlwdbPFr2kU) |
| **Evolutionary Dynamics** | Martin Nowak (Broad MIA), 54:22 | [▶](https://youtu.be/PuECCmT1Ioo) |

**Papers:** Felsenstein 1981, *J Mol Evol* 17:368 (ML phylogeny) ·
**Felsenstein 1985, *Evolution* 39:783 (phylogenies and the comparative method
— the non-independence paper)** · Yang & Rannala 2012, *Nat Rev Genet* 13:303 ·
**Thornton 2004, *Nat Rev Genet* 5:366 (ancestral sequence resurrection)** ·
Harms & Thornton 2013, *Nat Rev Genet* 14:559.

> **Felsenstein 1985 is the paper every machine learning practitioner in this
> field should have read and almost none have.** Sequences in your training set
> are not independent draws; they are tips on a tree. Two sequences at 90%
> identity are one observation, not two. **Every cross-validation split that
> does not account for phylogeny over-reports performance**, which is exactly the
> failure the CARE benchmark (Atlas Q.6) rediscovered empirically forty years
> later.
>
> **Derivation checkpoint 47.** Write down the effective sample size of a
> protein family given its phylogeny. Then state what a clustering-based split at
> 30% identity does and does not fix.

---

## N.3 Coevolution and statistical models of families

| Topic | Resource |
|---|---|
| Direct coupling analysis | → Atlas L.4 |
| Potts models and inverse statistical mechanics | Weigt, Marks, Hopf papers in L.4 |
| **Sectors and statistical coupling analysis** | → Atlas I (Ranganathan) |
| Fitness landscapes and epistasis | **Sparsity, Epistasis, and Models of Fitness Functions**, Aghazadeh & Brookes (Broad MIA), 1:36:47 [▶](https://youtu.be/gxYd1cHmbl8) |

**Papers:** **Morcos et al. 2011, *PNAS* 108:E1293** · Figliuzzi et al. 2016,
*Mol Biol Evol* 33:268 (DCA for fitness) · **Russ et al. 2020, *Science*
369:440 (an evolution-based model for designing chorismate mutase enzymes —
a Potts model designed working enzymes)** · Poelwijk et al. 2019,
*Nat Commun* 10:4213 (**sparse epistasis in a Fourier basis**) ·
Starr & Thornton 2016, *Protein Sci* 25:1204 (epistasis review).

> **Russ et al. 2020 is the strongest argument for the sequence-only culture
> that exists.** A Potts model — no structure, no neural network — generated
> functional chorismate mutases at a respectable rate. Read it next to ProGen
> and ESM3 and ask what the extra capacity in a transformer actually buys. The
> honest answer may be "less than you think, on this task."

---

## N.4 Databases and their biases

| Resource | What to know |
|---|---|
| UniProt / UniRef | Clustering levels (50/90/100) determine your effective dataset |
| Pfam, InterPro | Domain definitions; the labels most function benchmarks use |
| **BFD, MGnify, metagenomic sets** | Where AF2's deep MSAs come from |
| **AFDB** | 200M+ predicted structures; **Barrio-Hernandez et al. 2023, *Nature* 622:637** |
| PDB | **The structural training set, and the source of every bias in Part III** |

> **The PDB bias is not a footnote, it is a confound.** It over-represents
> soluble, stable, crystallizable, bacterially-expressible, human-disease-relevant
> proteins. Membrane proteins, IDPs, large assemblies and anything that resists
> crystallization are under-represented. Every model in Atlas P and R inherits
> this. When a method "fails on membrane proteins," the first hypothesis should
> be the training set, not the architecture.
>
> **Derivation checkpoint 48.** Quantify one PDB bias. Pick a property —
> transmembrane fraction, pI, length, organism — and compare the PDB
> distribution to UniProt's. Then state what that implies for a benchmark you
> actually use.

---

## N.5 Paired reading — Atlas N

| Watch this | Then read this | Hold this question |
|---|---|---|
| Langmead, alignment lectures | **Eddy 1998 and Eddy 2011** | What is a profile HMM, and why does it beat BLAST on remote homology? |
| Steinegger, *Protein Universe* | **Steinegger & Söding 2017**; Mirdita et al. 2022 | MSA generation is the bottleneck. What would improve it? |
| Petti, *Differentiable Smith-Waterman* | Her paper | If alignment is learnable, what else in the pipeline is? |
| Matsen, *Variational phylogenetics* | **Felsenstein 1985, *Evolution* 39:783** | Compute the effective sample size of a protein family. |
| Foley, *GRASP* | **Thornton 2004, *Nat Rev Genet* 5:366** | Ancestral sequences are often more stable than extant ones. Why? |
| Nowak, *Evolutionary Dynamics* | Nowak 2006 book, ch. 1–4 | What does a fitness landscape mean when the population is finite? |
| Aghazadeh & Brookes, *Epistasis* | **Poelwijk et al. 2019, *Nat Commun* 10:4213** | Sparse in a Fourier basis. What does that license you to measure? |
| — | **Russ et al. 2020, *Science* 369:440** | A Potts model made working enzymes. What does a transformer add? |
| — | **Barrio-Hernandez et al. 2023, *Nature* 622:637** | 200M predicted structures clustered. What is newly askable? |
