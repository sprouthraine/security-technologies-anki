# Lecture 1 – Scientific, Mathematical & Engineering Fundamentals: Waves and Fields

*Source: Lecture 1 Pt1 (Introductory Material), Pt2 (Electromagnetic Waves & Fields), Lecture 1 Notes (Dr Kevin Chetty)*

## Learning Outcomes
- Convert large/small values into scientific notation and use SI prefixes
- Name the 7 SI base quantities
- Perform dimensional analysis on units
- Describe wave parameters: amplitude, frequency, velocity
- Sketch the EM spectrum and explain each band
- Explain the Doppler effect and interference
- Use Fourier Series / Fourier Transform to describe real-world signals
- Relate electricity and magnetism via Faraday's law of electromagnetic induction

---

## 1. Context
- Security Technologies is a branch of **Crime Science**: highly multidisciplinary.
- Besides the technical principles, the module looks at context: real-world deployment, public acceptance, legal standing in courts, cost and safety.

---

## 2. Scientific Notation
- Used for very small numbers (e.g. sub-atomic masses) and very large ones (e.g. speeds of billions of m/s).
- **Method:** (1) write a number between 1 and 10; (2) multiply by a power of 10.

| Number | Scientific notation |
|---|---|
| 2350 | 2.35 × 10³ |
| 7,800,000,000 | 7.8 × 10⁹ |
| 1,000,001 | 1.000001 × 10⁶ |
| 0.065 | 6.5 × 10⁻² |
| 0.000098269 | 9.83 × 10⁻⁵ (2 d.p.) |

---

## 3. The International System of Units (SI)
- *Système international d'unités*: the most widely used system of measurement.
- Built on **7 base quantities**, which are assumed to be independent:

| Base quantity | SI unit | Symbol |
|---|---|---|
| Length | metre | m |
| Mass | kilogram | kg |
| Time | second | s |
| Electric current | ampere | A |
| Temperature | kelvin | K |
| Amount of substance | mole | mol |
| Luminous intensity | candela | cd |

- All other units are combinations of these: area (m²), velocity (m s⁻¹), acceleration (m s⁻²), density (kg m⁻³).

### 3.1 Dimensional Analysis
- Identifies the base units of a physical quantity. This allows real-world interpretation and comparison between measures.
- **Example 1:** density ρ = m / V → kg / m³ = **kg m⁻³**
- **Example 2:** force F = m·a → kg × m s⁻² → **N = m·kg·s⁻²**

### 3.2 SI Prefixes (learn at least 10⁻⁶ to 10⁶ for the class test)

| Prefix | Symbol | Power | Everyday example |
|---|---|---|---|
| peta | P | 10¹⁵ | |
| tera | T | 10¹² | THz airport security scanner |
| giga | G | 10⁹ | 8 GB memory stick |
| mega | M | 10⁶ | 800 MHz quad-core processor |
| kilo | k | 10³ | 42 km marathon |
| milli | m | 10⁻³ | 5 ml teaspoon |
| micro | µ | 10⁻⁶ | 100 µg of paracetamol |
| nano | n | 10⁻⁹ | 8 nm gold particle |
| pico | p | 10⁻¹² | |
| femto | f | 10⁻¹⁵ | |

---

## 4. Waves

### 4.1 What is a wave?
- A **time-varying quantity that is also a function of position**.
- A vehicle that **transports energy without transporting matter**. Analogy: a Mexican wave in a stadium.

### 4.2 Classification
| | Mechanical waves | Electromagnetic waves |
|---|---|---|
| Medium | **Requires** a medium | **No** medium needed (can travel in a vacuum) |
| Types | Longitudinal **or** transverse | **Transverse only** |
| Examples | Sound, water waves, guitar string, seismic waves | Light, microwaves, X-rays, radio waves |

### 4.3 Mechanical Waves
- The medium must have **elasticity** (ability to return to its original shape after being deformed) and **inertia** (resistance to a change in velocity).
- Produced by an initial input of energy (a disturbance), e.g. a stone thrown into a pond or a flick of a string.
  - A single input gives a **wave pulse**.
  - A continuous disturbance gives a **periodic (sinusoidal) wave**.
