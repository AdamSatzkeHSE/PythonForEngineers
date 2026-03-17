"""
Ausgangssituation:
Dieses Modul enthält Prüf-Funktionen für Messwerte.
Hier soll eine Funktion erstellt werden, die einen Spannungswert
bewertet und eine passende Meldung zurückgibt.
"""
#   - Spannung zu niedrig zurückgeben, wenn voltage < 4.5
#   - Spannung im Normalbereich, wenn 4.5 <= voltage <= 5.5
#   - Spannung zu hoch, wenn voltage > 5.5
# Schreibe hier deine Funktion
def check_voltage(voltage):
    if voltage < 4.5:
        return "Spannung zu niedrig"
    
    elif 4.5 <= voltage <= 5.5:
        return "Spannung im Normalbereich"
    else:
        return "Spannung zu hoch"

# Für die Zukunft.
def check_current(current):
    pass

def check_power(power):
    pass

