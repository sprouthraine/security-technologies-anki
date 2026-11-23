# Lecture 6 – Law Enforcement Technologies: Radar Systems, Non-Lethal Weapons & Alcohol Breathalysers

*Source: Lecture 6 Law Enforcement I – Radar Systems (Part 1 Fundamentals, Part 2 Case Studies); Law Enforcement II – High-Volume Technologies (Non-Lethal Weapons, Alcohol Breathalysers); Lecture 6 Problem Sheet (Dr Kevin Chetty)*

## Learning Outcomes
**Radar**
- Describe radar operation and its key parameters: **range, range resolution, bandwidth**
- Judge which radar types suit which police scenarios
- Explain **ground-penetrating radar (GPR)** and **through-the-wall radar (TTW)** and their technical challenges
- Convey civil-rights arguments against police use of TTW radar

**Non-lethal weapons**
- Explain how a stun gun (Taser) works, in terms of electrostatics and physiology
- Calculate shock current and show it is within safety bounds
- Convey civil-rights arguments against Taser use

**Breathalysers**
- Describe the chemistry of alcohol in blood, breath and urine, and the UK legal limits
- Explain the **fuel cell** principles behind breathalysers

---

# PART A – RADAR SYSTEMS (Law Enforcement I)

## 1. What Is Radar?
- **RADAR = RAdio Detection And Ranging.**
- Traditionally used by the **military, air traffic control and weather measurement**, and increasingly by **law enforcement**.

### 1.1 Police Uses
- Counter-terrorism and hostage scenarios
- Missing persons and hidden weapons
- Crime investigation and evidence gathering, cold cases
- Critical infrastructure protection
- Tactical planning
- Covert surveillance
- Border control

### 1.2 Radar Types Used by Police
| Radar | Use |
|---|---|
| **Ground Penetrating Radar (GPR)** | Searching for buried bodies, weapons, contraband |
| **Through-the-Wall Radar Imaging** | Point-of-entry decisions, covert surveillance, scene awareness |
| **Fencing radar** | Critical infrastructure and perimeter protection, VIP planning |
| **Doppler radar** | Vehicle speed monitoring |

## 2. Principle of Operation
1. A radio wave is transmitted from an **antenna** at t = 0.
2. It reaches the object after t_travel.
3. It **scatters in all directions**, and part of it returns to the antenna at t_return.
4. Round-trip time: **t_total = t_travel + t_return**.
- **Range:** **R = c · t_total / 2** (divide by 2 because the wave travels there and back).
- Radar can do more than detect and range (e.g. Doppler, imaging).

## 3. Range Resolution
- How **precisely** the radar can measure range.
- **Depends only on the bandwidth B** of the radio wave: **ΔR = c / (2B)**.
- Example: R = 100 m and ΔR = 2 m means the object lies somewhere within ±1 m (99–101 m).

## 4. Bandwidth
- A pure sinusoid has a single frequency. Real-world signals (sound, TV, WiFi) contain many frequencies.
- **Bandwidth = the range of frequencies in a wave or signal.**
- More bandwidth gives finer range resolution.

## 5. The Radar Band
- Occupies a large part of the EM spectrum: **radio and microwaves**, from **3 Hz to just under 3 THz**.
- Also heavily used for communications: cellular, TV/radio, WiFi, RFID, Bluetooth, satellites.
- Wavelengths range from **100,000 km** (space studies) to **1 mm** (whole-body scanning).

### 5.1 Sub-bands (learn these)
| Name | Abbrev. | Frequency range |
|---|---|---|
| Extremely low frequency | ELF | 3 – 30 Hz |
| Super low frequency | SLF | 30 – 300 Hz |
| Ultra low frequency | ULF | 300 Hz – 3 kHz |
| Very low frequency | VLF | 3 – 30 kHz |
| Low frequency | LF | 30 – 300 kHz |
| Medium frequency | MF | 300 kHz – 3 MHz |
| High frequency | HF | 3 – 30 MHz |
| Very high frequency | VHF | 30 – 300 MHz |
| Ultra high frequency | UHF | 300 MHz – 3 GHz |
| Super high frequency | SHF | 3 – 30 GHz |
| Extremely high frequency | EHF | 30 – 300 GHz |
- Memory aid: each band spans one decade, from **3×10ⁿ to 3×10ⁿ⁺¹ Hz**.

