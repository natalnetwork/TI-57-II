"""
Test: SST zeigt Programm-Inhalt
"""

from ti57_calculator import TI57Calculator

def test_sst_display():
    calc = TI57Calculator()
    
    print("=== Test: SST zeigt Programm-Inhalt ===\n")
    
    # Lade Programm
    calc.load_state()
    print(f"Programm geladen: {len(calc.program)} Schritte\n")
    
    # Aktiviere Programmiermodus
    calc.learn_mode()
    print("LRN aktiviert - Programmiermodus\n")
    
    print("Durchlaufe Programm mit SST:\n")
    
    # Gehe durch alle Schritte
    for i in range(len(calc.program) + 1):
        calc.step_program()
        print(f"  Schritt {i}: Display = '{calc.display}'")
    
    print("\n" + "="*50)
    print("Jetzt sollten Sie im Display sehen:")
    print("  00 ×")
    print("  01 9")
    print("  02 ÷")
    print("  03 5")
    print("  etc.")
    print("="*50)
    
if __name__ == "__main__":
    test_sst_display()
