"""
TI-57 II Calculator Engine
Implementiert alle Funktionen des Texas Instruments TI-57 II
"""

import math
import json
import os
from enum import Enum
from typing import List, Optional, Tuple


class AngleMode(Enum):
    """Winkelmodus: Degrees, Radians, Gradians"""
    DEG = 0
    RAD = 1
    GRAD = 2


class CalculatorState(Enum):
    """Zustand des Rechners"""
    NORMAL = 0
    SECOND = 1
    INV = 2
    SECOND_INV = 3
    ERROR = 4


class TI57Calculator:
    """Calculator Engine für den TI-57 II"""
    
    def __init__(self):
        # Display und Eingabe
        self.display = "0"
        self.input_buffer = ""
        self.last_result = 0.0
        self.entering_number = False
        
        # Rechner-Status
        self.state = CalculatorState.NORMAL
        self.angle_mode = AngleMode.DEG
        self.fix_mode = None  # None=Floating, oder Anzahl Dezimalstellen
        
        # Stack für Operationen
        self.x_register = 0.0  # Aktueller Wert (Display)
        self.t_register = 0.0  # Vorheriger Wert
        self.pending_operation = None
        self.pending_value = None
        
        # Speicher (8 Register: 0-7)
        self.memory = [0.0] * 8
        
        # Programmierung
        self.program = []  # Bis zu 50 Schritte
        self.program_counter = 0
        self.programming_mode = False
        self.running_program = False
        
        # Statistik-Register
        self.stat_n = 0
        self.stat_sum_x = 0.0
        self.stat_sum_x2 = 0.0
        self.stat_sum_y = 0.0
        self.stat_sum_y2 = 0.0
        self.stat_sum_xy = 0.0
        
        # Flags
        self.error_flag = False
        self.error_message = ""
        
    def clear_entry(self):
        """Clear Entry - löscht aktuelle Eingabe"""
        self.input_buffer = ""
        self.display = "0"
        self.entering_number = False
        self.error_flag = False
        
    def clear_all(self):
        """Clear All - vollständiger Reset"""
        self.__init__()
        
    def get_display_value(self) -> float:
        """Gibt den aktuellen Display-Wert als Float zurück"""
        try:
            if self.input_buffer:
                return float(self.input_buffer)
            else:
                return float(self.display)
        except:
            return 0.0
            
    def set_display_value(self, value: float):
        """Setzt den Display-Wert"""
        if math.isnan(value) or math.isinf(value):
            self.error("Error")
            return
            
        # Format basierend auf Fix-Modus
        if self.fix_mode is not None:
            self.display = f"{value:.{self.fix_mode}f}"
        else:
            # Automatische Formatierung
            if abs(value) < 1e-9 and value != 0:
                self.display = f"{value:.6e}"
            elif abs(value) >= 1e10:
                self.display = f"{value:.6e}"
            else:
                self.display = str(value)
                # Entferne unnötige Nullen
                if '.' in self.display:
                    self.display = self.display.rstrip('0').rstrip('.')
        
        self.x_register = value
        self.entering_number = False
        self.input_buffer = ""
        
    def error(self, message: str = "Error"):
        """Setzt Fehlerzustand"""
        self.error_flag = True
        self.error_message = message
        self.display = message
        self.state = CalculatorState.ERROR
        
    def digit_pressed(self, digit: str):
        """Ziffer wurde gedrückt"""
        if self.error_flag:
            self.clear_entry()
            
        if not self.entering_number:
            self.input_buffer = digit
            self.entering_number = True
        else:
            self.input_buffer += digit
            
        self.display = self.input_buffer
        
    def decimal_pressed(self):
        """Dezimalpunkt wurde gedrückt"""
        if self.error_flag:
            self.clear_entry()
            
        if not self.entering_number:
            self.input_buffer = "0."
            self.entering_number = True
        elif '.' not in self.input_buffer:
            self.input_buffer += '.'
            
        self.display = self.input_buffer
        
    def change_sign(self):
        """+/- Taste: Ändert Vorzeichen"""
        if self.entering_number:
            if self.input_buffer.startswith('-'):
                self.input_buffer = self.input_buffer[1:]
            else:
                self.input_buffer = '-' + self.input_buffer
            self.display = self.input_buffer
        else:
            value = self.get_display_value()
            self.set_display_value(-value)
            
    def to_radians(self, angle: float) -> float:
        """Konvertiert Winkel basierend auf aktuellem Modus nach Radiant"""
        if self.angle_mode == AngleMode.DEG:
            return math.radians(angle)
        elif self.angle_mode == AngleMode.GRAD:
            return angle * math.pi / 200.0
        else:  # RAD
            return angle
            
    def from_radians(self, angle: float) -> float:
        """Konvertiert von Radiant in aktuellen Winkelmodus"""
        if self.angle_mode == AngleMode.DEG:
            return math.degrees(angle)
        elif self.angle_mode == AngleMode.GRAD:
            return angle * 200.0 / math.pi
        else:  # RAD
            return angle
            
    # Mathematische Funktionen
    
    def add(self):
        """Addition"""
        self._binary_operation(lambda a, b: a + b)
        
    def subtract(self):
        """Subtraktion"""
        self._binary_operation(lambda a, b: a - b)
        
    def multiply(self):
        """Multiplikation"""
        self._binary_operation(lambda a, b: a * b)
        
    def divide(self):
        """Division"""
        self._binary_operation(lambda a, b: a / b if b != 0 else float('inf'))
        
    def _binary_operation(self, operation):
        """Führt binäre Operation durch"""
        current_value = self.get_display_value()
        
        if self.pending_operation is not None and self.entering_number:
            # Berechne vorherige Operation
            try:
                result = self.pending_operation(self.pending_value, current_value)
                self.set_display_value(result)
                self.pending_value = result
            except:
                self.error()
                return
        else:
            self.pending_value = current_value
            
        self.pending_operation = operation
        self.entering_number = False
        self.input_buffer = ""
        
    def equals(self):
        """= Taste"""
        if self.pending_operation is not None:
            current_value = self.get_display_value()
            try:
                result = self.pending_operation(self.pending_value, current_value)
                self.set_display_value(result)
                self.pending_operation = None
                self.pending_value = None
            except:
                self.error()
                
    def square(self):
        """x² - Quadrat"""
        value = self.get_display_value()
        self.set_display_value(value ** 2)
        
    def square_root(self):
        """√x - Quadratwurzel"""
        value = self.get_display_value()
        if value < 0:
            self.error()
        else:
            self.set_display_value(math.sqrt(value))
            
    def cube_root(self):
        """∛x - Kubikwurzel"""
        value = self.get_display_value()
        sign = 1 if value >= 0 else -1
        self.set_display_value(sign * abs(value) ** (1/3))
        
    def reciprocal(self):
        """1/x - Kehrwert"""
        value = self.get_display_value()
        if value == 0:
            self.error("Div by 0")
        else:
            self.set_display_value(1.0 / value)
            
    def power(self):
        """y^x - Potenz"""
        self._binary_operation(lambda a, b: a ** b)
        
    def log(self):
        """log - Logarithmus zur Basis 10"""
        value = self.get_display_value()
        if value <= 0:
            self.error()
        else:
            self.set_display_value(math.log10(value))
            
    def ln(self):
        """ln - Natürlicher Logarithmus"""
        value = self.get_display_value()
        if value <= 0:
            self.error()
        else:
            self.set_display_value(math.log(value))
            
    def exp(self):
        """e^x - Exponentialfunktion"""
        value = self.get_display_value()
        try:
            self.set_display_value(math.exp(value))
        except OverflowError:
            self.error("Overflow")
            
    def power_of_10(self):
        """10^x"""
        value = self.get_display_value()
        try:
            self.set_display_value(10 ** value)
        except OverflowError:
            self.error("Overflow")
            
    def sin(self):
        """sin - Sinus"""
        value = self.get_display_value()
        rad_value = self.to_radians(value)
        self.set_display_value(math.sin(rad_value))
        
    def cos(self):
        """cos - Kosinus"""
        value = self.get_display_value()
        rad_value = self.to_radians(value)
        self.set_display_value(math.cos(rad_value))
        
    def tan(self):
        """tan - Tangens"""
        value = self.get_display_value()
        rad_value = self.to_radians(value)
        try:
            self.set_display_value(math.tan(rad_value))
        except:
            self.error()
            
    def asin(self):
        """arcsin - Arkussinus"""
        value = self.get_display_value()
        if value < -1 or value > 1:
            self.error()
        else:
            rad_result = math.asin(value)
            self.set_display_value(self.from_radians(rad_result))
            
    def acos(self):
        """arccos - Arkuskosinus"""
        value = self.get_display_value()
        if value < -1 or value > 1:
            self.error()
        else:
            rad_result = math.acos(value)
            self.set_display_value(self.from_radians(rad_result))
            
    def atan(self):
        """arctan - Arkustangens"""
        value = self.get_display_value()
        rad_result = math.atan(value)
        self.set_display_value(self.from_radians(rad_result))
        
    def factorial(self):
        """n! - Fakultät"""
        value = self.get_display_value()
        if value < 0 or value != int(value) or value > 69:
            self.error()
        else:
            self.set_display_value(float(math.factorial(int(value))))
            
    def pi(self):
        """π - Pi-Konstante"""
        self.set_display_value(math.pi)
        
    # Speicher-Funktionen
    
    def store(self, register: int):
        """STO - Speichert Wert in Register (0-7)"""
        if 0 <= register <= 7:
            self.memory[register] = self.get_display_value()
            
    def recall(self, register: int):
        """RCL - Ruft Wert aus Register ab (0-7)"""
        if 0 <= register <= 7:
            self.set_display_value(self.memory[register])
            
    def sum_to_memory(self, register: int):
        """Σ+ - Addiert zu Speicher"""
        if 0 <= register <= 7:
            self.memory[register] += self.get_display_value()
            
    def exchange_memory(self, register: int):
        """EXC - Tauscht Display mit Speicher"""
        if 0 <= register <= 7:
            current = self.get_display_value()
            self.set_display_value(self.memory[register])
            self.memory[register] = current
            
    def clear_memory(self):
        """CM - Löscht alle Speicher"""
        self.memory = [0.0] * 8
        
    def exchange_t(self):
        """x⇄t - Tauscht x und t Register"""
        temp = self.x_register
        self.x_register = self.t_register
        self.t_register = temp
        self.set_display_value(self.x_register)
        
    # Winkel- und Koordinaten-Funktionen
    
    def toggle_drg(self):
        """DRG - Wechselt zwischen Deg/Rad/Grad"""
        if self.angle_mode == AngleMode.DEG:
            self.angle_mode = AngleMode.RAD
        elif self.angle_mode == AngleMode.RAD:
            self.angle_mode = AngleMode.GRAD
        else:
            self.angle_mode = AngleMode.DEG
            
    def dms_to_dd(self):
        """D.MS (DMS→DD) - Konvertiert Grad.Minuten.Sekunden zu Dezimalgrad"""
        value = self.get_display_value()
        degrees = int(value)
        minutes = int((value - degrees) * 100)
        seconds = ((value - degrees) * 100 - minutes) * 100
        
        decimal_degrees = degrees + minutes / 60.0 + seconds / 3600.0
        self.set_display_value(decimal_degrees)
        
    def dd_to_dms(self):
        """DMS DD (DD→DMS) - Konvertiert Dezimalgrad zu Grad.Minuten.Sekunden"""
        value = self.get_display_value()
        degrees = int(value)
        minutes_decimal = (value - degrees) * 60
        minutes = int(minutes_decimal)
        seconds = (minutes_decimal - minutes) * 60
        
        result = degrees + minutes / 100.0 + seconds / 10000.0
        self.set_display_value(result)
        
    def polar_to_rectangular(self):
        """P→R - Konvertiert Polar zu Kartesisch"""
        # r im Display, θ in t-Register
        r = self.get_display_value()
        theta = self.to_radians(self.t_register)
        
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        
        self.set_display_value(x)
        self.t_register = y
        
    def rectangular_to_polar(self):
        """R→P - Konvertiert Kartesisch zu Polar"""
        # x im Display, y in t-Register
        x = self.get_display_value()
        y = self.t_register
        
        r = math.sqrt(x**2 + y**2)
        theta_rad = math.atan2(y, x)
        theta = self.from_radians(theta_rad)
        
        self.set_display_value(r)
        self.t_register = theta
        
    # Statistik-Funktionen
    
    def sigma_plus(self):
        """Σ+ - Fügt Datenpunkt hinzu"""
        x = self.get_display_value()
        y = self.t_register
        
        self.stat_n += 1
        self.stat_sum_x += x
        self.stat_sum_x2 += x * x
        self.stat_sum_y += y
        self.stat_sum_y2 += y * y
        self.stat_sum_xy += x * y
        
        self.set_display_value(self.stat_n)
        
    def sigma_minus(self):
        """Σ- - Entfernt Datenpunkt"""
        if self.stat_n > 0:
            x = self.get_display_value()
            y = self.t_register
            
            self.stat_n -= 1
            self.stat_sum_x -= x
            self.stat_sum_x2 -= x * x
            self.stat_sum_y -= y
            self.stat_sum_y2 -= y * y
            self.stat_sum_xy -= x * y
            
            self.set_display_value(self.stat_n)
            
    def mean(self):
        """x̄ - Mittelwert"""
        if self.stat_n == 0:
            self.error()
        else:
            self.set_display_value(self.stat_sum_x / self.stat_n)
            
    def standard_deviation(self):
        """σ - Standardabweichung"""
        if self.stat_n == 0:
            self.error()
        else:
            mean = self.stat_sum_x / self.stat_n
            variance = (self.stat_sum_x2 / self.stat_n) - (mean ** 2)
            if variance < 0:
                variance = 0
            self.set_display_value(math.sqrt(variance))
            
    def clear_statistics(self):
        """Löscht Statistik-Register"""
        self.stat_n = 0
        self.stat_sum_x = 0.0
        self.stat_sum_x2 = 0.0
        self.stat_sum_y = 0.0
        self.stat_sum_y2 = 0.0
        self.stat_sum_xy = 0.0
        
    # Programmier-Funktionen
    
    def learn_mode(self):
        """LRN - Aktiviert Programmiermodus"""
        self.programming_mode = not self.programming_mode
        if self.programming_mode:
            self.program_counter = 0
            self.display = f"00"
        else:
            self.display = "0"
    
    def record_operation(self, operation_name: str, operation_func):
        """Zeichnet eine Operation im Programm auf"""
        if self.programming_mode and len(self.program) < 50:
            self.program.append((operation_name, operation_func))
            self.program_counter = len(self.program)
            self.display = f"{self.program_counter:02d}"
            
    def step_program(self):
        """SST - Einzelschritt im Programm"""
        if self.programming_mode:
            if self.program_counter < len(self.program):
                step_name, step_func = self.program[self.program_counter]
                
                # Zeige Schrittnummer und Inhalt
                step_display = self._format_step_display(step_name)
                self.display = f"{self.program_counter:02d} {step_display}"
                
                self.program_counter += 1
            else:
                self.program_counter = 0
                self.display = "00"
    
    def _format_step_display(self, step_name: str) -> str:
        """Formatiert Schritt-Namen für Display"""
        # Mapping für bessere Anzeige
        display_map = {
            "multiply": "×",
            "divide": "÷",
            "add": "+",
            "subtract": "−",
            "equals": "=",
            "square": "x²",
            "sqrt": "√x",
            "reciprocal": "1/x",
            "log": "log",
            "ln": "ln",
            "sin": "sin",
            "cos": "cos",
            "tan": "tan",
            "decimal": ".",
        }
        
        # Ziffern
        if step_name.startswith("digit_"):
            return step_name.split("_")[1]
        
        return display_map.get(step_name, step_name[:3])
                
    def run_stop(self):
        """R/S - Startet/Stoppt Programm"""
        if self.programming_mode:
            return
        
        if not self.running_program:
            # Programm starten
            self.running_program = True
            self.program_counter = 0
            
            # Sichere den aktuellen Eingabewert (wird als x für das Programm verwendet)
            input_value = self.get_display_value()
            
            # Reset für saubere Programmausführung
            saved_entering = self.entering_number
            self.entering_number = False
            self.input_buffer = ""
            
            # Setze Startwert
            self.set_display_value(input_value)
            self.entering_number = True  # Damit erste Operation den Wert verwendet
            self.input_buffer = str(input_value)
            
            # Führe alle Programmschritte aus
            try:
                for step_name, step_func in self.program:
                    if callable(step_func):
                        step_func()
                self.running_program = False
            except Exception as e:
                print(f"Program error: {e}")
                self.error("Prg Error")
                self.running_program = False
        else:
            # Programm stoppen
            self.running_program = False
            
    def reset_program(self):
        """RST - Reset Programmzähler"""
        self.program_counter = 0
        if self.programming_mode:
            self.display = "00"
            
    def insert_step(self, operation: str):
        """INS - Fügt Programmschritt ein"""
        if self.programming_mode and len(self.program) < 50:
            self.program.insert(self.program_counter, operation)
            self.program_counter += 1
            self.display = f"{self.program_counter:02d}"
            
    def delete_step(self):
        """DEL - Löscht Programmschritt"""
        if self.programming_mode and self.program_counter < len(self.program):
            del self.program[self.program_counter]
            self.display = f"{self.program_counter:02d}"
            
    def goto_step(self, step: int):
        """GTO - Springe zu Schritt"""
        if 0 <= step < len(self.program):
            self.program_counter = step
            
    def subroutine(self):
        """SBR - Subroutine (vereinfacht)"""
        # Vereinfachte Implementierung
        pass
        
    def decrement_and_skip(self):
        """Dsz - Dekrementiere und überspringe wenn Null"""
        value = self.get_display_value()
        value -= 1
        self.set_display_value(value)
        
        if self.running_program and value == 0:
            self.program_counter += 1
    
    def save_state(self, filename: str = "ti57_state.json"):
        """Speichert Calculator-Zustand in Datei (nur Programm)"""
        # Speichere nur die Namen der Programmschritte (nicht die Funktionen)
        # Display-Werte und Register werden NICHT gespeichert
        program_names = [step[0] for step in self.program]
        
        state = {
            "program": program_names
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(state, f, indent=2)
            return True
        except Exception as e:
            print(f"Fehler beim Speichern: {e}")
            return False
    
    def _get_operation_func(self, name: str):
        """Wandelt Operationsnamen in Funktionen um"""
        # Mapping von Namen zu Funktionen
        operations = {
            "add": self.add,
            "subtract": self.subtract,
            "multiply": self.multiply,
            "divide": self.divide,
            "equals": self.equals,
            "square": self.square,
            "sqrt": self.square_root,
            "reciprocal": self.reciprocal,
            "log": self.log,
            "ln": self.ln,
            "sin": self.sin,
            "cos": self.cos,
            "tan": self.tan,
            "pi": self.pi,
            "factorial": self.factorial,
            "exchange_t": self.exchange_t,
            "clear_memory": self.clear_memory,
            "decimal": self.decimal_pressed,
        }
        
        # Ziffern
        if name.startswith("digit_"):
            digit = name.split("_")[1]
            return lambda d=digit: self.digit_pressed(d)
        
        return operations.get(name, lambda: None)
    
    def load_state(self, filename: str = "ti57_state.json"):
        """Lädt Calculator-Zustand aus Datei (nur Programm, alles andere wird zurückgesetzt)"""
        if not os.path.exists(filename):
            return False
        
        try:
            with open(filename, 'r') as f:
                state = json.load(f)
            
            # Lade nur das Programm und rekonstruiere Funktionen
            program_names = state.get("program", [])
            self.program = [(name, self._get_operation_func(name)) for name in program_names]
            
            # Alle anderen Werte werden auf Standardwerte zurückgesetzt (wie beim Einschalten)
            self.memory = [0.0] * 8
            self.angle_mode = AngleMode.DEG
            self.fix_mode = None
            self.x_register = 0.0
            self.t_register = 0.0
            self.program_counter = 0
            
            # Display auf 0 setzen
            self.display = "0."
            return True
        except Exception as e:
            print(f"Fehler beim Laden: {e}")
            return False
