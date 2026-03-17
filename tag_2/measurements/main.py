"""
Ausgangssituation:
Ein kleines Messprogramm soll Spannung und Strom verarbeiten.
Die Berechnung der Leistung und die Spannungsprüfung sollen
nicht direkt im Hauptprogramm stehen, sondern aus eigenen Modulen
importiert werden.
"""

# Importiere hier die benötigten Funktionen
import checks as checker
import calculations as cl

voltage = 5.2
current = 0.3

print("---- Programm wird ausgeführt ----")
print("Leistungsberechnung...")

# Berechne hier die Leistung
power = cl.get_power(voltage, current)
print(f"Die Leistung beträgt {power:.2f} W")
# Prüfe hier die Spannung
print("Spannung wird geprüft...")
print(checker.check_voltage(voltage))
# Gib hier alle Ergebnisse aus