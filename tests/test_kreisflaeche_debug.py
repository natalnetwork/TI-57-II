#!/usr/bin/env python3
"""Detaillierter Test Kreisflächenprogramm"""

from ti57_calculator import TI57Calculator

calc = TI57Calculator()

# Programm laden
calc.load_state("ti57_state.json")

print("=== Detaillierter Test: Radius = 10 ===")
calc.digit_pressed("1")
calc.digit_pressed("0")
print(f"Nach Eingabe '10': display='{calc.display}', input_buffer='{calc.input_buffer}', entering={calc.entering_number}")
print(f"  get_display_value() = {calc.get_display_value()}")

# Schritt für Schritt manuell durchführen
print("\n--- Manuelles Durchlaufen der Programmschritte ---")

# Schritt 0: square
print("\n[0] square():")
print(f"  VOR: display='{calc.display}', x_reg={calc.x_register}, pending_op={calc.pending_operation}, pending_val={calc.pending_value}")
calc.square()
print(f"  NACH: display='{calc.display}', x_reg={calc.x_register}")

# Schritt 1: pi
print("\n[1] pi():")
print(f"  VOR: display='{calc.display}', x_reg={calc.x_register}, pending_op={calc.pending_operation}, pending_val={calc.pending_value}")
calc.pi()
print(f"  NACH: display='{calc.display}', x_reg={calc.x_register}")

# Schritt 2: multiply
print("\n[2] multiply():")
print(f"  VOR: display='{calc.display}', x_reg={calc.x_register}, pending_op={calc.pending_operation}, pending_val={calc.pending_value}")
calc.multiply()
print(f"  NACH: display='{calc.display}', x_reg={calc.x_register}, pending_op={calc.pending_operation}, pending_val={calc.pending_value}")

# Schritt 3: equals
print("\n[3] equals():")
print(f"  VOR: display='{calc.display}', x_reg={calc.x_register}, pending_op={calc.pending_operation}, pending_val={calc.pending_value}")
calc.equals()
print(f"  NACH: display='{calc.display}', x_reg={calc.x_register}")

print(f"\n=== ENDERGEBNIS: {calc.display} ===")
print(f"=== ERWARTET: ~314.159 ===")
