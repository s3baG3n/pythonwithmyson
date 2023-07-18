# Hello World in Python mit ein paar zusätzlichen Spielereien
# 20230718
# s3baG

# "Schöne Ausgabe von 'Hello World'"
print("\n\n###############\n# Hello World #\n###############\n")

# Funktion zum Prüfen ob im String (Zeichenkette, hier soll der Name geprüft werden) eine Zahl enthalten ist
def containsNumber(string):
    if (True in [char.isdigit() for char in string]):
        return True
    else:
        return False
    

# Initialisierung der Variable incorrect für die while-Schleifen-Bedingung
# Wert auf True gesetzt, damit die Schleife wenigestens einmal durchlaufen wird
incorrect = True

# while-Schleife zum Prüfen der Eingabe des Vornamens
while (incorrect == True):
    input_name = input("Bitte gebe Deinen Vornamen ein: ")
    incorrect = containsNumber(input_name)
    if (incorrect == True):
        print("\nDas war leider falsch, ein Vorname enthält keine Zahl(en)!\nBitte versuche es erneut...")
    else:
        print("\n\nToll, hallo " + input_name + "!!!")
        print("Fahren wir nun fort mit unserer kleinen Spielerei!\n\n")

# Es wird eine neue Variable initialisiert, um die Prüfung der nächsten Eingabe einzuleiten.
correct = False
while (correct == False):
    input_alter = input("Bitte gebe nun Dein Alter ein: ")

    # mit .isdigit() wird geprüft ob es sich um eine Zahl handelt.
    if (input_alter.isdigit()):
        print("Prima, du bist also " + input_alter + " Jahre alt!\n\nDanke für's mitmachen, bis zum nächsten Mal!!!\n\n")
        correct = True
    else:
        print("\nUiuiuiui...da ging was schief....\nEine Altersangebe darf nur Zahlen enthalten...versuche es erneut!\n\n")
        correct = False

print("#########################################")
print("#####  #   #   ####     #####")
print("#      ##  #   #   #    #")
print("####   # # #   #   #    ####")
print("#      #  ##   #   #    #")
print("#####  #   #   ####     #####")      
print("#########################################")   

