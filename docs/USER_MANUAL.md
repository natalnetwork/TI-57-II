# TI-57 II User Manual

## Overview

The TI-57 II is a programmable scientific calculator with 8 memory registers and 50 program steps.

## Key Layout

### Top Row (Control)
- **2nd**: Activates secondary functions (orange text above keys)
- **INV**: Activates inverse functions
- **R/S**: Run/Stop - Starts/Stops programs
- **OFF**: Power off
- **ON/C**: Power on / Clear (clears entry)

### Basic Arithmetic
- **+**: Addition
- **−**: Subtraction
- **×**: Multiplication
- **÷**: Division

### Scientific Functions

#### Trigonometry
- **sin**, **cos**, **tan**: Trigonometric functions
- **sin⁻¹**, **cos⁻¹**, **tan⁻¹**: Inverse functions (with INV)

#### Logarithms and Exponents
- **log**: Logarithm base 10
- **10ˣ** (2nd log): 10 to the power of x
- **lnx**: Natural logarithm
- **eˣ** (2nd lnx): e to the power of x

#### Roots and Powers
- **x²**: Square
- **√x**: Square root
- **∛x**: Cube root
- **yˣ**: Power function (y to the power of x)
- **1/x**: Reciprocal

#### Additional Functions
- **n!**: Factorial
- **π**: Pi constant (3.14159...)

### Angle Modes
- **DRG**: Switches between Degrees (DEG), Radians (RAD), and Gradians (GRAD)

### Coordinate Conversion
- **P→R** (2nd x⇄t): Polar to Cartesian
- **R→P** (2nd DRG): Cartesian to Polar

### Angle Conversion
- **D.MS**: Converts Degrees.Minutes.Seconds to decimal degrees
- **DMS DD** (2nd D.MS): Converts decimal degrees to Degrees.Minutes.Seconds

### Memory Functions

The TI-57 II has 8 memory registers (0-7):

- **STO**: Stores current value. Enter digit 0-7 after pressing
- **RCL**: Recalls value. Enter digit 0-7 after pressing
- **EXC**: Exchanges display with memory. Enter digit 0-7 after pressing
- **CM**: Clear Memory - Clears all memory
- **Σ+** (2nd STO): Adds to memory

### Statistics

- **Σ+**: Adds data point (x-value in display, y-value in t-register)
- **Σ-** (INV Σ+): Removes data point
- **x̄**: Calculates mean
- **σ** (2nd x̄): Calculates standard deviation

### Registers
- **x⇄t**: Exchanges x and t registers

### Programming

The TI-57 II can store up to 50 program steps:

- **LRN** (2nd RST): Activates/deactivates learning mode
- **R/S**: Run/Stop - Starts/stops program execution
- **RST**: Reset - Sets program counter to 0
- **GTO** (2nd SBR): Goto - Jumps to program step
- **SST** (2nd 1/x): Single Step - Single step
- **INS** (2nd π): Insert - Inserts step
- **DEL** (2nd n!): Delete - Deletes step
- **SBR**: Subroutine
- **Dsz**: Decrement and skip if zero

## Usage Examples

### Example 1: Simple Calculation
```
Task: 25 + 17 = ?

Key sequence:
2 5 + 1 7 =
Result: 42
```

### Example 2: Scientific Function
```
Task: sin(30°) = ?

Key sequence:
- Make sure DRG is set to "DEG"
- 3 0 sin
Result: 0.5
```

### Example 3: Square Root
```
Task: √144 = ?

Key sequence:
1 4 4 √x
Result: 12
```

### Example 4: Using Memory
```
Task: Store 42 in register 0

Key sequence:
4 2 STO 0
(Value is now stored)

Recall later:
RCL 0
Result: 42
```

### Example 5: Factorial
```
Task: 5! = ?

Key sequence:
5 n!
Result: 120
```

### Example 6: Logarithm
```
Task: log(100) = ?

Key sequence:
1 0 0 log
Result: 2
```

### Example 7: Power
```
Task: 2³ = ?

Key sequence:
2 yˣ 3 =
Result: 8
```

### Example 8: Statistics
```
Task: Average of 2, 4, 6, 8, 10

Key sequence:
2 Σ+
4 Σ+
6 Σ+
8 Σ+
1 0 Σ+
x̄
Result: 6
```

### Example 9: Angle Conversion
```
Task: Convert 45°30'15" to decimal degrees

Key sequence:
4 5 . 3 0 1 5 D.MS
Result: 45.504167 (equals 45.504167°)
```

### Example 10: Polar/Cartesian
```
Task: Convert Cartesian coordinates (3, 4) to Polar

Key sequence:
3 [Enter as x]
4 x⇄t [4 into t-register]
2nd DRG [R→P]
Result: r = 5, θ in t-register
```

## Keyboard Shortcuts

When the GUI is running, you can also use the computer keyboard:

- **0-9**: Digits
- **.**: Decimal point
- **+**: Addition
- **-**: Subtraction
- ***: Multiplication
- **/**: Division
- **=** or **Enter**: Equals
- **Esc** or **Backspace**: Clear

## Status Indicators

The following indicators are displayed in the status line:

- **2nd**: Secondary function is active (orange)
- **INV**: Inverse function is active (orange)
- **DEG/RAD/GRAD**: Current angle mode (green)
- **PGM**: Programming mode is active (green)

## Error Messages

- **Error**: General error (e.g., invalid operation)
- **Div by 0**: Division by zero
- **Overflow**: Number too large

## Tips

1. **Chaining**: The calculator executes operations in the order they are entered (no operator precedence).

2. **Combining 2nd and INV**: You can use 2nd and INV together for extended functions.

3. **Using Memory**: Use the 8 memory registers for complex calculations.

4. **DRG Mode**: Be aware of the correct angle mode for trigonometric functions.

5. **Programs**: Use programming mode (LRN) for repeated calculations.

## Technical Specifications

- **Display**: 12-digit LCD
- **Memory**: 8 registers (0-7)
- **Program Steps**: 50
- **Angle Modes**: Degrees, Radians, Gradians
- **Accuracy**: Double precision (Float)
- **Functions**: 40+ mathematical and scientific functions

## Differences from Original

This emulator implements all major functions of the TI-57 II. Some advanced programming features (such as nested subroutines) are simplified.
