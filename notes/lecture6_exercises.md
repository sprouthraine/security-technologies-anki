# Lecture 6 – Practice Exercises & Solutions: Law Enforcement Technologies (Radar, Tasers, Breathalysers)

> **Part 1** reproduces the official *Lecture 6 Problem Sheet* (with model answers, /20 marks). **Part 2** adds extra practice questions in the same style.

---

# PART 1 – Official Problem Sheet

### Q1. The waves used in radar systems fall into which band(s) of the EM spectrum? (Tick one) [1]
☐ Millimetre waves ☐ Infra-red and microwaves ☐ **Radio and microwaves** ☐ Radio waves ☐ X-rays

**Solution:** **Radio and microwaves** (3 Hz – just under 3 THz).

### Q2. State the formula for the range resolution ΔR of a radar. [1]
**Solution:** **ΔR = c / (2B)**, where c = 3 × 10⁸ m s⁻¹ and B = signal bandwidth.

### Q3. Tick the statement that best describes EM waves in through-the-wall radar. [1]
- ☐ High f: less attenuation, poorer images
- ☐ **High f: more attenuation, better / more accurate images** ✔
- ☐ Low f: more attenuation, poorer images
- ☐ Low f: less attenuation, better images

**Solution:** **High-frequency EM waves experience more attenuation by a wall but generate better/more accurate images** than low-frequency waves. Higher frequencies can hold more bandwidth, giving better range resolution.

### Q4. Hostage scenario: a TTW radar at 5.8 GHz with 100 MHz bandwidth measures a round-trip time of 1.6 × 10⁻⁷ s to the hostage-taker. [4]
**[a] What is the range? [b] What is the range resolution?**

**Solution**
- **[a]** R = c·t_total / 2 = (3 × 10⁸ × 1.6 × 10⁻⁷) / 2 = **24 m**
- **[b]** ΔR = c / 2B = 3 × 10⁸ / (2 × 100 × 10⁶) = **1.5 m** (that is, ±0.75 m)

### Q5. State Ohm's law in words and derive the relationship between I and V. [4]
**Solution**
- The current (I) through a conductor is **proportional to the voltage (V)**. The constant of proportionality involves the **resistance (R)**, which is inversely proportional to the current.
- I ∝ V, so I = constant × V, so **I = V/R**, which rearranges to **V = IR**.

### Q6. A new Taser design delivers 32 pulses per second, each carrying 650 µC. [4]
**[a] Calculate the current delivered per second (1 d.p.). [b] Will it pass safety checks?**

**Solution**
- **[a]** I = Q/t = (650 × 10⁻⁶ C × 32) / 1 s = 0.0208 A = **20.8 mA**
- **[b]** **No.** The PRF (32) is well below the dangerous tetanus region (above 70), but **20.8 mA is in the unsafe current region** (compare 24 mA as "probably lethal"). Effects include sustained muscular contraction, extreme pain, respiratory arrest and possibly death. A standard Taser delivers 1.9 mA.

### Q7. Which element do fuel cells typically use to convert chemical potential energy into electrical energy? [1]
**Solution:** **Hydrogen** (oxygen also accepted).

### Q8. Bob's BAC is 120 mg/100 ml. He is stopped and given a roadside breath test. [4]
**[a] What is the breathalyser reading in µg/100 ml (2 d.p.)? [b] Is he over the UK limit? (Blood : breath = 2100 : 1)**

**Solution**
- **[a]** 120 mg/100 ml = 120 × 10⁻³ g/100 ml. Breath = 120 × 10⁻³ / 2100 = 5.714 × 10⁻⁵ g = **57.14 µg/100 ml**
- **[b]** **Above the limit.** The limit is 80 mg/100 ml blood, equivalent to **35 µg/100 ml breath**.

---

# PART 2 – Extra Practice Questions

## Section A – Radar Fundamentals

### Q9. What does RADAR stand for? List four police uses. [3]
**Solution:** **RAdio Detection And Ranging.** Uses: counter-terrorism and hostage situations, missing persons and hidden weapons, crime investigation and cold cases, critical infrastructure protection, tactical planning, covert surveillance, border control.

### Q10. Match each police radar to its use: GPR, TTW, fencing radar, Doppler radar. [4]
**Solution**
- **GPR:** buried bodies, weapons, contraband
- **TTW:** point-of-entry decisions, covert surveillance, scene awareness
- **Fencing radar:** perimeter and critical infrastructure protection, VIP planning
- **Doppler radar:** vehicle speed monitoring

### Q11. A radar pulse returns after 2 × 10⁻⁷ s. What is the target range? [2]
**Solution:** R = 3 × 10⁸ × 2 × 10⁻⁷ / 2 = **30 m**

