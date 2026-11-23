# Lecture 4 – Airports: People Screening & Threat/Contraband Detection

*Source: Lecture 4 Parts 1–4 (Person Screening; mmWave; X-Ray Science; Real-World Systems), Lecture 4 Problem Sheet (Dr Kevin Chetty)*

## Learning Outcomes
- Describe the historically **reactive** nature of airport security
- Understand the privacy and safety features of whole-body scanners
- Explain the operating principles and hardware of whole-body scanners
- Explain **pulse induction** in metal detectors
- Judge which people-screening technologies suit which environments
- Describe how X-rays are produced (characteristic and bremsstrahlung)
- Use **Planck's law** for photon energy and the **Beer–Lambert law** for attenuation
- Compare **Standard, Dual-energy, Backscatter/Transmission and CT** X-ray systems
- Appreciate the security weaknesses that remain in airports and public areas

---

# PART 1 – PEOPLE SCREENING

## 1. History of Airport Security (Reactive Evolution)
- It began as bag and person searches to prevent **hijackings**. It then expanded to drug trafficking, contraband and identity confirmation. It is now on the **front line against terrorism**.
- **Key point:** each major incident triggered a new countermeasure.

| Date | Event | Response |
|---|---|---|
| 1974 | Bomb explodes at LAX | Metal detectors and X-ray screening at all US airports |
| 1976 | Cuban flight bomb, 73 killed | More prominent X-ray and metal-detector checks worldwide |
| 1980s | War on narcotics | Drug-sniffing dogs |
| 1986 | Ann Marie Murphy: bomb planted in her luggage by her boyfriend | New security questions ("has your bag been interfered with?") |
| 21 Dec 1988 | **Lockerbie bombing** (Pan Am), 270 killed | X-ray scanning of **all checked luggage** |
| 11 Sep 2001 | **9/11** coordinated attacks, 2,996 killed, >6,000 injured, >$10bn damage | New rules on **liquids, gels, toiletries** |
| 22 Dec 2001 | **Shoe bomber** (Richard Reid) | US passengers' **shoes scanned** |
| 2003 | — | First **Advanced Imaging Technology (AIT)** whole-body scanners; dogs trained for firearms and explosives |
| 2008 | — | TSA bans **lithium batteries** in checked luggage unless installed in devices |

## 2. Whole (Full) Body Scanners
- **Two types:**
  - **Millimetre-wave:** radio/microwaves, produces a **3D** image.
  - **Backscatter:** low-power **ionising X-rays**, produces a **2D** image.
- **Capabilities:**
  - Detect **metallic and non-metallic** items: liquid and plastic explosives, ceramic weapons, illicit drugs, all of which metal detectors miss.
  - **Non-intrusive** (no physical contact).
  - **Penetrate clothing but not skin**, so they detect contraband in or under clothing.
  - **Cannot detect items swallowed or hidden in body cavities.**

### 2.1 Privacy Features
- Images are viewed in a separate, out-of-sight room and **immediately deleted**; they are **never stored**.
- The operator does not see the passenger being scanned.
- Identifying details are removed (blurred faces, outline sketches). The US uses mm-wave exclusively, with a **generic outline/mannequin** image.

### 2.2 Safety
- mm-wave scanners emit **less energy than a mobile phone**.
- Backscatter X-ray exposure is about **2 minutes of flying**. It is insignificant but still a "dose".
- **Opt-out** in some countries (e.g. pregnant women), with an **enhanced pat-down** as an alternative. The question of whether passengers have the right to refuse remains debated.

### 2.3 Current Status
- **Expensive:** over **$250,000** per unit.
- **mm-wave is the scanner of choice.** X-rays are ionising: they remove electrons, can kill cells and cause mutations or cancer.
- The **TSA removed X-ray body scanners** from US airports in **2013** over privacy issues. Some countries (e.g. Russia) still use backscatter.

---

# PART 2 – MILLIMETRE-WAVE SCANNERS & METAL DETECTORS

## 3. Millimetre-Wave Scanners: The Science
- Use EM waves in the **microwave** region: **20–30 GHz**, wavelengths **15–10 mm**.

