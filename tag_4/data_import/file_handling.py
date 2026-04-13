import os

# Wiederholung
# Richtigen Pfad erstellen - Platformunabhängig!
path = os.getcwd()
my_path = os.path.dirname(__file__)
filename = os.path.join(os.path.dirname(__file__), "testfile.txt")

print(path)
print(my_path)

with open("testfile.txt", "w") as file:
    print("testfile created", "path:", os.getcwd())

