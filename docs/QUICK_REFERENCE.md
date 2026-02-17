# TI-57 II Quick Reference

## Key Assignments (Complete)

### Row 1: Control
| Key | Function | 2nd Function | INV Function |
|-----|----------|--------------|--------------|
| 2nd   | Activate secondary function | - | - |
| INV   | Activate inverse function | - | - |
| R/S   | Run/Stop program | - | - |
| OFF   | Power off | - | - |
| ON/C  | Power on / Clear | - | - |

### Row 2: Programming
| Key | Function | 2nd Function | Description |
|-----|----------|--------------|-------------|
| RST   | Reset program counter | **x=t** | Test: Is x equal to t? |
| GTO   | Go To step | **x≥t** | Test: Is x greater/equal t? |
| LBL   | Set label | **SBR** | Call subroutine |
| BST   | Backstep (step back) | **Dsz** | Decrement and skip |
| SST   | Single Step | **Del** | Delete program step |

### Row 3: Logarithms & Basic Functions
| Key | Function | 2nd Function |
|-----|----------|--------------|
| log   | Logarithm (base 10) | **10ˣ** |
| lnx   | Natural logarithm | **eˣ** |
| 1/x   | Reciprocal | - |
| x²    | Square | - |
| √x    | Square root | - |

### Row 4: Trigonometry
| Key | Function | 2nd Function | INV Function |
|-----|----------|--------------|--------------|
| DRG   | Switch angle mode | **DRG>** Convert | - |
| sin   | Sine | **P↔R** Polar↔Rect| **sin⁻¹** |
| cos   | Cosine | **DMS** D.MS→DD | **cos⁻¹** |
| tan   | Tangent | **π** Pi constant | **tan⁻¹** |
| yˣ    | Power y to x | **x!** Factorial | - |

### Row 5: Registers & Formats
| Key | Function | 2nd Function |
|-----|----------|--------------|
| x↔t   | Exchange x and t registers | **C.t** Clear t-register |
| EE    | Scientific notation | **Fix** Fixed decimals |
| (     | Open parenthesis | **Intg** Integer part |
| )     | Close parenthesis | **Frac** Fractional part |
| ÷     | Division | **\|x\|** Absolute value |

### Row 6-9: Digits & Memory
| Key | Function | 2nd Function |
|-----|----------|--------------|
| STO   | Store (0-7) | **part** Partition |
| RCL   | Recall (0-7) | **CM** Clear Memory |
| EXC   | Exchange Memory | **CP** Clear Program |
| LRN   | Learn Mode | **Pause** Pause program |

## Angle Modes (DRG)

- **DEG** - Degrees (360° = full circle)
- **RAD** - Radians (2π = full circle)
- **GRAD** - Gradians (400 gon = full circle)

Press **DRG** to switch.

## Memory Registers

8 registers available: **0, 1, 2, 3, 4, 5, 6, 7**

- **STO n** - Store value in register n
- **RCL n** - Recall value from register n
- **EXC n** - Exchange display with register n
- **2nd RCL** (CM) - Clear all registers

## Programming

### Programming Mode
1. Press **LRN** → Programming mode active (PGM lights up)
2. Enter key sequence (max. 50 steps)
3. Press **LRN** again → Exit programming mode

### Execute Program
1. **RST** - Set counter to beginning
2. **R/S** - Start program
3. **R/S** - Stop program

### Program Navigation
- **SST** - Single step forward
- **BST** - Single step backward
- **GTO** - Jump to step
- **2nd EXC** (CP) - Delete entire program

### Conditional Jumps
- **2nd RST** (x=t) - Skip next step if x = t
- **2nd GTO** (x≥t) - Skip next step if x ≥ t
- **2nd BST** (Dsz) - Decrement x, skip if = 0

### Labels & Subroutines
- **LBL** - Define jump target
- **2nd LBL** (SBR) - Call subroutine
