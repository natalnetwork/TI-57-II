"""
TI-57 II Calculator - Bedienungsanleitung und Beispiele
"""

from ti57_calculator import TI57Calculator, AngleMode


def test_basic_operations():
    """Test grundlegender Rechenoperationen"""
    print("=== Grundrechenarten ===")
    calc = TI57Calculator()
    
    # Addition: 5 + 3
    calc.digit_pressed("5")
    calc.add()
    calc.digit_pressed("3")
    calc.equals()
    print(f"5 + 3 = {calc.display}")  # Sollte 8 sein
    
    # Multiplikation: 12 × 4
    calc.clear_entry()
    calc.digit_pressed("1")
    calc.digit_pressed("2")
    calc.multiply()
    calc.digit_pressed("4")
    calc.equals()
    print(f"12 × 4 = {calc.display}")  # Sollte 48 sein
    
    # Division: 100 ÷ 4
    calc.clear_entry()
    calc.digit_pressed("1")
    calc.digit_pressed("0")
    calc.digit_pressed("0")
    calc.divide()
    calc.digit_pressed("4")
    calc.equals()
    print(f"100 ÷ 4 = {calc.display}")  # Sollte 25 sein
    
    print()


def test_scientific_functions():
    """Test wissenschaftlicher Funktionen"""
    print("=== Wissenschaftliche Funktionen ===")
    calc = TI57Calculator()
    
    # Quadratwurzel von 144
    calc.digit_pressed("1")
    calc.digit_pressed("4")
    calc.digit_pressed("4")
    calc.square_root()
    print(f"√144 = {calc.display}")  # Sollte 12 sein
    
    # sin(30°) im DEG Modus
    calc.angle_mode = AngleMode.DEG
    calc.digit_pressed("3")
    calc.digit_pressed("0")
    calc.sin()
    print(f"sin(30°) = {calc.display}")  # Sollte 0.5 sein
    
    # ln(e) ≈ 1
    calc.clear_entry()
    calc.digit_pressed("1")
    calc.exp()  # e^1
    calc.ln()
    print(f"ln(e) = {calc.display}")  # Sollte ≈ 1 sein
    
    # 5!
    calc.clear_entry()
    calc.digit_pressed("5")
    calc.factorial()
    print(f"5! = {calc.display}")  # Sollte 120 sein
    
    print()


def test_memory_operations():
    """Test der Speicherfunktionen"""
    print("=== Speicher-Operationen ===")
    calc = TI57Calculator()
    
    # Speichere 42 in Register 0
    calc.digit_pressed("4")
    calc.digit_pressed("2")
    calc.store(0)
    print(f"Gespeichert: 42 in Register 0")
    
    # Rechne etwas anderes
    calc.digit_pressed("1")
    calc.digit_pressed("0")
    calc.add()
    calc.digit_pressed("5")
    calc.equals()
    print(f"10 + 5 = {calc.display}")
    
    # Rufe 42 aus Register 0 ab
    calc.recall(0)
    print(f"Abgerufen aus Register 0: {calc.display}")
    
    print()


def test_angle_conversions():
    """Test der Winkelumrechnungen"""
    print("=== Winkelumrechnungen ===")
    calc = TI57Calculator()
    
    # Konvertiere 45.3015 von D.MS zu DD (45°30'15" zu Dezimalgrad)
    calc.digit_pressed("4")
    calc.digit_pressed("5")
    calc.decimal_pressed()
    calc.digit_pressed("3")
    calc.digit_pressed("0")
    calc.digit_pressed("1")
    calc.digit_pressed("5")
    calc.dms_to_dd()
    print(f"45°30'15\" in Dezimalgrad = {calc.display}")
    
    print()


def test_statistics():
    """Test der Statistik-Funktionen"""
    print("=== Statistik ===")
    calc = TI57Calculator()
    
    # Füge Datenpunkte hinzu: 2, 4, 6, 8, 10
    data = [2, 4, 6, 8, 10]
    for value in data:
        calc.clear_entry()
        calc.digit_pressed(str(value))
        calc.sigma_plus()
    
    print(f"Datenpunkte hinzugefügt: {data}")
    print(f"Anzahl (n) = {calc.display}")
    
    # Berechne Mittelwert
    calc.mean()
    print(f"Mittelwert (x̄) = {calc.display}")
    
    # Berechne Standardabweichung
    calc.standard_deviation()
    print(f"Standardabweichung (σ) = {calc.display}")
    
    print()


def test_polar_rectangular():
    """Test Polar/Kartesisch Konvertierung"""
    print("=== Polar ↔ Kartesisch ===")
    calc = TI57Calculator()
    calc.angle_mode = AngleMode.DEG
    
    # Konvertiere Kartesisch (3, 4) zu Polar
    calc.clear_entry()
    calc.digit_pressed("3")  # x
    calc.set_display_value(3)
    calc.t_register = 4  # y
    calc.rectangular_to_polar()
    print(f"Kartesisch (3, 4) → Polar")
    print(f"  r = {calc.display}")
    print(f"  θ = {calc.t_register:.2f}°")
    
    print()


def demonstrate_calculator():
    """Demonstriert verschiedene Rechner-Funktionen"""
    print("=" * 50)
    print("TI-57 II Calculator - Funktionsdemonstration")
    print("=" * 50)
    print()
    
    test_basic_operations()
    test_scientific_functions()
    test_memory_operations()
    test_angle_conversions()
    test_statistics()
    test_polar_rectangular()
    
    print("=" * 50)
    print("Alle Tests abgeschlossen!")
    print("=" * 50)


if __name__ == "__main__":
    demonstrate_calculator()