## 6. Case Study 1: Ground Penetrating Radar (GPR)
- The antenna transmits an EM wave into the ground, and the **reflections form an image** (e.g. of a clandestine burial).
- **Relative permittivity (εᵣ):** a material's ability to **store electrical energy**. When the wave meets a material with a **different εᵣ**, part of it reflects.
- **Reflectivity coefficient:** ρ = (√ε₁ − √ε₂) / (√ε₁ + √ε₂). The negative sign can be ignored.
  - Soil (εᵣ = 9) to bone (εᵣ = 4): ρ = (3 − 2)/(3 + 2) = **0.2**
  - Air (εᵣ = 1) to soil (εᵣ = 9): ρ = (1 − 3)/(1 + 3) = −0.5, so **0.5**
  - This explains why most energy is lost at the air–ground interface.

### 6.1 Image Quality vs Depth Trade-off (applies to all radars)
- **Higher frequencies** can "hold" more bandwidth, giving **better range resolution and image quality**.
- **Lower frequencies** suffer **less attenuation**, giving **deeper penetration**.

| GPR frequency | Max penetration depth |
|---|---|
| 1500 MHz | 0.5 m |
| 900 MHz | 1 m |
| 400 MHz | 4 m |
| 270 MHz | 6 m |
- Modern GPRs are **tunable**, so the operator picks the optimal frequency.

### 6.2 Suitability for Law Enforcement
- **Non-destructive:** evidence (e.g. bodies) is preserved for forensic archaeologists.
- **Non-contact:** large areas are scanned rapidly with no labour-intensive digging.
- **Hidden weapons:** metals and ceramics have **large εᵣ**, so they reflect strongly.
- Good for **landmine clearance**.

## 7. Case Study 2: Through-the-Wall (TTW) Radar
- The target is obscured by a barrier: walls, plasterboard, wooden or plastic doors, even curtains.
- **Differences from GPR:**
  - The target is usually **moving**, so the radar can exploit the **Doppler effect**.
  - Operations are **time-limited**, so speed is critical.
  - **Many air gaps**, and the operator is in a **high-risk position** next to the wall.

### 7.1 The Attenuation Problem
- Magnified at the **air–wall interface**, where there is significant scattering.
- At **high frequencies** only a tiny fraction penetrates concrete or brick. The weak reflection must also come **back through the wall**, so the signal is too weak for the radar to work.
- Therefore: **low frequency gives less attenuation but poorer images; high frequency gives more attenuation but better images.**

### 7.2 State of the Art
- **Ultra-wideband (UWB) radar:** novel techniques give **wide bandwidth at low frequencies**, combining penetration and resolution. Expensive.
- **Micro-Doppler:** small body movements (arm swing, legs, torso sway) allow **activity recognition, signs-of-life detection**, and distinguishing people from animals.
- **MIMO (Multiple-In, Multiple-Out):** borrowed from WiFi communications, enables **3D visualisation**.
- Different systems suit different scenarios.

## 8. TTW Radar and the Law: *United States v. Steven Denson* (2014)
- **December 2014:** US Marshals tracked fugitive Steven Denson to a house in Wichita. A **TTW radar** detected a person inside. Denson was arrested with **illegal firearms**.
- He tried to overturn the firearms charge on **invasion-of-privacy** grounds and was **unsuccessful**.
- The case led to national debate.
  - **Judge Neil Gorsuch:** *"New technologies bring with them not only new opportunities for law enforcement to catch criminals, but also new risks for abuse and new ways to invade constitutional rights."*
  - **Christopher Soghoian (ACLU):** TTW radar is among the **most intrusive** police tools. *"The idea that the government can send signals through the wall of your house to figure out what's inside is problematic."*
- The FBI and US Marshals had used these radars since **2012** (at least **$180,000** spent) with **no public disclosure** of how or when.

---

# PART B – NON-LETHAL WEAPONS (Law Enforcement II)

## 9. Non-Lethal Weapons
- Also called **compliance, less-lethal or pain-inducing** weapons: less likely to kill than a firearm.
- **Examples:**
  - **Water cannon**, **pepper spray / mace / tear gas** (civil disorder)
  - **Stun shields**, cattle-prods
  - **Dazzler:** directed visible light that temporarily blinds or disorients without long-term damage
  - **Long Range Acoustic Device (LRAD):** warning messages to crowds, with a jarring sound
  - **Riot control gun** (rubber bullets)
  - **Taser:** an **electroshock weapon**

## 10. The Taser
- A **Conducted Electrical Weapon (CEW)** that uses **high voltage** for **neuromuscular incapacitation** (disruption of voluntary muscle control).
- Used when lethal force is not required (shoot-to-kill prohibited) to **temporarily incapacitate** a suspect and **minimise escalation**.