- **Wave speed** (speed of energy propagation) ≠ **particle velocity** (how fast particles of the medium vibrate).
- **Wave speed on a string:** v = √(F/µ). F is tension (N) and µ is linear mass density (kg m⁻¹).
  - Higher tension gives a faster wave; a lighter string gives a faster wave.

### 4.4 Longitudinal vs Transverse
- **Longitudinal:** vibrations are **parallel** to the direction of propagation. They create **compressions** and **rarefactions**.
  - Sound is a longitudinal **pressure wave** from vibrating sources (loudspeaker, larynx).
  - Trick question: an explosion in space makes **no sound**, because there is no medium.
- **Transverse:** vibrations are **at right angles** to the direction of energy travel. Particles move up and down about their equilibrium position.
- Demonstrated with a slinky spring.

### 4.5 Speed of Sound in Different Media
| Medium | Speed (m s⁻¹) |
|---|---|
| Air at 0 °C | 331 |
| Air at 20 °C | 343 |
| Water at 20 °C | 1482 |
| Lead | 1960 |
| Glass | 5640 |
| Steel | 5960 |
- Speed depends on the medium's temperature (compressibility) and density.

### 4.6 Human Audible Range (Acoustic Spectrum)
- **20 Hz – 20 kHz**. Sensitivity at the high end decreases with age.
- **Ultrasound** (> 20 kHz): medical imaging, non-destructive testing (e.g. pipeline fractures), bat sonar.
- **Infrasound** (< 20 Hz): communication by elephants, giraffes and whales; detection of volcanic eruptions.

---

## 5. Properties of Waves
- **Amplitude (A):** the maximum disturbance from the equilibrium position. It represents the wave's power (loudness for sound). Units depend on what is measured: dB (sound), V (electrical), lumens (light).
- **Wavelength (λ):** the distance over which the wave shape repeats, e.g. crest to crest. Unit: m.
- **Frequency (f):** the number of wave cycles per second. Unit: Hz. For sound it relates to pitch.
- **Time period (T = 1/f):** the time for the wave to advance one wavelength.
- **Wave equation:** v = λ / T = **f λ**. For EM waves: **c = f λ**.

### 5.1 Electromagnetic Waves
- Need no medium. Always transverse.
- Made of **electric and magnetic field oscillations at right angles** to each other.
- Speed in a vacuum: **c = 299,792,458 m s⁻¹ ≈ 3 × 10⁸ m s⁻¹** (a universal constant).

---

## 6. The Electromagnetic Spectrum
- From high frequency / short λ to low frequency / long λ:
  **Gamma → X-rays → Ultraviolet → Visible → Infrared → Microwaves → Radio waves**
- **Visible light** (the reference point): λ ≈ **400–700 nm**. Violet has the shortest λ and red the longest.
- Bands are not always well-defined and can overlap. Example: λ = 0.1 nm can be gamma or X-ray. They are distinguished by **source**: gamma rays come from nuclear radioactivity, X-rays from electrons.
- *Learn the order, plus approximate frequencies and wavelengths of each band.*

### 6.1 Applications / Security Technologies by Band
| Band | Property / application |
|---|---|
| Gamma | Absorbed by cells, so used to kill bacteria in food; radiological threat detection |
| X-ray | Penetrates skin/tissue but not bone: medical imaging, baggage/cargo screening, backscatter body scanners |
| Infrared | Body heat: thermal imaging, night vision |
| Microwave | Similar frequency to water molecules (microwave ovens); mm-wave body scanners, radar |
| Radio | Communications (cellular, WiFi, satellite), radar, air traffic control, GPS, RFID, driverless cars |

---

## 7. Wave Phenomena

### 7.1 Interference
- Two waves **superimpose** to give a resultant wave of higher or lower amplitude.
- **Constructive:** waves are in phase and reinforce, giving a larger amplitude.
- **Destructive:** waves are in **antiphase** and cancel out.
- To interfere, waves must have the **same or similar frequency**. A radio wave and an X-ray will not interfere.

