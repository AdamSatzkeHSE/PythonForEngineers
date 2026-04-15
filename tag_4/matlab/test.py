from matplotlib.animation import FuncAnimation
# FuncAnimation: ruft wiederholt eine Update-Funktion auf und aktualisiert den Plot

import numpy as np
import matplotlib.pyplot as plt
from IPython.display import HTML

t = np.linspace(0, 10, 100)

signal = np.sin(t)

# Leere Linie initialisieren


fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)

line, = ax.plot([],[])

# Gibt einen Tupel mit Linie zurück.
def update(frame):
    # Zeigt Singal bis zum aktuellen Zeitpunkt
    x = t[:frame]
    y = signal[:frame]
    # aktualisiert die Linie
    line.set_data(x, y)

    return line, 


ani = FuncAnimation(
    fig,
    update,
    frames=len(t),
    interval=50 # Zeit zwischen Frames in ms
)
HTML(ani.to_jshtml())
plt.show()