### 10.1 Basic Operation
- **Two darts** are fired by a blast of **compressed nitrogen** at about **55 m s⁻¹** (under 20% of bullet speed).
- **Both darts must make contact** with the target (or one on the target and one on the ground) to **complete the circuit**.
- Delivers **high-voltage, low-amperage** pulses. Up to **50,000 V** is generated, but this is substantially reduced at the body.
- **Range: 7–11 m**, depending on model and limited by the trailing wire. Quick to reload.
- **Extras:** each trigger pull's time and duration is **recorded in memory**; **confetti** (ID tags) is released for identifying which gun fired; an attachable **video camera**; a **laser sight**.
- **Key parts:** confetti, darts, protective cover (blows off when fired), nitrogen propellant, in-built memory.

### 10.2 Closing the Circuit
- In about **30% of cases** darts lodge in clothing with no skin contact, leaving an open circuit.
- A **50 kV arcing pulse** **ionises the small air gap** to create a conductive path. It is used **only when the circuit is open**. **The body never experiences 50 kV.**
- Once the circuit is closed, the gun delivers a pulse train:
  - Each pulse lasts **100 µs**
  - Each pulse carries **100 µC** of charge
  - **19 pulses per second** (pulse repetition frequency, **PRF**)

### 10.3 Psychological Effect
- It often works **without being fired**, because of:
  - Taser effects seen on TV and social media
  - The **black and bright yellow** colour (the "bumble bee effect")
  - **Red laser dots** on the body, which tell the target they are in the line of sight

### 10.4 Physiological Effect
- **Skeletal muscle** is about **40% of body mass** and controls voluntary movement (flexing, grasping, walking, winking…).
- It is controlled by electrical impulses from the brain travelling along **motor nerves**.
- Taser pulses **jolt the motor nerves**, causing **involuntary contraction** of skeletal muscle fibres. The target spasms, drops and **loses motor control**.

### 10.5 Safety: "Current Kills!"
- **Ohm's law:** current through a conductor is **proportional to voltage**. The constant of proportionality involves **resistance R**, which is **inversely proportional** to current:
  **I = V / R** (equivalently V = IR). Units: A, V, Ω.
- **Household mains (240 V) example:**
  - Rubber shoes, R = 100,000 Ω: I = **2.4 mA**, a slight tingle, safe
  - Barefoot after a bath, R = 10,000 Ω: I = **24 mA**, probably **lethal**
- Danger: **ventricular fibrillation** (uneven, uncoordinated pumping of the heart).
- **Taser current:** I = Q/t (current = rate of flow of charge):
  I = (100 × 10⁻⁶ C × 19 pulses) / 1 s = **0.0019 A = 1.9 mA**
  This is **about 1% of the current needed to cause heart fibrillation**, so it is **safe**.
- **Tetanus region:** muscle contraction rates **above 70 per second** are dangerously strong (the disease tetanus causes contraction at this rate).
  - The Taser's PRF is **19 Hz**, far from the tetanus region. It is enough to disable without long-term damage.

### 10.6 Global & UK Use
- **Widely used:** UK, USA, Australia, Canada, Austria, Brazil, Greece, Israel, Singapore, Malaysia, New Zealand.
- **Limited specialist use (e.g. SWAT):** Germany, Ireland, Sweden.
- **UK timeline:**
  - **2003:** first 12-month trial. ACPO noted a striking **deterrent effect**.
  - **2007:** law changed to allow use in incidents of **serious threats and violence** (not only armed attackers).
  - **2008:** use no longer restricted to firearms officers.
  - **Illegal possession:** up to **10 years in prison** plus an unlimited fine. If disguised (e.g. as a torch or phone), a minimum of **5 years**.

### 10.7 Opposition
- **Amnesty International:** over **500 deaths** after Taser use in the US since 2001, though medical examiners cite electric shock as the cause in only a handful. Also reported as potential **torture tools** in policing and prisons.
- **"Don't tase me bro"** (Andrew Meyer, University of Florida): tasered by campus police while questioning a senator. This sparked national debate and memorabilia, and the publicity **enhanced the deterrent effect**.

---

# PART C – ALCOHOL BREATHALYSERS (Law Enforcement II)

## 11. The Problem of Drink Driving (UK, 2015)
- **220 killed**, **1,160 seriously injured**, over **8,000 casualties**
- Over **70,000** caught over the limit; over **5,000** charged with failing to provide a specimen
- Convictions are **85% male / 15% female**
- Deaths have fallen over recent decades.

## 12. Legal Limits
**England, Wales & Northern Ireland** (Road Traffic Act, s.11(2)):
| Specimen | Limit |
|---|---|
| **Blood (BAC)** | **80 mg / 100 ml** |
| **Breath** | **35 µg / 100 ml** |
| **Urine** | **107 mg / 100 ml** |
- These are equivalent. Blood is the "official standard"; breath and urine are **non-invasive** proxies.
- The UK is considering lowering BAC to 20 mg/100 ml.
- **Elsewhere:**
  - Scotland: 50 mg/100 ml (since 2014)
  - USA: 80
  - Europe: 50 (30 for new drivers under 2 years)
  - **Zero tolerance:** Croatia, Czech Republic, Brazil, Hungary
  - Most countries: 40–80
