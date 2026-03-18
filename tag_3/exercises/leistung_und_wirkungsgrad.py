# Ausgangssituation:
# Ein Gleichstrommotor wird bei verschiedenen Betriebspunkten untersucht.
# Es liegen Eingangsspannung, Eingangsstrom und abgegebene mechanische Leistung vor.
# Ziel ist es, elektrische Leistung und Wirkungsgrad zu berechnen und 
# grafisch darzustellen.

import numpy as np
import matplotlib.pyplot as plt

# Messdaten des Motors.
voltage_V = np.array([12, 12, 12, 12, 12], dtype=float)
current_A = np.array([0.8, 1.2, 1.8, 2.4, 3.0], dtype=float)
mechanical_power_W = np.array([6.5, 10.0, 14.8, 18.5, 21.0], dtype=float)

# Berechnung der elektrischen Eingangsleistung für jeden Betriebspunkt.
electrical_power_W = voltage_V * current_A

# Berechnung des Wirkungsgrades als Verhältnis von abgegebener zu aufgenommener Leistung.
efficiency = mechanical_power_W / electrical_power_W

# Bestimmung des Index des maximalen Wirkungsgrades.
best_index = np.argmax(efficiency)

# Grafische Darstellung des Wirkungsgrades über dem Motorstrom.

# Einfache Darstellung
plt.figure()
plt.plot(current_A, efficiency, marker="s")
plt.xlabel("Strom I in A")
plt.ylabel("Wirkungsgrad eta")
plt.title("Wirkungsgrad eines Gleichstrommotors")
plt.grid(True)
plt.show()

# Mit fig und ax

# fig, ax = plt.subplots(figsize=(8, 4))

# ax.plot(current_A, efficiency, marker="s")

# ax.set_xlabel("Strom [A]", fontsize=12)
# ax.set_ylabel("Wirkungsgrad", fontsize=12)
# ax.annotate("Bester Wirkungsgrad",
#             xy=(current_A[best_index], efficiency[best_index]),
#             xytext=(current_A[best_index], efficiency[best_index]),
#             arrowprops=dict(arrowstyle="->"))

plt.show()