### 7.2 The Doppler Effect
- A change in frequency/wavelength (a **Doppler shift**) when source and receiver move **relative to each other**.
- **Police siren example:** as the car approaches, the frequency rises (higher pitch). As it recedes, the frequency falls (lower pitch).
- **Formula:** Δf = (Δv / c) · f₀
  - Δv = velocity of the receiver relative to the source, f₀ = emitted frequency, c = wave speed
  - The shift is **positive** when moving towards and **negative** when moving away.
- **Application:** radar speed guns for detecting speeding motorists.

---

## 8. Real-World Signals: Fourier Analysis
- Real waves are not single-frequency sinusoids. They are made of many frequencies, e.g. speech, or WiFi signals carrying video and web data.

### 8.1 Fourier Series (periodic functions)
- Any periodic function can be written as a sum of sines and cosines (an infinite series, named after Joseph Fourier):
  f(x) = a₀/2 + Σₙ₌₁^∞ [aₙ cos(nπx/L) + bₙ sin(nπx/L)]
  - a₀, aₙ, bₙ are weighting coefficients and **L = half the period**.
  - Calculating the coefficients is **out of scope**.
- **Square wave example** (period 2π so L = π; amplitude h): all cosine terms drop out.
  f(x) = (4h/π) Σ sin((2n−1)x)/(2n−1) = (4h/π)[sin x + sin 3x/3 + sin 5x/5 + sin 7x/7 + …]
  - Adding more terms (n = 20, n = 100) gives a better approximation of the square wave.

### 8.2 Fourier Transform (non-periodic functions)
- Generalises the Fourier Series to non-periodic functions.
- Decomposes a **time-domain** signal into its **frequency-domain** components (spectral decomposition):
  F(ω) = ∫₋∞^∞ f(t) e^(−iωt) dt, where **ω = 2πf** (angular frequency)
- The **inverse Fourier Transform** goes from the frequency domain back to the time domain.
- |F(ω)|² = the power of the signal at a given frequency.
- Example: the FT of a WiFi signal shows its spectrum conforming to the **WiFi spectral mask**.

---

## 9. Electricity and Magnetism
- Electricity and magnetism are inextricably linked, as EM waves show.
- **James Clerk Maxwell** (1865) showed they are manifestations of the same phenomenon. **Maxwell's equations** are the "second great unification of physics" (after Newton).
- **Current-carrying wires produce a magnetic field.**
- **Right-hand grip rule:** the thumb points along the current and the curled fingers give the direction of the magnetic field.
- **Electromagnets:** coiling the wire increases field strength. It can be increased further with (a) an iron core, (b) more turns, (c) more current. The field exists only while current flows (unlike permanent magnets).

### 9.1 Faraday's Law of Electromagnetic Induction
- **Michael Faraday** (appears on the £20 note).
- Moving a magnet through a coil **induces a voltage**, the **electromotive force (EMF)**. If the circuit is closed, a current flows.
- **Law:** the induced EMF in a closed circuit equals the rate of change of magnetic flux:
  **ε = −ΔΦ / Δt**
  - ε = EMF (V), Φ = magnetic flux in **weber (Wb)** (amount of magnetic field per unit area), Δt = change in time
- **To maximise EMF:** (a) move the magnet faster, (b) use a stronger magnet, (c) add more turns, (d) increase coil area.
- In large-scale generation, the magnet is stationary and the coil spins.
- **Applications:** electric motors, transformers, generators, **RFID tags** (Lecture 7), **metal detectors / pulse induction** (Lecture 4).

---

## Relevant Tools & Technologies
| Tool / technology | Link to concept |
|---|---|
| Radar speed gun | Doppler effect |
| Thermal imaging / night vision | Infrared band |
| X-ray baggage scanners, backscatter scanners | X-ray band |
| mm-wave body scanners | Microwave / EHF band |
| WiFi, cellular, GPS, RFID | Radio band, Fourier analysis (spectral masks) |
| Ultrasound imaging / NDT | Ultrasonic acoustic waves |
| Infrasound receivers | Volcanic eruption detection |
| Generators, transformers, RFID, metal detectors | Faraday's law of induction |
| Slinky spring | Demonstrates longitudinal/transverse waves |