- **Statistical risk (North Review, 2010):**
  - BAC 20–50 mg/100 ml: **3×** the risk of dying in a crash
  - BAC 50–80 mg/100 ml: **6×** the risk

## 13. Testing Procedure
1. **Screening breath test** at the roadside. Police can stop any driver, but can only test if they suspect the driver has **consumed alcohol**, **committed a traffic offence**, or **been involved in an accident**.
2. If over the limit, an **evidential breath test** is taken on a fixed machine at the police station.
3. If the evidential reading is **40–50 µg/100 ml** (just over the limit, allowing a 5 µg tolerance), the driver may opt for a **blood or urine test**. This option dates from about 30 years ago, when there were doubts about breath-machine accuracy.
- Mobile evidential machines are expected in future.

## 14. The Chemistry of Alcohol
- Drinking alcohol is **ethanol, C₂H₅OH**. The **–OH (hydroxyl)** group defines alcohols (methanol, propanol, butanol, pentanol).
- It is absorbed into the bloodstream **without chemical change**.
- It is **volatile** (tends to vaporise), so it **evaporates as blood passes through the lungs**.
- The alcohol concentration in the **alveoli** (air sacs) is **directly proportional to BAC**.
- **Blood : breath ratio ≈ 2100 : 1**, meaning 2100 ml of alveolar air contains the same alcohol as 1 ml of blood.
- So a breathalyser **infers BAC** by measuring alcohol in expelled **alveolar air**.

## 15. Fuel Cells
- An **electrochemical energy conversion device** that converts the **chemical potential energy** of hydrogen (energy stored in molecular bonds) into **electrical energy**.
- Compact, quiet, lightweight. Reactions occur in a **Proton Exchange Membrane (PEM)**.
- **Fuel: hydrogen (H₂)** and **oxygen (O₂)** (often atmospheric).
- **By-products:** water, heat, electricity.
- **Unlike batteries**, which go "dead", fuel cells produce electricity **continuously as long as fuel is supplied**.

### 15.1 Basic Principle
- Components: **porous anode**, **porous cathode**, **electrolyte** (electrically conducting, made of anions and cations).
- **Anode:** hydrogen undergoes **oxidation** (loses electrons), producing **protons (H⁺)** and **electrons**.
  - H⁺ flows through the **electrolyte** to the cathode.
  - e⁻ flows through the **external circuit**, producing **current**.
- **Cathode:** H⁺, e⁻ and O₂ combine to form **water**.

## 16. Fuel Cell Breathalyser
- Contains **2 porous platinum electrodes** with an **acid electrolyte** between them.
- **Anode:** ethanol in breath is oxidised to **acetic acid (vinegar)**, protons and electrons:
  **CH₃CH₂OH(g) + H₂O(l) → CH₃CO₂H(l) + 4H⁺(aq) + 4e⁻**
- **Cathode:** atmospheric oxygen is reduced to water, completing the circuit:
  **O₂(g) + 4H⁺(aq) + 4e⁻ → 2H₂O(l)**
- **Measurement:** electrons flow through the circuit. **More alcohol gives more current.** A **microprocessor** converts the current into a breath-alcohol concentration.
- Cheap (**under £100**) and issued to all traffic police.
- **Further reading (not in the class test):** **infrared spectrometers**, which are bench-top and cannot be used in the field.

---

## Relevant Tools & Technologies
| Tool | Principle | Application |
|---|---|---|
| **Ground Penetrating Radar (GPR)** | Reflection at εᵣ boundaries; tunable frequency | Buried bodies, weapons, landmines |
| **Through-the-Wall Radar** | Doppler, UWB, micro-Doppler, MIMO | Hostage and counter-terrorism situations, surveillance |
| **Fencing radar** | Perimeter detection | Critical infrastructure, VIP protection |
| **Doppler radar / speed gun** | Doppler shift | Vehicle speed enforcement |
| **Taser (CEW)** | High-voltage, low-current pulses; Ohm's law; Q/t | Non-lethal incapacitation |
| Water cannon, pepper spray, tear gas, dazzler, LRAD, rubber bullets, stun shields | Various | Crowd and public-order control |
| **Fuel-cell breathalyser** | Ethanol oxidation on platinum electrodes produces current | Roadside screening |
| **Evidential breath machine** | Fixed, at police station | Prosecution evidence |
| **Infrared spectrometer** | IR absorption | Bench-top BAC measurement |
