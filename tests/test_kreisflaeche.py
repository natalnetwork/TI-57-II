#!/usr/bin/env python3
"""Test Kreisflächenprogramm"""

from ti57_calculator import TI57Calculator

calc = TI57Calculator()

# Programm laden
calc.load_state("ti57_state.json")

print("=== Test Kreisfläche ===")
print(f"Geladenes Programm: {len(calc.program)} Schritte")
for i, (name, _) in enumerate(calc.program):
    print(f"  {i:02d}: {name}")

# Test 1: Radius = 10 → Fläche = 314.159...
print("\n--- Test 1: Radius = 10 ---")
calc.digit_pressed("1")
calc.digit_pressed("0")
print(f"Eingabe: {calc.display}")
calc.run_stop()
print(f"Ergebnis: {calc.display}")
print(f"Erwartet: ~314.159")

# Test 2: Radius = 5 → Fläche = 78.540
print("\n--- Test 2: Radius = 5 ---")
calc.clear_all()
calc.digit_pressed("5")
print(f"Eingabe: {calc.display}")
calc.run_stop()
print(f"Ergebnis: {calc.display}")
print(f"Erwartet: ~78.540")

# Test 3: Radius = 1 → Fläche = 3.14159
print("\n--- Test 3: Radius = 1 ---")
calc.clear_all()
calc.digit_pressed("1")
print(f"Eingabe: {calc.display}")
calc.run_stop()
print(f"Ergebnis: {calc.display}")
print(f"Erwartet: ~3.14159")
