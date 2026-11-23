DECK = "L4 Airport Security Screening"
TAG = "L4"

CARDS = [
    # ---------------- concept cards ----------------
    ("basic", "Why is airport security described as 'reactive'?",
     "Most new countermeasures were introduced **after** an attack exposed a weakness (LAX 1974 → metal detectors; Lockerbie → hold-luggage X-ray; 9/11 → liquids rules; shoe bomber → shoe scanning)."),
    ("basic", "What countermeasure followed: (a) Lockerbie 1988, (b) 9/11, (c) the 2001 shoe bomber, (d) the 1986 Ann Marie Murphy case?",
     """- (a) X-ray scanning of **all checked luggage**
- (b) Rules on **liquids, gels and toiletries**
- (c) US passengers' **shoes scanned**
- (d) New security questions (has your bag been interfered with?)"""),
    ("basic", "The two types of whole-body scanner and how they differ",
     """- **Millimetre-wave:** radio/microwaves, **non-ionising**, **3D** image
- **Backscatter:** low-power **ionising X-rays**, **2D** image"""),
    ("basic", "What can whole-body scanners detect, and what can't they?",
     """- **Can:** metallic AND non-metallic items under clothing: liquid/plastic explosives, ceramic weapons, drugs (all missed by metal detectors); non-intrusive
- **Can't:** items **swallowed or in body cavities** (waves penetrate clothes, not skin)"""),
    ("basic", "Privacy safeguards of whole-body scanners",
     """- Images viewed in a **separate out-of-sight room** and **immediately deleted** (never stored)
- Operator does not see the passenger
- Identifying details removed (blurred faces, outlines); the US uses a **generic mannequin**"""),
    ("basic", "Safety issues and opt-outs for body scanners",
     """- mm-wave emits **less energy than a mobile phone**
- Backscatter dose ≈ **2 minutes of flying**: insignificant but still a dose
- Some countries allow **opt-out** (e.g. pregnant women) with an **enhanced pat-down**"""),
    ("basic", "Why did the TSA remove X-ray backscatter scanners in 2013?",
     "**Privacy** issues. X-rays are also **ionising** (can remove electrons, kill cells, cause mutations/cancer). mm-wave became the scanner of choice; some countries (e.g. Russia) still use backscatter."),
    ("basic", "mm-wave scanner hardware",
     """- **2 antennas** (front and back), each **transmits and receives**
- **Rotate** around the subject
- Protected by a plastic **radome** (transparent to mm-waves)
- Each antenna is an **array** of many small elements"""),
    ("basic", "How does a mm-wave scanner form its image?",
     "mm-waves **penetrate clothing** and **reflect off skin** and concealed objects. Rotation gives snapshots at different angles; the array plus **digital beamforming** locates the reflection points, giving a **high-resolution 3D image**."),
    ("basic", "How does a mm-wave scanner detect threats?",
     """- **Reflected signal strength:** materials reflect differently, allowing material discrimination
- **Image analysis:** shape detection, pattern matching
- **Automatic Target Detection (ATD)** algorithms: metallic/non-metallic objects, weapons, explosives (gels, plastics, powders)"""),
    ("basic", "Are mm-waves ionising? What is their biological effect?",
     "**Non-ionising** (1.2×10⁻⁴ to 1.2×10⁻³ eV, far below the ~10 eV needed to break bonds). The only effect is **heating** when absorbed; significant from **5 mW/cm²**; scanners operate far below this."),
    ("basic", "L3 ProVision 2: key specs",
     "20–30 GHz; **200–300 people/hr**; beam power density **6×10⁻⁶ mW/cm²** (zero heating); outputs a **generic mannequin** image, only viewed if a threat is flagged."),
    ("basic", "Advantages and disadvantages of walkthrough metal detectors",
     """- **Pros:** very cheap (**under £5k**, portable ~£100); **~500 people/hr**; easy to deploy (tube stations, schools, events, nightclubs)
- **Cons:** **cannot detect non-metals** (3D-printed weapons, plastic explosives, drugs, animals, food); portable units less sensitive"""),
    ("basic", "Explain pulse induction (PI) in a metal detector: normal operation",
     """1. A short sharp **current pulse** through the coil creates a temporary **magnetic field**
2. The pulse ends; the field reverses polarity and **collapses**
3. This induces a short current, the **reflected pulse** (~**30 µs**), by Faraday's law
4. Repeats ~**100 pulses per second**"""),
    ("basic", "Pulse induction: what happens when metal passes through the arch?",
     "The pulse induces a magnetic field **in the metal** of **opposite polarity**. This **prolongs the reflected pulse** (≫ 30 µs). A **sampling circuit** detects the slower-than-expected decay and raises an alarm."),
    ("basic", "Hard vs soft X-rays (frequency and wavelength)",
     """- **Soft:** 10¹⁶–10¹⁸ Hz, 10 nm – 100 pm
- **Hard:** **10¹⁸–10²⁰ Hz**, 100 pm – 1 pm (overlap with gamma)"""),
    ("basic", "Describe how an X-ray tube produces X-rays (electron bombardment)",
     """1. **Thermionic emission:** a heated cathode filament 'boils off' electrons
2. An **anode** accelerates them through **10³–10⁶ V**
3. They strike a metal target (**tungsten**), producing X-rays
In an evacuated glass tube with **lead casing**."""),
    ("basic", "What two types of radiation make up an X-ray spectrum?",
     """- **Characteristic radiation:** discrete energy **peaks**
- **Bremsstrahlung (braking) radiation:** a **continuum** of energies"""),
    ("basic", "Explain how characteristic X-rays are produced",
     """1. An incoming electron **ejects an inner-shell electron** (photoelectron), leaving a **vacancy**
2. A **higher-shell electron cascades down** to fill it (back to ground state)
3. The energy difference is emitted as an **X-ray**
4. Shell energies are unique to each element, so the X-ray energy is **characteristic of the element**"""),
    ("basic", "Kα vs Kβ radiation",
     "K-peaks: the vacancy is in the **n = 1 (K) shell**. **Kα** = n=2 → n=1 transition; **Kβ** = n=3 → n=1."),
    ("basic", "Explain bremsstrahlung radiation and its maximum energy",
     "Electrons pass close to the nucleus **without ejecting** a photoelectron; the path curves and they **decelerate (brake)**, emitting the lost energy as a **continuous** spectrum. **Maximum energy**: a head-on collision converts **all** the electron's energy into one X-ray."),
    ("basic", "Planck's law and wave–particle duality",
     "EM radiation comes in discrete packets of energy (**photons**): **E = hf**. EM radiation behaves as waves in some cases and particles in others (wave–particle duality). Max Planck, Nobel 1918."),
    ("basic", "Define attenuation and its two mechanisms",
     "The reduction in radiation intensity as it passes through a material, by **scattering** (deflection) and **absorption**."),
    ("basic", "What does the linear attenuation coefficient µ represent? How does it relate to the mass attenuation coefficient?",
     "The **fraction of the beam absorbed or scattered per unit thickness** (m⁻¹); depends on X-ray energy. **µ = µₘ × ρ** (ρ = density)."),
    ("basic", "What factors determine how well an EM wave penetrates a material? Give examples.",
     "Wave properties (energy, frequency), material properties, and the wave–atom interactions. E.g. X-rays pass through tissue not bone; γ through lead (reduced); WiFi through brick; light stopped by cardboard; microwaves blocked by wire mesh."),
    ("basic", "Standard X-ray system: how it works, pros/cons",
     """Source on one side, detectors on the other, giving a **2D greyscale shadowgram**.
- **Pros:** high throughput, low cost; good for **guns/knives**
- **Cons:** shape only; operator-dependent; **poor for explosives/drugs**; high false alarms"""),
    ("basic", "Dual-energy X-ray: how it works",
     "**Two beams** (high-energy, less absorbed; low-energy, more attenuated); the two 2D images are compared to find the **effective atomic number Z_eff**, which is then colour-coded."),
    ("basic", "Define effective atomic number (Z_eff)",
     "The **average atomic number** of a compound or mixture. It reveals light (low Z_eff, organic) vs heavy (high Z_eff, metallic) materials."),
    ("basic", "Transmission/backscatter X-ray systems",
     """Two detector types:
- **Transmission:** absorption
- **Reflection/scatter:** **density**; good discrimination of **low-Z_eff organic** materials
More expensive but much better at identifying threats; **not as safe as mm-wave** for people."""),
    ("basic", "Computed Tomography (CT) X-ray: how it works and its capabilities",
     """- **Rotating** source with detectors moving in tandem; a 2D slice (**tomogram**) at each position
- Combined by **tomographic reconstruction** into a **high-resolution 3D** image (a few mm)
- **Density + Z_eff** allow **automatic** alarms (cocaine, TNT; guns, knives, liquids)
- **Low throughput, high cost**"""),
    ("basic", "What did the Brussels Airport attack (22 March 2016) reveal, and what solutions were proposed?",
     """3 coordinated suicide bombs in the **check-in area, before any security checkpoint**.
- Option 1: move checkpoints to the front doors (creates new queues/targets)
- Option 2: **keep people moving and scan remotely** with nimbler or new sensors"""),

    # ---------------- cloze ----------------
    ("cloze", "mm-wave scanners operate at {{c1::20–30 GHz}}, wavelengths {{c2::15–10 mm}}, photon energies {{c3::1.2×10⁻⁴ – 1.2×10⁻³ eV}}", ""),
    ("cloze", "To be ionising, EM radiation needs energy well above {{c1::10 eV}}; X-rays are {{c2::100 eV – 100 keV}}", ""),
    ("cloze", "Significant thermal response in tissue begins at a power density of {{c1::5 mW/cm²}} (temperature rise above {{c2::0.5 °C}})", ""),
    ("cloze", "Throughput: metal detector ≈ {{c1::500}}/hr; mm-wave (ProVision 2) ≈ {{c2::200–300}}/hr; backscatter ≈ {{c3::100}}/hr", ""),
    ("cloze", "Costs: walkthrough metal detector under {{c1::£5k}}; portable ≈ {{c2::£100}}; whole-body scanner over {{c3::$250,000}}", ""),
    ("cloze", "In pulse induction the reflected pulse normally lasts about {{c1::30 µs}}; pulses are sent about {{c2::100}} times per second", ""),
    ("cloze", "Hard X-rays: {{c1::10¹⁸ – 10²⁰ Hz}}; soft X-rays: {{c2::10¹⁶ – 10¹⁸ Hz}}", ""),
    ("cloze", "X-ray tube accelerating voltage: {{c1::10³ to 10⁶}} V; typical target metal: {{c2::tungsten}}", ""),
    ("cloze", "Planck's law: E = {{c1::hf}}, h = {{c2::6.63 × 10⁻³⁴ J s}}; 1 eV = {{c3::1.602 × 10⁻¹⁹ J}}", "1 J = 6.242 × 10¹⁸ eV"),
    ("cloze", "Beer–Lambert law: I = {{c1::I₀ e^(−µx)}}", "µ = linear attenuation coefficient (m⁻¹), x = thickness (m)."),
    ("cloze", "Linear attenuation coefficients: vacuum {{c1::0}}, muscle {{c2::50}}, flesh {{c3::100}}, bone {{c4::330}}, lead {{c5::600}} m⁻¹", ""),
    ("cloze", "Dual-energy colours: {{c1::orange}} = organic (Z_eff 0–10), {{c2::green}} = inorganic (10–19), {{c3::blue}} = metallic (> 19)", ""),
    ("cloze", "The four X-ray system typologies: {{c1::standard}}, {{c2::dual-energy}}, {{c3::transmission & backscatter}}, {{c4::computed tomography (CT)}}", ""),
    ("cloze", "First Advanced Imaging Technology (AIT) whole-body scanners deployed in {{c1::2003}}; TSA banned loose {{c2::lithium batteries}} in checked luggage in {{c3::2008}}", ""),
    ("cloze", "Lockerbie: {{c1::21 December 1988}}, {{c2::270}} killed; 9/11: {{c3::2,996}} killed", ""),

    # ---------------- calculations ----------------
    ("calc", "X-rays have f = 3.5 × 10¹⁸ Hz. Find the photon energy in keV (1 d.p.). [h = 6.63×10⁻³⁴ J s]",
     """E = hf = 6.63×10⁻³⁴ × 3.5×10¹⁸ = 2.3205×10⁻¹⁵ J
× 6.242×10¹⁸ eV/J = 14,484.6 eV = **14.5 keV**"""),
    ("calc", "X-rays have f = 2.4 × 10¹⁸ Hz. Find the photon energy in keV.",
     "E = 6.63×10⁻³⁴ × 2.4×10¹⁸ = 1.59×10⁻¹⁵ J, giving 9924.8 eV = **9.92 keV**"),
    ("calc", "X-rays have f = 1.2 × 10¹⁹ Hz. Find E in keV and state hard or soft.",
     "E = 7.956×10⁻¹⁵ J, giving **49.66 keV**; **hard** (f > 10¹⁸ Hz)"),
    ("calc", "Find the photon energy (eV) of a 25 GHz mm-wave. Is it ionising?",
     "E = 6.63×10⁻³⁴ × 25×10⁹ = 1.66×10⁻²³ J, giving **1.03×10⁻⁴ eV**. Far below 10 eV, so **non-ionising**."),
    ("calc", "RDX has µ = 30 m⁻¹ at 80 keV. At what thickness does the X-ray intensity halve? (2 d.p.)",
     """0.5 = e^(−30x), so ln 0.5 = −30x
x = 0.0231 m = **2.31 cm**"""),
    ("calc", "50 keV X-rays pass through 2.5 cm of bone (µ = 330 m⁻¹) and muscle (µ = 50 m⁻¹). Find % transmitted.",
     """- Bone: e^(−330×0.025) = 2.61×10⁻⁴, so **0.026%**
- Muscle: e^(−50×0.025) = 0.2865, so **28.7%**"""),
    ("calc", "Lead has µ = 600 m⁻¹. Find (a) the half-value thickness, (b) % transmitted through 5 mm.",
     """- (a) x = ln2/600 = **1.16 mm**
- (b) e^(−600×0.005) = e^(−3) = **4.98%**"""),
    ("calc", "What thickness of bone (µ = 330 m⁻¹) reduces X-ray intensity to 10%?",
     "x = −ln(0.1)/330 = 2.303/330 = **6.98 mm ≈ 0.70 cm**"),
    ("calc", "1000 passengers must be screened. Compare time for one metal detector, one mm-wave scanner (250/hr), one backscatter unit.",
     "Metal detector **2 h**; mm-wave **4 h**; backscatter **10 h**"),

    # ---------------- exam-style (incl. official problem sheet) ----------------
    ("exam", "[1 mark] (Problem sheet Q1) What can a drug smuggler do to avoid a small package of cocaine being detected by a mm-wave whole-body scanner?",
     "Transport it **internally**: swallow it or hide it in a **body cavity**. mm-waves penetrate clothing but not skin."),
    ("exam", "[4 marks] (Problem sheet Q2) Describe the operation of a millimetre-wave whole-body scanner with reference to (a) the hardware, (b) the imaging and (c) threat detection.",
     """**(a) Antennas:**
- Booth with **2 antennas** (front/back), each transmits AND receives
- Antennas **rotate**; protected by a **radome**; made of many small elements (**array**)
**(b) Imaging:**
- mm-waves penetrate clothing, **reflect off skin** and concealed objects
- Snapshots at different angles; reflections received; the array/**beamforming** locates reflection points, giving a **3D image**
**(c) Threat detection:**
- **Reflected signal strength** discriminates materials
- **Image analysis** (shape detection, pattern matching)
- **ATD algorithms**: metallic/non-metallic objects, weapons, explosives (gels, plastics, powders)"""),
    ("exam", "[2 marks] (Problem sheet Q3) State one advantage and one disadvantage of security screening using metal detectors.",
     """- **Advantage:** very low cost (under £5k walkthrough, ~£100 portable) / high throughput ~500 per hour / easy to deploy (stations, schools, concerts)
- **Disadvantage:** cannot detect **non-metals**: 3D-printed weapons, plastic explosives, drugs"""),
    ("exam", "[3 marks] (Problem sheet Q7) An X-ray spectrum from electron bombardment of a metal target shows a continuum (bremsstrahlung) and discrete peaks. (a) Name the peaks. (b) Explain in terms of atomic processes how they are generated.",
     """**(a)** **Characteristic X-ray peaks** (K-lines: Kα, Kβ)
**(b)**
- An incoming electron **collides with and ejects an inner-shell electron** (photoelectron), leaving a vacancy
- An electron from a **higher shell drops** to fill it, emitting an **X-ray** equal to the shell energy difference
- Shell energies are unique per element, so the energies are **characteristic**; n=2→1 = Kα, n=3→1 = Kβ"""),
    ("exam", "[5 marks] Explain how a walkthrough metal detector uses pulse induction to detect metallic objects, and discuss its suitability for screening in different environments.",
     """**Marking points:**
- Based on **Faraday's law**
- Current pulse in a coil creates a field; the field collapses and induces a **reflected pulse ~30 µs**; ~100 pulses/s
- Metal object: induced **opposite-polarity field** prolongs the reflected pulse (≫ 30 µs)
- **Sampling circuit** detects the slow decay and raises the alarm
- Suitability: cheap, ~500/hr, portable, so good for stations/schools/events; but **misses non-metallic threats**, so supplement with mm-wave or other screening"""),
    ("exam", "[6 marks] Describe how X-rays are produced in an X-ray tube and explain the two components of the resulting X-ray spectrum.",
     """**Marking points:**
- Thermionic emission from a heated cathode; electrons accelerated by an anode at 10³–10⁶ V; strike a tungsten target; evacuated, lead-cased tube
- **Characteristic:** inner-shell electron ejected; higher-shell electron fills the vacancy and emits a discrete X-ray unique to the element (Kα, Kβ peaks)
- **Bremsstrahlung:** electron deflected/decelerated near the nucleus, giving a continuous spectrum
- **Maximum energy:** head-on collision converts all electron energy into one photon
- Changing the tube voltage alters the spectrum"""),
    ("exam", "[8 marks] Compare standard, dual-energy, transmission/backscatter and CT X-ray screening systems in terms of operation, threat-detection capability, throughput and cost.",
     """**Marking points:**
- **Standard:** source + detectors, 2D greyscale shadowgram; shape only; operator needed; good for guns/knives, poor for explosives/drugs; high false alarms; **high throughput, low cost**
- **Dual-energy:** high and low energy beams compared, giving **Z_eff**; colour-coded organic (orange), inorganic (green), metal (blue)
- **Transmission + backscatter:** two detectors, absorption plus scatter (density); good for **low-Z organic** threats; more expensive; less safe than mm-wave for people
- **CT:** rotating source, tomograms, **3D** reconstruction; density + Z_eff; **automatic** detection; **low throughput, high cost**, for detailed probing"""),
    ("exam", "[5 marks] Compare millimetre-wave and backscatter X-ray whole-body scanners in terms of physics, image produced, safety, privacy and current use.",
     """**Marking points:**
- mm-wave: 20–30 GHz radio/microwave, **non-ionising**, **3D**, heating only (ProVision 2 at 6×10⁻⁶ mW/cm², far below 5 mW/cm²)
- Backscatter: low-power **ionising** X-rays, **2D**, dose ≈ 2 min of flying
- Both detect metallic and non-metallic items under clothing; neither detects body-cavity items
- Privacy: remote viewing, images deleted, generic outline/mannequin
- TSA removed backscatter in **2013**; mm-wave is now the scanner of choice; backscatter is slower (~100/hr vs 200–300/hr)"""),
    ("exam", "[4 marks] State the Beer–Lambert law, define its terms, and explain why X-ray images can distinguish bone from muscle.",
     """**Marking points:**
- **I = I₀e^(−µx)**: I = intensity after thickness x; I₀ = initial intensity; µ = linear attenuation coefficient (fraction removed per unit thickness, energy-dependent)
- Attenuation = scattering + absorption
- Bone µ = 330 m⁻¹ vs muscle 50 m⁻¹: through 2.5 cm, 0.026% vs 28.7% transmitted
- So there is large contrast: bone appears bright (attenuates strongly)"""),
    ("exam", "[4 marks] Trace the history of airport security screening and explain what the 2016 Brussels attack shows about remaining weaknesses.",
     """**Marking points:**
- Began with bag/person searches against hijacking, then drugs/contraband, now counter-terrorism
- **Reactive:** LAX 1974 (metal detectors/X-ray), Lockerbie 1988 (all hold luggage X-rayed), 9/11 (liquids), shoe bomber (shoes), AIT scanners 2003
- Brussels 2016: bombs in the **landside check-in area before checkpoints**
- Weakness: crowded public areas; solutions: move checkpoints to the doors (new queues) or **remote stand-off scanning of moving people**"""),
]
