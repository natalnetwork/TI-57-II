# TI-57 II Program Library

This collection contains classic programs for the TI-57 II.

---

## Program 1: Circle Area (Radius → Area)

**Formula:** Area = πr²

**Program Entry:**
```
LRN
x²             (r²)
×              (Prepare multiplication)
2nd tan (π)    (Pi as second operand)
=              (r² × π)
LRN
```

**Usage:**
```
Enter radius (e.g., 10)
R/S
Result: 314.159... (area)
```

**Examples:**
- r = 10 → Area = 314.159
- r = 5 → Area = 78.540
- r = 1 → Area = 3.142

**JSON for ti57_state.json:**
```json
{
  "program": [
    "square",
    "multiply",
    "pi",
    "equals"
  ]
}
```

---

## Program 2: Circle Circumference (Radius → Circumference)

**Formula:** Circumference = 2πr

**Program Entry:**
```
LRN
×              (Prepare multiplication)
2nd tan (π)    (r × π)
×              (Prepare multiplication)
2
=              ((r × π) × 2)
LRN
```

**Usage:**
```
Enter radius (e.g., 10)
R/S
Result: 62.832... (circumference)
```

**Examples:**
- r = 10 → Circumference = 62.832
- r = 5 → Circumference = 31.416
- r = 1 → Circumference = 6.283

**JSON for ti57_state.json:**
```json
{
  "program": [
    "multiply",
    "pi",
    "multiply",
    "digit_2",
    "equals"
  ]
}
```

---

## Program 3: Percentage Calculation

Calculates a% of b

**Program Entry:**
```
LRN
×              (a × b)
100
÷              (÷ 100)
=
LRN
```

**Usage:**
```
Enter percentage (e.g., 15)
R/S
Enter base value (e.g., 200)
=
Result: 30
```

**JSON:**
```json
{
  "program": [
    "multiply",
    "digit_1",
    "digit_0",
    "digit_0",
    "divide",
    "equals"
  ]
}
```

---

## Program 4: Hypotenuse (Pythagoras)

Calculates c from a² + b² = c²

**Program Entry:**
```
LRN
x²             (a²)
x↔t            (Exchange)
x²             (b²)
+              (a² + b²)
=
√x             (√(a² + b²))
LRN
```

**Usage:**
```
Enter side a
R/S
Enter side b
Result: Hypotenuse c
```

**JSON:**
```json
{
  "program": [
    "square",
    "exchange_t",
    "square",
    "add",
    "equals",
    "sqrt"
  ]
}
```

---

## Program 5: Average of N Numbers

**Program Entry:**
```
LRN
2nd RCL (CM)   (Clear memory)
0
STO 0          (Counter = 0)
STO 1          (Sum = 0)
LBL 0          (Loop for input)
R/S            (Wait for number)
STO 2          (Temporary storage)
RCL 1          (Sum)
RCL 2          (Number)
+              (Add)
STO 1          (New sum)
RCL 0          (Counter)
1
+              (Counter + 1)
STO 0          (New counter)
GTO 0          (Next number)
LRN
```

**Calculate Average (after input):**
```
RCL 1          (Sum)
RCL 0          (Count)
÷
=
```

---
