# Security Technologies – Formula Sheet

> All formulas and constants from Lectures 1, 2, 4, 5, 6 and 7. Lecture 5 (Ekblom, crime prevention & design) is conceptual and has no formulas.

---

## Physical Constants & Conversions
| Quantity | Symbol | Value |
|---|---|---|
| Speed of light (vacuum) | c | 299,792,458 m s⁻¹ ≈ **3 × 10⁸ m s⁻¹** |
| Planck's constant | h | **6.63 × 10⁻³⁴ J s** |
| Electron charge unit | e | **1.602 × 10⁻¹⁹ C** |
| Atomic mass unit | mᵤ | **1.661 × 10⁻²⁷ kg** |
| Electron mass | mₑ | 1/1836 mᵤ |
| Magnetic constant (permeability of free space) | µ₀ | **4π × 10⁻⁷ H m⁻¹** |
| Electron-volt | eV | **1 eV = 1.602 × 10⁻¹⁹ J**; **1 J = 6.242 × 10¹⁸ eV** |
| Curie | Ci | **1 Ci = 3.7 × 10¹⁰ Bq** |
| Becquerel | Bq | 1 Bq = 1 decay s⁻¹ (SI: s⁻¹) |
| Weber | Wb | kg m² s⁻² A⁻¹ (1 Wb s⁻¹ induces 1 V) |
| Henry | H | kg m² s⁻² A⁻² |
| Newton | N | kg m s⁻² |
| Blood : breath alcohol ratio | — | **2100 : 1** |

## SI Prefixes
| P | T | G | M | k | — | m | µ | n | p | f |
|---|---|---|---|---|---|---|---|---|---|---|
| 10¹⁵ | 10¹² | 10⁹ | 10⁶ | 10³ | 10⁰ | 10⁻³ | 10⁻⁶ | 10⁻⁹ | 10⁻¹² | 10⁻¹⁵ |

## SI Base Units
Length **m** · Mass **kg** · Time **s** · Current **A** · Temperature **K** · Amount **mol** · Luminous intensity **cd**

---

## Lecture 1 – Waves & Fields

| Formula | Description | Variables |
|---|---|---|
| **T = 1 / f** | Period–frequency relation | T (s), f (Hz) |
| **v = f λ** (= λ / T) | Wave speed | v (m s⁻¹), λ (m) |
| **c = f λ** | EM waves | c = 3 × 10⁸ m s⁻¹ |
| **v = √(F / µ)** | Wave speed on a string | F = tension (N), µ = linear mass density (kg m⁻¹) |
| **Δf = (Δv / c) · f₀** | Doppler shift | Δv = relative velocity (+ approaching, − receding), f₀ = emitted frequency, c = wave speed |
| **F = m a** | Newton's 2nd law (dimensional analysis: N = kg m s⁻²) | |
| **ρ = m / V** | Density (kg m⁻³) | |
| **f(x) = a₀/2 + Σ [aₙ cos(nπx/L) + bₙ sin(nπx/L)]** | Fourier series | L = half period; a₀, aₙ, bₙ = weighting coefficients |
| **f(x) = (4h/π) Σ sin((2n−1)x)/(2n−1)** | Square wave (period 2π, amplitude h) | Odd harmonics only: sin x + sin3x/3 + sin5x/5 + … |
| **F(ω) = ∫ f(t) e^(−iωt) dt** | Fourier transform (time to frequency domain) | |
| **ω = 2πf** | Angular frequency | ω (rad s⁻¹) |
| **ε = −ΔΦ / Δt** | Faraday's law of induction | ε = EMF (V), Φ = magnetic flux (Wb) |

---

## Lecture 2 – Structure of Matter & Nuclear Science

| Formula | Description |
|---|---|
| **ᴬ_Z X** | Nuclide notation: A = mass number (nucleons), Z = atomic number (protons) |
| **N = A − Z** | Number of neutrons |
| **A = Z + N** | Mass number |
| **Max electrons in shell n = 2n²** | n = 1: 2; n = 2: 8; n = 3: 18 |
| **Ion charge = (protons − electrons) × e** | Cation (+) lost e⁻; anion (−) gained e⁻ |
| **N = N₀ (½)^(t / t½)** | Radioactive decay (amount after time t) |
| **Number of half-lives = t / t½** | |
| **Activity: 1 Bq = 1 decay s⁻¹** | 1 Ci = 3.7 × 10¹⁰ Bq |

