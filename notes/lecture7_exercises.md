# Lecture 7 – Practice Exercises & Solutions: RFID & EMMIE

> **Part 1** reproduces the official RFID problem sheet (the PDF is titled *"Lecture 9 – Problem Sheet"*, but it covers the Lecture 7 RFID content; /20 marks). The sheet had **no answer key**, so the solutions below were worked out from the lecture material. **Part 2** adds extra practice questions.

---

# PART 1 – Official Problem Sheet

### Q1. What does the acronym RFID stand for? [1]
**Solution:** **Radio Frequency Identification.**

### Q2. Describe a method by which the security of an RFID system/tag may be compromised. [4]
**Solution (any one, well described):**
- **Replay attack:** intercept and record the **modulated backscatter signal** (e.g. as a person enters a building), then **replay the same code to the reader later**, gaining unauthorised access.
- **Unauthorised scanning:** covertly read tags to spy on a person (ID, medication, passport biometrics). Requires the encryption to be known or hacked.
- **Reprogramming:** rewrite a chip so an expensive item reads as a cheap one.
- **Denial of Service:** RFID frequencies are well known, so an **interfering signal** can jam reader–tag communication.
- **Kill-command abuse:** disable a card holding important medical or financial information.

### Q3. Explain how a modulated backscatter signal is generated in a passive RFID tag through electromagnetic induction. [5]
**Solution**
1. The reader transmits an RF signal through its (loop) antenna.
2. The **EM field induces a voltage** in the tag's antenna coil (Faraday's law), producing a small current.
3. The current **charges a capacitor**, which **powers the IC** (no battery).
4. The IC outputs its **unique digital identifier** as **1s (high voltage) and 0s (low voltage)**.
5. The RF signal is sent back to the reader, but first a **transistor switches it on and off** according to the IC's high/low voltages, **embedding the identifier**. This is the **modulated backscatter signal**.
6. The reader **decodes** the signal and identifies the tag.

### Q4. A new HF RFID reader has a loop antenna of radius a = 4 cm carrying I = 20 mA. What is the minimum number of turns so that access cards can be read from 10 cm? (A minimum field of 1 × 10⁻⁶ Wb m⁻² is required.) [5]
**Solution**
- Use B ≈ µ₀ I N a² / (2r³) and rearrange: **N = 2 B r³ / (µ₀ I a²)**
- Convert units: a = 0.04 m (a² = 1.6 × 10⁻³ m²); r = 0.1 m (r³ = 1 × 10⁻³ m³); I = 0.02 A; µ₀ = 4π × 10⁻⁷
- Numerator: 2 × 1 × 10⁻⁶ × 1 × 10⁻³ = 2 × 10⁻⁹
- Denominator: 4π × 10⁻⁷ × 0.02 × 1.6 × 10⁻³ = 4.021 × 10⁻¹¹
- N = 2 × 10⁻⁹ / 4.021 × 10⁻¹¹ = 49.74, so the minimum is **50 turns** (round up)
- *Check with the exact formula (a² + r²)^(3/2): N = 62.1, so 63 turns. Here a is not much smaller than r, so the approximation underestimates N. Use the course approximation unless told otherwise.*

### Q5. An airport HF RFID reader's loop antenna carries 25 mA, has radius 5 cm and 75 turns. What is the magnetic field strength 10 cm from the centre of the loop (Wb m⁻², 2 d.p.)? [5]
**Solution**
- B ≈ µ₀ I N a² / (2r³)
- = (4π × 10⁻⁷ × 0.025 × 75 × 0.05²) / (2 × 0.1³)
- = (4π × 10⁻⁷ × 0.025 × 75 × 2.5 × 10⁻³) / (2 × 10⁻³)
- = 5.890 × 10⁻⁹ / 2 × 10⁻³
- **B ≈ 2.95 × 10⁻⁶ Wb m⁻²**
- *Exact formula: B = 2.11 × 10⁻⁶ Wb m⁻².*

---

# PART 2 – Extra Practice Questions

## Section A – RFID Basics & Applications

### Q6. Define RFID and give one example application in each of four urban categories. [4]
**Solution:** RFID uses radio-frequency EM fields to **identify and track tags** containing electronically stored information. It is a two-way communication system.
- **Access control:** biometric passports, university or work access cards
- **Transport monitoring:** New York E-ZPass
- **Payment:** Oyster card, contactless payment
- **Loss prevention:** retail item tagging
- **Goods tracking:** supply chains, animals

