"""
Test der Programmier-Funktion für Celsius → Fahrenheit
"""

from ti57_calculator import TI57Calculator

def test_programming():
    calc = TI57Calculator()
    
    print("=== Test: Celsius → Fahrenheit Programmierung ===\n")
    
    # 1. Programmiermodus
    print("1. LRN drücken")
    calc.learn_mode()
    print(f"   Programming mode: {calc.programming_mode}")
    print(f"   Display: {calc.display}\n")
    
    # 2. Programm eingeben: × 9 ÷ 5 + 32 =
    print("2. Programm eingeben: × 9 ÷ 5 + 32 =")
    
    steps = [
        ("×", calc.multiply),
        ("9", lambda: calc.digit_pressed("9")),
        ("÷", calc.divide),
        ("5", lambda: calc.digit_pressed("5")),
        ("=", calc.equals),
        ("+", calc.add),
        ("3", lambda: calc.digit_pressed("3")),
        ("2", lambda: calc.digit_pressed("2")),
        ("=", calc.equals),
    ]
    
    for name, func in steps:
        calc.record_operation(name, func)
        print(f"   Schritt {len(calc.program)}: {name}")
    
    print(f"\n   Programmschritte: {len(calc.program)}\n")
    
    # 3. Programmiermodus beenden
    print("3. LRN beenden")
    calc.learn_mode()
    print(f"   Programming mode: {calc.programming_mode}\n")
    
    # 4. Test mit 20°C
    print("4. Test: 20°C")
    calc.clear_entry()
    calc.digit_pressed("2")
    calc.digit_pressed("0")
    print(f"   Eingabe: {calc.display}")
    print("   R/S drücken...")
    calc.run_stop()
    print(f"   Ergebnis: {calc.display}")
    print(f"   Erwartet: 68\n")
    
    return calc.display == "68" or calc.display == "68.0"

if __name__ == "__main__":
    success = test_programming()
    if success:
        print("✓ Test erfolgreich!")
    else:
        print("✗ Test fehlgeschlagen - Programmierung muss repariert werden")
