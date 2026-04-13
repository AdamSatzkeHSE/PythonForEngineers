import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = np.linspace(0, 10, 100)
signal = np.sin(t)

fig, ax = plt.subplots()
line, = ax.plot([], [])

ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)

def update(frame):
    line.set_data(t[:frame], signal[:frame])
    return line,

ani = FuncAnimation(fig, update, frames=len(t), interval=50)

plt.show()