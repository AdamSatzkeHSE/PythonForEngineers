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
fig, ax = plt.subplots()

print(type(ax))

ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)

ax.set_title("U(t) mit und ohne Rauschen")
ax.set_xlabel("Zeit [s]")
ax.set_ylabel("Spannung [V]")

line1, = ax.plot([], [], label="Ohne Rauschen")
line2, = ax.plot([], [], label="Mit Rauschen")

# Legende (Voraussetzung ax.plot())
ax.legend()
# Hintergrundsfarbe
ax.set_facecolor("#c78c8c")
# Grid
ax.grid(True, linestyle="--", alpha=0.5)
# Automatische Aufteilung
fig.tight_layout()
# Linien hervorheben
ax.axhline(y=max(signal), color="black")
ax.axvline(4, color="blue")

def update(frame):
    line1.set_data(t[:frame], signal[:frame])
    line2.set_data(t[:frame], signal_rauschen[:frame])

    # update braucht ein Rueckgabewert
    return line1, line2

ani = FuncAnimation(
    fig,
    update,
    frames=len(t),
    interval=50
)

plt.show()