### Decay Rules
| Decay | Change in A | Change in Z | Change in N | Emitted |
|---|---|---|---|---|
| **α** | −4 | −2 | −2 | ⁴₂He |
| **β⁻** | 0 | +1 | −1 | ⁰₋₁e (n → p) |
| **β⁺** | 0 | −1 | +1 | ⁰₊₁e (p → n) |
| **γ** | 0 | 0 | 0 | EM photon |
- **Balance:** the sums of A and of Z must be equal on both sides.
  - ²³⁹₉₄Pu → ²³⁵₉₂U + ⁴₂He
  - ¹⁴₆C → ¹⁴₇N + ⁰₋₁e
- **Stability:** N ≈ Z for Z < 20; N > Z for Z > 20.

---

## Lecture 4 – Airports (X-ray & mm-wave)

| Formula | Description | Variables |
|---|---|---|
| **E = h f** | Planck's law (photon energy) | E (J), h = 6.63 × 10⁻³⁴ J s, f (Hz) |
| **E (eV) = E (J) / 1.602 × 10⁻¹⁹** | Joules to eV | divide by 10³ for keV |
| **E = h c / λ** | Photon energy from wavelength (combine with c = fλ) | |
| **I = I₀ e^(−µx)** | Beer–Lambert law (slides write µ as A) | I₀ = initial intensity (W m⁻²), µ = linear attenuation coeff. (m⁻¹), x = thickness (m) |
| **I / I₀ = e^(−µx)** | Fraction transmitted | |
| **x = −ln(I/I₀) / µ** | Thickness for a given fraction | |
| **x½ = ln 2 / µ** | Half-value thickness (intensity halves) | |
| **µ = µₘ × ρ** | Linear vs mass attenuation coefficient | ρ = density |

### Reference Values
| Item | Value |
|---|---|
| Soft X-rays | 10¹⁶ – 10¹⁸ Hz (10 nm – 100 pm) |
| Hard X-rays | 10¹⁸ – 10²⁰ Hz (100 pm – 1 pm) |
| X-ray photon energy | 100 eV – 100 keV |
| Ionising threshold | ≫ 10 eV |
| mm-wave scanner | 20 – 30 GHz, λ 15 – 10 mm, 1.2 × 10⁻⁴ – 1.2 × 10⁻³ eV |
| Thermal response threshold | 5 mW cm⁻² (> 0.5 °C rise) |
| L3 ProVision 2 power density | 6 × 10⁻⁶ mW cm⁻² |
| X-ray tube voltage | 10³ – 10⁶ V |
| µ (typical, at 50 keV) | vacuum 0, muscle 50, flesh 100, bone 330, lead 600 m⁻¹ |
| Metal detector reflected pulse | ~30 µs (metal makes it ≫ 30 µs); ~100 pulses s⁻¹ |
| Z_eff bands | organic 0–10 (orange), inorganic 10–19 (green), metal > 19 (blue) |
| Throughput | metal detector ~500/hr; mm-wave 200–300/hr; backscatter ~100/hr |

---

## Lecture 6 – Law Enforcement (Radar, Taser, Breathalyser)

### Radar
| Formula | Description | Variables |
|---|---|---|
| **R = c · t_total / 2** | Radar range | t_total = round-trip time (s) |
| **t_total = t_travel + t_return** | Round-trip time | |
| **ΔR = c / (2B)** | Range resolution | B = bandwidth (Hz); uncertainty = ± ΔR/2 |
| **ρ = (√ε₁ − √ε₂) / (√ε₁ + √ε₂)** | Reflectivity coefficient at an interface (ignore the sign) | εᵣ = relative permittivity (air = 1, soil = 9, bone = 4) |
| **λ = c / f** | Radar wavelength | |

