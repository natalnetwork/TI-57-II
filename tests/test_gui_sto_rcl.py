"""
Test: STO/RCL in GUI simulieren
"""

from ti57_gui import TI57GUI
import tkinter as tk

def test_gui_sto_rcl():
    print("=== Test: STO/RCL GUI Simulation ===\n")
    
    root = tk.Tk()
    gui = TI57GUI(root)
    
    # Test 1: 42 eingeben
    print("1. Eingabe: 42")
    gui.btn_digit("4")
    gui.btn_digit("2")
    print(f"   Display: {gui.calc.display}")
    print(f"   awaiting_memory_number: {gui.awaiting_memory_number}")
    print()
    
    # Test 2: STO drücken
    print("2. STO drücken")
    gui.btn_sto()
    print(f"   Display: {gui.calc.display}")
    print(f"   awaiting_memory_number: {gui.awaiting_memory_number}")
    print(f"   awaiting_memory_number ist None: {gui.awaiting_memory_number is None}")
    print()
    
    # Test 3: 0 drücken
    print("3. Taste 0 drücken (Register 0)")
    gui.btn_digit("0")
    print(f"   Display: {gui.calc.display}")
    print(f"   Memory[0]: {gui.calc.memory[0]}")
    print(f"   awaiting_memory_number: {gui.awaiting_memory_number}")
    print()
    
    # Test 4: Clear und RCL
    print("4. ON/C drücken")
    gui.btn_on_clear()
    print(f"   Display: {gui.calc.display}")
    print()
    
    print("5. RCL drücken")
    gui.btn_rcl()
    print(f"   awaiting_memory_number gesetzt: {gui.awaiting_memory_number is not None}")
    print()
    
    print("6. Taste 0 drücken (Register 0)")
    gui.btn_digit("0")
    print(f"   Display: {gui.calc.display}")
    print(f"   Sollte 42 sein")
    print()
    
    root.destroy()
    
    print("="*50)
    if gui.calc.memory[0] == 42.0 and gui.calc.display == "42":
        print("✓ STO/RCL funktionieren in der GUI!")
    else:
        print(f"✗ Problem: Memory[0]={gui.calc.memory[0]}, Display='{gui.calc.display}'")

if __name__ == "__main__":
    test_gui_sto_rcl()
