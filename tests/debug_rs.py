"""
Debug: Test R/S Funktion
"""

from ti57_calculator import TI57Calculator

def test_rs_button():
    calc = TI57Calculator()
    
    print("=== Debug: R/S Funktion ===\n")
    
    # 1. Zustand laden
    calc.load_state()
    print(f"1. Programm geladen: {len(calc.program)} Schritte")
    print(f"   Programming mode: {calc.programming_mode}")
    print(f"   Running program: {calc.running_program}\n")
    
    # 2. Zahl eingeben
    print("2. Eingabe: 20")
    calc.digit_pressed("2")
    calc.digit_pressed("0")
    print(f"   Display: {calc.display}")
    print(f"   Input buffer: {calc.input_buffer}")
    print(f"   Entering number: {calc.entering_number}\n")
    
    # 3. R/S drücken
    print("3. R/S drücken...")
    print(f"   Vor R/S - x_register: {calc.x_register}")
    print(f"   Vor R/S - display: {calc.display}")
    
    calc.run_stop()
    
    print(f"   Nach R/S - x_register: {calc.x_register}")
    print(f"   Nach R/S - display: {calc.display}")
    print(f"   Running program: {calc.running_program}")
    print(f"   Error flag: {calc.error_flag}\n")
    
    if calc.display == "68" or calc.display == "68.0":
        print("✓ Funktioniert!")
    else:
        print(f"✗ Fehler - Display zeigt '{calc.display}' statt 68")
        print("\nProgramm-Details:")
        for i, (name, func) in enumerate(calc.program):
            print(f"  {i}: {name}")

if __name__ == "__main__":
    test_rs_button()
