"""
Ausgangssituation:
Ein kleines Messprogramm soll Spannung und Strom verarbeiten.
Die Berechnung der Leistung und die Spannungsprüfung sollen
nicht direkt im Hauptprogramm stehen, sondern aus eigenen Modulen
importiert werden.
"""

# Importiere hier die benötigten Funktionen
# Version 1 mit Modulen im selben Ordner
# import checks as checker
# import calculations as cl

# voltage = 5.2
# current = 0.3

# print("---- Programm wird ausgeführt ----")
# print("Leistungsberechnung...")

# # Berechne hier die Leistung
# power = cl.get_power(voltage, current)
# print(f"Die Leistung beträgt {power:.2f} W")
# # Prüfe hier die Spannung
# print("Spannung wird geprüft...")
# print(checker.check_voltage(voltage))
# # Gib hier alle Ergebnisse aus

# Version 2

""" Imports """
import random
import modules.calculations as calc
import modules.checks as ch
import modules.conversions as conv
import modules.statistics as stat
import numpy as np

""" Tests """
# voltages = [3.3, 12, 24, 220, 400, 500, 600]
# List comprehensions - die Einzeiler. 
# Zufallswerte erzeugen.
voltages = [round(random.uniform(3.3, 400), 2) for i in range(5)]
# [output for i in iterable]

voltages = []
for i in range(5):
    # result = round...
    voltages.append(random.uniform(3.3, 400))

print(voltages)

current = 0.5

print("---- Programmstart ----")
print(f"Folgende Spannungen werden geprüft: {voltages}")
print(f"Mittelwert: {stat.get_mean(voltages)}")
print(f"Maximalwert (meine Version): {stat.get_max(voltages)}")
print(f"Maximalwert (numpy): {np.max(voltages)}")

print(f"Minima: {stat.get_min(voltages)}")

for voltage in voltages:
    power = calc.get_power(voltage, current)
    print(f"Die Leistung für {voltage} V beträgt {power:.2f} W")
    print("Spannung wird geprüft...")
    print(ch.check_voltage(voltage))
    print()

    # test conversions.py
    print(f"Spannung in mV: {conv.convert_mV(voltage)}")
    print(f"Strom in mA: {conv.convert_mA(current)}")
    print(f"Leistung in mW: {conv.convert_mW(power)}")
    print()

# pip: "pip installs packages"




