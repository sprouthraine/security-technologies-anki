# Lecture 4 – Practice Exercises & Solutions: Airport Security Screening

> **Part 1** reproduces the official *Lecture 4 Problem Sheet* (with model answers, /20 marks). **Part 2** adds extra practice questions in the same style.

---

# PART 1 – Official Problem Sheet

### Q1. Describe briefly what a drug smuggler can do to avoid a small package of cocaine being detected by a millimetre-wave whole-body scanner. [1]
**Solution:** Transport it **internally**, by swallowing it or hiding it inside a **body cavity**. mm-waves penetrate clothing but **not skin**.

### Q2. Describe the operation of a mm-wave whole-body scanner with reference to (a) hardware, (b) imaging and (c) threat detection. [4]
**Solution**
- **(a) Antennas:** the person steps into a booth surrounded by **2 antennas** (front and back), each **transmitting and receiving** mm-waves. They **rotate** around the subject and are protected by a plastic **radome** that is transparent to mm-waves. Each antenna is an **array** of many small elements.
- **(b) Imaging:** the mm-waves **penetrate clothing** and **reflect off skin** and concealed objects. Rotation captures snapshots from different angles. The antennas detect the reflected energy, and the array configuration (digital beamforming) locates the reflection points exactly, producing a **high-resolution 3D image**.
- **(c) Threat detection:** uses **reflected signal strength** (different materials reflect differently, which allows material discrimination); **image analysis** (shape detection, pattern matching); and **Automatic Target Detection (ATD)** algorithms for metallic and non-metallic objects, weapons, and explosives (gels, plastics, powders).

### Q3. State one advantage and one disadvantage of metal detectors. [2]
**Solution**
- **Advantages (any one):** very low cost (under £5k walkthrough, about £100 portable); high throughput (~500 people/hr); easy to set up and deploy (train stations, schools, concerts, sports events).
- **Disadvantage:** cannot detect **non-metals**, such as 3D-printed weapons, plastic explosives and drugs.

### Q4. Soft X-rays have frequencies of 10¹⁶ – 10¹⁸ Hz. What is the frequency range of hard X-rays? [1]
**Solution:** **10¹⁸ – 10²⁰ Hz**

### Q5. A baggage scanner transmits X-rays of frequency 3.5 × 10¹⁸ Hz. Calculate the photon energy in keV to 1 d.p. (h = 6.63 × 10⁻³⁴ J s; 1 eV = 1.602 × 10⁻¹⁹ J) [4]
**Solution**
- E = hf = 6.63 × 10⁻³⁴ × 3.5 × 10¹⁸ = **2.3205 × 10⁻¹⁵ J**
- Convert to eV: 1 J = 1/1.602 × 10⁻¹⁹ = 6.242 × 10¹⁸ eV, so E = 2.3205 × 10⁻¹⁵ × 6.242 × 10¹⁸ = **14,484.6 eV**
- ÷ 1000 gives **E = 14.5 keV**

### Q6a. State the two processes that cause an EM wave to lose energy during attenuation. [1]
**Solution:** **Scattering** (deflection) and **absorption**.

### Q6b. An 80 keV X-ray system is tested on RDX plastic explosive (µ = 30 m⁻¹ at 80 keV). Use the Beer–Lambert law to find the thickness at which the intensity halves, to 2 d.p. [4]
**Solution**
- I/I₀ = e^(−µx), so 0.5 = e^(−30x)
- ln 0.5 = −30x
- x = ln 0.5 / (−30) = 0.0231 m = **2.31 cm**

### Q7. An X-ray spectrum from electron bombardment of a metal target shows a continuum (b), the bremsstrahlung, with sharp peaks (a) on top. [3]
**[a] Name the peaks. [b] Explain how they are generated.**