### Q7. State the frequency bands and typical read ranges for LF, HF and UHF RFID. [3]
**Solution:** **LF:** 125–134 kHz, ~10 cm. **HF:** 13.56 MHz, under 3 m. **UHF:** 433 MHz and 865–960 MHz, up to 100 m.

### Q8. Give four advantages of RFID over barcodes. [4]
**Solution:** Wireless; works at much greater distances; holds more information; more robust; many tags can be read simultaneously (e.g. pallets).

### Q9. What are the two main components of an RFID tag? [2]
**Solution:** A **microchip/IC** (capacitor, diode, transistor) and an **antenna coil** (can be printed).

### Q10. Give three drivers of the global growth of RFID. [3]
**Solution:** Lower production costs (cheap ICs, **RFID printing**); tags built into goods at manufacture; retailers adopting it for stock tracking and loss prevention; growth of smart cards; the need for secure access control (growing cities, terror threat). The market was estimated at USD 40.5bn by 2025.

## Section B – Tag Types

### Q11. Compare passive, semi-passive and active tags. [6]
**Solution**
| | Passive | Semi-passive | Active |
|---|---|---|---|
| Power | None (induction) | Battery powers the IC | Battery powers the IC **and a transmitter** |
| Return signal | Modulated backscatter | Backscatter | **Broadcast** bespoke signal |
| Range | Short (LF 10 cm to UHF 100 m) | Similar, **faster response** | **Longest** |
| Cost | Under 1p | Moderate | **Expensive** |
| Use | Cards, retail tags | — | High-value goods (cars and parts on production lines) |

### Q12. Give four pros of passive RFID tags. [4]
**Solution:** **Cheap** (under 1p, no battery, though readers cost money); **simultaneous reading** of a few hundred tags; **long shelf life** (replace only if damaged); **variable ranges**.

## Section C – Magnetic Field Calculations

### Q13. State the exact and approximate formulas for the field on the axis of a loop antenna, and the condition for the approximation. [3]
**Solution**
- Exact: B = µ₀ I N a² / [2(a² + r²)^(3/2)]
- Approximation: B ≈ µ₀ I N a² / (2r³), valid when **a² ≪ r²**

### Q14. How does B change when the read distance doubles? What does this mean for RFID? [2]
**Solution:** B ∝ 1/r³, so doubling r reduces B by **2³ = 8**. This rapid decay is the **main limit on RFID read range**.

### Q15. Name three ways to increase a reader's field strength at a given distance. [3]
**Solution:** Increase the **current I**, the **number of turns N**, or the **loop radius a** (B ∝ a²).

### Q16. A reader has N = 100 turns, I = 50 mA, a = 3 cm. Find B at r = 20 cm. [4]
**Solution:** B = (4π × 10⁻⁷ × 0.05 × 100 × 0.03²) / (2 × 0.2³) = (4π × 10⁻⁷ × 4.5 × 10⁻³) / 0.016 = **3.53 × 10⁻⁷ Wb m⁻²**

### Q17. A reader has N = 60, I = 30 mA and a = 4 cm. A card needs at least 1 × 10⁻⁶ Wb m⁻². What is the maximum read range? [4]
**Solution**
- r³ = µ₀ I N a² / (2B) = (4π × 10⁻⁷ × 0.03 × 60 × 1.6 × 10⁻³) / (2 × 10⁻⁶) = 1.81 × 10⁻³ m³
- r = (1.81 × 10⁻³)^(1/3) = **0.122 m ≈ 12.2 cm**

### Q18. A 50-turn loop of radius 4 cm must produce 1 × 10⁻⁶ Wb m⁻² at 10 cm. What current is needed? [3]
**Solution:** I = 2 B r³ / (µ₀ N a²) = 2 × 10⁻⁶ × 10⁻³ / (4π × 10⁻⁷ × 50 × 1.6 × 10⁻³) = **0.0199 A ≈ 20 mA**

