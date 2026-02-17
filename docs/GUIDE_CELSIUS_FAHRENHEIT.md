# Celsius ↔ Fahrenheit Conversion - TI-57 II

## The Formula
**F = C × 9 ÷ 5 + 32**

Example: 20°C = 68°F

---

## ✅ Resolved Issues

### OFF Key
- Now works correctly
- Automatically saves state (program and memory)
- Cleanly exits the application

### PGM Indicator
- **Important**: Appears in the **status bar** below the display
- **NOT** in the main display!
- Lights up green when LRN mode is active
- Main display shows step number: `00`, `01`, `02`, ...

```
┌────────────────────────────┐
│        00                  │  ← Main Display (step number in LRN mode)
├────────────────────────────┤
│  2nd  INV  DEG  PGM       │  ← Status Bar (PGM appears here!)
└────────────────────────────┘
                    ↑
                    PGM lights up green when LRN is active
```

---

## 🎯 Recommended Method: Manual Calculation

**Manual calculation works perfectly** and is currently the best method:

### Step-by-Step:

1. **Enter Celsius value** (e.g., `2` `0`)
2. Press `×`
3. Press `9`
4. Press `÷`
5. Press `5`
6. Press `=` (intermediate result)
7. Press `+`
8. Press `3` `2`
9. Press `=` → **Result!**

### Examples:

| Celsius | Keys | Result |
|---------|------|--------|
| 20°C | `20` `×` `9` `÷` `5` `=` `+` `32` `=` | **68°F** ✓ |
| 0°C | `0` `×` `9` `÷` `5` `=` `+` `32` `=` | **32°F** ✓ |
| 100°C | `100` `×` `9` `÷` `5` `=` `+` `32` `=` | **212°F** ✓ |
| 37°C | `37` `×` `9` `÷` `5` `=` `+` `32` `=` | **98.6°F** ✓ |
| -40°C | `40` `+/-` `×` `9` `÷` `5` `=` `+` `32` `=` | **-40°F** ✓ |

---

## 🔄 Reverse Conversion: Fahrenheit → Celsius

**Formula: C = (F - 32) × 5 ÷ 9**

### Step-by-Step:

1. **Enter Fahrenheit value**
2. Press `−`
3. Press `3` `2`
4. Press `=`
5. Press `×`
6. Press `5`
7. Press `÷`
8. Press `9`
9. Press `=` → **Result in °C!**

### Example: 68°F → Celsius

```
68 − 32 = × 5 ÷ 9 = → 20°C
```

---

## 💡 Tips

### After each calculation:
- Press **ON/C** to clear display
- Enter new temperature
- Repeat formula

### On error:
- Press **ON/C**
- Start over

### Change sign:
- After entering digits press **+/−**
- Example: `40` `+/-` gives `-40`

---

## 📝 Common Temperatures

| Celsius | Fahrenheit | Meaning |
|---------|------------|---------|
| -40°C | -40°F | Same value! |
| -18°C | 0°F | Very cold |
| 0°C | 32°F | Freezing point of water |
| 10°C | 50°F | Cool |
| 20°C | 68°F | Room temperature |
| 25°C | 77°F | Pleasantly warm |
| 30°C | 86°F | Warm |
| 37°C | 98.6°F | Body temperature |
| 100°C | 212°F | Boiling point of water |

---

## ⚙️ For Advanced Users: Using Memory

You can store intermediate results in memory:

### Example with Memory 0:

```
20              (Enter Celsius)
STO 0           (Store in memory 0)
RCL 0           (Recall from memory 0)
× 9 ÷ 5 = + 32 =
```

### Multiple conversions in sequence:

```
20 STO 0        (Store 20°C)
RCL 0 × 9 ÷ 5 = + 32 =    → 68°F

25 STO 0        (Store 25°C)
RCL 0 × 9 ÷ 5 = + 32 =    → 77°F
```

---

## 🎓 Summary

**What works:**
- ✅ Manual calculation (recommended!)
- ✅ OFF key saves and exits
- ✅ PGM indicator in status bar
