"""
Ausgangssituation:
Ein Kondensator entlädt sich über die Zeit.

Formel:
U(t) = U0 * exp(-t / tau)

Aufgabe:
1. Simuliere die Entladung
2. Stelle sie animiert dar

Erweitert:
Füge Rauschen hinzu
Stelle das verrauschte Signal animiert im selben Plot dar
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Zufallszahlengenerator
rng = np.random.default_rng(0)
print(rng)
print(type(rng))

# Zeitachse
t = np.linspace(0, 10, 100)
# Signal
signal =- np.sin(t)

# Rauschen hinzufügen
# rng.normal erzeugt normalverteiltes Rauschen
noise = rng.normal(0, 0.2, len(t))
signal_rauschen = signal + noise

# Plotten
fig, ax = plt.subplots(2, 1)

print(ax)

ax[0].set_xlim(0, 10)
ax[0].set_ylim(-2, 2)

ax[0].set_title("U(t) ohne Rauschen")
ax[0].set_xlabel("Zeit [s]")
ax[0].set_ylabel("Spannung [V]")

ax[1].set_title("U(t) mit Rauschen")
ax[1].set_xlabel("Zeit [s]")
ax[1].set_ylabel("Spannung [V]")

ax[1].set_xlim(0, 10)
ax[1].set_ylim(-2, 2)

line1, = ax[0].plot([], [], label="Ohne Rauschen")
line2, = ax[1].plot([], [], label="Mit Rauschen")

def update(frame):
    line1.set_data(t[:frame], signal[:frame])
    line2.set_data(t[:frame], signal_rauschen[:frame])

ani = FuncAnimation(
    fig,
    update,
    frames=len(t),
    interval=50
)

plt.show()