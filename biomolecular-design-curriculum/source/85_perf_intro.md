# Part IV — Performance Engineering

## E.0 Why this part exists

Most curricula treat making things faster as plumbing — necessary, unglamorous,
and not where the ideas are. That is wrong, and the history of this specific
field is the proof.

**Consider what the last fifteen years of computational biology actually turned
on.** Anton was not a new force field or a new algorithm; it was an ASIC, and it
made a class of question askable that had not been askable before. FlashAttention
introduced no new mathematics — it computes exactly the same function as standard
attention — and it changed what everyone could train. ColabFold made AlphaFold
usable by thousands of labs, and the speedup came from replacing the sequence
search with MMseqs2, not from touching the network. GROMACS's dominance is a
twenty-year accumulation of SIMD kernels, cluster pair lists and careful
load balancing. OpenFold's contribution was partly scientific and substantially
a memory-efficiency result that let people fine-tune a model they previously
could only run.

**None of those are plumbing. All of them are contributions, and several are
more consequential than the methods they accelerated.**

---

## E.1 The argument for working here

Four reasons this is unusually good territory for one person with a few GPUs.

**The problems are well-posed.** "Make triangle attention fit in 11 GB" is a
statement with an unambiguous success criterion. Compare that to most method
papers, where the hard part is arguing that your benchmark means anything. **A
performance result is either reproducible on someone else's machine or it is
not**, which is a far healthier epistemics than most of Part II enjoys.

**The field is thin.** The number of people who understand both molecular
modeling and GPU kernel programming is small. Appendix B will tell you that
several of the most-used tools in structural biology have had their performance
work done by two or three individuals. That is not true of, say, binder design,
where every improvement is contested by a dozen groups.

**Speed changes what is scientifically possible, not just convenient.** A
10× speedup is not a 10% better paper. It is the difference between one
trajectory and thirty, between a pilot and a campaign, between a method you
demonstrate and a method people use. **Every statistical complaint in Atlas B.5
and Atlas S — n=1, no error bars, no replicates — is downstream of things being
too slow to do properly.**

**It compounds into everything else.** The person who can profile a model can
also debug it, can tell which of two architectures is actually cheaper, and can
evaluate a claim about efficiency without taking the authors' word for it. That
last skill is worth having in a literature where "efficient" is a marketing term
about as often as it is a measurement.

---

## E.2 The one idea to take from this part

If you internalize nothing else, internalize this: **most scientific code is not
limited by arithmetic. It is limited by memory movement.**

Modern accelerators can do far more floating-point operations per second than
they can feed with data. The ratio is brutal and getting worse with every
hardware generation. A kernel that reads a matrix from global memory, does one
multiply, and writes it back is running at a tiny fraction of the chip's
capability, and no amount of reducing the multiply count will help it.

This single observation explains FlashAttention, explains why fused kernels win,
explains why GROMACS's cluster pair algorithm is shaped the way it is, explains
why quantization helps inference more than it "should," and explains why TPUs
and GPUs reward different algorithms. **It is the roofline model, and once you
can place your own code on a roofline plot you will stop guessing about
performance.**

> **Derivation checkpoint 64.** Compute the arithmetic intensity of the triangle
> multiplicative update in an AlphaFold-class model — floating-point operations
> per byte of memory traffic — and place it on a roofline for a card you actually
> own. Then do the same for the pairwise non-bonded force calculation in MD.
> **The two land in very different places, and that difference is why the two
> communities optimize completely differently.**

---

## E.3 How this part is organized

| Section | Subject |
|---|---|
| **E.4** | GPU architecture and CUDA kernel engineering |
| **E.5** | Compilers, TPUs and alternative accelerators |
| **E.6** | Simulation engine internals and high-performance scientific computing |
| **E.7** | Systems engineering for biomolecular machine learning |
| **E.8** | The open engineering problems, and what to attempt |

**A note on sequencing.** E.4 and E.6 are the two that pay off immediately — one
teaches you why your GPU is idle, the other teaches you why your MD run is
slower than the benchmark table claims. E.5 is the most intellectually
interesting and the least immediately useful. E.7 is the one closest to your own
work and the thinnest in recorded material, which is itself the signal.

**On prerequisites.** You need C-level thinking for E.4 — not fluency, but the
willingness to read a kernel. Module B.3 covers the computer science this
assumes, and MIT's performance engineering course enumerated in E.6 is the
bridge if you want one.
