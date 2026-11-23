DECK = "L7 RFID & EMMIE"
TAG = "L7"

CARDS = [
    # ---------------- concept cards ----------------
    ("basic", "Define RFID",
     "**Radio Frequency Identification**: a technology that uses radio-frequency **electromagnetic fields** to **identify and track transponders (tags)** containing electronically stored information; tags attach to objects, animals or people. A **two-way communication** system (reader ↔ tag)."),
    ("basic", "RFID applications in the urban landscape",
     """- **Access control & ID:** biometric passports/borders, secure workplaces, gyms/lockers, car/bike sharing (Zipcar)
- **Transport flow:** NY **E-ZPass**
- **Payment:** **Oyster card**, contactless (Android Pay)
- **Loss prevention:** retail item tagging
- **Goods tracking**, including animals"""),
    ("basic", "Why was RFID developed, and its advantages over barcodes",
     "Originally to **replace barcodes in supply chains**: **wireless**, much **further distances**, **more information**, **more robust**, **simultaneous reading** of many tags (pallets)."),
    ("basic", "Two key components of an RFID tag",
     """- **Microchip (IC):** a few components, e.g. **capacitor, diode, transistor**
- **Antenna coil** (can be printed)
Some tags are only a few mm; active tags also contain a **battery**."""),
    ("basic", "What are passive RFID tags?",
     "The **most common** type (related to NFC); penny to credit-card size; **no internal power source**: they get **all their power by electromagnetic induction** from the reader's field."),
    ("basic", "Drivers of global RFID growth",
     "Falling production costs (cheap ICs, **RFID printing**); tags built into goods at manufacture; retailers' stock tracking and loss prevention (50% of the top 100 in 2016); smart cards (travel, payment); need for **secure access control** (city growth, terror threat). Est. **USD 40.5 bn by 2025**."),
    ("basic", "RFID attack: replay",
     "**Intercept and record** the modulated backscatter signal (e.g. as a person enters a building), then **replay the same code to the reader later**, causing a security breach."),
    ("basic", "RFID attacks: unauthorised scanning and reprogramming",
     """- **Unauthorised scanning:** spy on a person (ID, medication revealing illness, passport biometrics)
- **Reprogramming:** make an expensive item read as cheap
Both require the **encryption system to be known or hacked**."""),
    ("basic", "RFID attacks: denial of service and kill command",
     """- **DoS / jamming:** RFID frequencies are well known, so an **interfering signal** makes reader–tag communication impossible
- **Kill command abuse:** some tags have a kill command; an adversary could disable a card with important **medical or financial** information"""),
    ("basic", "Explain step by step how a passive RFID tag generates a modulated backscatter signal",
     """1. Reader sends an RF signal through its (loop) antenna
2. The EM field **induces a voltage** in the tag antenna, giving a small current
3. The current **charges a capacitor**, which **powers the IC**
4. The IC outputs its **unique ID** as **1s (high V) and 0s (low V)**
5. The RF signal is sent back to the reader, but first modified by a **transistor**
6. The transistor **switches the signal on/off** per the IC's voltages, embedding the ID: the **modulated backscatter signal**
7. The reader **decodes** it and identifies the tag (or not)"""),
    ("basic", "What is Ampère's law (as used in RFID read-range theory)?",
     "A current flowing through a conductor produces a **magnetic field** around the conductor. A circular loop antenna with N turns produces a field at a point on its axis."),
    ("basic", "Key observation from the loop-antenna field equation for RFID",
     "**B ∝ 1/r³**: the field decays very rapidly with distance. This is the **main limiting factor on RFID read range**; the equation is used to calculate reader range/sensitivity."),
    ("basic", "Three ways to increase the read range of an RFID reader (from B = µ₀INa²/2r³)",
     "Increase the **current I**, the **number of turns N**, or the **loop radius a** (B ∝ a²)."),
    ("basic", "Define the weber and the henry",
     """- **Weber (Wb):** unit of **magnetic flux** (density of field lines in an area); a change of 1 Wb/s induces 1 V EMF (Faraday). SI: kg m² s⁻² A⁻¹
- **Henry (H):** unit of **inductance**. SI: kg m² s⁻² A⁻²"""),
    ("basic", "Pros of passive RFID tags",
     """- **Cheap:** under 1p per tag, no batteries (but reader infrastructure costs)
- **Simultaneous reading:** a few hundred at a time
- **Long shelf life:** replace only if the coil/IC is damaged
- **Variable ranges:** LF 10 cm, HF < 3 m, UHF up to 100 m"""),
    ("basic", "Semi-passive vs active RFID tags",
     """- **Semi-passive:** battery powers the IC/circuitry, so **quicker response**; still backscatter
- **Active:** battery powers the IC **and a transmitter**; return signal is **broadcast** (not backscatter), a bespoke signal with more info and **longer range**; **expensive**; used for high-value goods over long distances (cars/parts on production lines)"""),
    ("basic", "What is a systematic review?",
     """A literature review that collects and **critically analyses multiple studies** to find what can reliably be said.
- Clear, **reproducible** strategy: specified databases, **pre-defined search terms**
- Clear **inclusion/exclusion rules**
- Explicit, systematic methods, so **less bias** than standard reviews"""),
    ("basic", "What is EMMIE and who developed it?",
     "An evidence rating / **coding system** designed for **crime prevention** systematic reviews, distilling their quality and coverage across 5 dimensions (**Effect, Mechanisms, Moderators, Implementation, Economic costs**). Johnson, Tilley & Bowers (2015)."),
    ("basic", "Apply each EMMIE dimension to RFID tagging in retail (the question asked)",
     """- **Effect:** are tags effective at reducing theft?
- **Mechanisms:** through what mechanisms do they reduce theft?
- **Moderators:** what conditions moderate effectiveness?
- **Implementation:** what are the implementation considerations?
- **Economics:** what are the costs and returns?"""),
    ("basic", "Retail crime context and loss prevention spending",
     "Global cost over **$214 bn** (2014–15); leads to business closure and higher prices. ~**0.65% of sales** spent on loss prevention (store detectives, CCTV, locked displays, packaging, staff screening, signage, alarms, floor design, RFID tags)."),
    ("basic", "What are EAS tags and their main advantage?",
     "**Electronic Article Surveillance** tags (incl. RFID), used for apparel, groceries, books, electronics. Advantage: tagged products **remain on open display**, accessible to customers and staff."),
    ("basic", "Sidebottom et al. inclusion criteria",
     """- Explicit goal of reducing **theft, shrinkage or loss** via security tags
- Specifically **retail** environments
- At least **one quantitative outcome** measure
- **Original research** findings"""),
    ("basic", "EMMIE Effect: findings of the retail tagging review",
     "**8 studies**, outcome usually **shrinkage**: **5 positive, 2 negative (backfire), 1 no significant change**, so mixed. Factors: hard vs soft tags, staff training/awareness, ease of removal, colour."),
    ("basic", "What is the backfire effect in retail tagging?",
     "Faulty tags, tags not disabled correctly, and system issues cause **high false-alarm rates**, so **staff are less likely to react** to alarms and tagging can increase theft."),
    ("basic", "EMMIE Mechanisms: how do tags reduce theft?",
     """- **Increased risk:** **perceived** (offender sees tags and chooses not to steal) and **actual** (alarm, staff detain offender)
- **Reduced reward:** item **damaged** if the tag is removed illegitimately (ink tags, apparel)
- **Increased effort:** harder to remove tagged items; tag removability becomes an **arms race**"""),
    ("basic", "EMMIE Moderators of tag effectiveness (5)",
     """1. **Shop setting and staff attitude**
2. **Customers** (including thieves)
3. **Tag type**
4. **Product**
5. **Police and criminal justice system**"""),
    ("basic", "Moderator: shop setting and staff attitude",
     """- Unalarmed doors are attractive low-risk exits; some areas allow tag removal; **signage** reminds shoppers
- Effectiveness **relies heavily on staff response**
- False alarms reduce staff confidence and anger shoppers, so staff wave people through (−); but they remind thieves tags are in use (+)"""),
    ("basic", "Casual vs professional shoplifters: which tagging strategy works best?",
     """- **Casual** (opportunistic, amateur, impulsive, unplanned): **high-profile tags + significant publicity**
- **Professional** (plan ahead, steal to order for resale, analyse store weaknesses, know which tags can be circumvented): **short-term and covert tags**; thieves aren't fully aware of the risk, which leads to arrests"""),
    ("basic", "Hard vs soft tags; selective tagging; display",
     """- **Hard:** conspicuous (overt), conveys risk of apprehension
- **Soft:** inconspicuous (covert); relies on staff vigilance; spotted only when the alarm sounds
- **Selective/fractional:** tag high-value / frequently stolen goods or a proportion
- **Display:** show only part of an item (one shoe/glove)"""),
    ("basic", "Moderator: police and criminal justice system",
     """- Effectiveness depends on **arrest, conviction, punishment**
- **Slow arrest:** staff deal with violent offenders, are off the floor, no guarantee of conviction
- **Removing a tag is not illegal; walking out without paying is**, so one offender de-tags and passes the item on
- Punishment may be 'worth the risk'"""),
    ("basic", "EMMIE Implementation: source vs in-store tagging",
     """- **Source:** proper, consistent application; saves staff time; but manufacturers use **different tag types/systems** (need multiple systems or supplier unification)
- **In-store:** correct attachment needed (too easy / too hard to remove)
- Correct **deactivation** at point of sale and avoiding **double-tagging** (both cause false alarms)
- One system for all merchandise"""),
    ("basic", "EMMIE Economics of tagging",
     """- **Costs:** tags (type, reusability); infrastructure (gates, removal/deactivation equipment); employees (gate security, training, tagging/de-tagging time)
- **Returns:** reduced **shrinkage**; efficient **stock-checking** tool"""),

    # ---------------- cloze ----------------
    ("cloze", "RFID bands: LF = {{c1::125–134 kHz}} (~10 cm); HF = {{c2::13.56 MHz}} (< 3 m); UHF = {{c3::433 MHz and 865–960 MHz}} (up to 100 m)", ""),
    ("cloze", "Loop antenna field (exact): B = {{c1::µ₀INa² / [2(a² + r²)^(3/2)]}}; when a² ≪ r²: B ≈ {{c2::µ₀INa² / (2r³)}}", ""),
    ("cloze", "Magnetic constant µ₀ = {{c1::4π × 10⁻⁷}} H m⁻¹", ""),
    ("cloze", "Magnetic field B is measured in {{c1::Wb m⁻² (tesla)}}; the weber in SI base units is {{c2::kg m² s⁻² A⁻¹}}", ""),
    ("cloze", "EMMIE = {{c1::Effect}}, {{c2::Mechanisms/mediators}}, {{c3::Moderators}}, {{c4::Implementation}}, {{c5::Economic costs}}", ""),
    ("cloze", "Retail tagging review: {{c1::8}} studies, {{c2::5}} positive, {{c3::2}} negative (backfire), {{c4::1}} no significant change", "Sidebottom et al. (2017), Crime Science 6:7"),
    ("cloze", "Global retail crime cost exceeded {{c1::$214 billion}} (2014–15); about {{c2::0.65%}} of sales is spent on loss prevention", ""),
    ("cloze", "Passive tags cost as little as {{c1::under 1 penny}} and can be read {{c2::a few hundred}} at a time", ""),

    # ---------------- calculations ----------------
    ("calc", "An HF reader loop: a = 4 cm, I = 20 mA. Minimum turns to read cards at 10 cm if B_min = 1 × 10⁻⁶ Wb m⁻²?",
     """N = 2Br³/(µ₀Ia²) = (2 × 10⁻⁶ × 0.1³) / (4π×10⁻⁷ × 0.02 × 0.04²)
= 2×10⁻⁹ / 4.021×10⁻¹¹ = 49.7, so **50 turns** (round up)
(Exact formula gives 63.)"""),
    ("calc", "A loop antenna carries 25 mA, radius 5 cm, 75 turns. Find B at 10 cm (Wb m⁻², 2 d.p.).",
     """B = µ₀INa²/(2r³) = (4π×10⁻⁷ × 0.025 × 75 × 0.05²)/(2 × 0.1³)
= 5.890×10⁻⁹ / 2×10⁻³ = **2.95 × 10⁻⁶ Wb m⁻²**
(Exact formula gives 2.11 × 10⁻⁶.)"""),
    ("calc", "N = 100, I = 50 mA, a = 3 cm. Find B at r = 20 cm.",
     "B = (4π×10⁻⁷ × 0.05 × 100 × 0.03²)/(2 × 0.2³) = **3.53 × 10⁻⁷ Wb m⁻²**"),
    ("calc", "N = 60, I = 30 mA, a = 4 cm; cards need 1 × 10⁻⁶ Wb m⁻². Find the maximum read range.",
     "r³ = µ₀INa²/(2B) = 1.81×10⁻³ m³, so r = **0.122 m ≈ 12.2 cm**"),
    ("calc", "A 50-turn, 4 cm radius loop must give 1 × 10⁻⁶ Wb m⁻² at 10 cm. What current is needed?",
     "I = 2Br³/(µ₀Na²) = 2×10⁻⁹ / (4π×10⁻⁷ × 50 × 1.6×10⁻³) = **0.0199 A ≈ 20 mA**"),
    ("calc", "If the read distance doubles, by what factor does B change? What if the loop radius doubles?",
     """- r doubled: B falls by **2³ = 8**
- a doubled: B rises by **2² = 4**"""),

    # ---------------- exam-style ----------------
    ("exam", "[1 mark] (Problem sheet Q1) What does the acronym RFID stand for?", "**Radio Frequency Identification**"),
    ("exam", "[4 marks] (Problem sheet Q2) Describe a method by which the security of an RFID system/tag may be compromised.",
     """**Model answer (replay attack):**
- An attacker uses a receiver to **intercept and record** the modulated backscatter signal transmitted by a legitimate tag (e.g. as an employee enters a building)
- The recorded identifier is stored
- Later the attacker **replays the same code** to the reader
- The reader accepts it as genuine, giving **unauthorised access**
**Alternatives:** unauthorised scanning/spying; reprogramming (cheap price); DoS jamming on known frequencies; kill command disabling medical/financial cards"""),
    ("exam", "[5 marks] (Problem sheet Q3) Explain how a modulated backscatter signal is generated in a passive RFID tag through electromagnetic induction.",
     """**Marking points:**
- Reader transmits an RF signal via a **loop antenna**
- The EM field **induces a voltage/current** in the tag's antenna coil (Faraday's law), with **no battery**
- The current **charges a capacitor**, which **powers the IC**
- The IC outputs its **unique ID** as high/low voltages (1s and 0s)
- A **transistor switches** the returning RF signal on/off according to the ID, giving the **modulated backscatter**
- The reader decodes it and identifies the tag"""),
    ("exam", "[5 marks] (Problem sheet Q4) A new HF RFID reader loop antenna has radius 4 cm and current 20 mA. What is the minimum number of turns so access cards can be read from 10 cm? (B_min = 1×10⁻⁶ Wb m⁻²)",
     """- State B = µ₀INa²/(2r³) (a² ≪ r²) and rearrange: **N = 2Br³/(µ₀Ia²)**
- Convert: a = 0.04 m, r = 0.1 m, I = 0.02 A
- N = (2 × 1×10⁻⁶ × 1×10⁻³)/(4π×10⁻⁷ × 0.02 × 1.6×10⁻³) = 2×10⁻⁹/4.021×10⁻¹¹
- N = 49.7, so **50 turns** (round up to meet the minimum)"""),
    ("exam", "[5 marks] (Problem sheet Q5) An airport HF RFID reader loop carries 25 mA, has radius 5 cm and 75 turns. What is the magnetic field strength 10 cm from the centre? (Wb m⁻², 2 d.p.)",
     """- B = µ₀INa²/(2r³)
- = (4π×10⁻⁷ × 0.025 × 75 × (0.05)²)/(2 × (0.1)³)
- = 5.890×10⁻⁹ / 2×10⁻³
- **B = 2.95 × 10⁻⁶ Wb m⁻²**"""),
    ("exam", "[6 marks] Compare passive, semi-passive and active RFID tags and state the frequency bands and read ranges of RFID systems.",
     """**Marking points:**
- **Passive:** no battery, powered by induction, modulated backscatter; cheap (< 1p); long shelf life; simultaneous reads; most common
- **Semi-passive:** battery powers the IC, giving faster response
- **Active:** battery powers the IC and a **transmitter**; broadcasts a bespoke signal; more info, longest range; expensive; high-value goods tracking
- **LF 125–134 kHz (~10 cm); HF 13.56 MHz (< 3 m); UHF 433 / 865–960 MHz (up to 100 m)**"""),
    ("exam", "[5 marks] Explain the factors that determine the read range of a passive RFID system, with reference to the magnetic field of a loop antenna.",
     """**Marking points:**
- Ampère's law: current in the loop produces a magnetic field
- **B = µ₀INa²/[2(a²+r²)^(3/2)] ≈ µ₀INa²/(2r³)** when a ≪ r
- **B ∝ 1/r³**: rapid decay is the main limit on read range
- Increase I, N or a to extend range (B ∝ I, N, a²)
- The tag needs a minimum field to induce enough current to power the IC; frequency band also sets typical range (LF/HF/UHF)"""),
    ("exam", "[4 marks] Discuss the privacy and security concerns associated with the growing use of RFID in cities.",
     """**Marking points:**
- Massive growth: smart cards, passports, retail, access control
- **Unauthorised scanning:** profiling (ID, medication, biometrics)
- **Reprogramming:** price fraud
- **Replay:** cloning access credentials
- **DoS jamming** on well-known frequencies; **kill command** abuse disabling medical/financial cards
- Encryption is the key defence (attacks need it known or hacked)"""),
    ("exam", "[8 marks] Using the EMMIE framework, evaluate the evidence on whether RFID/security tagging is an effective method of reducing theft in retail environments.",
     """**Marking points:**
- Systematic review (Sidebottom et al.): reproducible search, inclusion criteria (retail, theft goal, quantitative outcome, original research)
- **Effect:** 8 studies, 5 positive, 2 backfire, 1 null, so mixed; backfire from false alarms reducing staff response
- **Mechanisms:** increased perceived/actual risk; reduced reward (damage, e.g. ink tags); increased effort (arms race in removal)
- **Moderators:** shop layout/staff response; casual (overt + publicity) vs professional (covert, short-term) thieves; hard vs soft tags, selective tagging; product value/shape; CJS response (removing a tag isn't illegal)
- **Implementation:** source vs in-store tagging; deactivation; double-tagging; one system
- **Economics:** tag/infrastructure/staff costs vs reduced shrinkage + stock checking
- **Conclusion:** effectiveness is context-dependent and relies on staff and implementation"""),
    ("exam", "[4 marks] What is a systematic review, and why is the EMMIE framework useful for assessing crime-prevention evidence?",
     """**Marking points:**
- Collects and critically analyses multiple studies with explicit, reproducible methods (databases, pre-defined terms, inclusion rules), giving less bias
- EMMIE: designed for crime prevention; a coding system for review quality/coverage
- It goes beyond 'does it work?' (**Effect**) to **how** (Mechanisms), **when/for whom** (Moderators), **how to deliver** (Implementation) and **cost** (Economics)
- This lets practitioners transfer interventions to their own context"""),
    ("exam", "[5 marks] Explain how the type of shoplifter and the type of tag moderate the effectiveness of retail tagging.",
     """**Marking points:**
- **Casual:** opportunistic/impulsive; deterred by **high-profile overt (hard) tags + publicity** raising perceived risk
- **Professional:** plan, steal to order, know how to defeat tags; **covert/soft, short-term** tags catch them unaware, leading to arrests
- **Hard tags:** conspicuous deterrence; **soft tags:** covert, rely on staff vigilance
- **Selective/fractional** tagging of high-value/high-theft items; display part items
- Little benefit tagging low-value goods; tag shape must suit shelving"""),
]
