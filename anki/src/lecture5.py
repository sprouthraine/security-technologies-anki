DECK = "L5 Crime Prevention & Design Against Crime"
TAG = "L5"

CARDS = [
    # ---------------- concept cards ----------------
    ("basic", "Why is equating 'opportunity' with the situation incomplete (Ekblom)?",
     "Opportunity is an **ecological interaction between situation and offender**. An open window three floors up is only an opportunity to someone with the **resources** (agility, courage, a ladder). And opportunity requires a **goal**: opportunity to do *what*?"),
    ("basic", "Elements needed for a full characterisation of opportunity",
     """- **Perception/affordance**: can the offender see and understand it?
- **Goals** (positive + hygiene)
- **Resources/capability**
- **Presence/access** (incl. telepresence via internet, drones)
- **Actions/scripts**
- **Dynamics**: encountering, seeking, creating opportunities"""),
    ("basic", "Positive goals vs hygiene goals",
     "**Positive:** what the offender wants to achieve (steal the car / get the money). **Hygiene:** what they want to avoid while doing it (arrest, injury)."),
    ("basic", "How does Rational Choice relate to opportunity and risk (ISO 31000)?",
     "Rational Choice factors **risk of harm, effort, reward** all relate to goal states and all contain a risk element; ISO 31000 defines **risk = effect of uncertainty on objectives**."),
    ("basic", "Definitions of 'problem' and 'problem solving' used in the lecture",
     """- **Problem:** 'the difference between a goal state and a current state' (**Jonassen 2000**)
- **Problem solving:** 'the generation and selection of discretionary actions to bring about a goal state' (**Scandura 1977**)
- Ekblom: what stops exploiting an opportunity being 'child's play'; purpose that is frustrated"""),
    ("basic", "How are opportunity and problem related? Why is this 'flip' useful?",
     "One party's opportunity is another's (or the state's) **problem**. Useful for **conflicts** (entangled problems/opportunities) and **arms races** (each move sets a problem for the opponent, who finds an 'adjacent opportunity' as a countermove)."),
    ("basic", "Definition of technology used by Ekblom (adapted from W. Brian Arthur)",
     "Principles derived from **natural phenomena**, realised as applications and products in more or less complex combinations, to meet some **criminal or security goal**."),
    ("basic", "Four roles technology can play in crime/prevention (with examples)",
     """- Part of the **opportunity or problem** (CCTV can monitor misbehaviour OR spy on changing rooms; car alarms)
- Helps either side **adapt to conditions** (street lighting)
- **Halts** a launched attack (personal attack alarm)
- **Mitigates** consequences (backing up phone data)"""),
    ("basic", "Three ways to reduce the risk of a crime type",
     """1. **Eliminate** the possibility (designing out car tax discs removes forgery)
2. **Reduce the likelihood**
3. **Reduce the harm**, during (injury in robbery) or after (ID theft from a stolen wallet)"""),
    ("basic", "Strategic preventive actions from the speaker notes (anticipate, learning path…)",
     """- **Anticipate:** crime impact statements (could it be a target, tool, or environment for crime?)
- **Learning path:** feed info on new crimes back to designers, planners, insurers
- **Encourage variety** (criminals love standardisation)
- **Performance standards**, research-based
- **Exploit new tech** for prevention
- **Avoid rigidity** (remember the dinosaurs)"""),
    ("basic", "Civil-world trade-offs that constrain security technology",
     "Security vs: **convenience, social inclusivity, market freedom, sustainability, freedom of movement, aesthetics, health & safety, privacy, trust & collective efficacy**. Offenders are less constrained."),
    ("basic", "What is a crime script and a script clash?",
     "**Crime script** (Derek Cornish): the procedure for preparing for and committing a crime. Both offenders and preventers use scripts, giving **tactical script clashes** between them."),
    ("basic", "List the generic script clashes (offender v preventer)",
     """- Wield force v resist
- Conceal intent v detect
- Conceal traces v detect them
- Challenge suspect v give plausible response
- Snoop v maintain privacy
- Act at will v control misbehaviour
- Take v keep target asset
- Confront v avoid
- Surprise/ambush v be alert
- Trap v elude
- Surveil v conceal
- Pursue v escape"""),
    ("basic", "Why do script clashes matter for technology design?",
     "They are **generic and perennial**; technology can **disrupt the balance** and favour one side after a breakthrough, so we must **design to advantage the good side**."),
    ("basic", "Desirable techno-trends for tweaking trade-offs and biasing clashes",
     """- **Creative leap, not compromise** (internal combustion engine gave armour AND mobility)
- **Tunability** to context ('what works' is context-dependent)
- **Smart discriminator functions** (serve users, thwart thieves)
- **Adaptable/reconfigurable form** (swing-down fire escapes)"""),
    ("basic", "What is the 'smart discriminator' problem?",
     "What's good for legitimate users (smaller, lighter, portable, durable, cheap, easy) is also good for thieves. How do you serve one while thwarting the other? **User-friendly but abuser-unfriendly**."),
    ("basic", "Examples of large-scale evolutionary change creating crime opportunities",
     """- **Godfrey-Smith:** cultural-phylogenetic change, e.g. the **Neolithic Revolution** (farming, density, stealable property)
- **Felson & Eckert:** **mass transportation** changing routine activities
- Now: **ICT, generative/agentic AI, LLMs**
Script clashes can flip to favour offenders, causing obsolescence."""),
    ("basic", "Examples of offender–preventer co-evolution (arms races)",
     "Banknote security, tax evasion, **car theft (Rick Brown)**, malware, script kiddies, rogue AI; classic case: **the safe (Neil Shover)**."),
    ("basic", "How has the spread of criminal know-how accelerated?",
     "From **pubs and prisons**, to the **internet**, guidance documents, video tips, to **crime-as-a-service** (e.g. Ransomware-as-a-Service) and **AI agents**."),
    ("basic", "Gearing up against crime: the dynamic strategy for arms races",
     """- Encourage **variety**
- Build capacity to **out-innovate** offenders
- **Performance standards** / generic principles
- **Study offender resources**
- **Exploit new technology**
- **Avoid rigidity & lock-in**
- **Future-proofing**; **pipelines of innovation**
- **Prepare for disruption** (quantum crypto/cracking)
- **Learn from other evolutionary struggles**"""),
    ("basic", "Other evolutionary struggles to learn from, and one lesson",
     "**Military/hybrid warfare, predator–prey, pest–farmer, bacteria–antibiotic, immune system–virus.** E.g. gazelles use **remote sensing** (vision evolved 60+ times) and integrate senses to avoid **false alarms**; antibiotics show 'wonder solutions' are impermanent; IBM's artificial immune systems."),
    ("basic", "Hard vs soft approaches: the Victoria Centre example",
     "Youths spitting and dropping cans in the Victoria Centre, Nottingham, were moved on **softly** with an uncomfortable rail, a sloped floor and hot lights, so they left **without realising they were manipulated** and weren't motivated to retaliate. Hard isn't always best (the reed and the oak)."),
    ("basic", "What is TRIZ and how does it relate to crime prevention?",
     """Theory of inventive problem solving from analysis of patents:
- **40 inventive principles**; **39 contradiction parameters**; lookup tables
- **Evolutionary trends** (solid → segmented → flexible → field)
- Addresses the fundamental contradiction: **user-friendly vs abuser-unfriendly**"""),
    ("basic", "Limitations of technological approaches to security",
     """- **Self-defeating**: clunky systems exceed the **compliance budget**
- **Make things worse**: false burglar alarms
- **'Bolt-on, drop-off'** single fixed defence
- **Solution/supply-driven**: canalises responses (CCTV rush, white elephants)
- **Simplistic techno-determinism**: ignores complex adaptive systems"""),
    ("basic", "Why are these not inherent limitations of security technology?",
     "They apply only to tech that is **poorly designed**, **over-relied on in isolation**, **incorporated too late**, **rigid**, or **not adaptable/upgradable** during its lifetime."),
    ("basic", "Wheelie bin: what failure does it illustrate and what was the design response?",
     "**Failure to 'think thief'**: 'a receptacle for grime or a tool for crime?' Burglars use it as a **leg-up**. A trapping lid was rejected (child safety). Response: the **No ClimBIN** (Jenny Loqvist, Griffith University, 2008)."),
    ("basic", "Example of 'failure to think drug user'",
     "Phone boxes with sides obscured by adverts became convenient places for drug users to inject, one even under an advert for a drug-help organisation."),
    ("basic", "What is a crime harvest?",
     "**Ken Pease**: a new product, not designed against crime, generates a wave of crime (e.g. 'What made Queen Victoria go red?')."),
    ("basic", "What are 'paranoid products'?",
     "A warning against **obsession** with security: over-secured designs that sacrifice usability."),
    ("basic", "Define Design Against Crime (DAC)",
     "Uses the **tools, processes and products of design**, in partnership with agencies, companies, individuals and communities, to **prevent all kinds of crime** (incl. ASB, drugs, terrorism) and **promote quality of life/sustainable living**, via designs that are **fit for purpose** and contextually appropriate."),
    ("basic", "Scope of Design Against Crime, with examples",
     """- Secure products (Puma bike; milled vs hammered coins against clipping)
- Security products (clothes tagging device)
- Security components (brand protection)
- Security systems (chips protecting alpacas)
- Security communication/art
- Secure clothing (jacket camera, anti-theft bag)
- Secure places (Maiden Castle, Sandy Hook School)
- Secure communities"""),
    ("basic", "Is design a product or a process? What is reframing?",
     "**Both.** SCP/CPTED practitioners see end products, but design is fundamentally a **process and way of thinking**, covering **problem-finding/formulation** as well as solving. **Reframing** = redefining the problem (e.g. the CT litter bin, UT Sydney)."),
    ("basic", "The four elements of the Security Function Framework",
     """- **Purpose**: what crime problem does it address?
- **Niche**: how does it fit the security ecosystem?
- **Mechanism**: how does it prevent crime?
- **Technology**: how is it realised (materials, construction, operation)?"""),
    ("basic", "Stop Thief Chair: mechanism and technicality",
     """**Mechanism:** physical **anchorage** of the bag (easier for the user to release); **mobilises people** as preventers (surveillance, reaction); bag within **personal defensible space**; **deters** by raising perceived risk.
**Technicality:** **twin notch** in the leading edge of the seat; the bag handle is held between the seat and the back of the user's knees."""),

    # ---------------- cloze ----------------
    ("cloze", "CRAVED hot products: {{c1::Concealable}}, {{c2::Removable}}, {{c3::Available}}, {{c4::Valuable}}, {{c5::Enjoyable}}, {{c6::Disposable}}", "Risk factors for theft."),
    ("cloze", "Crime scripts were proposed by {{c1::Derek Cornish}}; crime harvests by {{c2::Ken Pease}}; the safe arms race by {{c3::Neil Shover}}", ""),
    ("cloze", "A problem is 'the difference between a {{c1::goal state}} and a {{c2::current state}}' (Jonassen 2000)", ""),
    ("cloze", "ISO 31000 defines risk as the {{c1::effect of uncertainty on objectives}}", ""),
    ("cloze", "TRIZ has {{c1::40}} inventive principles and {{c2::39}} contradiction parameters; evolution trend: solid → {{c3::segmented}} → {{c4::flexible}} → {{c5::field}}", ""),
    ("cloze", "Security Function Framework: {{c1::Purpose}}, {{c2::Niche}}, {{c3::Mechanism}}, {{c4::Technology}}", ""),
    ("cloze", "The fundamental contradiction at the heart of crime prevention: designs must be {{c1::user-friendly}} yet {{c2::abuser-unfriendly}}", ""),
    ("cloze", "Stop Thief Chair security niche: a {{c1::securing product}}; key feature: a {{c2::twin notch}} in the seat edge", ""),
    ("cloze", "The {{c1::No ClimBIN}} was designed by Jenny Loqvist (Griffith University, 2008) in response to burglars using wheelie bins as a {{c2::leg-up}}", ""),

    # ---------------- exam-style ----------------
    ("exam", "[6 marks] 'Opportunity is not simply a property of the situation.' Discuss, explaining the elements required for a full characterisation of opportunity and how opportunity relates to problems.",
     """**Marking points:**
- Opportunity = **ecological interaction** of situation and offender (open-window/ladder example)
- Needs a stated **goal**: positive + hygiene (Rational Choice: risk, effort, reward; ISO 31000)
- **Perception/affordance, resources, presence/access (telepresence), scripts, dynamics** (encounter/seek/create)
- Problem = gap between goal and current state (Jonassen); problem solving (Scandura)
- **Flip:** offender's opportunity = preventer's problem; drives **arms races** via adjacent opportunities"""),
    ("exam", "[6 marks] Explain the concept of script clashes between offenders and preventers. Give examples and discuss how technology can shift the balance.",
     """**Marking points:**
- Crime scripts (Cornish): procedures for preparing for and committing crime; preventers have scripts too
- Clashes: wield force v resist; conceal intent v detect; snoop v privacy; take v keep; surveil v conceal; pursue v escape; trap v elude…
- They are **generic and perennial**
- Technology breakthroughs **disrupt the balance**, favouring whoever adopts first (e.g. through-wall radar favours police; encryption/AI may favour offenders)
- Hence **design to advantage the good side**; smart discriminators, tunability, creative leaps"""),
    ("exam", "[6 marks] Using the idea of co-evolution, explain why technological crime-prevention solutions become obsolete, and outline a strategy for 'gearing up' against crime.",
     """**Marking points:**
- Offenders adapt; arms races (the safe, car theft, banknotes, malware)
- Wider change: Neolithic revolution, mass transport, ICT/AI; know-how spreads via the internet and crime-as-a-service
- Script clashes flip, so what works now may not later
- Gearing up: **variety**, out-innovate capacity, **performance standards**, study offender resources, exploit new tech, **avoid rigidity/lock-in**, future-proofing, innovation pipelines, prepare for disruption (quantum), learn from other struggles (predator–prey, antibiotics, immune system)"""),
    ("exam", "[5 marks] Discuss the limitations of purely technological approaches to security, and explain why Ekblom argues these are not inherent to technology.",
     """**Marking points:**
- Compliance budget overload; false alarms make things worse; bolt-on/drop-off single defences; solution-driven lock-in (CCTV white elephants); techno-determinism ignoring complex adaptive systems
- Civil trade-offs: privacy, convenience, aesthetics, inclusivity, etc.
- Not inherent: the failures arise when tech is poorly designed, used in isolation, added too late, rigid, or not upgradable
- Therefore integrate with human/system factors and use **Design Against Crime** thinking early"""),
    ("exam", "[6 marks] Using the Security Function Framework, describe the Stop Thief Chair as a designed crime-prevention intervention.",
     """**Marking points:**
- **Purpose:** principally a functional chair; subsidiary purpose of reducing bag theft in bars/restaurants; desire requirements (stylish, economical, venue reputation) and hygiene requirements (safe, sustainable)
- **Niche:** a securing product
- **Mechanism:** anchorage that is easier for the user to release; mobilises users as preventers; personal defensible space; deterrence by perceived risk
- **Technology:** twin notch cut into the seat front; handle trapped between seat and knees"""),
    ("exam", "[5 marks] What is meant by 'thinking thief'? Illustrate with examples of design failures and responses, and explain how CRAVED helps designers.",
     """**Marking points:**
- Designers must anticipate how products/places can be **misused** by offenders
- Wheelie bin as a burglar's leg-up, leading to the **No ClimBIN**; phone boxes with obscured sides used for drug injection
- **Crime harvests** (Pease): new products trigger crime waves
- **CRAVED** (Concealable, Removable, Available, Valuable, Enjoyable, Disposable) identifies hot products to protect
- Avoid **paranoid products**; balance with usability (user-friendly / abuser-unfriendly)"""),
    ("exam", "[4 marks] Explain the scope of Design Against Crime and whether design should be viewed as a product or a process.",
     """**Marking points:**
- DAC: design tools/processes/products in partnership to prevent crime and promote quality of life; fit for purpose
- Scope: secure products, security products/components, systems, communication/art, clothing, places (Maiden Castle, Sandy Hook), communities
- Both product and **process**; design thinking includes **problem-finding/reframing** (CT litter bin)
- Can be hi-tech or lo-tech"""),
]
