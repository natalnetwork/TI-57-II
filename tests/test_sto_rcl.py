"""
Test: STO und RCL Funktionen
"""

from ti57_calculator import TI57Calculator

def test_sto_rcl():
    calc = TI57Calculator()
    
    print("=== Test: STO und RCL (Engine) ===\n")
    
    # Test 1: Wert in Register 0 speichern
    print("1. Speichere 42 in Register 0:")
    calc.clear_entry()
    calc.digit_pressed("4")
    calc.digit_pressed("2")
    print(f"   Eingabe: {calc.display}")
    
    # STO 0
    calc.store(0)
    print(f"   Nach STO 0: Memory[0] = {calc.memory[0]}")
    print()
    
    # Test 2: Display löschen und Wert abrufen
    print("2. Display löschen und aus Register 0 abrufen:")
    calc.clear_entry()
    print(f"   Display nach Clear: {calc.display}")
    
    # RCL 0
    calc.recall(0)
    print(f"   Nach RCL 0: Display = {calc.display}")
    print()
    
    # Test 3: Mehrere Register
    print("3. Teste mehrere Register:")
    for i in range(3):
        calc.clear_entry()
        value = (i + 1) * 10
        for digit in str(value):
            calc.digit_pressed(digit)
        calc.store(i)
        print(f"   STO {i}: Memory[{i}] = {calc.memory[i]}")
    
    print()
    print("4. Abrufen der gespeicherten Werte:")
    for i in range(3):
        calc.clear_entry()
        calc.recall(i)
        print(f"   RCL {i}: Display = {calc.display}")
    
    print("\n" + "="*50)
    if calc.memory[0] == 10 and calc.memory[1] == 20 and calc.memory[2] == 30:
        print("✓ STO und RCL funktionieren in der Engine!")
    else:
        print("✗ Problem in der Engine")
    print("="*50)

if __name__ == "__main__":
    test_sto_rcl()