**Solution**
- **[a]** **Characteristic X-ray peaks / characteristic radiation** (K-peaks: Kα and Kβ).
- **[b]**
  - An incoming high-energy electron **collides with and ejects an inner-shell electron** (a photoelectron) from a target atom, leaving a **vacancy**. The atom is no longer in its ground state.
  - An electron from a **higher energy shell drops down** to fill the vacancy, **emitting an X-ray** with energy equal to the difference between the shell energies.
  - Each element has unique shell energies, so the X-ray energies are **characteristic of the element**. A transition from n = 2 to n = 1 gives **Kα**; from n = 3 to n = 1 gives **Kβ**.

---

# PART 2 – Extra Practice Questions

## Section A – History, Privacy & Safety

### Q8. Why is airport security described as "reactive"? Give three examples. [4]
**Solution:** New measures have mostly been introduced **after** attacks:
- **Lockerbie 1988:** X-ray screening of all checked luggage
- **9/11 2001:** liquids, gels and toiletries rules
- **Shoe bomber 2001:** shoe scanning in the US
- **1974 LAX bomb:** metal detectors and X-ray at all US airports

### Q9. List three privacy safeguards used with whole-body scanners. [3]
**Solution:** Images are viewed in a separate out-of-sight room and **immediately deleted** (never stored); the operator never sees the passenger; identifying details are removed (blurred faces, or a **generic mannequin/outline**).

### Q10. Why did the TSA remove backscatter X-ray scanners in 2013, and why are mm-wave scanners preferred? [3]
**Solution**
- Backscatter was removed over **privacy** concerns. It also uses **ionising** X-rays, which can remove electrons, kill cells and cause mutations or cancer (the dose is small: about 2 minutes of flying).
- mm-wave is **non-ionising** (about 10⁻⁴ – 10⁻³ eV), emits less than a mobile phone, and gives a 3D image.

## Section B – mm-Wave Physics

### Q11. Calculate the photon energy (in eV) of a 25 GHz mm-wave, and state whether it is ionising. [3]
**Solution**
- E = hf = 6.63 × 10⁻³⁴ × 25 × 10⁹ = 1.66 × 10⁻²³ J
- ÷ 1.602 × 10⁻¹⁹ = **1.03 × 10⁻⁴ eV**
- This is far below the ~10 eV ionising threshold, so it is **non-ionising**. Its only biological effect is heating.

### Q12. At what power density does tissue heating become significant, and how does the L3 ProVision 2 compare? [2]
**Solution:** **5 mW cm⁻²** (temperature rise above 0.5 °C). The ProVision 2 operates at **6 × 10⁻⁶ mW cm⁻²**, about a million times lower, so there is no heating effect.

### Q13. An airport must screen 1,000 passengers. How long would this take with (a) one walkthrough metal detector, (b) one mm-wave scanner at 250/hr, (c) one backscatter unit? [3]
**Solution**
- (a) 1000/500 = **2 h**
- (b) 1000/250 = **4 h**
- (c) 1000/100 = **10 h**

## Section C – Metal Detectors

### Q14. Explain pulse induction in a walkthrough metal detector, with and without metal present. [5]
**Solution**
- **Without metal:** a short current pulse through a coil creates a temporary magnetic field. When the pulse ends, the field reverses and collapses, inducing a short **reflected pulse** (~**30 µs**) by Faraday's law. This repeats about 100 times per second.
- **With metal:** the pulse induces a magnetic field of **opposite polarity** in the metal object. This **prolongs the reflected pulse** (≫ 30 µs). A **sampling circuit** detects the slower decay and raises an alarm.

## Section D – X-Ray Physics

### Q15. Describe how X-rays are produced in an X-ray tube. [4]
**Solution**
1. **Thermionic emission:** a heated cathode filament boils off electrons.
2. An **anode** with a potential difference of 10³ – 10⁶ V accelerates them.
3. They strike a **tungsten** target, producing characteristic and bremsstrahlung X-rays.
4. This happens in an evacuated glass tube with **lead casing**.