### Q12. What bandwidth is needed for a range resolution of 0.3 m? [2]
**Solution:** B = c / (2ΔR) = 3 × 10⁸ / 0.6 = 5 × 10⁸ Hz = **500 MHz**

### Q13. A radar's range is 100 m with ΔR = 2 m. Between what distances could the object actually be? [1]
**Solution:** **99 m to 101 m** (±1 m).

### Q14. Define bandwidth. Why does range resolution depend only on bandwidth? [2]
**Solution:** Bandwidth is the **range of frequencies** contained in a signal. ΔR = c/2B has no other variable: more bandwidth gives a sharper effective pulse and finer range discrimination.

### Q15. Name the radio sub-band containing (a) 5.8 GHz, (b) 13.56 MHz, (c) 125 kHz, (d) 900 MHz, (e) 25 GHz. [5]
**Solution:** (a) **SHF**; (b) **HF**; (c) **LF**; (d) **UHF**; (e) **SHF** (EHF starts at 30 GHz).

## Section B – GPR

### Q16. What is relative permittivity, and why does it matter for GPR? [2]
**Solution:** εᵣ is a material's ability to **store electrical energy**. When the radar wave meets a boundary between materials of **different εᵣ**, part of it reflects back to the antenna and forms the image.

### Q17. Calculate the reflectivity coefficient for (a) soil (εᵣ = 9) to bone (εᵣ = 4), (b) air (εᵣ = 1) to soil, (c) soil to water (εᵣ = 81). [6]
**Solution:** ρ = (√ε₁ − √ε₂)/(√ε₁ + √ε₂)
- (a) (3 − 2)/(3 + 2) = **0.2**
- (b) (1 − 3)/(1 + 3) = −0.5, so **0.5** (ignore the sign)
- (c) (3 − 9)/(3 + 9) = −0.5, so **0.5**

### Q18. A forensic team suspects a body is buried 3 m deep. Which GPR frequency should they use and why? [3]
**Solution:** **400 MHz** (max depth about 4 m). 900 MHz and 1500 MHz cannot reach 3 m. 270 MHz reaches 6 m but has lower frequency, so less bandwidth and poorer resolution. Choose the **highest frequency that still reaches the target depth**.

### Q19. Give three reasons GPR suits law enforcement. [3]
**Solution:** **Non-destructive** (evidence preserved for forensic archaeologists); **non-contact** and rapid (large areas, no labour-intensive digging); detects **hidden weapons** (metals and ceramics have large εᵣ); good for landmine clearance.

## Section C – Through-the-Wall Radar

### Q20. Give three ways TTW radar scenarios differ from GPR. [3]
**Solution:** The target is usually **moving** (Doppler can be exploited); the operation is **time-limited**; there are **many air gaps**, and the operator is in a **high-risk position** next to the wall.

### Q21. Explain the attenuation problem for TTW radar and how UWB addresses it. [3]
**Solution:** Significant scattering at the **air–wall interface**. At high frequencies only a tiny fraction penetrates brick or concrete, and the weak reflection must pass back through the wall, so the signal is too weak. **UWB** uses novel techniques to obtain **wide bandwidth at low frequencies**, giving both penetration and resolution (but it is expensive).

### Q22. What are micro-Doppler and MIMO, and what do they add to TTW radar? [3]
**Solution**
- **Micro-Doppler:** Doppler signatures of small body movements (arm swing, legs, torso sway). Enables **activity recognition, signs-of-life detection**, and distinguishing people from animals.
- **MIMO** (borrowed from WiFi): **3D visualisation**.

### Q23. Summarise *United States v. Denson* and the civil-liberties arguments against TTW radar. [4]
**Solution**
- **2014:** US Marshals used TTW radar to confirm Denson was inside a Wichita house. He was arrested with illegal firearms and argued **invasion of privacy**, unsuccessfully.
- **Judge Gorsuch:** new technologies bring "new risks for abuse and new ways to invade constitutional rights".
- **ACLU (Soghoian):** among the most intrusive tools; "sending signals through the wall of your house… is problematic".
- Agencies used the radars from **2012** (at least $180k spent) with **no public disclosure**.

## Section D – Tasers & Non-Lethal Weapons

### Q24. List five non-lethal weapons. [3]
**Solution:** Water cannon, pepper spray/mace/tear gas, stun shields/cattle-prods, dazzler, Long Range Acoustic Device, riot-control gun (rubber bullets), Taser.

### Q25. Describe how a Taser completes its circuit, including when the darts are stuck in clothing. [4]
**Solution:** Two darts are fired by **compressed nitrogen** (~55 m s⁻¹, range 7–11 m). Both must touch the target (or one on the target and one on the ground) to close the circuit. In about **30%** of cases the darts lodge in clothing. A **50 kV arcing pulse** then **ionises the air gap** to create a conductive path. It is used only on an open circuit, so **the body never receives 50 kV**.