### 3.1 Hardware (Antennas)
- **2 antennas** (one front, one back), each **transmitting and receiving**.
- They **rotate** around the subject.
- They are protected by a plastic **radome**, which is transparent to mm-waves.
- Each antenna is an **antenna array** made of many small elements.

### 3.2 Imaging
- The transmitted mm-wave **penetrates clothing** and **reflects off skin** and any concealed objects.
- Rotation gives "snapshots" from different angles, and the reflected energy is received by the antennas.
- The array configuration plus **digital beamforming** locates the reflection points precisely, giving a **high-resolution 3D image**.

### 3.3 Threat Detection
- **Reflected signal strength:** different materials reflect different amounts, which allows **material discrimination**.
- **Image analysis:** shape detection and pattern matching.
- **Automatic Target Detection (ATD)** algorithms flag metallic and non-metallic objects, weapons, and explosives (gels, plastics, powders).

### 3.4 Biological Effects
- **Ionising** EM radiation needs energies **well above 10 eV**. X-rays are 100 eV – 100 keV.
  - **1 eV = 1.602 × 10⁻¹⁹ J.** The SI unit of energy (J) is kg m² s⁻².
- **mm-waves are non-ionising:** 1.2 × 10⁻⁴ to 1.2 × 10⁻³ eV, not enough to break atomic bonds.
- The main effect is **heating** when absorbed by skin and tissue.
  - Exposure is measured as **power density (mW cm⁻²)**.
  - At **5 mW cm⁻²** there is a significant thermal response (temperature rise above 0.5 °C).
  - **≫ 5 mW cm⁻²** causes tissue damage and pain (used therapeutically, e.g. to burn cancerous tissue).
  - Scanners operate **far below** this limit.

### 3.5 Case Study: L3 ProVision 2
| Parameter | Value |
|---|---|
| Frequency | 20–30 GHz |
| Throughput | **200–300 people/hour**: faster than backscatter (~100/hr), slower than metal detectors (~500/hr) |
| Beam power density | **6 × 10⁻⁶ mW cm⁻²**, so zero heating or biological effects |
| Output | Generic **mannequin** image, only viewed if a threat is flagged |

## 4. Walkthrough Metal Detectors
- Use **pulse induction (PI)**, which exploits **Faraday's law** (Lecture 1). Used in thousands of airports.
- **Advantages:**
  - High throughput (~**500 people/hour**), so shorter queues
  - Very low cost (**under £5k**). Portable versions cost about **£100** but are less sensitive.
  - Easy to set up and deploy: tube stations, schools, events, nightclubs
- **Disadvantage:** **cannot detect non-metallic threats**: 3D-printed weapons, plastic explosives, drugs, animals, food.

### 4.1 Pulse Induction: How It Works
**Normal operation (no metal):**
1. A coil of wire sits on one side of the arch.
2. A short, sharp **pulse of current** through the coil creates a temporary **magnetic field**.
3. When the pulse ends, the field reverses polarity and collapses. This induces a short current, the **reflected pulse**, lasting about **30 µs**.
4. This repeats about **100 pulses per second**.

**Metal present:**
- The pulse induces a magnetic field in the metal object, of **opposite polarity**.
- This extra field **prolongs the reflected pulse** to ≫ 30 µs.
- A **sampling circuit** detects that the reflected pulse is decaying more slowly than expected, and raises an alarm.

---

# PART 3 – X-RAY SCIENCE

## 5. X-Rays
- High frequency, short wavelength, **ionising**, **penetrate tissue but not bone**.
- They lie between **gamma** and **ultraviolet** in the EM spectrum.

| | Soft X-rays | Hard X-rays |
|---|---|---|
| Frequency | 10¹⁶ – 10¹⁸ Hz | **10¹⁸ – 10²⁰ Hz** |
| Wavelength | 10 nm – 100 pm | 100 pm – 1 pm |
- Hard X-rays overlap with gamma rays. The difference is the **source**: X-rays come from **accelerated electrons**, gamma rays from **atomic nuclei**.

