"""
Animation einer RC-Entladung.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameter
U0 = 5.0       # Anfangsspannung
tau = 2.0      # Zeitkonstante

# Zeitachse
t = np.linspace(0, 10, 100)

# np.exp berechnet die Exponentialfunktion
U = U0 * np.exp(-t / tau)

fig, ax = plt.subplots()
line, = ax.plot([], [])

ax.set_xlim(0, 10)
ax.set_ylim(0, 5)

def update(frame):
    line.set_data(t[:frame], U[:frame])
    return line,

ani = FuncAnimation(fig, update, frames=len(t), interval=50)

plt.xlabel("Zeit (s)")
plt.ylabel("Spannung (V)")
plt.title("RC-Entladung")

plt.show()