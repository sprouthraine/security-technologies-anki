DECK = "L1 Waves & Fields"
TAG = "L1"

CARDS = [
    # ---------------- concept cards ----------------
    ("basic", "What is a wave? (definition + key idea)",
     """**Definition:** a time-varying quantity that is also a function of position.
- Waves **transport energy without transporting matter**
- Analogy: a Mexican wave in a stadium (energy moves round, people stay put)"""),
    ("basic", "What two properties must a medium have for a mechanical wave to travel through it? Define each.",
     """- **Elasticity:** ability to return to original size/shape after being deformed (stretched/compressed)
- **Inertia:** resistance of an object to a change in its velocity"""),
    ("basic", "How is a mechanical wave produced? Distinguish a wave pulse from a periodic wave.",
     """An initial input of energy (a disturbance) into the medium, e.g. a stone thrown into a pond or a flick of a string.
- **Single** disturbance gives a **wave pulse**
- **Continuous** regular disturbance gives a **periodic (sinusoidal) wave**"""),
    ("basic", "What is the difference between wave speed and particle velocity?",
     """- **Wave speed (v):** speed at which the **energy** propagates through the medium
- **Particle velocity:** speed at which the **particles** of the medium vibrate about equilibrium"""),
    ("basic", "Longitudinal wave: definition and example",
     """Vibrations are **parallel** to the direction of propagation. They create **compressions** and **rarefactions**.
Example: **sound**, a pressure wave from vibrating sources (loudspeaker, larynx)."""),
    ("basic", "Transverse wave: definition and examples",
     """Vibrations are **at right angles** to the direction of energy travel (particles move up and down about equilibrium).
Examples: waves on a string, water waves, **all EM waves**."""),
    ("basic", "Mechanical vs electromagnetic waves: medium, type, examples",
     """- **Mechanical:** need a medium; longitudinal **or** transverse; e.g. sound, water waves, guitar string, seismic waves
- **EM:** no medium (travel in a vacuum at c); **transverse only**; perpendicular E and B field oscillations; e.g. light, microwaves, X-rays, radio"""),
    ("basic", "What sound does a massive explosion make in space? Why?",
     "**None.** Sound is a mechanical (longitudinal pressure) wave and needs a medium. Space is a vacuum."),
    ("basic", "Define amplitude (and what it represents)",
     "The maximum disturbance from the undisturbed (equilibrium) position. It represents the **power** of the wave (loud sound = high amplitude). Units depend on the quantity measured (dB, V, lumens)."),
    ("basic", "Define wavelength (λ)",
     "The distance over which the wave shape repeats: the distance between the same points on two adjacent waves (e.g. crest to crest). Unit: **m**."),
    ("basic", "Define frequency and time period",
     """- **Frequency (f):** number of wave cycles per second (Hz). For sound it relates to pitch.
- **Period (T = 1/f):** time for the wave pattern to advance one wavelength (s)"""),
    ("basic", "Why must we use dimensional analysis?",
     "It identifies the **base SI units** of physical quantities. This allows real-world interpretation and comparison between measures (e.g. N = m·kg·s⁻²)."),
    ("basic", "How are gamma rays and X-rays of the same wavelength (e.g. 0.1 nm) distinguished?",
     "By their **source**: gamma rays come from **nuclear radioactivity** (the nucleus); X-rays originate from **electrons**."),
    ("basic", "Give a property/application of each EM band: gamma, X-ray, infrared, microwave, radio",
     """- **Gamma:** absorbed by cells, used to kill bacteria in food
- **X-ray:** penetrates skin/tissue but not bone (medical imaging, baggage scanners)
- **Infrared:** body heat (thermal imaging, night vision)
- **Microwave:** similar frequency to water molecules (ovens); mm-wave scanners, radar
- **Radio:** communications (cellular, WiFi, satellite), radar, ATC, GPS, RFID"""),
    ("basic", "What are ultrasound and infrasound? Give uses of each.",
     """- **Ultrasound (> 20 kHz):** medical imaging, non-destructive testing (pipeline fractures), bat sonar
- **Infrasound (< 20 Hz):** communication by elephants, giraffes and whales; detecting volcanic eruptions"""),
    ("basic", "Interference: what is it, the two types, and the condition required?",
     """Superposition of two waves giving a resultant with higher or lower amplitude.
- **Constructive:** waves in phase reinforce, giving larger amplitude
- **Destructive:** waves in antiphase cancel
- **Condition:** same or similar frequency (a radio wave and an X-ray won't interfere)"""),
    ("basic", "What is the Doppler effect?",
     """A change in frequency/wavelength (a **Doppler shift**) when source and receiver **move relative to each other**.
- Approaching: frequency increases (higher pitch)
- Receding: frequency decreases (lower pitch)
Application: **radar speed guns**."""),
    ("basic", "Fourier Series vs Fourier Transform",
     """- **Fourier Series:** any **periodic** function expressed as an infinite sum of sines and cosines
- **Fourier Transform:** generalisation to **non-periodic** functions; decomposes a **time-domain** signal into its **frequency-domain** components (spectral decomposition)"""),
    ("basic", "What does the magnitude squared of the Fourier Transform, |F(ω)|², represent?",
     "The amount of **power** a signal has at a particular frequency."),
    ("basic", "Why are Fourier methods relevant to real-world security signals?",
     "Real signals (speech, WiFi, radar returns) are not single-frequency sinusoids but contain **many frequencies**. The FT reveals their spectral content, e.g. checking a WiFi signal against its **spectral mask**."),
    ("basic", "What did James Clerk Maxwell show?",
     "That electricity and magnetism are manifestations of the **same phenomenon**, travelling together perpendicularly as a transverse wave at the speed of light (**Maxwell's equations**, the 'second great unification of physics')."),
    ("basic", "State the right-hand grip rule",
     "Wrap the right hand around a current-carrying wire with the **thumb pointing in the direction of current**. The **curled fingers** show the direction of the magnetic field."),
    ("basic", "Three ways to increase the strength of an electromagnet",
     """1. Place an **iron core** in the coil
2. Add **more turns**
3. Increase the **current**"""),
    ("basic", "State Faraday's law of electromagnetic induction (words)",
     "The induced EMF (voltage) in a closed circuit is equal to the **rate of change of magnetic flux** through it. Moving a magnet through a coil induces an EMF, and a current if the circuit is complete."),
    ("basic", "Four ways to maximise the EMF induced in a coil",
     """1. Move the magnet **faster**
2. Use a **stronger** magnet
3. **More turns** in the coil
4. **Larger coil area**"""),
    ("basic", "Applications of Faraday's law relevant to security technology",
     "Electric motors, generators, transformers, **RFID tags** (passive tags powered by induction), **pulse-induction metal detectors**."),

    # ---------------- cloze / recall ----------------
    ("cloze", "The 7 SI base quantities: length ({{c1::metre, m}}), mass ({{c2::kilogram, kg}}), time ({{c3::second, s}}), electric current ({{c4::ampere, A}}), temperature ({{c5::kelvin, K}}), amount of substance ({{c6::mole, mol}}), luminous intensity ({{c7::candela, cd}})", ""),
    ("cloze", "SI prefixes: tera = {{c1::10¹²}}, giga = {{c2::10⁹}}, mega = {{c3::10⁶}}, kilo = {{c4::10³}}, milli = {{c5::10⁻³}}, micro = {{c6::10⁻⁶}}, nano = {{c7::10⁻⁹}}, pico = {{c8::10⁻¹²}}", "Learn at least 10⁻⁶ to 10⁶ for the class test."),
    ("cloze", "Scientific notation: 0.000098269 = {{c1::9.83 × 10⁻⁵}} (2 d.p.); 7,800,000,000 = {{c2::7.8 × 10⁹}}", "Step 1: a number between 1 and 10. Step 2: multiply by a power of 10."),
    ("cloze", "Speed of light in a vacuum c = {{c1::299,792,458}} m s⁻¹ ≈ {{c2::3 × 10⁸}} m s⁻¹", ""),
    ("cloze", "Wave equation: v = {{c1::f λ}}; for EM waves {{c2::c = f λ}}; period T = {{c3::1/f}}", ""),
    ("cloze", "Wave speed on a string: v = {{c1::√(F/µ)}}, where F = {{c2::tension (N)}} and µ = {{c3::linear mass density (kg m⁻¹)}}", "Higher tension or a lighter string gives a faster wave."),
    ("cloze", "Speed of sound: air at 0 °C = {{c1::331}} m/s, air at 20 °C = {{c2::343}} m/s, water = {{c3::1482}} m/s, steel = {{c4::5960}} m/s", "Lead 1960, glass 5640. Depends on temperature (compressibility) and density."),
    ("cloze", "Human audible range: {{c1::20 Hz}} to {{c2::20 kHz}}", ""),
    ("cloze", "Visible light wavelength: approximately {{c1::400}} to {{c2::700}} nm; {{c3::violet}} has the shortest wavelength, {{c4::red}} the longest", ""),
    ("cloze", "EM spectrum, high to low frequency: {{c1::gamma}} → {{c2::X-ray}} → {{c3::ultraviolet}} → visible → {{c4::infrared}} → {{c5::microwave}} → {{c6::radio}}", "Learn the order, approximate frequencies and wavelengths."),
    ("cloze", "Doppler shift (lecture formula): Δf = {{c1::(Δv / c) · f₀}}, where Δv = {{c2::relative velocity of receiver to source}} and f₀ = {{c3::emitted frequency}}", "Positive when approaching, negative when receding."),
    ("cloze", "Faraday's law: ε = {{c1::−ΔΦ / Δt}}, where Φ is {{c2::magnetic flux}} measured in {{c3::webers (Wb)}}", ""),
    ("cloze", "Angular frequency ω = {{c1::2πf}}", ""),
    ("cloze", "Fourier series of a square wave (amplitude h, period 2π): f(x) = {{c1::(4h/π)[sin x + sin 3x/3 + sin 5x/5 + …]}}; it contains only {{c2::odd sine}} harmonics", "Adding more terms (n = 20, 100) gives a closer approximation to the square wave."),
    ("cloze", "Newton in base units: 1 N = {{c1::kg m s⁻²}} (from F = ma); density unit = {{c2::kg m⁻³}}", ""),

    # ---------------- calculations ----------------
    ("calc", "A 440 Hz note travels in air at 20 °C (343 m/s). Find its wavelength (2 d.p.).",
     "λ = v/f = 343/440 = **0.78 m**"),
    ("calc", "Find the wavelength of (a) a 2.4 GHz WiFi signal and (b) a 25 GHz mm-wave scanner.",
     """- (a) λ = c/f = 3×10⁸ / 2.4×10⁹ = **0.125 m**
- (b) λ = 3×10⁸ / 25×10⁹ = **0.012 m = 12 mm** (hence 'millimetre waves')"""),
    ("calc", "A string has tension 100 N and linear mass density 0.01 kg/m. Find the wave speed.",
     "v = √(F/µ) = √(100/0.01) = √10000 = **100 m/s**"),
    ("calc", "A 1000 Hz siren approaches a pedestrian at 20 m/s (sound speed 343 m/s). Find Δf and the heard frequency.",
     """Δf = (Δv/c)·f₀ = (20/343) × 1000 = **58.3 Hz**
Heard ≈ **1058.3 Hz** (higher pitch); about 941.7 Hz when receding."""),
    ("calc", "A radar speed gun transmits at 24 GHz; a car approaches at 30 m/s. Find the Doppler shift (lecture formula).",
     """Δf = (30 / 3×10⁸) × 24×10⁹ = **2400 Hz**
(A real two-way radar shift would be 2vf₀/c = 4.8 kHz.)"""),
    ("calc", "The magnetic flux through a coil falls from 0.5 Wb to 0.1 Wb in 0.2 s. Find |EMF|.",
     "|ε| = ΔΦ/Δt = (0.5 − 0.1)/0.2 = **2 V**"),
    ("calc", "Using dimensional analysis, give the SI base units of (a) pressure (F/A) and (b) energy (F × d).",
     """- (a) Pa = kg m s⁻² / m² = **kg m⁻¹ s⁻²**
- (b) J = kg m s⁻² × m = **kg m² s⁻²**"""),
    ("calc", "Find the period of a 50 Hz wave.", "T = 1/f = 1/50 = **0.02 s (20 ms)**"),

    # ---------------- exam-style long form ----------------
    ("exam", "[6 marks] Compare mechanical and electromagnetic waves. In your answer explain the difference between longitudinal and transverse waves and give examples of each.",
     """**Marking points:**
- Mechanical waves need a **medium** with elasticity and inertia; EM waves need **no medium** (travel in a vacuum)
- EM waves travel at **c ≈ 3×10⁸ m/s** in a vacuum; mechanical wave speed depends on the medium (e.g. sound 343 m/s in air, 5960 m/s in steel)
- EM waves = oscillating **electric and magnetic fields at right angles**
- **Longitudinal:** vibrations parallel to propagation; compressions and rarefactions; e.g. **sound**
- **Transverse:** vibrations perpendicular to propagation; e.g. string, water, **all EM waves**
- Mechanical can be either type; EM are **only transverse**"""),
    ("exam", "[5 marks] Sketch/describe the electromagnetic spectrum. Order the bands, indicate how frequency and wavelength vary, and give a security technology that operates in each band.",
     """**Marking points:**
- Order (high f / short λ to low f / long λ): **gamma, X-ray, UV, visible, IR, microwave, radio**
- f and λ are inversely related: **c = fλ**
- Visible light is the reference point: **400–700 nm**
- Examples: gamma (radiological detection), X-ray (baggage/CT/backscatter scanners), IR (thermal imaging/night vision), microwave/mm-wave (body scanners, radar), radio (RFID, GPR, through-wall radar, communications)
- Bands can overlap (gamma/X-ray distinguished by source)"""),
    ("exam", "[4 marks] Explain the Doppler effect using the example of a police car siren, state the equation for the Doppler shift, and describe one security application.",
     """**Marking points:**
- Change in frequency when source and receiver move **relative to each other**
- Car approaching: waves compressed, **higher frequency/pitch**; receding: **lower**
- **Δf = (Δv/c)·f₀** (Δv = relative velocity, f₀ = emitted frequency); positive approaching, negative receding
- Application: **radar speed gun** measures vehicle speed from Δf; also through-wall radar detecting moving targets / micro-Doppler"""),
    ("exam", "[5 marks] State Faraday's law of electromagnetic induction, give its equation, and explain how it is exploited in a security technology of your choice.",
     """**Marking points:**
- Induced EMF in a closed circuit = **rate of change of magnetic flux**; **ε = −ΔΦ/Δt**, Φ in webers
- A magnet moving through a coil induces a voltage; current flows if the circuit is closed
- EMF increased by faster motion, stronger magnet, more turns, bigger area
- **Example (RFID):** the reader's changing EM field induces a current in the tag coil, charging a capacitor that powers the IC (no battery)
- **OR (metal detector):** a pulse in the coil creates a field; its collapse induces a reflected pulse; metal prolongs it beyond ~30 µs"""),
    ("exam", "[4 marks] Explain why real-world signals cannot be described by a single sine wave, and how the Fourier Series and Fourier Transform are used to analyse them.",
     """**Marking points:**
- Real signals (speech, WiFi) contain **many frequencies**
- **Fourier Series:** any **periodic** signal = weighted sum of sines and cosines (e.g. square wave = odd harmonics; more terms give a better approximation)
- **Fourier Transform:** for **non-periodic** signals; converts the **time domain to the frequency domain** (inverse FT goes back)
- |F(ω)|² = power at each frequency; e.g. a WiFi signal must conform to its **spectral mask**"""),
    ("exam", "[4 marks] Define amplitude, wavelength, frequency and time period, and derive the wave equation v = fλ.",
     """**Marking points:**
- Amplitude: max displacement from equilibrium (power)
- Wavelength: distance between adjacent identical points (m)
- Frequency: cycles per second (Hz); period T: time to advance one wavelength, **T = 1/f**
- Speed = distance/time = λ/T, so **v = fλ** (for EM waves **c = fλ**)"""),
]
