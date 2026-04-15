"""
Ein verrauschtes Sensorsignal (Sinus) soll gefiltert und animiert dargestellt werden (Anfangszustand)

Dieses Sinus-Signal wollen wir mit einem Butterworth Tiefpassfilter filtern.
Nutze dafür das scipy modul
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy import signal

# 1. Zeitachse erzeugen
# 2. Nutzsignal erzeugen
# 3. Rauschen hinzufügen
# 4. Tiefpassfilter mit scipy entwerfen
# 5. Signal filtern
# 6. Plot vorbereiten
#    - Zwei leere Linien erzeugen
#    - Achsen konfigurieren
# 7. Update Funktion schreiben
# 8. Animation erzeugen

# signal.butter(): Erzeugt ein voreingestellten Butterworth-Filter
# Parameter:
# - Filterordnung, Grenzfrequenz, type, Abtastfrequenz
# t = zeitvektor
# fs = len(t) / (t[-1] - t[0])
# b, a = signal.butter(4, 1.0, bytype="low", fs=fs)  # b und a sind die Filterkoeffizienten.

# Zum Filtern mit scipy:
# filtered_signal = signal.filtfilt(b, a, rauschsignal) # rauschsignal sollt ihr selbst berechnen und eingeben.

# 1. Zeitachse erzeugen
t = np.linspace(0, 10, 500)

# 2. Nutzsignal erzeugen
clean_signal = np.sin(t)

# 3. Rauschen hinzufügen
rng = np.random.default_rng(0)
noise = rng.normal(0, 0.4, len(t))

# Verrauschtes Signal
noisy_signal = clean_signal + noise

# 4. Tiefpassfilter mit scipy entwerfen
# signal.butter() erzeugt die Koeffizienten eines Butterworth-Filters.
# Parameter:
# - 4: Filterordnung
# - 1.0: Grenzfrequenz
# - btype="low": Tiefpass
# - fs=..: Abtastfrequenz

fs = len(t) / (t[-1] - t[0])
b, a = signal.butter(4, 1.0, btype="low", fs=fs)

# 5. Signal filtern
# signal.filtfilt() filtert.
filtered_signal = signal.filtfilt(b, a, noisy_signal)

# 6. Plot vorbereiten
fig, ax = plt.subplots()

# Zwei leere Linien erzeugen:
# Eine für das verrauschte Signal
# Eine für das gefilterte Signal
line_noisy, = ax.plot([], [], label="Verrauschtes Signal")
line_filtered, = ax.plot([], [], label="Gefiltertes Signal")

# Achsen konfigurieren
ax.set_xlim(t[0], t[-1])
ax.set_ylim(-2, 2)
ax.set_xlabel("Zeit [s]")
ax.set_ylabel("Amplitude")
ax.set_title("Animierte Signalfilterung")
ax.legend()
ax.grid(linestyle="--")

# Initialisierungsfunktion
def init_signals():
    line_noisy.set_data([], [])
    line_filtered.set_data([], [])
    
    return line_noisy, line_filtered

# Updatefunktion
def update(frame):
    line_noisy.set_data(t[:frame], noisy_signal[:frame])
    line_filtered.set_data(t[:frame], filtered_signal[:frame])

    return line_noisy, line_filtered # Return, welche Objekten wurden geändert? -- Infos für FuncAnimation

# 7. Animation erzeugen
ani = FuncAnimation(
    fig,
    update, 
    frames=len(t),
    init_func=init_signals,
    interval=20
)

plt.show()
