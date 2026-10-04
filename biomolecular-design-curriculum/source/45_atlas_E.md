# Atlas E — Free Energy

> **Problem.** Compute a binding affinity, a solvation free energy, or a ΔΔG of
> mutation that an experimentalist would bet on.
>
> This family has the most mature error theory in computational biology and the
> widest gap between what is possible and what is typically done. The methods
> are rigorous. The practice frequently is not.

---

## E.1 The standing resource

**The 2018 free energy workshop — 43 talks, every one enumerated in Appendix B.4.** This
is the densest single archive on free energy calculation anywhere, covering
theory, methods, software, and a blunt assessment of what works. Several of the
talks are by people who build the methods arguing with each other about
protocol, which is the most instructive content in the field.

| Archive | Contents | Link |
|---|---|---|
| **Alchemistry.org** | Method documentation, best practices, the workshop | [alchemistry.org](http://www.alchemistry.org) |
| **Chodera lab channel** | The 2018 workshop talks | [▶](https://www.youtube.com/@choderalab) |
| **Open Force Field Initiative** | Parameterization and benchmarking talks | [▶](https://openforcefield.org) |
| **D3R / SAMPL challenges** | Blind prediction results and post-mortems | [drugdesigndata.org](https://drugdesigndata.org) |

> **SAMPL is the CASP of free energy, and almost nobody outside the field knows
> it exists.** Blind challenges on host-guest binding, solvation free energies
> and partition coefficients, with results published whether good or bad. The
> post-mortem papers are the most honest writing in computational chemistry.

---

## E.1b The recorded literature, filled

The second edition pointed at the Chodera workshop without enumerating it. **All
43 talks are now in Appendix B.4.** What follows is the rest of the family.

### Alchemical foundations

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **Free energies: What we've learned about how to estimate them** | **Michael Shirts** (CU Boulder, MBAR author) | 30:13 | [▶](https://www.youtube.com/watch?v=fhMjOYvnGcY) |
| Estimator variance and convergence diagnosis | Michael Shirts | 29:49 | [▶](https://www.youtube.com/watch?v=pCQeSE9JAXk) |
| **A guide to multistate reweighting** — the MBAR tutorial proper | Michael Shirts | 36:27 | [▶](https://www.youtube.com/watch?v=yGyQa8opfi0) |
| Teaching free energy calculations to learn | **John Chodera** (MSKCC) | 29:22 | [▶](https://www.youtube.com/watch?v=NiQYxnKx7kw) |
| **Developing and Using FE Calculations to Guide Lead Optimization** | **David Mobley** (UC Irvine) | 1:00:03 | [▶](https://www.youtube.com/watch?v=ZahfL03lujo) |
| Introduction to Free Energy Calculations | **Christophe Chipot** (CNRS/UIUC) | 56:09 | [▶](https://www.youtube.com/watch?v=LCKtsR1ijsA) |
| **A General Overview of Free Energy Methods** | Christophe Chipot | 1:30:38 | [▶](https://www.youtube.com/watch?v=OEmxv5GnywA) |
| **Accurate Calculation of Protein-Ligand Binding Energies** | Christophe Chipot | 1:40:42 | [▶](https://www.youtube.com/watch?v=_guJYDwm5mU) |
| Introduction to Free-Energy Calculations, Part 1 | Christophe Chipot | 1:31:10 | [▶](https://www.youtube.com/watch?v=zn7Fd6F9lB0) |
| Introduction to Free-Energy Calculations, Part 2 | Christophe Chipot | 1:32:55 | [▶](https://www.youtube.com/watch?v=WIdZNjZFGRM) |
| **Geometrical Free Energy Methods** (the CV/PMF route) | Giacomo Fiorin (NIH, Colvars author) | 2:25:35 | [▶](https://www.youtube.com/watch?v=iLw7acCoCrs) |
| Accelerating Convergence with replica-exchange alchemy | Wei Jiang (Argonne) | 1:11:26 | [▶](https://www.youtube.com/watch?v=Duq09xMTzgc) |
| Introduction to free energy calculations (GROMACS-flavoured) | BioExcel | 55:25 | [▶](https://www.youtube.com/watch?v=-FAdiM7PkWc) |
| **A rigorous statistical-mechanics-first derivation** | Leandro Martínez (UNICAMP) | 1:34:46 | [▶](https://www.youtube.com/watch?v=xBUYrEAgzz4) |
| Statistical-mechanical basis of binding free energy | **Benoit Roux** (Chicago) | 33:43 | [▶](https://www.youtube.com/watch?v=k6B6U0dvf2o) |
| λ-dynamics and multisite λ-dynamics | **Charles Brooks III** (Michigan) | 30:56 | [▶](https://www.youtube.com/watch?v=IhXUxA_Qr_g) |
| Constant-pH and charge-change alchemy | Thomas Simonson (Polytechnique) | 30:44 | [▶](https://www.youtube.com/watch?v=KFPCq783_PQ) |
| **Soft-core potentials and the end-point singularity** | Darrin York (Rutgers) | 26:16 | [▶](https://www.youtube.com/watch?v=cQQM1DTLR5g) |
| Reducing free energy simulations to the bare essentials | Stefan Boresch (Vienna) | 23:34 | [▶](https://www.youtube.com/watch?v=2HX_Fwz4znI) |
| Polarizable force fields in alchemy (AMOEBA) | Jay Ponder (WashU) | 30:23 | [▶](https://www.youtube.com/watch?v=I2zm3hAO-eI) |
| **Binding free energy calculations with non-equilibrium alchemy** | **Vytautas Gapsys** (MPI-NAT) | 52:01 | [▶](https://www.youtube.com/watch?v=hHCUW50cRuA) |
| Free Energy Calculations with BioSimSpace | CCPBioSim | 19:45 | [▶](https://www.youtube.com/watch?v=YG5r6vUebhQ) |
| **MDAnalysis and alchemlyb** — not fooling yourself with your own estimator | Richard Gowers (OpenFE) | 35:31 | [▶](https://www.youtube.com/watch?v=MIQAm5SbJtw) |
| Open Free Energy: Open Source Alchemy | Hannah Baumann (OpenFE) | 22:03 | [▶](https://www.youtube.com/watch?v=ZDQcmPvd-1E) |
| Engineering FEP science in the open | Julien Michel (Edinburgh) | 31:18 | [▶](https://www.youtube.com/watch?v=id5D_9PC1mA) |
| **Free energy of solids: the 1983 CECAM workshop retrospective** | CECAM | 3:17:06 | [▶](https://www.youtube.com/watch?v=-oqN-bMnPjs) |

**Shirts's thirty minutes is the best overview talk in this family. Start
there.** Then his MBAR tutorial, then Chipot's long survey.

### Industrial practice, and the skeptics

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **FEP and Drug Discovery: Where We've Been and Where We'd Like to Go** | **Derek Lowe** (Novartis, *In the Pipeline*) | 35:09 | [▶](https://www.youtube.com/watch?v=HSh4AzzhGKM) |
| **Promises and Limitations: Free Energy Methods in Drug Discovery Projects** | Xin Yan (Merck) | 26:51 | [▶](https://www.youtube.com/watch?v=bRX2yxa3laA) |
| **The FEP+ author on the FEP+ benchmark** | **Lingle Wang** (Schrödinger) | 35:36 | [▶](https://www.youtube.com/watch?v=zNkRZENCg-8) |
| Updated FEP+ results | Lingle Wang | 30:08 | [▶](https://www.youtube.com/watch?v=OMzzwbxu93I) |
| IFD-MD and FEP+ with AlphaFold inputs | Márton Vass (Schrödinger) | 55:23 | [▶](https://www.youtube.com/watch?v=92K8gbk6WhA) |
| **Physics-Driven Discovery of SNX281** | **Woody Sherman** (Silicon Therapeutics) | 54:06 | [▶](https://www.youtube.com/watch?v=luPTHy2FRV8) |
| From Concept to Clinic: a non-CDN STING agonist | Woody Sherman (Psivant) | 29:15 | [▶](https://www.youtube.com/watch?v=VEXAc_jYWPA) |
| **Free Energy Calculations from Butane to COVID-19** | **William Jorgensen** (Yale) | 36:33 | [▶](https://www.youtube.com/watch?v=a2axeq_E3RQ) |
| Absolute binding free energy for pose prediction | David Minh (IIT) | 23:25 | [▶](https://www.youtube.com/watch?v=LPYzLZ1WmG4) |
| Active learning for absolute binding free energies | Steven Jerome (Broad) | 23:11 | [▶](https://www.youtube.com/watch?v=boQ5VDYvMKM) |
| Large-scale alchemical screening with GROMACS/pmx | BioExcel #63 | 54:29 | [▶](https://www.youtube.com/watch?v=hXg61gmpQw4) |

> **Lowe's talk is the most useful skeptical hour in this family** — a working
> medicinal chemist on what FEP has and has not delivered. **Pair it immediately
> with Lingle Wang's FEP+ advocacy.** Yan's is the industrial retrospective on
> prospective failures. **Jorgensen's is the field's founder narrating forty
> years of it**, having run the first FEP on a biomolecular system.

### Blind challenges

**D3R 2019 Community Discussion on the Future of Blinded Prediction
Challenges**, 1:09:32 ([▶](https://www.youtube.com/watch?v=UAYm7Hs82KY)) — **the
single most valuable blind-challenge retrospective available**, the field
arguing openly about what the challenges actually measured · the 2018 version
([▶](https://www.youtube.com/watch?v=q9KwQiV_MeM)) · Chodera's submission
post-mortem ([▶](https://www.youtube.com/watch?v=Y6TbBE3gp-I)) · Gapsys under
blind conditions ([▶](https://www.youtube.com/watch?v=QJq6v7fLFmA)) · Mobley on
SAMPL ([▶](https://www.youtube.com/watch?v=h2fFILu5E7U)) · **Patrick Walters on
why most reported blind-challenge rankings are not statistically significant**
([▶](https://www.youtube.com/watch?v=P2mMIQOKF1s)) · **the SAMPL6 pKa challenge,
where nearly every method failed informatively**
([▶](https://www.youtube.com/watch?v=njouUbHEVP0)).

### Nonequilibrium methods

**Christopher Jarzynski himself** — *Scaling down the laws of thermodynamics*,
1:14:06 ([▶](https://www.youtube.com/watch?v=OQhNdgjjwBk)) · *Nonequilibrium
Statistical Mechanics II*, a proper lecture-course treatment
([▶](https://www.youtube.com/watch?v=Epud4i_Y5KM)) · strong-coupling
corrections, which matter when the "system" is a ligand in a binding site
([▶](https://www.youtube.com/watch?v=0u5vrtgGBh4)) · nanoscale thermodynamics
([▶](https://www.youtube.com/watch?v=nk8R9-nQvjo)).

**Also:** the LMU biophysics lecture covering **both Jarzynski and Crooks
properly** ([▶](https://www.youtube.com/watch?v=7LyHDQnmmro)) · a two-hour
derivation ([▶](https://www.youtube.com/watch?v=gsq3irAz8Ok)) · **Giovanni Bussi
connecting the fluctuation theorems to practical steered MD** — the bridge the
other talks skip ([▶](https://www.youtube.com/watch?v=Fpiy-66bl1U)).

### ΔΔG of mutation

**pmx from its authors** — Gapsys and de Groot, BioExcel #4, 1:02:18
([▶](https://www.youtube.com/watch?v=tIAzMZP8BlU)) · the current pmx
([▶](https://www.youtube.com/watch?v=ZqWdo_2YZdg)) · the teaching version
([▶](https://www.youtube.com/watch?v=XE-xOhFRJn4)) · applications to protein
stability and resistance mutations
([▶](https://www.youtube.com/watch?v=MdaTPYLL2Gs)) · **the one honest,
non-promotional MM-GBSA tutorial**, Brandon Havranek (Drexel)
([▶](https://www.youtube.com/watch?v=goheM2OvfWk)).

> **Two gaps that matter, both critical rather than foundational.** There is
> **no good critical MM-PBSA lecture on YouTube** — that search space is almost
> entirely uncritical tutorial-mill content. Use **Genheden & Ryde 2015, *Expert
> Opin Drug Discov* 10:449** and Hou et al. 2011, *JCIM* 51:69.
>
> And there is **no talk at all on the ΔΔG anti-symmetry failure**; the only
> FoldX videos are promotional. That literature is **Usmanova et al. 2018,
> *Bioinformatics* 34:3653**, Pucci et al. 2018, *Bioinformatics* 34:3659, and
> Caldararu et al. 2021, *Sci Rep* 11:9234. **Derivation checkpoint 28 is this
> gap.**

---

## E.2 The estimators

| Topic | Resource | Link |
|---|---|---|
| Thermodynamic integration, FEP, BAR, MBAR | Alchemistry workshop talks | [▶](https://www.youtube.com/@choderalab) |
| **Free energy perturbation theory** | CECAM free energy schools | → Atlas B.8 |
| **FEAT: Free energy Estimators with Adaptive Transport** | Du & He (Valence) | [▶](https://youtu.be/D-VriormkRM) |
| Alchemical pathways in practice | BioExcel PMX workshop recordings | [▶](https://www.youtube.com/@BioExcelCoE) |

**Papers, and this is a short canonical list:** Zwanzig 1954, *JCP* 22:1420
(FEP) · Kirkwood 1935, *JCP* 3:300 (thermodynamic integration) ·
**Bennett 1976, *J Comput Phys* 22:245 (BAR)** · **Shirts & Chodera 2008,
*JCP* 129:124105 (MBAR) [the one to internalize]** · Crooks 1999, *PRE* 60:2721
(the fluctuation theorem) · **Jarzynski 1997, *PRL* 78:2690** · Pohorille,
Jarzynski & Chipot 2010, *JPCB* 114:10235 (good practices).

> **Derivation checkpoint 26.** Derive BAR from the Crooks fluctuation theorem.
> Then show that MBAR is its multi-state generalization and that it is the
> minimum-variance unbiased estimator given the samples you have. This is the
> single most elegant derivation in the Atlas and it takes an afternoon.
>
> **Checkpoint 27.** Explain why the Zwanzig exponential average is correct in
> expectation but useless in practice — the variance argument, with the
> overlap integral written down explicitly.

---

## E.3 Binding free energies

| Topic | Talk / resource | Link |
|---|---|---|
| Absolute binding free energy | Alchemistry workshop; Gilson/Mobley talks | [▶](https://www.youtube.com/@choderalab) |
| Relative binding free energy (RBFE) | Open Force Field, FEP+ benchmark talks | [▶](https://openforcefield.org) |
| **Boltz-2: affinity prediction** | Valence | [▶](https://youtu.be/iHDauMATkr0) |
| **Quantitative Affinity Data at Scale: the Data Bottleneck** | Murakowska (BPDMC) | [▶](https://youtu.be/tjAPYPpQylo) |
| MM-GBSA and endpoint methods | — | see note below |

**Papers:** Gilson et al. 1997, *Biophys J* 72:1047 (the statistical-thermodynamic
basis) · **Mobley & Gilson 2017, *Annu Rev Biophys* 46:531 (binding free energy
calculations — the review)** · Wang et al. 2015, *JACS* 137:2695 (FEP+ on
congeneric series) · Cournia et al. 2017, *JCIM* 57:2911 · **Schindler et al.
2020, *JCIM* 60:5457 (large-scale industrial FEP benchmark)** · Genheden &
Ryde 2015, *Expert Opin Drug Discov* 10:449 (MM-PBSA/GBSA review).

> **On MM-GBSA, since you use it.** It is fast and it is not a free energy
> calculation. It omits the entropy term or approximates it badly, it is
> extremely sensitive to the solute dielectric, and its correlation with
> experiment across *unrelated* ligands is typically poor. Where it works is
> **ranking within a congeneric series with consistent protocol** — which is a
> real and useful thing, just not the thing the name suggests. Genheden & Ryde
> are honest about this; read them before quoting a number.
>
> **Alchemical FEP is the method that actually predicts affinity**, at roughly
> 1 kcal/mol RMSE on well-behaved congeneric series after substantial setup
> effort. The Schindler benchmark is what that looks like at industrial scale.

---

## E.4 ΔΔG of mutation and protein stability

| Resource | Note |
|---|---|
| PMX / BioExcel tutorials | Alchemical mutation setup end-to-end |
| FoldX, Rosetta ddg_monomer | Empirical, fast, and **systematically biased toward destabilizing** |
| **ThermoMPNN** tutorial (RosettaCommons, 42:39) | [▶](https://www.youtube.com/watch?v=vtusNLxgxTg) |
| **Mega-scale stability** (Tsuboyama, ML4PE, 50:57) | [▶](https://youtu.be/M3fARv8GYA8) |
| Antibody ΔΔG data requirements (Hummer, BPDMC, 1:14:43) | [▶](https://youtu.be/C7PnokVsT4I) |

**Papers:** Gapsys et al. 2016, *Chem Sci* 7:4728 (PMX, accurate alchemical
ΔΔG) · Steinbrecher et al. 2017, *J Mol Biol* 429:948 · **Tsuboyama et al.
2023, *Nature* 620:434 (the 500,000-measurement dataset that changed what is
trainable)** · Dieckhaus et al. 2024, *PNAS* 121:e2314853121 (ThermoMPNN) ·
Nisthal et al. 2019, *PNAS* 116:16367 · **Pancotti et al. 2022,
*Brief Bioinform* 23:bbab555 (the anti-symmetry audit — most ΔΔG predictors
fail the simple test that ΔΔG(A→B) = −ΔΔG(B→A))**.

> **The anti-symmetry test is the cheapest and most damning benchmark in this
> family.** A predictor should give exactly opposite answers for a forward and
> reverse mutation. Most do not, because they were trained on a dataset that is
> itself asymmetric — experimentalists report destabilizing mutations far more
> often. **Derivation checkpoint 28: explain how a training-set asymmetry
> becomes a model asymmetry, and design the correction.** That is a publishable
> idea stated as a homework problem.

---

## E.5 BUILD — Atlas E

1. **Run a relative binding free energy calculation** on a small congeneric
   series with known experimental affinities. Three or four ligands is enough.
2. **Compute the overlap** between neighboring lambda windows. If any pair has
   poor overlap, your result is wrong regardless of how small the error bar looks.
3. **Estimate with BAR and with the Zwanzig exponential average** from the same
   data. Compare both the values and the variances.
4. **Run the same series through MM-GBSA** and plot both against experiment.
5. **Write the one page.** Report RMSE and Spearman for each method, and state
   what you would need to halve the error.

**Derivation checkpoints due: 26, 27, 28.**

---

## E.6 Paired reading — Atlas E

| Watch this | Then read this | Hold this question |
|---|---|---|
| Alchemistry workshop, estimators | **Bennett 1976** then **Shirts & Chodera 2008** | Derive BAR from Crooks. Then show MBAR generalizes it. |
| Alchemistry workshop, overlap | Pohorille et al. 2010, *JPCB* 114:10235 | Write the overlap integral. At what value is a result untrustworthy? |
| Du & He, *FEAT* | The FEAT paper | Learned transport between thermodynamic states. What replaces lambda windows? |
| Mobley/Gilson talks | **Mobley & Gilson 2017, *Annu Rev Biophys* 46:531** | What are the standard-state and symmetry corrections, and when do they bite? |
| FEP+ benchmark talks | **Schindler et al. 2020, *JCIM* 60:5457** | Industrial scale, honest numbers. What is the actual RMSE distribution? |
| Valence, *Boltz-2 affinity* | The Boltz-2 paper | A learned affinity head. Against what data, and what is the generalization gap? |
| **Murakowska, *Affinity data bottleneck*** | Compare to Schindler 2020 | Is the limit the method or the measurements? |
| ThermoMPNN tutorial | **Tsuboyama et al. 2023, *Nature* 620:434** | 500k stabilities. What became trainable that was not before? |
| — | **Pancotti et al. 2022, *Brief Bioinform* 23:bbab555** | Run the anti-symmetry test on any ΔΔG predictor you use. |
| SAMPL post-mortems | Any SAMPL challenge overview paper | Blind prediction. What systematically went wrong, across groups? |