### Q19. Define the weber and the henry, with SI base units. [4]
**Solution**
- **Weber:** the unit of magnetic flux. A change of 1 Wb per second induces 1 V (Faraday's law). **kg m² s⁻² A⁻¹**.
- **Henry:** the unit of inductance. **kg m² s⁻² A⁻²**.

## Section D – EMMIE & Systematic Reviews

### Q20. What is a systematic review, and why does it involve less bias than a standard literature review? [4]
**Solution:** A literature review that collects and critically analyses multiple studies using a **clear, reproducible strategy**: specified databases, **pre-defined search terms**, and **explicit inclusion/exclusion rules**. Because the methods are explicit and systematic rather than selective, it introduces **less bias**.

### Q21. What does EMMIE stand for? State the question each dimension asks of RFID tagging in retail. [5]
**Solution**
- **E**ffect: do tags reduce theft?
- **M**echanisms: how do they reduce theft?
- **M**oderators: under what conditions do they work better or worse?
- **I**mplementation: what practical issues arise?
- **E**conomics: what are the costs and returns?

### Q22. State the inclusion criteria used by Sidebottom et al. [4]
**Solution:** An explicit goal of reducing theft, shrinkage or loss through security tags; a **retail** setting; at least **one quantitative outcome** measure; **original research** findings.

### Q23. Summarise the "Effect" findings, and explain the backfire effect. [4]
**Solution**
- **8 studies**, with **shrinkage** as the outcome: **5 positive, 2 negative, 1 no significant change**, so mixed results.
- **Factors:** hard vs soft tags, staff training, ease of removal, colour.
- **Backfire effect:** faulty tags, incorrect deactivation and system issues cause **high false-alarm rates**, so staff stop reacting to alarms and theft can increase.

### Q24. Describe the three mechanisms by which tags reduce theft. [4]
**Solution**
1. **Increased risk:** **perceived** (the thief sees tags and decides not to steal) and **actual** (the alarm sounds and staff detain the thief).
2. **Reduced reward:** the item is damaged if the tag is removed illegitimately (ink tags, mainly on apparel).
3. **Increased effort:** tagged items are harder to remove, though tag removability becomes an arms race.

### Q25. List the five moderators of tag effectiveness. [5]
**Solution:** (1) shop setting and staff attitude; (2) customers, including thieves; (3) tag type; (4) product; (5) police and criminal justice system.

### Q26. Which tagging strategy works best against (a) casual and (b) professional shoplifters, and why? [4]
**Solution**
- **(a) Casual** (opportunistic, impulsive, unplanned): **high-profile (overt) tags plus significant publicity**, which raise perceived risk.
- **(b) Professional** (plan ahead, steal to order, know how to defeat tags): **short-term and covert tags**. They aren't fully aware of the risk, which leads to **arrests**.

### Q27. Compare hard and soft tags, and explain selective/fractional tagging. [4]
**Solution**
- **Hard tags:** conspicuous (overt), conveying risk of apprehension.
- **Soft tags:** inconspicuous (covert). They rely on staff vigilance; the thief only notices when the alarm sounds.
- **Selective/fractional tagging:** tag only high-value or frequently stolen goods, or a proportion of stock.

### Q28. How can false alarms have both negative and positive effects? [2]
**Solution:** **Negative:** staff lose confidence and wave people through, and legitimate shoppers are angered. **Positive:** alarms remind would-be thieves that tags are in use.

### Q29. Why does the criminal justice system moderate tag effectiveness? [3]
**Solution:** Deterrence depends on **arrest, conviction and punishment**. Slow police response leaves staff dealing with possibly violent offenders, off the shop floor, with no guarantee of conviction. **Removing a tag is not illegal**, only leaving without paying is, so offenders pass de-tagged items to accomplices. The punishment may be "worth the risk".

### Q30. Compare source tagging and in-store tagging (Implementation). [4]
**Solution**
- **Source** (by the manufacturer): proper and consistent application; saves staff time. But different manufacturers use different tags and systems, requiring multiple systems or supplier unification.
- **In-store:** depends on correct attachment by staff (tags can be too easy or too hard to remove). Incorrect deactivation at the till or **double-tagging** causes false alarms. One system for all merchandise is preferable.

### Q31. List the costs and returns considered under Economics. [4]
**Solution**
- **Costs:** tags (vary by type and **reusability**); **infrastructure** (gates, removal and deactivation equipment); **employees** (gate security, training, tagging and de-tagging time).
- **Returns:** **reduced shrinkage**; an efficient **stock-checking** tool.

### Q32. What are EAS tags, and what is their key advantage for retailers? [2]
**Solution:** **Electronic Article Surveillance** tags, used across apparel, groceries, books and electronics. The key advantage: products can **stay on open display** and remain accessible, rather than being locked away.