## 6. X-Ray Generation: Electron Bombardment (X-ray tube)
1. **Thermionic emission:** a heated metal filament (**cathode**) "boils off" electrons.
2. An **anode** accelerates the electrons through a potential difference of **10³ – 10⁶ V**.
3. The electrons strike a **metal target** (typically **tungsten**) and produce X-rays of various energies and intensities.
- This takes place in an **evacuated glass tube with lead casing**.

## 7. X-Ray Spectra
The spectrum has two components:

### 7.1 Characteristic Radiation (discrete peaks)
- An incoming electron **collides with and ejects an inner-shell electron** (a photoelectron), leaving a **vacancy**, so the atom is no longer in its ground state.
- Electrons from **higher shells cascade down** to fill the gap and **emit X-rays** equal to the energy difference between the shells.
- Each element has unique shell energies, so it emits X-rays at **characteristic energies/wavelengths**.
- **K-peaks:** the vacancy is in the **n = 1 (K) shell**.
  - **Kα:** n = 2 → n = 1 transition
  - **Kβ:** n = 3 → n = 1 transition

### 7.2 Bremsstrahlung ("Braking") Radiation (continuum)
- Incoming electrons pass through atoms **without ejecting** a photoelectron.
- Close approach to the nucleus curves their path and **decelerates** them rapidly.
- The energy lost is emitted as a **continuous X-ray spectrum**.
- **Maximum energy limit:** a head-on collision with the nucleus converts **all** of the electron's energy into one X-ray.
- Changing the tube voltage changes the spectrum (example: molybdenum target at 35 kV).

## 8. X-Ray Energy: Planck's Law
- **Max Planck:** originator of quantum theory (Nobel Prize 1918). **Wave–particle duality**: EM radiation behaves as waves in some cases and particles in others.
- EM radiation comes in discrete packets called **photons**:
  **E = h f**, with h = 6.63 × 10⁻³⁴ J s
- Convert to eV: **1 eV = 1.602 × 10⁻¹⁹ J**, or **1 J = 6.242 × 10¹⁸ eV**.
- **Worked example:** f = 2.4 × 10¹⁸ Hz gives E = 1.59 × 10⁻¹⁵ J = 9924.78 eV ≈ **9.92 keV**.

## 9. Material Penetration & Attenuation
- Penetration depends on the wave (energy, frequency), the material, and the wave–atom interactions.
  - X-rays: pass through skin and soft tissue, not bone.
  - Gamma: can penetrate lead, but is significantly reduced.
  - Some radio waves (e.g. WiFi) pass through brick walls.
  - Light: stopped by cardboard, passes through clear glass and thin paper.
  - Microwaves: cannot pass through a see-through wire mesh (microwave oven door).
- **Attenuation:** the reduction in intensity as radiation passes through a material, by two mechanisms:
  1. **Scattering** (deflection)
  2. **Absorption**

### 9.1 Beer–Lambert Law
**I = I₀ e^(−μx)** (written in the slides as I = I₀e^(−Ax))
- I = intensity at depth x (W m⁻²), I₀ = initial intensity, x = thickness (m)
- μ (A) = **linear attenuation coefficient** (m⁻¹): the fraction of the beam absorbed or scattered per unit thickness. It **depends on X-ray energy**.
- **Mass attenuation coefficient** μₘ: μ = μₘ × ρ (ρ = density).

| Material | μ (m⁻¹, typical / at 50 keV) |
|---|---|
| Vacuum | 0 |
| Muscle | 50 |
| Flesh | 100 |
| Bone | 330 |
| Lead | 600 |

- **Worked example (50 keV, 2.5 cm):**
  - Bone: I/I₀ = e^(−330×0.025) = 2.61 × 10⁻⁴, so **0.026%** transmitted
  - Muscle: I/I₀ = e^(−50×0.025) = 0.2865, so **28.7%** transmitted

---

# PART 4 – REAL-WORLD X-RAY SYSTEMS

## 10. Application Areas
- Mail/parcel, checkpoint, large baggage/cargo, people screening, mobile screening, vehicles.
- All use one of **four X-ray system typologies**.

## 11. The Four Types of X-Ray System