### Q16. Explain bremsstrahlung radiation and the maximum-energy limit. [3]
**Solution**
- Electrons pass close to the nucleus without ejecting a photoelectron. Their path curves and they **decelerate ("brake")**, emitting the lost energy as a **continuous** X-ray spectrum.
- **Maximum energy:** a head-on collision with the nucleus converts **all** of the electron's kinetic energy into a single X-ray photon.

### Q17. A scanner emits X-rays at 1.2 × 10¹⁹ Hz. Find the photon energy in keV (2 d.p.). Is this a hard or soft X-ray? [3]
**Solution**
- E = 6.63 × 10⁻³⁴ × 1.2 × 10¹⁹ = 7.956 × 10⁻¹⁵ J
- ÷ 1.602 × 10⁻¹⁹ = 49,662.9 eV = **49.66 keV**
- **Hard** X-ray (f > 10¹⁸ Hz)

### Q18. X-rays at 50 keV pass through 2.5 cm of (a) bone (µ = 330 m⁻¹) and (b) muscle (µ = 50 m⁻¹). What percentage is transmitted? [4]
**Solution**
- (a) e^(−330 × 0.025) = e^(−8.25) = 2.61 × 10⁻⁴, so **0.026%**
- (b) e^(−50 × 0.025) = e^(−1.25) = 0.2865, so **28.7%**
- Bone attenuates far more, which is why it shows up white on X-ray images.

### Q19. Find the half-value thickness of lead (µ = 600 m⁻¹) in mm, and the percentage transmitted through 5 mm of lead. [4]
**Solution**
- x½ = ln 2 / µ = 0.693/600 = 1.155 × 10⁻³ m = **1.16 mm**
- 5 mm: e^(−600 × 0.005) = e^(−3) = 0.0498, so **4.98%**

### Q20. What thickness of bone (µ = 330 m⁻¹) reduces X-ray intensity to 10%? [3]
**Solution:** x = −ln(0.1)/330 = 2.3026/330 = 6.98 × 10⁻³ m ≈ **0.70 cm**

### Q21. What is the difference between the linear and mass attenuation coefficients? [2]
**Solution:** The linear coefficient µ (m⁻¹) is the fraction of the beam absorbed or scattered per unit thickness. The mass attenuation coefficient µₘ is normalised by density: **µ = µₘ × ρ**. Both depend on X-ray energy.

## Section E – Real-World X-Ray Systems

### Q22. Compare Standard, Dual-energy, Transmission/Backscatter and CT X-ray systems. [8]
**Solution**
| System | How it works | Strengths | Weaknesses |
|---|---|---|---|
| Standard | Source on one side, detectors on the other, giving a 2D greyscale shadowgram | High throughput, low cost; good for guns and knives | Shape only; operator-dependent; poor for explosives and drugs; high false alarms |
| Dual-energy | High- and low-energy beams, two images compared, giving Z_eff | Colour-codes organic, inorganic and metal | Still 2D |
| Transmission + backscatter | Transmission detector (absorption) plus scatter detector (density) | Good discrimination of low-Z (organic) threats | More expensive; not as safe as mm-wave for people |
| CT | Rotating source and detectors; tomograms combined by tomographic reconstruction into 3D | High-resolution 3D; density + Z_eff; automatic alarms (cocaine, TNT, guns, liquids) | Low throughput; high cost |

### Q23. In a dual-energy X-ray image, what do orange, green and blue represent, and what are the Z_eff bands? [3]
**Solution:** **Orange = organic** (Z_eff 0–10); **green = inorganic** (~10–19); **blue = metallic** (above ~19).

### Q24. What is Z_eff? [1]
**Solution:** The **effective atomic number**: the average atomic number of a compound or mixture.

### Q25. What weakness did the Brussels Airport attack (22 March 2016) expose, and what solutions were proposed? [3]
**Solution**
- The bombers attacked the **check-in area, before any security checkpoint**. Screening focuses on keeping threats off planes, not on the landside public areas.
- **Solutions:** move checkpoints to the entrances (but this creates new queues that become targets), or **scan people remotely while they keep moving** using nimbler or new sensors.
