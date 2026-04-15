"""Mini-Projekt
Ihr sollt selbst eine Klasse bauen, die:
- Daten lädt
- Leistung berechnet
- Mittelwerte ausgibt
- einen Plot erstellt
- optional eine Animation zeigt

Messdaten eines elektrischen Systems sollen strukturiert verarbeitet werden.
Die Daten sollen geladen, analysiert und visualisiert werden.
Dafür wird eine Klasse verwendet, die Daten und zugehörige Methoden zusammenfasst.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from scipy import signal

class MeasurementAnalyzer:
    """Diese Klasse kapselt Messdaten und typische Auswertungen

    Parameter - filename: Name der CSV-Datei
    """
    def __init__(self, filename):
        # Daten laden
        self.filename = filename
        self.data = np.loadtxt(filename, delimiter=",", skiprows=1)
        # Spalten der Datenmatrix extrahieren
        self.time = self.data[:, 0]
        self.voltage = self.data[:, 1]
        self.current = self.data[:, 2]

    def compute_power(self):
        """Berechnet die elektrische Leistung

        Returns:
            Array mit Leistungswerte
        """
        return self.voltage * self.current

    def average_voltage(self):
        return np.mean(self.voltage)

    def average_current(self):
        return np.mean(self.current)

    def average_power(self):
        return np.mean(self.compute_power())

    def filter_voltage(self):
        """Filtert die Spannung mit einem Butterworth-Tiefpass
        mit signal.butter(), signal.filtfilt()

        Return Wert:
        Array mit gefilterten Spannungswerten
        """ 

        dt = self.time[1] - self.time[0]
        # Abtastfrequenz
        fs = 1 / dt

        b, a = signal.butter(4, 1.0, btype="low", fs=fs)
        filtered_voltage = signal.filtfilt(b, a, self.voltage)

        return filtered_voltage

    def plot_voltage(self):
        """Erstellt einen Plot der Spannung über der Zeit"""
        plt.figure()
        plt.plot(self.time, self.voltage, label="Voltage")
        plt.xlabel("Time [s]")
        plt.ylabel("Voltage [V]")
        plt.title("Spannung über der Zeit")
        plt.legend()
        plt.grid()
        plt.show()
    
    def plot_power(self):
        """Erstellt einen Plot der Leistung über der Zeit
        """
        power = self.compute_power()

        plt.figure()
        plt.plot(self.time, power, label="Power")
        plt.xlabel("Time [s]")
        plt.ylabel("Power [W]")
        plt.title("Leistung über der Zeit")
        plt.legend()
        plt.grid()
        plt.show()

    def animate_voltage(self):
        """Erstellt eine Animation der Spannung über der Zeit
        """
        fig, ax = plt.subplots()
        line, = ax.plot([], [])

        ax.set_xlim(np.min(self.time), np.max(self.voltage))
        ax.set_ylim(np.min(self.voltage) - 0.2, np.max(self.voltage) + 0.2)

        def update(frame):
            """Aktualisiert die Linie bis zum aktuellen Frame"""
            line.set_data(self.time[:frame], self.voltage[:frame])
            return line,

        ani = FuncAnimation(
            fig,
            update,
            frames=len(self.time),
            interval=50
        )

        plt.xlabel("Time [s]")
        plt.ylabel("Voltage [V]")
        plt.title("Animierte Spannung")
        plt.grid()
        plt.show()

    def export_data(self, output_filename):
        """Exportiert verarbeitete Daten in eine neue CSV-Datei

        Gespeichert werden:
        - time
        - voltage
        - current
        - power
        - filtered_voltage

        Parameter:
            output_filename: Name der Output Datei.
        """
        power = self.compute_power()
        filtered_voltage = self.filter_voltage()

        # Spalten zu einer Matrix zusammenfügen
        output_data = np.column_stack((
            self.time,
            self.voltage,
            self.current,
            power,
            filtered_voltage
        ))

        np.savetxt(
            output_filename,
            output_data,
            delimiter=",",
            header="time,voltage,current,power,filtered_voltage",
            comments=""
        )

# Test
import os
file_path = os.path.join(os.path.dirname(__file__), "measurement.csv")

print(file_path)
analyzer = MeasurementAnalyzer(file_path)

print("Mittlere Spannung:", analyzer.average_voltage)
print("Mittlerer Strom:", analyzer.average_current())
print("Mittlere Leistung:", analyzer.average_power())

output_filepath = os.path.join(os.path.dirname(__file__), "output_2.csv")
analyzer.export_data(output_filepath)


# analyzer.plot_voltage()
analyzer.animate_voltage()

class SensorAnalyzer(MeasurementAnalyzer):
    def laser_reinigung(self):
        pass

    def druck_mittelwert(self):
        pass


# sensor_analyzer = SensorAnalyzer(file_path)

# class MotorAnalyzer(MeasurementAnalyzer):
#     pass

# class WeatherAnalyzer(MeasurementAnalyzer):
#     pass

