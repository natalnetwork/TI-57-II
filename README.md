# TI-57 II Calculator Emulator

<!-- google-site-verification: pxW23T4prUTu_86vqpjeIFWKA-bIu0x2LKNUMAlEhe8 -->

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform: Windows | macOS | Linux](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://python.org)
[![Status: Active](https://img.shields.io/badge/Status-Active-success.svg)](https://github.com)

A complete emulation of the Texas Instruments TI-57 II programmable scientific calculator.

![TI-57 II Calculator GUI](docs/images/calculator_gui.png)

## Features

- **Scientific Functions**: Trigonometry (sin, cos, tan), Logarithms (log, ln), Exponential functions
- **Programmable**: 50 program steps
- **8 Memory Registers**: For storing and retrieving values
- **Statistical Functions**: Sums, averages, standard deviations
- **DRG Modes**: Degrees, Radians, Gradians
- **Polar/Rectangular Conversion**
- **Original Layout**: Authentic key distribution and display

## Installation

```bash
pip install -r requirements.txt
python ti57_gui.py
```

## Usage

The emulator works exactly like the original TI-57 II:
- **ON/C**: Power on and Clear
- **2nd**: Access secondary functions
- **INV**: Inverse functions
- **STO/RCL**: Store/Recall memory values
- **R/S**: Run/Stop for programs

## Keyboard Layout

The layout matches 1:1 with the original TI-57 II with all keys and labels.

## Project Structure

```
TI-57 II/
├── ti57_calculator.py      # Core - All mathematical functions
├── ti57_gui.py             # GUI - User interface with tkinter
├── ti57_state.json         # Saved state (program, registers, etc.)
├── requirements.txt        # Python dependencies
│
├── docs/                   # Documentation
│   ├── USER_MANUAL.md              # Complete user manual
│   ├── QUICK_REFERENCE.md          # Quick reference guide
│   ├── PROGRAM_LIBRARY.md          # Example programs
│   └── GUIDE_CELSIUS_FAHRENHEIT.md
│
├── tests/                  # Tests and examples
│   ├── test_programming.py
│   ├── test_circle_area.py
│   ├── examples.py
│   └── ... (additional tests)
│
└── programs/               # Prebuilt programs to load
    ├── circle_area.json
    ├── circle_circumference.json
    ├── pyramid_volume.json
    ├── pythagorean_theorem.json
    ├── percentage_calculation.json
    ├── compound_interest.json
    ├── fahrenheit_to_celsius.json
    ├── celsius_to_fahrenheit.json
    ├── km_to_miles.json
    ├── miles_to_km.json
    ├── bmi_calculator.json
    └── standard_deviation.json
```

## 📚 Program Library

The calculator includes **12 prebuilt programs** that are easy to load:

### Quick Start - Loading Programs

1. **Via GUI** (recommended):
   - Start the calculator: `python ti57_gui.py`
   - Right-click on the LCD display
   - Select "📂 Load Program..."
   - Choose a program from the `programs/` folder

2. **Show available programs**:
   - Right-click on the display
   - Select "ℹ️ Show Programs..."

### 📋 Program Library Overview

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

See [programs/README.md](programs/README.md) for **detailed instructions** on each program with examples!

## Documentation

The calculator works exactly like the original TI-57 II. Learn more here:

- **[docs/USER_MANUAL.md](docs/USER_MANUAL.md)** - Complete user manual
- **[docs/QUICK_REFERENCE.md](docs/QUICK_REFERENCE.md)** - All functions at a glance
- **[docs/PROGRAM_LIBRARY.md](docs/PROGRAM_LIBRARY.md)** - Classic programs for practice
- **[programs/README.md](programs/README.md)** - Instructions for all 12 programs
- **[Online Manual](https://manualmachine.com/texasinstruments/ti57ii/)** - Original Texas Instruments manual

## Disclaimer

TI-57 II is a trademark of Texas Instruments Incorporated.

This project is an independent hobby project and **not approved, endorsed, or otherwise affiliated with Texas Instruments**.

This is an unofficial emulator created for educational purposes and as a nostalgic project.

## License

MIT License - See [LICENSE](LICENSE) file
