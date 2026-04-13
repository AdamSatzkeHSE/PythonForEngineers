"""
Animation eines verrauschten Signals.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Zufallszahlen-Generator
rng = np.random.default_rng(0)

# Zeitachse
t = np.linspace(0, 10, 100)

# Signal
signal = np.sin(t)

# Rauschen hinzufügen
# rng.normal erzeugt normalverteiltes Rauschen
noise = rng.normal(0, 0.2, len(t))

signal_noisy = signal + noise

fig, ax = plt.subplots()
line, = ax.plot([], [])

ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)

def update(frame):
    line.set_data(t[:frame], signal_noisy[:frame])
    return line,

ani = FuncAnimation(fig, update, frames=len(t), interval=50)

plt.show()