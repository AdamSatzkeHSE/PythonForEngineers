""" Ausgangssituation

In einem Laborversuch wurde der Strom durch einen Widerstand bei verschiedenen Spannungen
gemessen. Die Werte wurde bereits in Arrays eingetragen. Ziel ist es, die Messwerte mit numpy zu analysieren,
den Widerstand zu berechnen und die Kennlinie mit matplotlib darzustellen.
"""

import numpy as np
import matplotlib.pyplot as plt

voltages = [0, 1, 2, 3, 4, 5]
currents_mA = [0, 9.8, 20.1, 29.7, 40.5, 49.8]

# Aufgabe 1
# Wandle den Strom von mA in A um

# Aufgabe 2
# Berechne für alle Punkte mit Strom > 0 den Widerstand R = U / I

# Aufgabe 3:
# Bestimme den mittleren Widerstand in Ohm

# Aufgabe 4:
# Erzeuge ein Diagramm Strom vs. Spannung