- **Trade-off:** high f gives more bandwidth, better resolution, but more attenuation. Low f gives deeper penetration but poorer images.
- **GPR depths:** 1500 MHz → 0.5 m; 900 MHz → 1 m; 400 MHz → 4 m; 270 MHz → 6 m.

### Radio Sub-bands
ELF 3–30 Hz · SLF 30–300 Hz · ULF 300 Hz–3 kHz · VLF 3–30 kHz · LF 30–300 kHz · MF 300 kHz–3 MHz · HF 3–30 MHz · VHF 30–300 MHz · UHF 300 MHz–3 GHz · SHF 3–30 GHz · EHF 30–300 GHz

### Taser / Electric Shock
| Formula | Description |
|---|---|
| **V = I R**, **I = V / R** | Ohm's law (I in A, V in V, R in Ω) |
| **I = Q / t** | Current = rate of flow of charge (Q in C) |
| **I_taser = (charge per pulse × PRF) / 1 s** | Average Taser current |
| Taser: 100 µC × 19 pulses s⁻¹ = **1.9 mA** | ~1% of fibrillation current, so safe |
| Mains example: 240 V / 100 kΩ = 2.4 mA (safe); 240 V / 10 kΩ = 24 mA (lethal) | |
| **Tetanus region: > 70 contractions s⁻¹** (Taser PRF = 19) | |
| Taser: up to 50 kV arc; pulses 100 µs; darts ~55 m s⁻¹; range 7–11 m | |

### Breathalyser
| Formula | Description |
|---|---|
| **Breath alcohol = Blood alcohol / 2100** | Blood : breath ratio 2100 : 1 |
| **Blood alcohol = Breath alcohol × 2100** | |
| UK limits: **80 mg/100 ml blood ≡ 35 µg/100 ml breath ≡ 107 mg/100 ml urine** | |
| **Anode:** CH₃CH₂OH(g) + H₂O(l) → CH₃CO₂H(l) + 4H⁺(aq) + 4e⁻ | Ethanol oxidised to acetic acid |
| **Cathode:** O₂(g) + 4H⁺(aq) + 4e⁻ → 2H₂O(l) | Oxygen reduced to water |
| Current ∝ alcohol concentration | |
- Unit tip: 1 mg = 1000 µg, so X mg/100 ml blood gives (X × 1000 / 2100) µg/100 ml breath.

---

## Lecture 7 – RFID

| Formula | Description |
|---|---|
| **B_P = µ₀ I N a² / [2 (a² + r²)^(3/2)]** | On-axis magnetic field of a loop antenna (exact) |
| **B_P ≈ µ₀ I N a² / (2 r³)** | Approximation when a² ≪ r² (used in the course) |
| **N = 2 B r³ / (µ₀ I a²)** | Minimum turns for a required field (round **up**) |
| **I = 2 B r³ / (µ₀ N a²)** | Required current |
| **r = [µ₀ I N a² / (2B)]^(1/3)** | Maximum read range for a minimum field B |
| **B ∝ 1/r³** | Field decays rapidly, which limits read range |

| Variable | Unit |
|---|---|
| B_P | Wb m⁻² (tesla) |
| µ₀ | 4π × 10⁻⁷ H m⁻¹ |
| I | A |
| N | turns |
| a | loop radius (m) |
| r | distance from loop centre (m) |

### RFID Bands & Ranges
| Band | Frequency | Range |
|---|---|---|
| LF | 125 – 134 kHz | ~10 cm |
| HF | 13.56 MHz | < 3 m |
| UHF | 433 MHz; 865 – 960 MHz | up to 100 m |

---

## Quick Calculation Tips
- Always convert to **SI base units** first (cm → m, mA → A, µC → C, GHz → Hz).
- **ln and e:** if I/I₀ = e^(−µx), then x = −ln(I/I₀)/µ.
- **Radar:** remember the **÷2** for the round trip in both R and ΔR.
- **RFID:** cube the distance (r³) and square the radius (a²). Round the number of turns **up**.
- **Photon energy:** E = hf in J, then ÷ 1.602 × 10⁻¹⁹ for eV, then ÷ 1000 for keV.
