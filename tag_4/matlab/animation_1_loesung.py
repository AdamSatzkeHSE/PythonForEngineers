"""
Animation eines wachsenden Signals.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# np.linspace erzeugt 100 Werte zwischen 0 und 10
t = np.linspace(0, 10, 100)

# np.sin berechnet den Sinus für jeden Wert
signal = np.sin(t)

# Figur und Achse erstellen
fig, ax = plt.subplots()

# Leere Linie erstellen
line, = ax.plot([], [])

# Achsenbegrenzung setzen
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)

# Update-Funktion wird für jeden Frame aufgerufen
def update(frame):
    # Daten bis zum aktuellen Frame anzeigen
    x = t[:frame]
    y = signal[:frame]

    # Linie aktualisieren
    line.set_data(x, y)

    return line,

# FuncAnimation steuert die Animation
ani = FuncAnimation(
    fig,
    update,
    frames=len(t),
    interval=50
)

plt.show()