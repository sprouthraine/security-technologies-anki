# Lecture 1 – Practice Exercises & Solutions: Waves and Fields

> No Lecture 1 problem sheet was in the slide folder (the slides refer to "Problem Sheet 1"). These exercises follow the style and mark scheme of the other course problem sheets and cover every Lecture 1 learning outcome.

---

## Section A – Scientific Notation, SI Units & Prefixes

### Q1. Write the following in scientific notation. [3]
(a) 0.00045  (b) 63,000,000  (c) 0.000098269 (to 2 d.p.)

**Solution**
- (a) 4.5 × 10⁻⁴
- (b) 6.3 × 10⁷
- (c) 9.83 × 10⁻⁵

### Q2. Express using SI prefixes or powers of 10. [3]
(a) 2.4 GHz in Hz  (b) 35 µg in g  (c) 0.000 005 m using a prefix

**Solution**
- (a) 2.4 × 10⁹ Hz
- (b) 3.5 × 10⁻⁵ g
- (c) 5 µm (5 × 10⁻⁶ m)

### Q3. Name the 7 SI base quantities and their units. [3]
**Solution:** length (metre, m); mass (kilogram, kg); time (second, s); electric current (ampere, A); temperature (kelvin, K); amount of substance (mole, mol); luminous intensity (candela, cd).

### Q4. Dimensional analysis. [4]
(a) Show that the newton (N) is m·kg·s⁻².
(b) Pressure = force / area. Express the pascal in SI base units.
(c) Energy = force × distance. Express the joule in SI base units.

**Solution**
- (a) F = ma, so N = kg × m s⁻² = **m·kg·s⁻²**
- (b) Pa = N / m² = kg m s⁻² / m² = **kg m⁻¹ s⁻²**
- (c) J = N × m = **kg m² s⁻²**

---

## Section B – Wave Properties

### Q5. Define amplitude, wavelength, frequency and time period, with units. [4]
**Solution**
- **Amplitude:** maximum disturbance from equilibrium. It represents the wave's power. Units depend on what is measured (dB, V…).
- **Wavelength (λ):** distance over which the wave shape repeats, e.g. crest to crest (m).
- **Frequency (f):** number of wave cycles per second (Hz).
- **Period (T):** time for the wave to advance one wavelength, T = 1/f (s).

### Q6. A wave has frequency 50 Hz. What is its period? [1]
**Solution:** T = 1/f = 1/50 = **0.02 s (20 ms)**

### Q7. A 440 Hz note travels through air at 20 °C (v = 343 m s⁻¹). Calculate its wavelength to 2 d.p. [2]
**Solution:** λ = v/f = 343/440 = **0.78 m**

### Q8. Calculate the wavelength of (a) a 2.4 GHz WiFi signal and (b) a 25 GHz mm-wave scanner signal. [2]
**Solution**
- (a) λ = c/f = 3 × 10⁸ / 2.4 × 10⁹ = **0.125 m (12.5 cm)**
- (b) λ = 3 × 10⁸ / 25 × 10⁹ = **0.012 m (12 mm)**, which is why they are called "millimetre waves"

### Q9. A string is under a tension of 100 N and has a linear mass density of 0.01 kg m⁻¹. Find the wave speed. [2]
**Solution:** v = √(F/µ) = √(100/0.01) = √10,000 = **100 m s⁻¹**

### Q10. Compare mechanical and electromagnetic waves, and longitudinal and transverse waves. [4]
**Solution**
- **Mechanical waves** need a medium with elasticity and inertia, and can be longitudinal or transverse (sound, water, strings).
- **EM waves** need no medium, travel at c in a vacuum, and are **transverse only**. They consist of perpendicular E and B field oscillations.
- **Longitudinal:** vibration is parallel to propagation, with compressions and rarefactions (sound).
- **Transverse:** vibration is perpendicular to propagation (light, waves on a string).

### Q11. "What sound does a massive explosion make in space?" Explain. [2]
**Solution:** **None.** Sound is a mechanical (longitudinal pressure) wave that needs a medium. Space is a vacuum, so there is no medium to carry the compressions and rarefactions.

### Q12. What is the human audible range? Name the waves above and below it and give one use of each. [3]
**Solution**
- Audible range: **20 Hz – 20 kHz**.
- **Ultrasound** (above 20 kHz): medical imaging, non-destructive testing, bat sonar.
- **Infrasound** (below 20 Hz): elephant and whale communication, volcanic eruption detection.

