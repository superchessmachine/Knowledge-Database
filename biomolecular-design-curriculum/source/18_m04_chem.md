# B.4 Chemistry and Structural Biology

> **The module most computational people skip, and the one whose absence shows.**
>
> You can build a generative model of protein backbones without knowing what a
> hydrogen bond costs in kcal/mol, what pKa shifts do in a buried active site, or
> why a designed interface with perfect shape complementarity still has
> micromolar affinity. You will just be unable to tell, when your design fails,
> whether the model was wrong or the chemistry was always going to refuse.
>
> **This module is the vocabulary for arguing with a wet-lab collaborator**, and
> the single best predictor of whether a computational person's designs get
> made.

---

## B.4.1 Physical chemistry of macromolecules

| Course / resource | Instructor | Note |
|---|---|---|
| **Biophysical Chemistry (full course)** | Erik Lindahl (KTH/Stockholm) | [▶](https://www.youtube.com/@eriklindahl) — thermodynamics, kinetics and simulation taught by someone who writes the software |
| MIT 5.60 Thermodynamics & Kinetics | MIT OCW | Classical, rigorous, free |
| **Physical Biology of the Cell** lectures | Rob Phillips (Caltech) | Order-of-magnitude biology; the best training in estimation in all of biology |
| Molecular Biophysics lectures | NPTEL / various | — |

**Required reading, and these are short:** **Dill & Bromberg, *Molecular Driving
Forces*** — the best textbook in this entire curriculum, and the one to work
through with a pencil. **Phillips et al., *Physical Biology of the Cell*** —
read it for the estimation culture, not the content.

> **Derivation checkpoint 1.** Compute, from scratch, the free energy cost of
> burying a charged residue in a protein core. Use a Born solvation estimate and
> a reasonable interior dielectric. Then explain why that number is both roughly
> right and systematically wrong, and what the protein actually does about it.
>
> **Checkpoint 2.** Estimate the entropic cost of restraining a single rotatable
> bond on binding. Then multiply by the number of rotatable bonds in a 14-residue
> macrocycle and ask yourself what cyclization is buying.

---

## B.4.2 The forces, one at a time

The whole module compresses to understanding five contributions and their
magnitudes, because every scoring function in Atlas A and L is an attempt to
approximate them:

| Force | Rough magnitude | What usually goes wrong |
|---|---|---|
| **Hydrophobic effect** | ~25 cal/mol/Å² of buried nonpolar surface | It is entropic at room temperature and the temperature dependence is almost never modeled |
| **Hydrogen bonds** | 1–5 kcal/mol, but ~0 net in water | The desolvation penalty nearly cancels the bond; this is why H-bond counting overpredicts affinity |
| **Electrostatics** | Huge, and screened | Dielectric is not a constant; buried pairs behave nothing like surface pairs |
| **Van der Waals** | Small individually, decisive collectively | Packing density, not pair energies, is what distinguishes real cores |
| **Conformational entropy** | 0.5–1.5 kcal/mol per restrained side chain | Omitted from nearly every design score function |

**Papers:** **Chandler 2005, *Nature* 437:640 (interfaces and the driving force
of hydrophobic assembly)** · Baldwin 2007, *J Mol Biol* 371:283 · Pace et al.
2014, *J Biol Chem* 289:19165 (contribution of hydrogen bonding to stability) ·
**Fleming & Rose 2005, *Protein Sci* 14:1911** · Dill 1990, *Biochemistry*
29:7133 (**dominant forces in protein folding — the review to read first**).

> **The most useful single fact in this module.** A hydrogen bond in water is
> worth close to nothing net, because forming it requires breaking two bonds to
> water. Design scoring functions that reward hydrogen bonds therefore
> systematically overvalue polar interfaces. **This is a known, quantified,
> decades-old result, and it is still visibly present in design output** — which
> is exactly why interfaces that score beautifully bind weakly.

---

## B.4.3 Protein structure and folding

| Resource | Note |
|---|---|
| **IPD lecture 1: Intro + review of protein structure** (41:06) | [▶](https://youtu.be/TUyo8NFi_3Q) |
| **IPD lecture 2: Protein Geometry** (1:09:31) | [▶](https://youtu.be/q1pcAqOgYac) |
| Branden & Tooze, *Introduction to Protein Structure* | The fold atlas; skim, do not read |
| Petsko & Ringe, *Protein Structure and Function* | Short and excellent |
| **Energy landscape theory** | → Atlas H.5 (Onuchic, Wolynes, Dill, Chan) |

**Papers:** Ramachandran et al. 1963, *J Mol Biol* 7:95 · **Anfinsen 1973,
*Science* 181:223** · Richardson 1981, *Adv Protein Chem* 34:167 (**the anatomy
and taxonomy of protein structure — still the best single document on folds**) ·
Levinthal 1969 · **Bryngelson & Wolynes 1987, *PNAS* 84:7524 (the funnel)**.

> **Derivation checkpoint 3.** Explain the Ramachandran plot from steric clashes
> alone — which regions are forbidden, by which atoms, and why glycine and
> proline differ. Then explain why a rotamer library exists at all, which is
> **checkpoint 4**, and why the backbone-dependent version is better, which is
> the beginning of Atlas L.

---

## B.4.4 Enzymology and catalysis

| Resource | Note |
|---|---|
| Fersht, *Structure and Mechanism in Protein Science* | **The canonical text; chapters on transition state theory and catalysis are essential** |
| MIT 5.08J / Harvard enzymology lectures | OCW |
| **Enzyme design talks** | → Atlas R.5 |

**Papers:** **Pauling 1946, *Chem Eng News* 24:1375 (transition state
stabilization — two pages)** · Warshel et al. 2006, *Chem Rev* 106:3210
(**electrostatic basis for enzyme catalysis**) · Bruice 2002, *Acc Chem Res*
35:139 (near attack conformations) · **Kamerlin & Warshel 2010, *Proteins*
78:1339 (at the dawn of the 21st century: is dynamics the missing link?)** ·
Blomberg et al. 2013, *Nature* 503:418.

> **The Warshel-versus-dynamics argument is worth following carefully**, because
> it is the clearest case in biochemistry of a well-posed mechanistic question
> that resisted resolution for twenty years. Warshel's position — catalysis is
> electrostatic preorganization, and "dynamics" adds nothing beyond
> transition-state theory — is the one to understand first, and the one most
> design papers implicitly assume without saying so.
>
> **Derivation checkpoint 5.** Write down the rate enhancement a perfectly
> preorganized active site can provide, from transition-state theory, and compare
> it to the enhancements achieved by designed enzymes in Atlas R.5. The gap is
> roughly ten orders of magnitude and nobody fully knows why.

---

## B.4.5 Nucleic acids

| Resource | Note |
|---|---|
| Bloomfield, Crothers & Tinoco, *Nucleic Acids* | The reference |
| SantaLucia nearest-neighbor thermodynamics | The basis of every melting-temperature calculation |
| **RNA structure and design** | → Atlas Q.5 |

**Papers:** **SantaLucia 1998, *PNAS* 95:1460 (unified nearest-neighbor
parameters)** · Turner & Mathews 2010, *NAR* 38:D280 (NNDB) ·
Tinoco & Bustamante 1999, *J Mol Biol* 293:271 (**how RNA folds**) ·
Leontis & Westhof 2001, *RNA* 7:499 (**base-pair classification — the
vocabulary RNA structure papers assume you have**).

> **Derivation checkpoint 6.** Compute the melting temperature of a 14-mer
> duplex from nearest-neighbor parameters by hand. Then explain why the same
> machinery works far less well for RNA secondary structure, and what that
> implies for the difficulty gap between RNA and protein structure prediction
> you will meet in Atlas Q.5.

---

## B.4.6 Experimental methods — enough to read a figure honestly

**You do not need to run these. You need to know what their error bars mean**,
because every structure, affinity and stability number you train on came from
one of them.

| Method | What it actually measures | What it cannot tell you |
|---|---|---|
| X-ray crystallography | Electron density, averaged over the crystal | Anything about the solution ensemble; crystal contacts can lock conformations |
| Cryo-EM | A density map from averaged particles | Local resolution varies enormously; flexible regions vanish |
| NMR | Ensembles consistent with restraints | Size limited; restraints are averages over states |
| SPR / BLI | Association and dissociation kinetics | Surface immobilization changes avidity |
| ITC | **Enthalpy directly** — the only method that does | Needs lots of material |
| DSF / thermal shift | A melting temperature | Not ΔG at your temperature of interest |
| Yeast display / deep mutational scanning | Relative enrichment | Not affinity; expression confounds everything |

**Papers:** **Fowler & Fields 2014, *Nat Methods* 11:801 (deep mutational
scanning)** · Rodrigues & Bonvin 2014 (on interpreting interface data) ·
**Wlodawer et al. 2008, *FEBS J* 275:1 (protein crystallography for
non-crystallographers — read before you trust a PDB entry)**.

> **The most important row in that table is the last one.** Deep mutational
> scanning data — which trains ProteinGym, ThermoMPNN and half of Atlas Q — is
> enrichment in a selection, not a thermodynamic quantity. **Expression,
> stability and binding are confounded in a single number**, and models trained
> on it learn the confound. Tsuboyama's mega-scale stability dataset is valuable
> precisely because it separates them.

---

## B.4.7 Paired reading — B.4

| Watch this | Then read this | Hold this question |
|---|---|---|
| Lindahl, *Biophysical Chemistry* | **Dill & Bromberg, *Molecular Driving Forces*, ch. 1–10** | Work the problems. This is the one textbook to do properly. |
| Phillips, *Physical Biology of the Cell* | The book's estimation chapters | Estimate three quantities in your own project before computing them. |
| — | **Dill 1990, *Biochemistry* 29:7133** | Rank the forces by magnitude. Which does your score function model worst? |
| — | **Chandler 2005, *Nature* 437:640** | Why is the hydrophobic effect length-scale dependent? |
| — | Pace et al. 2014, *J Biol Chem* 289:19165 | What is a hydrogen bond worth in water, net? |
| IPD lectures 1–2 | **Richardson 1981, *Adv Protein Chem* 34:167** | Learn twenty folds by sight. It pays off constantly. |
| — | **Anfinsen 1973, *Science* 181:223** then **Bryngelson & Wolynes 1987, *PNAS* 84:7524** | Sequence determines structure. What did the funnel add? |
| Atlas R.5 enzyme talks | **Warshel et al. 2006, *Chem Rev* 106:3210** | Preorganization versus dynamics. Take a side and defend it. |
| — | **Pauling 1946** (two pages) | Then compare designed enzyme rate enhancements to the theoretical ceiling. |
| — | **SantaLucia 1998, *PNAS* 95:1460** | Compute a Tm by hand. Why is RNA harder? |
| — | **Fowler & Fields 2014, *Nat Methods* 11:801** | What is a DMS score, physically? What is confounded in it? |
| — | **Wlodawer et al. 2008, *FEBS J* 275:1** | Before trusting a PDB entry: what do you check? |
