#script scale.py
#!/usr/bin/python3
"""
Auteur: Vianney Adou
date: 9 /Nov/ 2014
Version: 0.0.1
Licence: GPL2
"""

from tkinter import *
""" BKM couleur est une apllication pour les webmasters
   BKM couleur produit les codes de couleurs en hexadecimal """

rougeb ="00"
vertb ="00"
bleub ="00"

#decodeur hexadecimale sur deux digits
def decode(valeur):
    # nouvelle valeur en argument
    if((valeur%16)==10):
        result = "A"
    elif((valeur%16)==11):
        result = "B"
    elif((valeur%16)==12):
        result = "C"
    elif((valeur%16)==13):
        result = "D"
    elif((valeur%16)==14):
        result = "E"
    elif((valeur%16)==15):
        result = "F"
    else:
        result =str(valeur%16)
    return result

def maj(valeur):
    conver = []
    #permet le decodage sur deux digits
    conver.append(decode(valeur))
    valeur //= 16
    conver.append(decode(valeur))
    var = conver[1]+conver[0]
    return var


#fonction pour la gestion des modificateurs (Scale)
def coderouge(rouge):
    global vertb
    global bleub
    global rougeb
    rougeb = maj(int(rouge))
    cod.set("#"+rougeb+vertb+bleub)
    couleur["bg"]=str(cod.get())

def codevert(vert):
    global rougeb
    global bleub
    global vertb
    vertb  = maj(int(vert))
    cod.set("#"+rougeb+vertb+bleub)
    couleur["bg"]=str(cod.get())


def codebleu(bleu):
    global rougeb
    global vertb
    global bleub
    global codCouleur
    bleub  = maj(int(bleu))
    cod.set("#"+rougeb+vertb+bleub)
    couleur["bg"]=str(cod.get())

#cration de la fenetre principale (main window)

Mafenetre = Tk()
Mafenetre.title("BKM couleur")

rouge, vert, bleu = StringVar(), StringVar(), StringVar()
rouge.set(0)
vert.set(0)
bleu.set(0)

#creatrion de 3 widgets scale

Srouge = Scale(Mafenetre, from_ = 0, to=255, resolution=1, orient=HORIZONTAL, length=300, width=10, label='Rouge', variable=rouge, command=coderouge)
Srouge.grid(row=0, column=0)

Svert = Scale(Mafenetre, from_ = 0, to=255, resolution=1, orient=HORIZONTAL, length=300, width=10, label='Vert', variable=vert, command=codevert)
Svert.grid(row=1, column=0)

Sbleu = Scale(Mafenetre, from_ = 0, to=255, resolution=1, orient=HORIZONTAL, length=300, width=10, label='Bleu',  variable=bleu, command=codebleu)
Sbleu.grid(row=2, column=0)

#Creation du canvas pour la couleur
couleur = Canvas(Mafenetre, width=100, height=100)
couleur.grid(row=0, column=1, rowspan=2)

#ceation du label pour le code
cod = StringVar()
code = Entry(Mafenetre, textvariable=cod ,width=10, bg="white")

code.grid(row=2, column=1)
Mafenetre.mainloop()
