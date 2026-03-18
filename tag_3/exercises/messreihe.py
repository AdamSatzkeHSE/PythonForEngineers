""" Ausgangssituation

In einem Laborversuch wurde der Strom durch einen Widerstand bei verschiedenen Spannungen
gemessen. Die Werte wurde bereits in Arrays eingetragen. Ziel ist es, die Messwerte mit numpy zu analysieren,
den Widerstand zu berechnen und die Kennlinie mit matplotlib darzustellen.
"""
import numpy as np
import matplotlib.pyplot as plt

voltages = [0, 1, 2, 3, 4, 5]
currents_mA = [0, 9.8, 20.1, 29.7, 40.5, 49.8]

# Aufgabe 1:
# Wandle den Strom von mA in A um
voltages_np = np.array(voltages)
currents_np = np.array(currents_mA) / 1000

# Aufgabe 2:
# Berechne für alle Punkte mit Strom > 0 den Widerstand R = U / I
# Auswahl aller Punkte, bei denen der Strom ungleich null ist.
filtered = currents_np > 0 # Bedingung
print("Gefilterte Stromwerte:", currents_np[filtered])

# Aufgabe 3:
# Bestimme den mittleren Widerstand in Ohm
# Berechnung des Widerstands pro Messpunkt
resistances = voltages_np[filtered] / currents_np[filtered]
resistances = voltages_np[currents_np > 0] / currents_np[currents_np > 0]
r_mittelwert = np.mean(resistances)


# Aufgabe 4:
# Erzeuge ein Diagramm Strom vs. Spannung
plt.figure()
plt.plot(voltages_np, currents_np, marker="o")
plt.xlabel("Spannung [V]")
plt.ylabel("Strom [A]")
plt.title("I-U Kennlinie")
plt.grid(True)
plt.show()
