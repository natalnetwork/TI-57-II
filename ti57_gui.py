"""
TI-57 II Calculator GUI
Authentisches Layout des Texas Instruments TI-57 II - KORREKT
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import math
import json
import shutil
from pathlib import Path
from ti57_calculator import TI57Calculator, CalculatorState, AngleMode


class TI57GUI:
    """GUI für den TI-57 II Calculator"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("TI-57 II Calculator")
        self.root.configure(bg='#C0C5CE')
        self.root.resizable(False, False)
        
        # Pfad zur State-Datei
        self.state_file = Path(__file__).parent / "ti57_state.json"
        
        # Calculator Engine
        self.calc = TI57Calculator()
        
        # Lade gespeicherten Zustand
        self.calc.load_state(str(self.state_file))
        
        # Warte auf Speicher-/Register-Nummer
        self.awaiting_memory_number = None
        
        # Haupt-Container
        self.main_frame = tk.Frame(root, bg='#C0C5CE', padx=15, pady=15)
        self.main_frame.pack(padx=10, pady=10)
        
        # Erstelle GUI-Komponenten
        self.create_display()
        self.create_status_indicators()
        self.create_keyboard()
        
        # Update Display
        self.update_display()
        
    def on_closing(self):
        """Speichert Zustand beim Beenden"""
        self.calc.save_state(str(self.state_file))
        self.root.destroy()
        
    def create_display(self):
        """Erstellt das LCD-Display"""
        display_frame = tk.Frame(self.main_frame, bg='#7c8c6f', bd=3, relief=tk.SUNKEN)
        display_frame.grid(row=0, column=0, columnspan=5, pady=(0, 10), sticky='ew')
        
        # Display mit LCD-Stil
        self.display_var = tk.StringVar(value="0")
        self.display = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=('Courier', 24, 'bold'),
            bg='#9db88f',
            fg='#1a1a1a',
            anchor='e',
            padx=10,
            pady=8,
            width=12
        )
        self.display.pack(fill=tk.BOTH, expand=True)
        
        # Rechtsklick-Menü für Programm laden
        self.display.bind("<Button-3>", self.show_context_menu)
        
    def create_status_indicators(self):
        """Erstellt Status-Indikatoren"""
        status_frame = tk.Frame(self.main_frame, bg='#C0C5CE')
        status_frame.grid(row=1, column=0, columnspan=5, pady=(0, 10))
        
        # Indikatoren für 2nd, INV, DRG, etc.
        self.indicator_2nd = tk.Label(status_frame, text="2nd", font=('Arial', 8), 
                                      bg='#C0C5CE', fg='#7f8c8d', width=4)
        self.indicator_2nd.pack(side=tk.LEFT, padx=5)
        
        self.indicator_inv = tk.Label(status_frame, text="INV", font=('Arial', 8),
                                      bg='#C0C5CE', fg='#7f8c8d', width=4)
        self.indicator_inv.pack(side=tk.LEFT, padx=5)
        
        self.indicator_drg = tk.Label(status_frame, text="DEG", font=('Arial', 8),
                                      bg='#C0C5CE', fg='#27ae60', width=4)
        self.indicator_drg.pack(side=tk.LEFT, padx=5)
        
        self.indicator_pgm = tk.Label(status_frame, text="", font=('Arial', 8),
                                      bg='#C0C5CE', fg='#7f8c8d', width=4)
        self.indicator_pgm.pack(side=tk.LEFT, padx=5)
        
    def create_keyboard(self):
        """Erstellt die Tastatur"""
        # Zeile 1: 2nd, INV, R/S, OFF, ON/C
        self.create_button(2, 0, "2nd", "#6B7280", self.btn_2nd, "", False, "white")
        self.create_button(2, 1, "INV", "#6B7280", self.btn_inv, "", False, "white")
        self.create_button(2, 2, "R/S", "#6B7280", self.btn_run_stop, "", False, "white")
        self.create_button(2, 3, "OFF", "#6B7280", self.btn_off, "", False, "white")
        self.create_button(2, 4, "ON/C", "#4A90E2", self.btn_on_clear, "", False, "white")
        
        # Zeile 2: RST, GTO, LBL, BST, SST (2nd: x=t, x>=t, SBR, Dsz, Del)
        self.create_button(3, 0, "RST", "#6B7280", self.btn_rst, "x=t", True, "white")
        self.create_button(3, 1, "GTO", "#6B7280", self.btn_gto, "x≥t", True, "white")
        self.create_button(3, 2, "LBL", "#6B7280", self.btn_lbl, "SBR", True, "white")
        self.create_button(3, 3, "BST", "#6B7280", self.btn_bst, "Dsz", True, "white")
        self.create_button(3, 4, "SST", "#6B7280", self.btn_sst, "Del", True, "white")
        
        # Zeile 3: log, lnx, 1/x, x², √x (2nd: 10^x, e^x)
        self.create_button(4, 0, "log", "#6B7280", self.btn_log, "10ˣ", True, "white")
        self.create_button(4, 1, "lnx", "#6B7280", self.btn_ln, "eˣ", True, "white")
        self.create_button(4, 2, "1/x", "#6B7280", self.btn_reciprocal, "", False, "white")
        self.create_button(4, 3, "x²", "#6B7280", self.btn_square, "", False, "white")
        self.create_button(4, 4, "√x", "#6B7280", self.btn_sqrt, "", False, "white")
        
        # Zeile 4: DRG, sin, cos, tan, y^x (2nd: DRG>, P<>R, DMSDD, PI, x!)
        self.create_button(5, 0, "DRG", "#6B7280", self.btn_drg, "DRG>", True, "white")
        self.create_button(5, 1, "sin", "#6B7280", self.btn_sin, "P↔R", True, "white")
        self.create_button(5, 2, "cos", "#6B7280", self.btn_cos, "DMS", True, "white")
        self.create_button(5, 3, "tan", "#6B7280", self.btn_tan, "π", True, "white")
        self.create_button(5, 4, "yˣ", "#6B7280", self.btn_power, "x!", True, "white")
        
        # Zeile 5: x<>t, EE, (, ), / (2nd: C.t, Fix, Intg, Frac, |x|)
        self.create_button(6, 0, "x↔t", "#6B7280", self.btn_exchange_t, "C.t", True, "white")
        self.create_button(6, 1, "EE", "#6B7280", self.btn_ee, "Fix", True, "white")
        self.create_button(6, 2, "(", "#6B7280", self.btn_paren_open, "Intg", True, "white")
        self.create_button(6, 3, ")", "#6B7280", self.btn_paren_close, "Frac", True, "white")
        self.create_button(6, 4, "÷", "#4A90E2", self.btn_divide, "|x|", True, "white")
        
        # Zeile 6: STO, 7, 8, 9, × (2nd: part)
        self.create_button(7, 0, "STO", "#6B7280", self.btn_sto, "part", True, "white")
        self.create_button(7, 1, "7", "#FFFFFF", lambda: self.btn_digit("7"), "", False, "black")
        self.create_button(7, 2, "8", "#FFFFFF", lambda: self.btn_digit("8"), "", False, "black")
        self.create_button(7, 3, "9", "#FFFFFF", lambda: self.btn_digit("9"), "", False, "black")
        self.create_button(7, 4, "×", "#4A90E2", self.btn_multiply, "", False, "white")
        
        # Zeile 7: RCL, 4, 5, 6, - (2nd: CM)
        self.create_button(8, 0, "RCL", "#6B7280", self.btn_rcl, "CM", True, "white")
        self.create_button(8, 1, "4", "#FFFFFF", lambda: self.btn_digit("4"), "", False, "black")
        self.create_button(8, 2, "5", "#FFFFFF", lambda: self.btn_digit("5"), "", False, "black")
        self.create_button(8, 3, "6", "#FFFFFF", lambda: self.btn_digit("6"), "", False, "black")
        self.create_button(8, 4, "−", "#4A90E2", self.btn_subtract, "", False, "white")
        
        # Zeile 8: EXC, 1, 2, 3, + (2nd: CP)
        self.create_button(9, 0, "EXC", "#6B7280", self.btn_exc, "CP", True, "white")
        self.create_button(9, 1, "1", "#FFFFFF", lambda: self.btn_digit("1"), "", False, "black")
        self.create_button(9, 2, "2", "#FFFFFF", lambda: self.btn_digit("2"), "", False, "black")
        self.create_button(9, 3, "3", "#FFFFFF", lambda: self.btn_digit("3"), "", False, "black")
        self.create_button(9, 4, "+", "#4A90E2", self.btn_add, "", False, "white")
        
        # Zeile 9: LRN, 0, ., +/-, = (2nd: Pause)
        self.create_button(10, 0, "LRN", "#6B7280", self.btn_lrn, "Pause", True, "white")
        self.create_button(10, 1, "0", "#FFFFFF", lambda: self.btn_digit("0"), "", False, "black")
        self.create_button(10, 2, ".", "#FFFFFF", self.btn_decimal, "", False, "black")
        self.create_button(10, 3, "+/−", "#6B7280", self.btn_change_sign, "", False, "white")
        self.create_button(10, 4, "=", "#4A90E2", self.btn_equals, "", False, "white")
        
    def create_button(self, row, col, text, bg_color, command, secondary_text="", has_secondary=False, fg_color='white'):
        """Erstellt einen Button mit optionaler Sekundär-Funktion"""
        btn_frame = tk.Frame(self.main_frame, bg='#C0C5CE')
        btn_frame.grid(row=row, column=col, padx=3, pady=3, sticky='s')
        
        # Sekundär-Text oben (klein)
        if has_secondary and secondary_text:
            sec_label = tk.Label(btn_frame, text=secondary_text, 
                                font=('Arial', 7), bg='#C0C5CE', fg='#8B3A3A')
            sec_label.pack()
        
        # Haupt-Button
        btn = tk.Button(
            btn_frame,
            text=text,
            command=command,
            bg=bg_color,
            fg=fg_color,
            font=('Arial', 10, 'bold'),
            width=6,
            height=2,
            relief=tk.RAISED,
            bd=3,
            activebackground='#95a5a6'
        )
        btn.pack()
        
    # Button-Handler
    
    def btn_digit(self, digit):
        """Zifferntaste"""
        if self.awaiting_memory_number is not None:
            try:
                num = int(digit)
                if 0 <= num <= 7:
                    self.awaiting_memory_number(num)
                    self.awaiting_memory_number = None
            except:
                pass
        elif self.calc.programming_mode:
            # Im Programmiermodus: Operation aufzeichnen
            self.calc.record_operation(f"digit_{digit}", lambda d=digit: self.calc.digit_pressed(d))
        else:
            self.calc.digit_pressed(digit)
        self.update_display()
        
    def btn_decimal(self):
        """Dezimalpunkt"""
        if self.calc.programming_mode:
            self.calc.record_operation("decimal", self.calc.decimal_pressed)
        else:
            self.calc.decimal_pressed()
        self.update_display()
        
    def btn_change_sign(self):
        """+/- Taste"""
        self.calc.change_sign()
        self.update_display()
        
    def btn_add(self):
        """Addition"""
        if self.calc.programming_mode:
            self.calc.record_operation("add", self.calc.add)
        else:
            self.calc.add()
        self.update_display()
        
    def btn_subtract(self):
        """Subtraktion"""
        if self.calc.programming_mode:
            self.calc.record_operation("subtract", self.calc.subtract)
        else:
            self.calc.subtract()
        self.update_display()
        
    def btn_multiply(self):
        """Multiplikation"""
        if self.calc.programming_mode:
            self.calc.record_operation("multiply", self.calc.multiply)
        else:
            self.calc.multiply()
        self.update_display()
        
    def btn_divide(self):
        """Division oder |x| (2nd)"""
        if self.calc.state == CalculatorState.SECOND or self.calc.state == CalculatorState.SECOND_INV:
            # |x| - Absolute value
            value = self.calc.get_display_value()
            self.calc.set_display_value(abs(value))
            self.reset_state()
        elif self.calc.programming_mode:
            self.calc.record_operation("divide", self.calc.divide)
        else:
            self.calc.divide()
        self.update_display()
        
    def btn_equals(self):
        """Gleichheitszeichen"""
        if self.calc.programming_mode:
            self.calc.record_operation("equals", self.calc.equals)
        else:
            self.calc.equals()
        self.update_display()
        
    def btn_square(self):
        """x²"""
        self.calc.square()
        self.update_display()
        
    def btn_sqrt(self):
        """√x"""
        self.calc.square_root()
        self.update_display()
        
    def btn_reciprocal(self):
        """1/x"""
        self.calc.reciprocal()
        self.update_display()
        
    def btn_power(self):
        """y^x oder x! (2nd)"""
        if self.calc.state == CalculatorState.SECOND or self.calc.state == CalculatorState.SECOND_INV:
            # x! - Factorial
            self.calc.factorial()
            self.reset_state()
        else:
            self.calc.power()
        self.update_display()
        
    def btn_log(self):
        """log oder 10^x (2nd)"""
        if self.calc.state == CalculatorState.SECOND or self.calc.state == CalculatorState.SECOND_INV:
            self.calc.power_of_10()
            self.reset_state()
        else:
            self.calc.log()
        self.update_display()
        
    def btn_ln(self):
        """ln oder e^x (2nd)"""
        if self.calc.state == CalculatorState.SECOND or self.calc.state == CalculatorState.SECOND_INV:
            self.calc.exp()
            self.reset_state()
        else:
            self.calc.ln()
        self.update_display()
        
    def btn_sin(self):
        """sin oder P↔R (2nd) oder sin⁻¹ (INV)"""
        if self.calc.state == CalculatorState.SECOND or self.calc.state == CalculatorState.SECOND_INV:
            # P↔R - Polar to Rectangular
            self.calc.polar_to_rectangular()
            self.reset_state()
        elif self.calc.state == CalculatorState.INV:
            self.calc.asin()
            self.reset_state()
        else:
            self.calc.sin()
        self.update_display()
        
    def btn_cos(self):
        """cos oder DMS (2nd) oder cos⁻¹ (INV)"""
        if self.calc.state == CalculatorState.SECOND or self.calc.state == CalculatorState.SECOND_INV:
            # DMS - DMS to Decimal Degrees
            self.calc.dms_to_dd()
            self.reset_state()
        elif self.calc.state == CalculatorState.INV:
            self.calc.acos()
            self.reset_state()
        else:
            self.calc.cos()
        self.update_display()
        
    def btn_tan(self):
        """tan oder π (2nd) oder tan⁻¹ (INV)"""
        if self.calc.state == CalculatorState.SECOND or self.calc.state == CalculatorState.SECOND_INV:
            # π - Pi constant
            self.calc.pi()
            self.reset_state()
        elif self.calc.state == CalculatorState.INV:
            self.calc.atan()
            self.reset_state()
        else:
            self.calc.tan()
        self.update_display()
        
    def btn_2nd(self):
        """2nd Taste - Aktiviert Sekundärfunktionen"""
        if self.calc.state == CalculatorState.NORMAL:
            self.calc.state = CalculatorState.SECOND
        elif self.calc.state == CalculatorState.INV:
            self.calc.state = CalculatorState.SECOND_INV
        else:
            self.calc.state = CalculatorState.NORMAL
        self.update_display()
        
    def btn_inv(self):
        """INV Taste - Aktiviert Inverse Funktionen"""
        if self.calc.state == CalculatorState.NORMAL:
            self.calc.state = CalculatorState.INV
        elif self.calc.state == CalculatorState.SECOND:
            self.calc.state = CalculatorState.SECOND_INV
        else:
            self.calc.state = CalculatorState.NORMAL
        self.update_display()
        
    def btn_on_clear(self):
        """ON/C Taste"""
        self.calc.clear_entry()
        self.calc.state = CalculatorState.NORMAL
        self.awaiting_memory_number = None
        self.update_display()
    
    def btn_off(self):
        """OFF - Speichert und beendet"""
        self.calc.save_state(str(self.state_file))
        self.root.destroy()
        
    def btn_drg(self):
        """DRG - Wechselt Winkelmodus oder DRG> (2nd)"""
        self.calc.toggle_drg()
        if self.calc.state == CalculatorState.SECOND or self.calc.state == CalculatorState.SECOND_INV:
            self.reset_state()
        self.update_display()
        
    def btn_exchange_t(self):
        """x↔t oder C.t (2nd)"""
        if self.calc.state == CalculatorState.SECOND or self.calc.state == CalculatorState.SECOND_INV:
            # C.t - Clear t-register
            self.calc.t_register = 0.0
            self.reset_state()
        else:
            self.calc.exchange_t()
        self.update_display()
        
    def btn_ee(self):
        """EE - Scientific Notation oder Fix (2nd)"""
        if self.calc.state == CalculatorState.SECOND or self.calc.state == CalculatorState.SECOND_INV:
            # Fix - Fixed decimal mode (vereinfacht)
            self.reset_state()
        else:
            # EE - Scientific Notation
            try:
                current = self.calc.get_display_value()
                self.calc.pending_operation = lambda a, b: a * (10 ** b)
                self.calc.pending_value = current
                self.calc.entering_number = False
            except:
                pass
        self.update_display()
        
    def btn_paren_open(self):
        """( oder Intg (2nd)"""
        if self.calc.state == CalculatorState.SECOND or self.calc.state == CalculatorState.SECOND_INV:
            # Intg - Integer part
            value = self.calc.get_display_value()
            self.calc.set_display_value(int(value))
            self.reset_state()
        else:
            # Klammer - vereinfacht
            pass
        self.update_display()
        
    def btn_paren_close(self):
        """) oder Frac (2nd)"""
        if self.calc.state == CalculatorState.SECOND or self.calc.state == CalculatorState.SECOND_INV:
            # Frac - Fractional part
            value = self.calc.get_display_value()
            self.calc.set_display_value(value - int(value))
            self.reset_state()
        else:
            # Klammer - vereinfacht
            pass
        self.update_display()
        
    def btn_sto(self):
        """STO - Speichern oder part (2nd)"""
        if self.calc.state == CalculatorState.SECOND or self.calc.state == CalculatorState.SECOND_INV:
            # part - Partition (Statistics, vereinfacht)
            self.reset_state()
        else:
            self.awaiting_memory_number = self.calc.store
        self.update_display()
        
    def btn_rcl(self):
        """RCL - Abrufen oder CM (2nd)"""
        if self.calc.state == CalculatorState.SECOND or self.calc.state == CalculatorState.SECOND_INV:
            # CM - Clear Memory
            self.calc.clear_memory()
            self.reset_state()
        else:
            self.awaiting_memory_number = self.calc.recall
        self.update_display()
        
    def btn_exc(self):
        """EXC - Exchange oder CP (2nd)"""
        if self.calc.state == CalculatorState.SECOND or self.calc.state == CalculatorState.SECOND_INV:
            # CP - Clear Program
            self.calc.program = []
            self.calc.program_counter = 0
            self.reset_state()
        else:
            self.awaiting_memory_number = self.calc.exchange_memory
        self.update_display()
        
    def btn_run_stop(self):
        """R/S - Run/Stop"""
        self.calc.run_stop()
        self.update_display()
        
    def btn_rst(self):
        """RST - Reset oder x=t (2nd)"""
        if self.calc.state == CalculatorState.SECOND or self.calc.state == CalculatorState.SECOND_INV:
            # x=t - Test if x equals t
            if self.calc.get_display_value() == self.calc.t_register:
                if self.calc.running_program:
                    self.calc.program_counter += 1
            self.reset_state()
        else:
            self.calc.reset_program()
        self.update_display()
        
    def btn_gto(self):
        """GTO - Go To oder x≥t (2nd)"""
        if self.calc.state == CalculatorState.SECOND or self.calc.state == CalculatorState.SECOND_INV:
            # x≥t - Test if x >= t
            if self.calc.get_display_value() >= self.calc.t_register:
                if self.calc.running_program:
                    self.calc.program_counter += 1
            self.reset_state()
        else:
            # GTO - Go to step (vereinfacht)
            pass
        self.update_display()
        
    def btn_lbl(self):
        """LBL - Label oder SBR (2nd)"""
        if self.calc.state == CalculatorState.SECOND or self.calc.state == CalculatorState.SECOND_INV:
            # SBR - Subroutine
            self.calc.subroutine()
            self.reset_state()
        else:
            # LBL - Label (vereinfacht)
            pass
        self.update_display()
        
    def btn_bst(self):
        """BST - Backstep oder Dsz (2nd)"""
        if self.calc.state == CalculatorState.SECOND or self.calc.state == CalculatorState.SECOND_INV:
            # Dsz - Decrement and skip if zero
            self.calc.decrement_and_skip()
            self.reset_state()
        else:
            # BST - Backstep (program counter -1)
            if self.calc.program_counter > 0:
                self.calc.program_counter -= 1
        self.update_display()
        
    def btn_sst(self):
        """SST - Single Step oder Del (2nd)"""
        if self.calc.state == CalculatorState.SECOND or self.calc.state == CalculatorState.SECOND_INV:
            # Del - Delete step
            self.calc.delete_step()
            self.reset_state()
        else:
            # SST - Single step
            self.calc.step_program()
        self.update_display()
        
    def btn_lrn(self):
        """LRN - Learn mode oder Pause (2nd)"""
        if self.calc.state == CalculatorState.SECOND or self.calc.state == CalculatorState.SECOND_INV:
            # Pause - Pause program execution
            self.calc.running_program = False
            self.reset_state()
        else:
            # LRN - Learn mode
            self.calc.learn_mode()
        self.update_display()
        
    def reset_state(self):
        """Setzt 2nd/INV Status zurück"""
        self.calc.state = CalculatorState.NORMAL
        
    def show_context_menu(self, event):
        """Zeigt das Kontextmenü beim Rechtsklick auf das Display"""
        context_menu = tk.Menu(self.root, tearoff=0)
        context_menu.add_command(label="📂 Programm laden...", command=self.load_program_from_file)
        context_menu.add_separator()
        context_menu.add_command(label="ℹ️ Programme anzeigen", command=self.show_programs_info)
        
        try:
            context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            context_menu.grab_release()
    
    def load_program_from_file(self):
        """Öffnet einen Dateiselector zum Laden von Programmen"""
        # Bestimme Programm-Ordner
        current_dir = Path(__file__).parent
        programs_dir = current_dir / "programs"
        
        if not programs_dir.exists():
            messagebox.showwarning("Programm-Ordner nicht gefunden", 
                                   "Der 'programs' Ordner existiert nicht.")
            return
        
        # Dateiselector
        file_path = filedialog.askopenfilename(
            initialdir=programs_dir,
            title="Wähle ein Programm zum Laden",
            filetypes=[("JSON Programme", "*.json"), ("Alle Dateien", "*.*")]
        )
        
        if not file_path:
            return  # Benutzer hat abgebrochen
        
        try:
            # Lade die Programm-Datei
            with open(file_path, 'r', encoding='utf-8') as f:
                program_data = json.load(f)
            
            # Kopiere die Programm-Datei zur ti57_state.json
            shutil.copy(file_path, self.state_file)
            
            # Lade den neuen Zustand
            self.calc.load_state(str(self.state_file))
            
            program_name = Path(file_path).stem
            messagebox.showinfo("Erfolg", 
                               f"Programm '{program_name}' erfolgreich geladen!\n\n"
                               f"Schritte: {len(self.calc.program)}")
            
            self.update_display()
            
        except json.JSONDecodeError:
            messagebox.showerror("Fehler", "Die ausgewählte Datei ist kein gültiges JSON-Programm.")
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Laden des Programms:\n{str(e)}")
    
    def show_programs_info(self):
        """Zeigt verfügbare Programme an"""
        current_dir = Path(__file__).parent
        programs_dir = current_dir / "programs"
        
        if not programs_dir.exists():
            messagebox.showinfo("Programme", "Der 'programs' Ordner wurde nicht gefunden.")
            return
        
        json_files = list(programs_dir.glob("*.json"))
        
        if not json_files:
            messagebox.showinfo("Programme", 
                               "Keine Programme im 'programs' Ordner gefunden.")
            return
        
        msg = "📋 Verfügbare Programme:\n\n"
        for i, f in enumerate(json_files, 1):
            msg += f"• {f.stem}.json\n"
        
        msg += "\n💡 Tipp: Rechtsklick auf das Display → 'Programm laden...'"
        messagebox.showinfo("Verfügbare Programme", msg)
        

    def update_display(self):
        """Aktualisiert das Display und die Indikatoren"""
        self.display_var.set(self.calc.display)
        
        # Update Indikatoren
        if self.calc.state == CalculatorState.SECOND or self.calc.state == CalculatorState.SECOND_INV:
            self.indicator_2nd.config(fg='#e67e22')
        else:
            self.indicator_2nd.config(fg='#7f8c8d')
            
        if self.calc.state == CalculatorState.INV or self.calc.state == CalculatorState.SECOND_INV:
            self.indicator_inv.config(fg='#e67e22')
        else:
            self.indicator_inv.config(fg='#7f8c8d')
            
        # DRG Indikator
        if self.calc.angle_mode == AngleMode.DEG:
            self.indicator_drg.config(text="DEG")
        elif self.calc.angle_mode == AngleMode.RAD:
            self.indicator_drg.config(text="RAD")
        else:
            self.indicator_drg.config(text="GRAD")
            
        # Programmier-Modus
        if self.calc.programming_mode:
            self.indicator_pgm.config(text="PGM", fg='#27ae60')
        else:
            self.indicator_pgm.config(text="", fg='#7f8c8d')


def main():
    """Hauptfunktion"""
    root = tk.Tk()
    app = TI57GUI(root)
    
    # Window-Icon und Titel
    root.title("TI-57 II Programmable Calculator")
    
    # Speichern beim Beenden
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    
    # Keyboard Shortcuts
    def on_key_press(event):
        key = event.char
        if key.isdigit():
            app.btn_digit(key)
        elif key == '.':
            app.btn_decimal()
        elif key == '+':
            app.btn_add()
        elif key == '-':
            app.btn_subtract()
        elif key == '*':
            app.btn_multiply()
        elif key == '/' or key == '÷':
            app.calc.divide()
            app.update_display()
        elif key in ['=', '\r']:
            app.btn_equals()
        elif event.keysym == 'Escape':
            app.btn_on_clear()
        elif event.keysym == 'BackSpace':
            app.btn_on_clear()
            
    root.bind('<Key>', on_key_press)
    
    root.mainloop()


if __name__ == "__main__":
    main()
