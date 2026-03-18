import logging
# Logging in Datei

logging.basicConfig(
    filename="pythonschulung.log",
    level=logging.INFO,
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Programmstart")
logging.warning("Etwas stimmt nicht...")
logging.error("Ein Fehler ist augetreten")
logging.error("Fehler 2")
logging.error("Stromausfall")
logging.error("Jupyter Notebooks spinnt")
logging.info("Programm läuft weiter")

# Logfile auswerten

error_count = 0

# 1. Weg zu filtern.
with open("pythonschulung.log", "r") as f:
    # Zeilen aus logging Datei holen und ausgeben
    for line in f:
        # print(line)
        if "ERROR" in line:
            print(line)

# 2. Weg, fortgeschritten: Das regex Modul.
# import regex

print(error_count)
if error_count > 3:
    print("Zu viele Fehler")