"""
Umfassende Tests der Programmier-Funktion
"""

from ti57_calculator import TI57Calculator

def program_celsius_to_fahrenheit(calc):
    """Programmiert Celsius → Fahrenheit: × 9 ÷ 5 + 32 ="""
    print("=== Programmiere: Celsius → Fahrenheit ===\n")
    
    # LRN aktivieren
    calc.learn_mode()
    print(f"LRN: Display zeigt '{calc.display}' (Schrittnummer)")
    
    # Programm: × 9 ÷ 5 + 32 =
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
    
    print(f"Schritte eingegeben: {len(calc.program)}")
    
    # LRN beenden
    calc.learn_mode()
    print(f"LRN beendet\n")


def test_temperature(calc, celsius):
    """Testet eine Temperatur-Umrechnung"""
    expected = celsius * 9 / 5 + 32
    
    # Eingabe
    calc.clear_entry()
    for digit in str(int(celsius)):
        calc.digit_pressed(digit)
    
    # Programm ausführen
    calc.run_stop()
    
    result = float(calc.display)
    success = abs(result - expected) < 0.01
    
    symbol = "✓" if success else "✗"
    print(f"{symbol} {celsius}°C → {result}°F (erwartet: {expected}°F)")
    
    return success


def main():
    calc = TI57Calculator()
    
    # Programm einmalig eingeben
    program_celsius_to_fahrenheit(calc)
    
    # Mehrere Tests
    print("=== Teste verschiedene Temperaturen ===\n")
    
    test_cases = [
        -40,  # Gleicher Wert in C und F
        0,    # Gefrierpunkt
        20,   # Raumtemperatur
        25,   # Angenehm
        37,   # Körpertemperatur
        100,  # Siedepunkt
    ]
    
    results = []
    for temp in test_cases:
        results.append(test_temperature(calc, temp))
    
    print(f"\n{'='*50}")
    if all(results):
        print("✓ ALLE TESTS ERFOLGREICH!")
        print("\nDie Programmier-Funktion funktioniert perfekt!")
        print("Sie können jetzt Programme eingeben und speichern.")
    else:
        print("✗ Einige Tests fehlgeschlagen")
    
    print(f"{'='*50}\n")
    
    # Zeige gespeichertes Programm
    print("Das Programm bleibt gespeichert und kann")
    print("beliebig oft mit verschiedenen Werten genutzt werden!")


if __name__ == "__main__":
    main()
