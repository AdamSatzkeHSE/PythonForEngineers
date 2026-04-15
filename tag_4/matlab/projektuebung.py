"""
Ein verrauschtes Sensorsignal soll gefiltert und animiert dargestellt werden (Anfangszustand)
Dieses Signal wollen wir mit einem Butterworth Tiefpassfilter filtern.
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