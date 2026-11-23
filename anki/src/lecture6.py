DECK = "L6 Law Enforcement (Radar, Taser, Breathalyser)"
TAG = "L6"

CARDS = [
    # ---------------- concept cards: radar ----------------
    ("basic", "What does RADAR stand for and which EM bands does it use?",
     "**RA**dio **D**etection **A**nd **R**anging. Uses **radio and microwave** bands (3 Hz to just under 3 THz)."),
    ("basic", "Police uses of radar",
     "Counter-terrorism and hostage scenarios; missing persons and hidden weapons; crime investigation and evidence gathering; critical infrastructure protection; tactical planning; cold cases; covert surveillance; border control."),
    ("basic", "Match the police radar type to its use: GPR, through-the-wall, fencing, Doppler",
     """- **GPR:** buried bodies, weapons, contraband
- **TTW radar:** point-of-entry determination, covert surveillance, scene awareness
- **Fencing radar:** critical infrastructure and perimeter monitoring, VIP planning
- **Doppler radar:** vehicle velocity"""),
    ("basic", "Describe the basic principle of radar ranging",
     """1. A radio wave is transmitted from the antenna at t = 0
2. It reaches the object (t_travel) and **scatters in all directions**
3. Part returns to the antenna (t_return); t_total = t_travel + t_return
4. **R = c·t_total / 2**"""),
    ("basic", "What is range resolution and what does it depend on?",
     "The **precision** of the range measurement (the uncertainty in object position). It depends **only on bandwidth B**: **ΔR = c/2B**. E.g. R = 100 m, ΔR = 2 m, so the object is at 99–101 m."),
    ("basic", "Define bandwidth",
     "The **range of frequencies** within a wave or signal (real signals are made of many frequencies, unlike a pure sinusoid)."),
    ("basic", "What is relative permittivity and why does it matter for GPR?",
     "εᵣ = a material's ability to **store electrical energy**. When the radar wave meets a material of **different εᵣ**, a portion is **reflected** back to the antenna, forming the image."),
    ("basic", "The image-quality vs depth trade-off in radar",
     """- **High frequency:** can hold more **bandwidth**, so **better range resolution / image quality**, but more attenuation
- **Low frequency:** **less attenuation**, so **deeper penetration**, but poorer resolution
Modern GPRs are **tunable**."""),
    ("basic", "Why is GPR suitable for law enforcement?",
     """- **Non-destructive**: evidence/bodies preserved for forensic archaeologists
- **Non-contact**: rapid scanning of large areas, no labour-intensive digging
- **Hidden weapons**: metals/ceramics have large εᵣ
- Landmine clearance"""),
    ("basic", "How do through-the-wall radar scenarios differ from GPR?",
     """- Target is usually **moving**, so the **Doppler effect** can be used
- **Time-limited**, so speed is critical
- **Lots of air gaps**; the operator is in a **high-risk position** next to the wall"""),
    ("basic", "Explain the attenuation problem in through-the-wall radar",
     "Magnified at the **air–wall interface** (significant scattering). At **high frequencies** only a tiny proportion penetrates brick/concrete, and the weak reflection must come **back through the wall**, so the signal is too weak for the radar to operate."),
    ("basic", "State-of-the-art TTW radar techniques: UWB, micro-Doppler, MIMO",
     """- **Ultra-wideband (UWB):** wide bandwidth at **low frequencies** (penetration + resolution); expensive
- **Micro-Doppler:** small body movements, enabling activity recognition, **signs-of-life**, person vs animal
- **MIMO** (from WiFi): **3D visualisation**"""),
    ("basic", "United States v. Steven Denson (2014): facts and outcome",
     "US Marshals used a **TTW radar** to detect Denson inside a Wichita house; he was arrested with **illegal firearms**. He tried to overturn the charge as an **invasion of privacy**, and was **unsuccessful**, but the case sparked national debate."),
    ("basic", "Civil liberties arguments against TTW radar (Gorsuch, ACLU)",
     """- **Judge Neil Gorsuch:** new technologies bring 'new risks for abuse and new ways to invade constitutional rights'
- **Christopher Soghoian (ACLU):** among the **most intrusive** police tools; sending signals through your wall to see inside is 'problematic'
- FBI/Marshals used them since **2012** (≥ $180k) with **no public disclosure**"""),

    # ---------------- concept cards: non-lethal ----------------
    ("basic", "What are non-lethal weapons? Give examples.",
     "Compliance / less-lethal / pain-inducing weapons, less likely to kill than firearms. E.g. **water cannon, pepper spray/mace/tear gas, stun shields, cattle-prods, dazzler, Long Range Acoustic Device, riot-control gun (rubber bullets), Taser**."),
    ("basic", "What do a dazzler and an LRAD do?",
     """- **Dazzler:** directed visible light to temporarily **blind/disorient** without long-term damage
- **LRAD:** communicates warnings to crowds with a jarring sound"""),
    ("basic", "What is a Taser and why do police use it?",
     "A **conducted electrical weapon (CEW)** using high voltage for **neuromuscular incapacitation**. Used when lethal force isn't required/permitted, to **temporarily incapacitate** and **minimise escalation**."),
    ("basic", "Taser basic operation",
     """- **2 darts** fired by **compressed nitrogen** at ~**55 m/s**
- Both must contact the target (or one on the ground) to **complete the circuit**
- **High voltage, low amperage** pulses (up to 50 kV generated)
- Range **7–11 m** (wire length)
- Extras: memory logs each trigger pull; **confetti** IDs the gun; video camera; laser sight"""),
    ("basic", "How does a Taser close the circuit if the darts are stuck in clothing?",
     "In ~**30%** of cases there's no skin contact. A **50 kV arcing pulse ionises the air gap** to make a conductive path. It's used **only for an open circuit**, so **the body never receives 50 kV**."),
    ("basic", "Taser pulse train parameters once the circuit is closed",
     "Each pulse **100 µs** long, carries **100 µC**; **19 pulses per second** (PRF)."),
    ("basic", "Psychological effects of a Taser (compliance without firing)",
     "Effects seen on **TV/social media**; **black and bright yellow** colour (bumble bee effect); **red laser dots** showing the target they're in line of sight."),
    ("basic", "Physiological effect of a Taser",
     "Skeletal muscle (~40% of body mass) is controlled by electrical impulses via **motor nerves**. Taser pulses **jolt the motor nerves**, causing **involuntary contraction**, so the target spasms, drops and loses motor control."),
    ("basic", "State Ohm's law in words",
     "The current through a conductor is **proportional to the voltage**; the constant of proportionality relates to the **resistance R**, which is inversely proportional to the current: **I = V/R**, V = IR."),
    ("basic", "What is the tetanus region and how does the Taser avoid it?",
     "Muscle contraction rates **> 70 per second** are dangerously strong (the disease tetanus causes contraction at this rate). The Taser PRF is **19**, far below, enough to disable without long-term damage."),
    ("basic", "UK Taser timeline and law",
     """- **2003:** 12-month trial; ACPO noted the striking **deterrent effect**
- **2007:** use allowed for **serious threats and violence**
- **2008:** not restricted to firearms officers
- Illegal possession: up to **10 years** plus unlimited fine (min **5 years** if disguised)"""),
    ("basic", "Opposition to Tasers",
     """- **Amnesty International:** > **500 deaths** in the US since 2001 (shock cited in only a handful); potential **torture** tool in policing/prisons
- **'Don't tase me bro'** (Andrew Meyer, Univ. of Florida) led to national debate, which also enhanced the deterrent effect"""),

    # ---------------- concept cards: breathalyser ----------------
    ("basic", "When can UK police carry out a roadside breath test?",
     "They can stop any driver, but can only test if they suspect the driver has **consumed alcohol**, **committed a traffic offence**, or **been involved in an accident**."),
    ("basic", "Describe the UK breath testing procedure",
     """1. **Screening** breath test at the roadside (fuel cell device)
2. If over: **evidential** breath test on a fixed machine at the police station
3. If the evidential reading is **40–50 µg/100 ml**, the driver may opt for a **blood or urine** test"""),
    ("basic", "Why can breath be used to infer blood alcohol concentration?",
     "Ethanol (C₂H₅OH) is absorbed into the blood **without chemical change** and is **volatile**, so it evaporates into the **alveoli** as blood passes the lungs. Alveolar concentration is **directly proportional to BAC** (blood:breath = **2100:1**)."),
    ("basic", "What is a fuel cell?",
     "An **electrochemical energy conversion device** converting the **chemical potential energy** of hydrogen into **electrical energy** (reactions in a proton exchange membrane). Fuel: H₂ and O₂; by-products: water, heat, electricity. Compact, quiet, lightweight."),
    ("basic", "Fuel cell vs battery",
     "A battery stores its chemicals and eventually goes **dead**; a fuel cell produces electricity **continuously as long as fuel is supplied**."),
    ("basic", "Basic fuel cell principle (anode, electrolyte, cathode)",
     """- **Anode:** hydrogen **oxidised** (loses electrons), giving H⁺ + e⁻
- **H⁺** travels through the **electrolyte** to the cathode
- **e⁻** flow through the **external circuit** (current)
- **Cathode:** H⁺ + e⁻ + O₂ form **water**"""),
    ("basic", "How does a fuel cell breathalyser produce a reading?",
     "Two **porous platinum electrodes** with an **acid electrolyte**. Ethanol is oxidised at the anode to acetic acid, releasing electrons into the circuit. **More alcohol means a larger current**; a **microprocessor** converts the current into a breath-alcohol concentration."),

    # ---------------- cloze ----------------
    ("cloze", "Radar range: R = {{c1::c·t_total / 2}}; range resolution: ΔR = {{c2::c / 2B}}", "Divide by 2 for the round trip."),
    ("cloze", "Radio sub-bands: LF = {{c1::30–300 kHz}}, MF = {{c2::300 kHz–3 MHz}}, HF = {{c3::3–30 MHz}}, VHF = {{c4::30–300 MHz}}, UHF = {{c5::300 MHz–3 GHz}}, SHF = {{c6::3–30 GHz}}, EHF = {{c7::30–300 GHz}}", "ELF 3–30 Hz, SLF 30–300 Hz, ULF 300 Hz–3 kHz, VLF 3–30 kHz."),
    ("cloze", "GPR max depth: 1500 MHz = {{c1::0.5 m}}, 900 MHz = {{c2::1 m}}, 400 MHz = {{c3::4 m}}, 270 MHz = {{c4::6 m}}", ""),
    ("cloze", "Reflectivity coefficient ρ = {{c1::(√ε₁ − √ε₂)/(√ε₁ + √ε₂)}}; soil εᵣ = {{c2::9}}, bone εᵣ = {{c3::4}}", ""),
    ("cloze", "Taser: darts at ~{{c1::55}} m/s; range {{c2::7–11}} m; arc pulse {{c3::50 kV}}; darts miss skin in ~{{c4::30%}} of cases", ""),
    ("cloze", "Taser pulses: {{c1::100 µs}} long, {{c2::100 µC}} each, {{c3::19}} per second, giving a current of {{c4::1.9 mA}}", "About 1% of the fibrillation current."),
    ("cloze", "Mains 240 V: with rubber shoes (100 kΩ) I = {{c1::2.4 mA}} (safe); barefoot after a bath (10 kΩ) I = {{c2::24 mA}} (probably lethal)", ""),
    ("cloze", "UK limits (E, W, NI): blood {{c1::80 mg/100 ml}}, breath {{c2::35 µg/100 ml}}, urine {{c3::107 mg/100 ml}}; Scotland BAC {{c4::50 mg/100 ml}}", "Europe 50 (30 for new drivers); USA 80; zero tolerance: Croatia, Czech Rep., Brazil, Hungary."),
    ("cloze", "Blood : breath alcohol ratio = {{c1::2100 : 1}}", "2100 ml of alveolar air contains the same alcohol as 1 ml of blood."),
    ("cloze", "Drivers with BAC 20–50 mg/100 ml have {{c1::3×}} the risk of dying in a crash; 50–80 mg/100 ml have {{c2::6×}} (North Review 2010)", ""),
    ("cloze", "Breathalyser anode: CH₃CH₂OH + H₂O → {{c1::CH₃CO₂H}} + {{c2::4H⁺ + 4e⁻}}; cathode: O₂ + 4H⁺ + 4e⁻ → {{c3::2H₂O}}", "Ethanol is oxidised to acetic acid (vinegar)."),
    ("cloze", "UK drink driving 2015: {{c1::220}} killed, {{c2::1,160}} seriously injured, over {{c3::70,000}} caught over the limit; convictions {{c4::85%}} male", ""),

    # ---------------- calculations ----------------
    ("calc", "A TTW radar (5.8 GHz, 100 MHz bandwidth) measures a round-trip time of 1.6 × 10⁻⁷ s. Find (a) range, (b) range resolution.",
     """- (a) R = 3×10⁸ × 1.6×10⁻⁷ / 2 = **24 m**
- (b) ΔR = 3×10⁸ / (2 × 100×10⁶) = **1.5 m** (±0.75 m)"""),
    ("calc", "A radar echo returns after 2 × 10⁻⁷ s. Find the range.", "R = 3×10⁸ × 2×10⁻⁷ / 2 = **30 m**"),
    ("calc", "What bandwidth gives a range resolution of 0.3 m?", "B = c/(2ΔR) = 3×10⁸/0.6 = **500 MHz**"),
    ("calc", "Find the reflectivity coefficient for (a) soil (εᵣ 9) to bone (εᵣ 4), (b) air to soil, (c) soil to water (εᵣ 81).",
     """- (a) (3−2)/(3+2) = **0.2**
- (b) (1−3)/(1+3) = −0.5, so **0.5**
- (c) (3−9)/(3+9) = −0.5, so **0.5**"""),
    ("calc", "A body is suspected 3 m deep. Which GPR frequency should be used?",
     "**400 MHz** (reaches ~4 m). Higher frequencies can't reach 3 m; 270 MHz reaches it but with poorer resolution. Pick the **highest frequency that reaches the depth**."),
    ("calc", "Show that a standard Taser (19 pulses/s, 100 µC each) is safe.",
     "I = Q/t = 100×10⁻⁶ × 19 / 1 = **1.9 mA**, about 1% of the fibrillation current; PRF 19 is far below the tetanus region (> 70)."),
    ("calc", "A new Taser delivers 32 pulses/s of 650 µC. Find the current (1 d.p.). Will it pass safety checks?",
     "I = 650×10⁻⁶ × 32 = 0.0208 A = **20.8 mA**. **Fails**: PRF is fine (< 70) but the current is in the unsafe region (sustained contraction, extreme pain, respiratory arrest, possible death)."),
    ("calc", "A person touches 240 V with 2000 Ω to ground. Find the current.", "I = V/R = 240/2000 = **120 mA**: lethal, high fibrillation risk"),
    ("calc", "Bob's BAC is 120 mg/100 ml. Find his breath reading (µg/100 ml, 2 d.p.). Is he over the UK limit?",
     "120×10⁻³ g / 2100 = 5.714×10⁻⁵ g, so **57.14 µg/100 ml**. **Over** (limit 35 µg/100 ml breath = 80 mg/100 ml blood)."),
    ("calc", "An evidential breath reading is 50 µg/100 ml. What is the equivalent BAC?",
     "50 µg × 2100 = 105,000 µg = **105 mg/100 ml** (over 80; in the 40–50 band the driver may request blood/urine)"),
    ("calc", "BAC = 60 mg/100 ml. Breath reading? Over the limit in England? In Scotland?",
     "60,000/2100 = **28.57 µg/100 ml**. England: **under**. Scotland (50 mg): **over**."),

    # ---------------- exam-style ----------------
    ("exam", "[1 mark] (Problem sheet Q1) Radar waves fall into which band(s) of the EM spectrum? (millimetre-waves / IR and microwaves / radio and microwaves / radio waves / X-rays)",
     "**Radio and microwaves**"),
    ("exam", "[1 mark] (Problem sheet Q3) Which statement best describes EM waves in a through-the-wall radar?",
     "**High-frequency EM waves experience MORE attenuation by a wall and generate BETTER/more accurate images than low-frequency waves.**"),
    ("exam", "[4 marks] (Problem sheet Q5) State Ohm's law in words and derive the relationship between current and voltage.",
     """- The current through a conductor is **proportional to the voltage**; the constant of proportionality involves the **resistance R**, which is inversely proportional to the current
- I ∝ V, so I = const × V, so **I = V/R**, so **V = IR**"""),
    ("exam", "[1 mark] (Problem sheet Q7) Which element do fuel cells typically use to convert chemical potential energy into electrical energy?",
     "**Hydrogen** (oxygen also accepted)"),
    ("exam", "[5 marks] Describe how a radar system measures the range of a target and explain what determines its range resolution. Illustrate with a numerical example.",
     """**Marking points:**
- Wave transmitted at t = 0, scattered by the target, part returns; **t_total = t_travel + t_return**
- **R = c·t_total/2** (round trip)
- Range resolution = precision; depends **only on bandwidth**: **ΔR = c/2B**
- Bandwidth = range of frequencies in the signal; higher frequencies can hold more bandwidth
- Example: t = 1.6×10⁻⁷ s gives R = 24 m; B = 100 MHz gives ΔR = 1.5 m (±0.75 m)"""),
    ("exam", "[6 marks] Explain how ground-penetrating radar is used to locate a clandestine burial. Include the role of relative permittivity, the reflectivity coefficient and the frequency/depth trade-off.",
     """**Marking points:**
- Antenna transmits an EM wave into the ground; reflections form an image
- Reflection occurs where **εᵣ changes** (εᵣ = ability to store electrical energy)
- **ρ = (√ε₁ − √ε₂)/(√ε₁ + √ε₂)**: soil (9) to bone (4) gives 0.2; air to soil gives 0.5
- **High f:** more bandwidth, better resolution, shallower; **low f:** less attenuation, deeper (1500 MHz 0.5 m … 270 MHz 6 m); tunable systems
- Advantages: non-destructive, non-contact, rapid, detects weapons (high εᵣ metals/ceramics)"""),
    ("exam", "[6 marks] Explain the technical challenges of through-the-wall radar and how state-of-the-art systems overcome them.",
     """**Marking points:**
- Targets behind walls/doors/curtains; usually **moving** (Doppler), **time-critical**, many air gaps, operator at risk
- **Attenuation:** scattering at the air–wall interface; at high f little penetrates and the echo must return through the wall
- Low f penetrates but gives poor resolution: the trade-off
- **UWB:** wide bandwidth at low frequencies (expensive)
- **Micro-Doppler:** limb/torso motion gives activity recognition, signs of life, people vs animals
- **MIMO:** 3D visualisation"""),
    ("exam", "[4 marks] Convey the arguments civil rights activists have put forward against police use of through-the-wall radar, with reference to a legal case.",
     """**Marking points:**
- US v. Denson (2014): Marshals used TTW radar to confirm presence; firearms found; privacy challenge failed
- **Gorsuch:** new tech brings opportunities but also 'new risks for abuse and new ways to invade constitutional rights'
- **ACLU (Soghoian):** among the most intrusive tools; seeing inside homes through walls is problematic
- Agencies used them since 2012 (≥ $180k) **without public disclosure**, so there is a lack of oversight/transparency"""),
    ("exam", "[6 marks] Describe how a Taser incapacitates a suspect, in terms of its operation, the electrical pulses and human physiology.",
     """**Marking points:**
- Two darts propelled by compressed nitrogen (~55 m/s, 7–11 m), wires back to the gun; both must contact to complete the circuit
- If stuck in clothing (~30%): **50 kV arc ionises the air gap**; the body never sees 50 kV
- Pulse train: **100 µs** pulses, **100 µC** each, **19 per second**
- Pulses jolt the **motor nerves**, causing **involuntary skeletal muscle contraction**, so the target loses motor control and falls
- Psychological compliance: colours, laser dots, media"""),
    ("exam", "[5 marks] Using Ohm's law and the definition of current, show that the electric current delivered by a Taser is within safety bounds. Compare with a mains-voltage shock.",
     """**Marking points:**
- **I = Q/t**: 100 µC × 19 / 1 s = **1.9 mA**
- About **1%** of the current causing **ventricular fibrillation**
- PRF 19 is far below the **tetanus region (> 70/s)**
- Mains: I = V/R; 240 V / 100 kΩ = 2.4 mA (tingle, safe); 240 V / 10 kΩ = 24 mA (probably lethal)
- Hence it is **current, not voltage, that kills**; the Taser is high voltage but low current"""),
    ("exam", "[4 marks] (Problem sheet Q6) A Taser delivers 32 pulses per second, each of 650 µC. (a) Calculate the current (1 d.p.). (b) Explain whether it will pass safety checks.",
     """- (a) I = Q/t = 650×10⁻⁶ × 32 / 1 = **20.8 mA**
- (b) **No.** PRF (32) is well below the tetanus region, but **20.8 mA is in the unsafe region** (compare 24 mA probably lethal; the standard Taser gives 1.9 mA). Effects: sustained muscular contraction, extreme pain, respiratory arrest, possible death"""),
    ("exam", "[4 marks] Convey the arguments civil rights activists have made against police use of Tasers.",
     """**Marking points:**
- Amnesty: over 500 US deaths since 2001 (though shock is cited as cause in only a handful)
- Potential use as **torture / pain-compliance** tools in policing and prisons
- High-profile misuse ('Don't tase me bro', Andrew Meyer) led to national debate on proportionality
- Expanding UK use (2007 serious violence, 2008 non-firearms officers) raises concerns of escalation creep"""),
    ("exam", "[6 marks] Describe the chemistry of alcohol in the body and explain the scientific principles of the fuel cell breathalyser, including the electrode reactions.",
     """**Marking points:**
- Ethanol C₂H₅OH (hydroxyl group); absorbed into the blood unchanged; **volatile**, evaporates in the alveoli; **2100:1** blood:breath
- Fuel cell = electrochemical device; anode, electrolyte, cathode; continuous while fuel is supplied
- Breathalyser: **porous platinum electrodes**, **acid electrolyte**
- Anode: **CH₃CH₂OH + H₂O → CH₃CO₂H + 4H⁺ + 4e⁻**
- Cathode: **O₂ + 4H⁺ + 4e⁻ → 2H₂O**
- H⁺ through the electrolyte, e⁻ through the circuit; **current ∝ alcohol**; microprocessor converts to a concentration"""),
    ("exam", "[4 marks] (Problem sheet Q8) Bob's BAC is 120 mg/100 ml. (a) What will the roadside breathalyser read in µg/100 ml (2 d.p.)? (b) Is he over the UK limit? (ratio 2100:1)",
     """- (a) 120×10⁻³ g / 2100 = 5.714×10⁻⁵ g, so **57.14 µg/100 ml**
- (b) **Above**: limit is 80 mg/100 ml blood = **35 µg/100 ml breath**"""),
    ("exam", "[4 marks] State the UK legal drink-driving limits and describe the procedure from roadside stop to evidential test.",
     """**Marking points:**
- E/W/NI: 80 mg/100 ml blood ≡ 35 µg/100 ml breath ≡ 107 mg/100 ml urine; Scotland 50 mg
- Stop any driver; test only if alcohol, traffic offence or accident is suspected
- Roadside **screening** (fuel cell); if over, **evidential** test on a fixed machine at the station
- 40–50 µg/100 ml: option of a blood/urine test (historical doubts about breath machines)"""),
]