---

## Section C – The Electromagnetic Spectrum

### Q13. List the EM spectrum bands from highest to lowest frequency, and give one security technology for each. [5]
**Solution**
| Band | Technology |
|---|---|
| Gamma | Radiological threat detection, sterilising food |
| X-ray | Baggage/cargo scanners, backscatter body scanners |
| Ultraviolet | (e.g. forensic / banknote checks) |
| Visible | CCTV, dazzlers |
| Infrared | Thermal imaging, night vision |
| Microwave | mm-wave body scanners, radar |
| Radio | RFID, radar, GPR, communications |

### Q14. What is the wavelength range of visible light? How are gamma rays and X-rays of the same wavelength (e.g. 0.1 nm) distinguished? [2]
**Solution:** Visible light is about **400–700 nm**. Gamma and X-rays are distinguished by **source**: gamma rays come from nuclear radioactivity, X-rays from electrons.

---

## Section D – Interference & Doppler Effect

### Q15. Explain constructive and destructive interference. What condition must two waves meet to interfere? [3]
**Solution**
- **Constructive:** waves are in phase and reinforce, giving a larger amplitude.
- **Destructive:** waves are in antiphase and cancel.
- Condition: they must have the **same or similar frequency**.

### Q16. A police car siren emits 1000 Hz and approaches a stationary pedestrian at 20 m s⁻¹ (speed of sound 343 m s⁻¹). Using Δf = (Δv/c) f₀, find the Doppler shift and the frequency heard. What happens as the car moves away? [4]
**Solution**
- Δf = (20/343) × 1000 = **58.3 Hz**
- Heard frequency ≈ 1000 + 58.3 = **1058.3 Hz** (higher pitch)
- Moving away, Δf is negative: about 941.7 Hz (lower pitch).

### Q17. A radar speed gun transmits at 24 GHz. A car moves towards it at 30 m s⁻¹. Using the lecture formula, calculate the Doppler shift. [2]
**Solution:** Δf = (Δv/c) f₀ = (30 / 3 × 10⁸) × 24 × 10⁹ = **2400 Hz (2.4 kHz)**
*(Note: a real monostatic radar sees a two-way shift of 2vf₀/c = 4.8 kHz. Use the lecture formula unless told otherwise.)*

---

## Section E – Fourier Analysis

### Q18. What is the difference between a Fourier Series and a Fourier Transform? [2]
**Solution**
- **Fourier Series:** represents a **periodic** function as an infinite sum of sines and cosines.
- **Fourier Transform:** generalises this to **non-periodic** functions. It decomposes a time-domain signal into its frequency-domain components (spectral decomposition).

### Q19. Write the first four terms of the Fourier series of a square wave of amplitude h and period 2π. What happens as more terms are added? [3]
**Solution:** f(x) = (4h/π)[sin x + (sin 3x)/3 + (sin 5x)/5 + (sin 7x)/7 + …]. Only odd harmonics appear and the cosine terms vanish. As more terms are added (n = 20, n = 100) the sum approaches a true square wave.

### Q20. Give a security-relevant example of using the Fourier Transform. [1]
**Solution:** Transforming a WiFi signal from the time domain into the frequency domain to check that it conforms to the **WiFi spectral mask**. Another example is radar micro-Doppler analysis.

---

## Section F – Electricity & Magnetism

### Q21. State the right-hand grip rule. [2]
**Solution:** Wrap the right hand around the wire with the **thumb pointing in the direction of current**. The **curled fingers** show the direction of the magnetic field.

### Q22. Give three ways to increase the strength of an electromagnet. [3]
**Solution:** (a) insert an iron core; (b) add more turns to the coil; (c) increase the current.

### Q23. State Faraday's law. The flux through a coil drops from 0.5 Wb to 0.1 Wb in 0.2 s. Find the magnitude of the induced EMF. [3]
**Solution**
- The induced EMF in a closed circuit equals the rate of change of magnetic flux: ε = −ΔΦ/Δt.
- |ε| = (0.5 − 0.1) / 0.2 = **2 V**

### Q24. Give four ways to maximise the induced EMF, and three applications of Faraday's law. [4]
**Solution**
- **Ways:** move the magnet faster; use a stronger magnet; increase the number of turns; increase the coil area.
- **Applications:** electric motors, generators, transformers, **RFID tags**, **pulse-induction metal detectors**.
