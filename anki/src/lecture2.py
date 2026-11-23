DECK = "L2 Structure of Matter & Nuclear Science"
TAG = "L2"

CARDS = [
    # ---------------- concept cards ----------------
    ("basic", "Describe the Bohr model of the atom. Why is it called a 'planetary' model?",
     """- Negatively charged **electrons orbit** a central **nucleus** of positive **protons** and neutral **neutrons** (nucleons)
- Equal numbers of protons and electrons, so **net charge zero**
- Electrons sit in fixed-energy **shells**
- 'Planetary': electrons are planets orbiting the sun (nucleus); the **electrostatic force** plays the role of gravity"""),
    ("basic", "What are nucleons? What is the atomic number Z?",
     "**Nucleons** = protons + neutrons (particles in the nucleus). **Z** = number of protons; the periodic table is ordered by increasing Z."),
    ("basic", "What is the ground state of an atom?",
     "When electrons occupy the **lowest energy levels**, filling the shells from n = 1, then n = 2, n = 3, and so on."),
    ("basic", "What are valence electrons and why do they matter?",
     "The **outermost** (highest-energy shell) electrons. They determine how an atom **bonds** with other atoms, i.e. its **reactivity**."),
    ("basic", "Define an isotope. Give the carbon example.",
     "Same **atomic number Z** (same element), **different number of neutrons** N (so different A). C-12 (6n), C-13 (7n), C-14 (8n, unstable). Over 100 elements, but over 2000 isotopes."),
    ("basic", "Cation vs anion",
     """- **Cation:** positive ion, has **lost electrons** (not gained protons)
- **Anion:** negative ion, has **gained electrons**"""),
    ("basic", "Properties of Group 1 alkali metals",
     "1 valence electron, so **highly reactive** (more so down the group); form +1 cations; soft (cut with a knife); shiny surface tarnishes by oxidation, so they are **stored in oil**."),
    ("basic", "Properties of transition metals (groups 3–12)",
     "Good conductors of heat and electricity, malleable, less reactive than alkali metals, high density and melting point (except mercury). E.g. Fe, Cu, Ag, Au."),
    ("basic", "What are metalloids and why are they useful?",
     "Elements on the step-like boundary between metals and non-metals, with properties of both. Si and Ge are **semiconductors**, used in electronic components."),
    ("basic", "Properties and a use of the noble gases (group 18)",
     "**Full outer shells**, so highly stable/unreactive; odourless, colourless, monatomic. Used where reactions such as oxidation are unwanted, e.g. **argon in light bulbs** protects the tungsten filament."),
    ("basic", "What is mass spectrometry and what does it measure?",
     "An analytical technique to **identify substances, even in trace amounts**, quickly and accurately. It measures the masses and abundances of atoms/molecules by their **mass-to-charge ratio (m/z)**."),
    ("basic", "Three ionisation methods used in mass spectrometry",
     """- **Electron ionisation:** electron beam knocks off electrons
- **Chemical ionisation:** ions created through chemical reactions
- **Electrospray ionisation:** high voltage applied to an aerosol sprayed through a nozzle"""),
    ("basic", "ToF vs magnetic sector mass spectrometer: how are ions separated?",
     """- **Time-of-Flight:** an **electric field** accelerates ions; **lighter ions travel faster** and the flight time to the detector is measured
- **Magnetic sector:** a **magnetic field** bends ions along curved paths depending on charge-to-mass ratio; they hit different detector regions"""),
    ("basic", "How do you read a mass spectrograph?",
     "Each peak = a detected ion. **Peak height = abundance**; **x-axis position = mass-to-charge ratio**. Each substance has a **unique signature** (e.g. cocaine, TNT)."),
    ("basic", "Security applications of mass spectrometry",
     "Drug detection, explosive detection, blood-alcohol measurement, identifying radioactive materials, forensic trace evidence."),
    ("basic", "Define radioactivity / radioactive decay",
     "The **spontaneous disintegration of the nuclei of some nuclides** (radionuclides): unstable nuclei emit α, β⁻ or β⁺ particles, sometimes with γ rays, to become stable. α/β emission changes Z, creating a **new element**."),
    ("basic", "Alpha particle: composition, charge, mass, effect on the nucleus",
     "**2 protons + 2 neutrons** (helium nucleus ⁴₂He). Charge **+2e**, mass **4 mᵤ**, ~3×10⁷ m/s. **Z −2, A −4**."),
    ("basic", "Beta-minus particle: what is it, where does it come from, effect on the nucleus?",
     "An **electron emitted from the nucleus**, NOT from the electron shells. A **neutron changes into a proton**. Charge −e, mass 1/1836 mᵤ. **Z +1, N −1, A unchanged**."),
    ("basic", "Beta-plus (positron): what is it and its effect on the nucleus?",
     "A positively charged electron (anti-electron). A **proton changes into a neutron**. Charge +e, mass 1/1836 mᵤ. **Z −1, N +1, A unchanged**."),
    ("basic", "Gamma rays: nature and effect on the nucleus",
     "**EM waves** emitted from the nucleus after an energy change. **No charge, no mass**, no change to protons or neutrons. Highest frequency / shortest λ (10⁻¹⁰ to 2×10⁻¹³ m)."),
    ("basic", "Penetration of α, β, γ: range in air and what stops each",
     """- **α:** a few cm in air; stopped by **paper or skin** (very dangerous if ingested)
- **β:** a few m in air; stopped by **wood/plastic/thin metal**
- **γ:** large distances; only stopped by **high-Z materials, e.g. lead**"""),
    ("basic", "What is ionising radiation? Rank α, β, γ by ionising power.",
     "Radiation able to **eject electrons** from atoms/molecules, leaving ions. **α > β > γ**. Effects: tissue damage, radiation sickness, cancer, mutation, death. X-rays are non-nuclear ionising radiation."),
    ("basic", "Why doesn't the nucleus fly apart from proton repulsion?",
     "The **strong force**: a short-range attractive force between nucleons. Its associated **binding energy** determines whether a nucleus is stable."),
    ("basic", "State the two rules of nuclear stability and explain the second",
     """- (i) **N ≈ Z for Z < 20**
- (ii) **N > Z for Z > 20**: extra neutrons separate the protons, reducing repulsion
Smallest stable nucleus ¹₁H; largest **²⁰⁹₈₃Bi**."""),
    ("basic", "How do neutron-rich and proton-rich nuclides decay?",
     """- **Neutron-rich** (above the stability line): **β⁻** (n → p)
- **Proton-rich** (below the line): **β⁺** (lighter) or **α** (heavier) (p → n)"""),
    ("basic", "Define activity and the becquerel",
     "Activity = rate at which a radioactive material emits radiation. **1 Bq = 1 disintegration per second** (SI: s⁻¹). 3.7×10¹⁰ Bq = 1 curie."),
    ("basic", "Define radioactive half-life",
     "The time in which the amount of a radionuclide **decays to half its original value**. All radioactive decay follows a characteristic (exponential) decay curve."),
    ("basic", "What is a decay chain (radioactive series)?",
     "An unstable parent decays to an **unstable daughter**, which decays again, and so on, until a **stable** nuclide is reached. Shown on an A vs Z plot, e.g. Th-228 → Pb-208."),
    ("basic", "Why is Polonium-210 an effective assassination poison?",
     """- **Alpha emitter**: contained by glass, so easily smuggled through airports
- Once **ingested**, alpha is the most strongly ionising radiation, causing DNA damage, cell destruction and organ failure
- Max safe dose only **7 pg**; a speck is fatal
- Biological half-life ~30 days; physical half-life 138 days (intensely radioactive)"""),
    ("basic", "Evidence that the Litvinenko poisoning was state-sponsored",
     """- Po-210 extremely rare: ~**100 g/year**, made in **nuclear reactors**
- Amount used would cost **tens of millions of dollars**
- Suspects (Lugovoy, Kovtun) protected from extradition by Russia
- Inquiry (2016): 'probably' FSB, 'probably' approved by Putin"""),
    ("basic", "How was the Litvinenko radiation detected and identified?",
     """- **Geiger counter:** ionising events in a Geiger–Müller tube, read out as counts per second / clicks
- **Alpha-particle spectrometer:** identifies the isotope by characteristic energy (Po-210 alphas = **5.3 MeV**)
- A trail of contamination across London ('Hansel and Gretel breadcrumbs'): hotel tea room, teapot"""),

    # ---------------- cloze ----------------
    ("cloze", "Electron charge unit e = {{c1::1.602 × 10⁻¹⁹ C}}; atomic mass unit mᵤ = {{c2::1.661 × 10⁻²⁷ kg}}", ""),
    ("cloze", "Relative masses: proton = {{c1::1}} mᵤ, neutron = {{c2::1}} mᵤ, electron = {{c3::1/1836}} mᵤ", ""),
    ("cloze", "The nth electron shell holds up to {{c1::2n²}} electrons: n=1 holds {{c2::2}}, n=2 holds {{c3::8}}, n=3 holds {{c4::18}}", ""),
    ("cloze", "Nuclide notation ᴬ_Z X: A = {{c1::mass number (protons + neutrons)}}, Z = {{c2::atomic number (protons)}}, N = {{c3::A − Z}}", ""),
    ("cloze", "The first mass spectrometer was built by {{c1::Francis William Aston}} in {{c2::1919}} to measure the masses of {{c3::isotopes}}", "Nobel Prize in Chemistry 1922."),
    ("cloze", "1 curie (Ci) = {{c1::3.7 × 10¹⁰}} Bq", ""),
    ("cloze", "Half-lives: U-238 ≈ {{c1::4.5 billion years}}; C-14 = {{c2::5,730 years}}; tritium (H-3) = {{c3::12.32 years}}; Po-210 = {{c4::138 days}}", "U-235 is given as 25,000 years in the slides. H-7 = 21 yoctoseconds."),
    ("cloze", "Henri {{c1::Becquerel}} discovered radioactivity in {{c2::uranium}} and shared the {{c3::1903}} Nobel Prize with Marie and Pierre Curie", ""),
    ("cloze", "Speeds: α ≈ {{c1::3 × 10⁷}} m/s; β ≈ {{c2::2.9 × 10⁸}} m/s; γ = {{c3::c (3 × 10⁸ m/s)}}", ""),
    ("cloze", "Litvinenko was poisoned on {{c1::1 November 2006}} at the {{c2::Millennium Hotel, Mayfair}} with {{c3::Polonium-210}} in tea; he died after {{c4::23}} days", "Suspects: Andrey Lugovoy and Dmitry Kovtun. Inquiry report 21 January 2016."),
    ("cloze", "Po-210: maximum safe dose = {{c1::7 picograms}}; biological half-life ≈ {{c2::30 days}}; alpha energy = {{c3::5.3 MeV}}; decays to {{c4::lead}}", ""),
    ("cloze", "Largest stable nucleus: {{c1::bismuth-209 (²⁰⁹₈₃Bi)}}; smallest: {{c2::hydrogen-1}}", ""),

    # ---------------- calculations ----------------
    ("calc", "For ²³⁵₉₂U give the number of protons, neutrons and electrons (neutral atom).",
     "p = **92**, n = 235 − 92 = **143**, e = **92**"),
    ("calc", "Give p, n, e for ²⁴₁₂Mg²⁺ and ³⁵₁₇Cl⁻.",
     """- ²⁴₁₂Mg²⁺: p 12, n 12, **e 10** (cation, lost 2 e⁻)
- ³⁵₁₇Cl⁻: p 17, n 18, **e 18** (anion, gained 1 e⁻)"""),
    ("calc", "Complete: ²¹⁰₈₄Po → ? + ⁴₂He", "**²⁰⁶₈₂Pb** (A: 210 − 4; Z: 84 − 2)"),
    ("calc", "Complete: ²³⁹₉₄Pu → ? + ⁴₂He", "**²³⁵₉₂U** (plutonium in nuclear warheads)"),
    ("calc", "Complete: ¹⁴₆C → ? + ⁰₋₁e", "**¹⁴₇N** (β⁻: Z +1, A unchanged; radiocarbon dating)"),
    ("calc", "Complete: ⁹⁰₃₈Sr → ? + ⁰₋₁e  and  ¹¹₆C → ? + ⁰₊₁e",
     "**⁹⁰₃₉Y** (β⁻) and **¹¹₅B** (β⁺: Z −1)"),
    ("calc", "Th-228 (Z = 90) decays to Pb-208 (Z = 82). How many α and β⁻ decays?",
     """- ΔA = 20; only α changes A, so **5 α** (5 × 4)
- 5 α give Z 90 → 80; need 82, so **2 β⁻**"""),
    ("calc", "Po-210 (t½ = 138 days): what fraction remains after 414 days?",
     "414/138 = 3 half-lives, so (½)³ = **1/8 = 12.5%**"),
    ("calc", "80 µg of C-14 (t½ = 5730 yr). How much is left after 17,190 years?",
     "3 half-lives: 80 → 40 → 20 → **10 µg**"),
    ("calc", "Convert 7.4 × 10¹⁰ Bq to curies.", "7.4×10¹⁰ / 3.7×10¹⁰ = **2 Ci**"),
    ("calc", "Give the charge (C) and mass (kg) of an α-particle.",
     "Charge = 2 × 1.602×10⁻¹⁹ = **3.204 × 10⁻¹⁹ C**; mass = 4 × 1.661×10⁻²⁷ = **6.644 × 10⁻²⁷ kg**"),
    ("calc", "How many electrons can the n = 4 shell hold? Give the electron arrangement of Na (Z = 11).",
     "2n² = **32**; Na = **2, 8, 1** (1 valence electron, so a reactive Group 1 metal)"),

    # ---------------- exam-style ----------------
    ("exam", "[5 marks] Describe the Bohr model of the atom and explain how nuclide notation is used to describe elements and their isotopes. Use carbon as an example.",
     """**Marking points:**
- Electrons orbit a nucleus of protons and neutrons; electrostatic attraction (planetary analogy)
- Electrons in shells of fixed energy, 2n² per shell; ground state fills from n = 1
- Neutral atom: protons = electrons
- Notation ᴬ_Z X: A = nucleons, Z = protons, **N = A − Z**
- Isotopes: same Z, different N; e.g. ¹²₆C, ¹³₆C, ¹⁴₆C (6, 7, 8 neutrons); C-14 unstable (β⁻ decay, carbon dating)"""),
    ("exam", "[6 marks] Explain how a time-of-flight mass spectrometer identifies a substance, how the results are displayed, and give security applications.",
     """**Marking points:**
1. **Ionisation:** the sample (solid/liquid/gas) is converted to positive ions (electron, chemical or electrospray ionisation)
2. **Acceleration:** an electric field accelerates the ions across the mass analyser; lighter ions (same charge) travel faster, separating by m/z
3. **Detection:** ions trigger a current; flight time measured; current strength = abundance
- Output = **mass spectrograph**: peak height = abundance, x-position = m/z; a unique fingerprint
- Applications: drugs (cocaine), explosives (TNT), blood alcohol, radioactive material, forensic traces"""),
    ("exam", "[6 marks] Compare alpha, beta-minus, beta-plus and gamma radiation in terms of composition, charge, mass, effect on the nucleus, penetration and ionising ability.",
     """**Marking points:**
- **α:** 2p + 2n (He nucleus), +2e, 4 mᵤ; Z −2, A −4; stopped by paper/skin; **most ionising**
- **β⁻:** electron from the nucleus (n → p), −e, 1/1836 mᵤ; Z +1; stopped by wood/thin metal
- **β⁺:** positron (p → n), +e, 1/1836 mᵤ; Z −1
- **γ:** EM wave, no charge/mass, no change to Z or A; needs lead; least ionising, most penetrating
- α/β change the element; γ often accompanies them"""),
    ("exam", "[5 marks] Using an N vs Z plot, explain nuclear stability and how unstable nuclides decay towards stability.",
     """**Marking points:**
- Proton repulsion is balanced by the **strong force**; **binding energy** determines stability
- Light stable nuclei lie on **N ≈ Z** (Z < 20); heavier nuclei need **N > Z**, as extra neutrons separate the protons
- Stable range from ¹H to ²⁰⁹Bi
- **Neutron-rich** (above the line): β⁻ converts n → p
- **Proton-rich** (below the line): β⁺ (light) or α (heavy) converts p → n
- May proceed via a **decay chain** until stable"""),
    ("exam", "[6 marks] With reference to the Litvinenko case, explain why Polonium-210 was chosen as a weapon, why the attack was considered state-sponsored, and how the radioactive trail was detected.",
     """**Marking points:**
- Po-210 is an **α emitter**; α is stopped by glass, so it is undetectable in a sealed container and easy to smuggle
- Ingested α is highly ionising: DNA damage, organ failure; 7 pg safe dose; biological t½ ~30 days; t½ 138 days
- Rare (~100 g/yr from reactors), costing tens of millions, implying **state** resources; suspects shielded from extradition; inquiry implicated the FSB/Putin
- **Geiger counter** traced contamination (hotel, teapot, across London)
- **Alpha spectrometer** identified Po-210 by its characteristic **5.3 MeV** alpha energy"""),
    ("exam", "[4 marks] Define half-life and activity, and explain why Becquerel's uranium appeared to emit radiation endlessly.",
     """**Marking points:**
- Half-life: time for the amount of a radionuclide to halve; exponential decay curve
- Activity in becquerels: 1 Bq = 1 decay/s (s⁻¹); 1 Ci = 3.7×10¹⁰ Bq
- Uranium has a very long half-life (U-238 ~4.5 billion years)
- So it has been decaying slowly since Earth formed (~4500 million years ago) and appears constant"""),
    ("exam", "[4 marks] Describe the main sections of the periodic table and explain how electron configuration determines the chemical behaviour of group 1 and group 18 elements.",
     """**Marking points:**
- Ordered by Z; periods (rows) and groups (columns) with similar properties
- Most elements are metals; non-metals top right; metalloids on the boundary (semiconductors); transition metals in groups 3–12
- **Group 1:** 1 valence electron, easily lost to form +1 ions, so highly reactive
- **Group 18:** full outer shell, so inert (e.g. argon in light bulbs)"""),
]
