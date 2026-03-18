# Ausgangssituation:
# Ein Gleichstrommotor wird bei verschiedenen Betriebspunkten untersucht.
# Es liegen Eingangsspannung, Eingangsstrom und abgegebene mechanische Leistung vor.
# Ziel ist es, elektrische Leistung und Wirkungsgrad zu berechnen und grafisch darzustellen.

import numpy as np
import matplotlib.pyplot as plt


# Hallo das ist ein Kommentar


# Messdaten des Motors.
voltage_V = np.array([12, 12, 12, 12, 12], dtype=float)
current_A = np.array([0.8, 1.2, 1.8, 2.4, 3.0], dtype=float)

# Aufgabe 1:
# Berechne die elektrische Eingangsleistung P_el = U * I.


# Aufgabe 2:
# Berechne den Wirkungsgrad eta = P_mech / P_el.

# Aufgabe 3:
# Finde den Betriebspunkt mit dem höchsten Wirkungsgrad.

# Aufgabe 4:
# Stelle den Wirkungsgrad über dem Strom dar.

fig = plt.figure()