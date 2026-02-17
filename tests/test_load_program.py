"""
Test: Lädt das Programm aus der JSON-Datei
"""

from ti57_calculator import TI57Calculator

def test_load_program():
    calc = TI57Calculator()
    
    print("=== Test: Programm aus JSON laden ===\n")
    
    # Lade Zustand (mit Programm)
    success = calc.load_state()
    print(f"Laden erfolgreich: {success}")
    print(f"Programmschritte geladen: {len(calc.program)}\n")
    
    if calc.program:
        print("Programm-Inhalt:")
        for i, (name, func) in enumerate(calc.program):
            print(f"  {i+1}. {name}")
        print()
    
    # Test mit verschiedenen Temperaturen
    print("=== Teste das geladene Programm ===\n")
    
    test_values = [
        (0, 32),
        (20, 68),
        (100, 212),
        (37, 98.6),
    ]
    
    for celsius, expected in test_values:
        # Eingabe
        calc.clear_entry()
        for digit in str(celsius):
            calc.digit_pressed(digit)
        
        # Programm ausführen
        calc.run_stop()
        
        result = float(calc.display)
        success_marker = "✓" if abs(result - expected) < 0.1 else "✗"
        print(f"{success_marker} {celsius}°C → {result}°F (erwartet: {expected}°F)")
    
    print("\n" + "="*50)
    print("Das Programm ist bereit zum Testen in der GUI!")
    print("Starten Sie einfach: python ti57_gui.py")
    print("="*50)

if __name__ == "__main__":
    test_load_program()
