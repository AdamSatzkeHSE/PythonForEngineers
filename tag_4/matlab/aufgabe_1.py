"""
Ein Sensorsignal soll nicht sofort komplett angezeigt werden,
sondern sich Schritt für Schritt über die Zeit aufbauen.

Aufgabe:
1. Erzeuge ein Sinussignal
2. Stelle es animiert dar (wachsender Plot)
"""

# 1. Module importieren
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Anfangsbedingungen
t = np.linspace(0, 10, 100)
signal = np.sin(t)

# Figur und Achse erstellen
fig, ax = plt.subplots()

# Leere Linie erstellen
print(type(ax.plot([], [])))
print(ax.plot([], []))
# line = ax.plot([], [])[0]
# line_tupel = tuple(line)
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