### 11.1 Standard X-Ray
- Source on one side, **detectors** on the other, measuring attenuation.
- Produces a **2D greyscale "shadowgram"**. An **operator** must identify threats.
- **Only discerns shapes:** good for guns and knives, **poor for explosives and drugs**. High false-alarm rate.
- **High throughput, low cost.** Suits high-traffic, low-precision situations.

### 11.2 Dual-Energy X-Ray
- **Two beams:** high-energy (less absorbed) and low-energy (more easily attenuated). The two 2D images are compared.
- This determines the **effective atomic number (Z_eff)**: the average Z of a compound or mixture.
- **Colour coding:**

| Colour | Material | Z_eff band |
|---|---|---|
| **Orange** | Organic | 0 – ~10 |
| **Green** | Inorganic | ~10 – ~19 |
| **Blue** | Metallic | > ~19 |

### 11.3 Transmission & Backscatter X-Ray
- Uses **two detector types**:
  - **Transmission** detector: measures absorption.
  - **Reflection/scatter** detector: gives **density** measurements and good discrimination of **low-Z_eff (organic)** materials.
- **More expensive** than standard or dual-energy, but **much better at identifying threat materials**.
- **Not as safe as mm-wave** for screening people.

### 11.4 Computed Tomography (CT)
- A **rotating X-ray source** moves around the object, with detectors moving in tandem.
- A 2D slice (**tomogram**) is taken at every position, and the slices are combined by **tomographic reconstruction** into a **high-resolution 3D image** (resolution of a few mm).
- **Density + Z_eff** gives excellent material discrimination, plotted as a **Z_eff vs density** plot.
- Allows **automatic screening**: an alarm sounds if the density and Z_eff fall within dangerous ranges (cocaine, TNT). High-resolution pattern recognition picks out guns, knives and large liquid volumes.
- **Low throughput, high cost.** Used where detailed probing is needed.

### 11.5 Summary Comparison
| System | Image | Material ID | Throughput | Cost |
|---|---|---|---|---|
| Standard | 2D shadowgram | Shape only | High | Low |
| Dual-energy | 2D (colour) | Z_eff (organic/inorganic/metal) | High | Low–medium |
| Transmission + backscatter | 2D | Density + good organic discrimination | Medium | Higher |
| CT | 3D | Density + Z_eff, automatic | Low | High |

## 12. The Threat Continues: the Brussels Airport Attack (22 March 2016)
- **3 coordinated suicide bombings** targeted the **busy check-in area**, **before** any security checks.
- Lesson: **attackers target weaknesses**, so innovation must continue.
- Proposed solutions:
  - Move checkpoints to the front doors (common in Asia). Downside: new queues that become new targets.
  - **Keep people moving and scan them remotely** with nimbler or new sensing technologies.

---

## Comparison: People-Screening Technologies
| Technology | Detects | Throughput | Cost | Safety / privacy |
|---|---|---|---|---|
| Walkthrough metal detector | Metal only | ~500/hr | < £5k (portable ~£100) | Safe; no images |
| mm-wave scanner (e.g. L3 ProVision 2) | Metallic + non-metallic under clothing (3D) | 200–300/hr | > $250k | Non-ionising; generic mannequin image |
| Backscatter X-ray scanner | Metallic + non-metallic (2D) | ~100/hr | > $250k | Ionising (small dose); removed from US in 2013 |
| Sniffer dogs | Drugs, explosives, firearms | — | — | — |
| Pat-down | Anything on the body | Slow | Labour | Intrusive |

## Relevant Tools & Technologies
- **Advanced Imaging Technology (AIT)** whole-body scanners: mm-wave and backscatter
- **L3 ProVision 2** mm-wave scanner
- **Antenna arrays, radome, digital beamforming, ATD algorithms**
- **Pulse-induction walkthrough metal detectors** and portable wands
- **X-ray tube** (thermionic cathode, anode, tungsten target, lead casing)
- **Standard / dual-energy / transmission-backscatter / CT** X-ray scanners
- **X-ray diffraction** machines (checked luggage), **explosive trace swabbing**
- Sniffer dogs (drugs, firearms, explosives)