### Q26. Explain the physiological effect of a Taser. [3]
**Solution:** Skeletal muscle (~40% of body mass) is controlled by electrical impulses from the brain via **motor nerves**. Taser pulses **jolt the motor nerves**, causing **involuntary contraction** of the muscle fibres. The target spasms, falls and loses motor control (**neuromuscular incapacitation**).

### Q27. A standard Taser delivers 19 pulses per second, each of 100 µC. Show that it is safe in terms of (a) current and (b) contraction rate. [4]
**Solution**
- (a) I = 100 × 10⁻⁶ × 19 / 1 = **1.9 mA**, about 1% of the fibrillation current, so safe.
- (b) PRF = 19 Hz, far below the **tetanus region (above 70 contractions per second)**.

### Q28. A prototype stun gun delivers 20 pulses per second of 50 µC. Calculate the current. [2]
**Solution:** I = 50 × 10⁻⁶ × 20 = **1.0 mA**, which is safe.

### Q29. A person touches 240 V mains with a body-to-ground resistance of 2,000 Ω. Find the current and comment. [2]
**Solution:** I = V/R = 240/2000 = **0.12 A = 120 mA**. This is far above the 24 mA "probably lethal" level, with a high risk of ventricular fibrillation.

### Q30. Give three psychological factors that let Tasers achieve compliance without being fired. [3]
**Solution:** Effects seen on **TV and social media** ("Don't tase me bro"); the **black and bright yellow** colour (bumble bee effect); **red laser dots** showing the target they are in the line of sight.

### Q31. Outline the UK history of Taser use and the main opposition arguments. [4]
**Solution**
- **2003:** 12-month trial with a strong deterrent effect (ACPO). **2007:** use allowed for serious threats and violence. **2008:** not restricted to firearms officers. **Illegal possession:** up to 10 years plus an unlimited fine (minimum 5 years if disguised).
- **Opposition (Amnesty):** over 500 US deaths since 2001 (shock cited in only a handful); potential use as a **torture** tool in policing and prisons.

## Section E – Breathalysers

### Q32. State the UK (England, Wales, NI) limits for blood, breath and urine, and the Scottish BAC limit. [4]
**Solution:** Blood **80 mg/100 ml**; breath **35 µg/100 ml**; urine **107 mg/100 ml**. Scotland: **50 mg/100 ml** BAC (since 2014).

### Q33. An evidential breath reading is 50 µg/100 ml. What is the equivalent BAC? What option does the driver have? [3]
**Solution**
- Blood = 50 µg × 2100 = 105,000 µg = **105 mg/100 ml**, which is over the 80 mg limit.
- Readings of **40–50 µg/100 ml** give the driver the option of a **blood or urine** test.

### Q34. A driver has a BAC of 60 mg/100 ml. Find the breath reading and state whether they are over the limit in (a) England and (b) Scotland. [3]
**Solution**
- Breath = 60,000 µg / 2100 = **28.57 µg/100 ml**
- (a) **Under** (below 35 µg / 80 mg)
- (b) **Over** (Scotland's limit is 50 mg/100 ml)

### Q35. Explain why breath can be used to infer blood alcohol. [3]
**Solution:** Ethanol (C₂H₅OH) is absorbed into the blood **without chemical change** and is **volatile**, so it evaporates into the alveoli as blood passes through the lungs. The alveolar concentration is **directly proportional to BAC**, with a blood : breath ratio of **2100 : 1**.

### Q36. When can UK police require a roadside breath test? [3]
**Solution:** When they suspect the driver has **consumed alcohol**, **committed a traffic offence**, or **been involved in an accident**.

### Q37. Describe how a fuel cell breathalyser works, including the electrode equations. [6]
**Solution**
- **Structure:** two **porous platinum electrodes** with an **acid electrolyte** between them.
- **Anode (oxidation):** CH₃CH₂OH + H₂O → CH₃CO₂H + 4H⁺ + 4e⁻ (ethanol to acetic acid)
- H⁺ moves through the electrolyte; e⁻ flows through the **external circuit**.
- **Cathode:** O₂ + 4H⁺ + 4e⁻ → 2H₂O
- **Current is proportional to alcohol concentration.** A microprocessor converts the current into a breath-alcohol reading.

### Q38. How does a fuel cell differ from a battery? [2]
**Solution:** A battery stores all its chemicals inside and eventually goes "dead". A fuel cell produces electricity **continuously as long as fuel (H₂/O₂) is supplied**. By-products: water, heat, electricity.
