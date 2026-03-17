# Built-In Module in Python
import random
import math
import os       # Ressourcen Zur Systemverwaltung, Dateien usw.
import sys

for path in sys.path:
    print(path)

# Mein erstelltes Modul calc.py importieren
import tag_2.module.calc as calc

print(random.choice([1, 2, 3, 4, 5]))
print(random.choice([1, 2, 3, 4, 5]))
print(random.choice([1, 2, 3, 4, 5]))

print(random.randrange(1, 100))

print(math.sqrt(2))
print(round(math.sqrt(3), 3))
print(math.pi)

# Modul calc verwenden.
print(calc.addieren(3, 4))
print(calc.product(2, 2))
print(calc.division(9, 3))

# Konkretes import
from tag_2.module.calc import addieren, division

# calc.addieren() X --> addieren(): Ich wähle, unter welchen Namen die Operation
# ausgeführt werden soll, und das nur addieren() benutzt wird.
print(addieren(2, 2))
print(division(3, 4))

# Wildcard import -> Nicht best practice
from tag_2.module.calc import *
# addieren, division, product, durchschnitt, power, exp kenne ich nicht immer...

# Import mit alias
# import numpy as np
# import scipy as sci
# import matplot.matplotlib as plt

from tag_2.module.calc import addieren as adi

# Module aus Verzeichnes (Paket)
from module import calc
from module import statistic

print(calc.addieren(2, 2))
print(calc.division(4, 5))

print(statistic.mean([1, 2, 3]))

from module.calc import addieren

print(addieren(2, 2))
