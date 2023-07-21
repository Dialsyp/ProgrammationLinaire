import subprocess

from tkinter import *

choix = Tk()
choix.title("traitement")
choix['bg']='white'
file = open("donnees/variable_contrainte.txt", "r")
v = file.readline()
c = file.readline()
file.close()
column = int(v) + int(c) + 2
row = int(c) + 1
mat = [[0 for j in range(column)] for i in range(row)]
variableentrante = ["e%d" % j for j in range(1, row)]

file2 = open("donnees/variable.txt", "w")
i = 1
case1 = ""
for j in range(0, row - 1):
    file2.write(variableentrante[j] + ';')
file2.close()

filerempliemat = open("donnees/remplissagetableau.txt", "r")
j = 1
h = 0
case = ""
while 1:  # preremplissage
    ligne = filerempliemat.readline()

    for i in range(0, len(ligne)):
        if ligne[i].isnumeric() or ligne[i] == "-":
            case = case + ligne[i]
        if ligne[i] == '\n':
            if h != 0:
                mat[h][column - 1] = int(case)
            else:
                mat[h][j] = int(case)
            case = ""
            h += 1
            j = 1
        if ligne[i] == ';':
            mat[h][j] = int(case)
            case = ""
            j += 1
    if ligne == "":
        break

filerempliemat.close()
i = 1
j = int(v) + 1
k = 1

while i <= int(c):  # variable d'ecart
    mat[k][j] = 1
    j += 1
    k += 1
    i += 1

frameP = Frame(choix)
frameP['bg']='white'
frametitre = Frame(frameP)
Label(choix, text='Programme Lineaire', font=("Times New Roman", 30,'bold'),bg="white").pack(padx=60,pady=10)
frametitre.pack()
framefunction = LabelFrame(frameP, text='function objective', font=("Times New Roman", 19), borderwidth=0)
framefunction['bg']='white'
Label(framefunction, text='Z =', font=("Times New Roman", 15),bg="white").pack(side=LEFT)
for i in range(1, int(v)):
    Label(framefunction, text='%d' % mat[0][i], fg="red", font=("Times New Roman", 15),bg="white").pack(side=LEFT)
    Label(framefunction, text='X%d' % i, font=("Times New Roman", 15),bg="white").pack(side=LEFT)
    Label(framefunction, text='+', font=("Times New Roman", 15),bg="white").pack(side=LEFT)
Label(framefunction, text='%d' % mat[0][i + 1], fg="red", font=("Times New Roman", 15),bg="white").pack(side=LEFT)
Label(framefunction, text='X%s' % str(i + 1), font=("Times New Roman", 15),bg="white").pack(side=LEFT)
framefunction.pack()

frameprogramme = LabelFrame(frameP, text='contrainte', font=("Times New Roman", 20), borderwidth=0,bg="white")
for j in range(1, int(c) + 1):
    framecon = Frame(frameprogramme, name='%d' % j)
    framecon['bg']='white'
    for i in range(1, int(v)):
        Label(framecon, text='%d' % mat[j][i], font=("Times New Roman", 15), fg="red",bg="white").pack(side=LEFT, padx=2)
        Label(framecon, text='X%d' % i, font=("Times New Roman", 15),bg="white").pack(side=LEFT, padx=2)
        Label(framecon, text='+', font=("Times New Roman", 15),bg="white").pack(side=LEFT, padx=2)
    Label(framecon, text='%d' % mat[j][i + 1], font=("Times New Roman", 15), fg="red",bg="white").pack(side=LEFT, padx=2)
    Label(framecon, text='X%s' % str(i + 1), font=("Times New Roman", 15),bg="white").pack(side=LEFT, padx=2)
    Label(framecon, text='<=', font=("Times New Roman", 15),bg="white").pack(side=LEFT, padx=2)
    Label(framecon, text='%d' % mat[j][column - 1], font=("Times New Roman", 15), fg="red",bg="white").pack(side=LEFT, padx=2)
    framecon.pack()
    frameprogramme.pack(pady=10,padx=10)
frameP.pack()


def maxs():
    fileremplie2 = open("donnees/remplissagetableaucomplete.txt", "w")
    for i in range(0, row):
        for j in range(0, column - 1):
            fileremplie2.write(str(mat[i][j]) + ";")
        fileremplie2.write(str(mat[i][j + 1]) + "\n")
    fileremplie2.close()
    choix.destroy()
    subprocess.call(" python PL/Maximisation.py 1", shell=True)
    pass


def mins():
    i = 1
    j = int(v) + 1
    z = 1
    while i <= int(c):  # variable d'ecart
        mat[z][j] = 1
        j += 1
        z += 1
        i += 1
    j = 1
    fileremplie2 = open("donnees/remplissagetableaucomplete.txt", "w")
    for i in range(0, row):
        for j in range(0, column - 1):
            fileremplie2.write(str(mat[i][j]) + ";")
        fileremplie2.write(str(mat[i][j + 1]) + "\n")
    fileremplie2.close()
    choix.destroy()
    subprocess.call(" python PL/Minimisation.py 1", shell=True)
    pass


b_min = Button(choix, text="Minimisation", command=mins, font=("Times New Roman", 18,'bold'),relief=SOLID,bg="#17992b", borderwidth=1).pack(side=RIGHT, padx=7, pady=10)
b_MAX = Button(choix, text="Maximisation", command=maxs, font=("Times New Roman", 18,'bold'),relief=SOLID,bg="#17992b", borderwidth=1).pack(side=LEFT, padx=7, pady=10)



choix.update()

fenwidth = choix.winfo_reqwidth()
fenheight = choix.winfo_reqheight()
sw = choix.winfo_screenwidth()
sh = choix.winfo_screenheight()
choix.geometry("%dx%d+%d+%d" % (fenwidth, fenheight, (sw - fenwidth) / 2, (sh - fenheight) / 2))
choix.resizable(width="false", height="false")
choix.mainloop()
