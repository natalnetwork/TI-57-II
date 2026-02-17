# 📚 Program Library - Prebuilt Programs to Load

This folder contains **12 ready-made programs** as JSON files that you can load directly into the TI-57 II Emulator.

## How to Load a Program (New Method ✨)

**Most convenient via the GUI:**

1. Start the calculator: `python ti57_gui.py`
2. Right-click on the LCD display
3. Select "📂 **Load Program...**"
4. Select a JSON program from this folder
5. The program is automatically loaded!

---

## 📋 Program Library - Overview

| # | Filename | Category | Description |
|---|----------|----------|-------------|
| 1 | `circle_area.json` | 📐 Geometry | Calculate circle area (πr²) |
| 2 | `circle_circumference.json` | 📐 Geometry | Calculate circle circumference (2πr) |
| 3 | `pyramid_volume.json` | 📐 Geometry | Calculate pyramid volume |
| 4 | `pythagorean_theorem.json` | 📐 Geometry | Hypotenuse using Pythagoras |
| 5 | `percentage_calculation.json` | 💰 Finance | Percentage calculation (a% of b) |
| 6 | `compound_interest.json` | 💰 Finance | Compound interest calculator |
| 7 | `fahrenheit_to_celsius.json` | 🌡️ Conversion | Temperature °F → °C |
| 8 | `celsius_to_fahrenheit.json` | 🌡️ Conversion | Temperature °C → °F |
| 9 | `km_to_miles.json` | 🌍 Distance | Kilometers → Miles |
| 10 | `miles_to_km.json` | 🌍 Distance | Miles → Kilometers |
| 11 | `bmi_calculator.json` | 💪 Health | Body Mass Index |
| 12 | `standard_deviation.json` | 📊 Statistics | RMS (Standard Deviation) |

---

## 📐 GEOMETRY

### 1. circle_area.json
**Function:** Calculate circle area from radius (πr²)

**Usage:**
```
Enter radius (e.g., 10)
R/S
Result: 314.159 (area)
```

**Examples:**
- r = 10 → 314.159
- r = 5 → 78.540
- r = 1 → 3.142

---

### 2. circle_circumference.json
**Function:** Calculate circle circumference from radius (2πr)

**Usage:**
```
Enter radius (e.g., 10)
R/S
Result: 62.832 (circumference)
```

**Examples:**
- r = 10 → 62.832 cm
- r = 5 → 31.416 cm
- r = 1 → 6.283 cm

---

### 3. percentage_calculation.json
**Function:** Calculate a% of b

**Usage:**
```
Enter percentage (e.g., 15)
R/S
Enter base value (e.g., 200)
=
Result: 30
```

**Examples:**
- 20% of 500 = 100
- 7.5% of 1000 = 75
- 100% of 42 = 42

---

### 4. fahrenheit_to_celsius.json
**Function:** Convert Fahrenheit → Celsius

**Usage:**
```
Enter temperature in °F (e.g., 98.6)
R/S
Result in °C: 37
```

**Examples:**
- 32°F = 0°C (freezing point)
- 98.6°F = 37°C (body temperature)
- 212°F = 100°C (boiling point)

---

### 5. celsius_to_fahrenheit.json
**Function:** Convert Celsius → Fahrenheit

**Usage:**
```
Enter temperature in °C (e.g., 25)
R/S
Result in °F: 77
```

**Examples:**
- 0°C = 32°F (freezing point)
- 37°C = 98.6°F (body temperature)
- 100°C = 212°F (boiling point)

---

### 6. km_to_miles.json
**Function:** Convert kilometers → miles (1 km = 0.621371 mi)

**Usage:**
```
Enter distance in km (e.g., 100)
R/S
Result in miles: 62.1371
```

**Examples:**
- 1 km = 0.621 mi
- 10 km = 6.214 mi
- 160 km = 99.419 mi

---

### 7. miles_to_km.json
**Function:** Convert miles → kilometers (1 mi = 1.60934 km)

**Usage:**
```
Enter distance in miles (e.g., 10)
R/S
Result in km: 16.0934
```

**Examples:**
- 1 mi = 1.609 km
- 5 mi = 8.047 km
- 26.2 mi = 42.195 km (marathon distance)

---

## 💪 HEALTH & SPORTS

### 8. bmi_calculator.json
**Function:** Calculate Body Mass Index: BMI = Weight(kg) / Height(m)²

**Usage:**
```
Enter weight in kg (e.g., 75)
R/S
Enter height in meters (e.g., 1.75)
R/S
Result: 24.49 (normal weight)
```

**Examples:**
- 70 kg / 1.75 m = 22.86 BMI
- 80 kg / 1.80 m = 24.69 BMI
- 100 kg / 1.70 m = 34.60 BMI

**BMI Categories:**
- < 18.5: Underweight
- 18.5–24.9: Normal weight ✓
- 25–29.9: Overweight
- ≥ 30: Obesity

---

## 📐 ADDITIONAL GEOMETRY

### 9. pyramid_volume.json
**Function:** Calculate pyramid volume: V = (Base Area × Height) / 3

**Usage:**
```
Enter base area (e.g., 100)
R/S
Enter height (e.g., 9)
R/S
Result: 300 (volume in units³)
```

**Examples:**
- Base area 100, height 10 → Volume 333.33
- Base area 144, height 15 → Volume 720
- Base area 50, height 12 → Volume 200

---

### 10. pythagorean_theorem.json
**Function:** Calculate hypotenuse: c = √(a² + b²)

**Usage:**
```
Enter side a (e.g., 3)
R/S
Enter side b (e.g., 4)
R/S
Result: 5 (hypotenuse)
```

**Examples:**
- a = 3, b = 4 → c = 5 (classic 3-4-5 triangle)
- a = 5, b = 12 → c = 13 (5-12-13 triangle)
- a = 6, b = 8 → c = 10

---

## 💰 FINANCE

### 11. compound_interest.json
**Function:** Compound interest calculator: A = P(1 + r)^n

**Usage:**
```
Enter capital (e.g., 1000)
R/S
Enter interest rate as factor (e.g., 1.05 for 5%)
yˣ
Enter number of periods (e.g., 10)
=
Result: 1628.89 (amount after 10 years)
```

**Examples:**
- 1000 € with 5% interest p.a. for 10 years
  - Factor: 1.05, years: 10 → 1628.89 €
- 5000 € with 3% interest p.a. for 20 years
  - Factor: 1.03, years: 20 → 8955.30 €

---

## 📊 STATISTICS

### 12. standard_deviation.json
**Function:** Calculate RMS (Root Mean Square) from 3 measurement values

**Usage:**
```
Enter measurement value 1 (e.g., 2)
R/S
Enter measurement value 2 (e.g., 3)
R/S
Enter measurement value 3 (e.g., 4)
R/S
Result: 3.11 (RMS of measurements)
```

**Examples:**
- Values: 2, 3, 4 → RMS ≈ 3.11
- Values: 1, 2, 3 → RMS ≈ 2.16
- Values: 5, 10, 15 → RMS ≈ 11.55

**Note:** RMS = √((x₁² + x₂² + x₃²) / 3) simplified for 3 measurement values

---

## 💾 Save Your Own Programs

If you have entered a program yourself:

1. Enter program in LRN mode
2. Press OFF (saves to ti57_state.json)
3. Copy and rename ti57_state.json:
   ```bash
   cp ti57_state.json programs/my_program.json
   ```
4. Load it again via the right-click menu!

---

## 🐛 Debug a Program

Use the SST key to step through the program one step at a time:
```
LRN → SST → SST → SST → ... 
```

Shows each program step like: `00 ×`, `01 9`, etc.
