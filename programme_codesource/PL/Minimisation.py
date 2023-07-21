from tkinter import *

minimisation_fen = Tk()

minimisation_fen.title("minimisation")
minimisation_fen['bg']="white"
file2 = open("donnees/variable_contrainte.txt", "r")
var = file2.readline()
cont = file2.readline()
file2.close()
column = int(var) + int(cont) + 2
row = int(cont) + 1
mat = [[0 for j in range(column)] for i in range(row)]

i = 0
donnee = ""
h = 0
j = 0
fileremplie2 = open("donnees/remplissagetableaucomplete.txt", "r")
while 1:
    ligne = fileremplie2.readline()
    for i in range(0, len(ligne)):
        if ligne[i] == ';':
            mat[j][h] = float(donnee)
            donnee = ""
            h += 1

        if ligne[i] == '\n':
            mat[j][h] = float(donnee)
            h = 0
            j += 1
            donnee = ""

        if ligne[i].isnumeric() or ligne[i] == '.' or ligne[i] == '-':
            donnee = donnee + ligne[i]
    if ligne == "":
        break

fileremplie2.close()

variableentrante = []

file1 = open("donnees/variable.txt", "r")
i = 1
casee = ""
while 1:
    ligne = file1.readline()
    for j in range(0, len(ligne)):
        if ligne[j] != ";":
            casee = casee + ligne[j]
        else:
            variableentrante.append(casee)
            casee = ""
            i += 1
    if ligne == "":
        break
file1.close()


Label(minimisation_fen,text="MINIMISATION", font=("Times New Roman", 30,'bold'),bg="white").pack()
frameinitial = Frame(minimisation_fen)
Label(frameinitial, text="tableau initial",bg="white", font=("Times New Roman", 20,'bold')).pack(side=LEFT)
frameinitial.pack()
frameT = Frame(minimisation_fen)
Label(frameT, text="BASE", borderwidth=1, relief=SOLID,bg="white", width=5, font=("Times New Roman", 15)).pack(side=LEFT)
for i in range(1, int(var) + 1):
    Label(frameT, text="X%d" % i, borderwidth=1, relief=SOLID,bg="white", width=5, font=("Times New Roman", 15)).pack(side=LEFT)
for i in range(1, int(cont) + 1):
    Label(frameT, text="e%d" % i, borderwidth=1, relief=SOLID,bg="white", width=5, font=("Times New Roman", 15)).pack(side=LEFT)
Label(frameT, text="SM", borderwidth=1, relief=SOLID, width=5,bg="white", font=("Times New Roman", 15)).pack(side=LEFT)
frameT.pack(padx=20)

frametableau = Frame(minimisation_fen)
for i in range(0, row - 1):
    frametable = Frame(frametableau)
    Label(frametable, text="%s" % variableentrante[i], borderwidth=1,bg="white", relief=SOLID, width=5, font=("Times New Roman", 15)).pack(
        side=LEFT)
    for j in range(0, column - 1):
        Label(frametable, text="%.2f" % mat[i + 1][j + 1], borderwidth=1,bg="white", relief=SOLID, width=5,
              font=("Times New Roman", 15)).pack(side=LEFT)
    frametable.pack()
frametable = Frame(frametableau)
Label(frametable, text="Z", borderwidth=1, relief=SOLID, width=5,bg="white", font=("Times New Roman", 15)).pack(side=LEFT)
for j in range(1, column):
    if j != column - 1:
        Label(frametable, text="%.2f" % mat[0][j], borderwidth=1,bg="white", relief=SOLID, width=5,
              font=("Times New Roman", 15)).pack(side=LEFT)
    if j == column - 1:
        Label(frametable, text="%.2f" % mat[0][j], borderwidth=1,bg="white", relief=SOLID, width=5,
              font=("Times New Roman", 15)).pack(side=LEFT)

    frametable.pack()
frametableau.pack(padx=20)

a = 1
while min(mat[0][1:column - 1]) < 0:
    sm_cp_column = []
    sm_cp_column_pos = []
    ligne_pivot = []
    column_pivot = []
    indicemax = mat[0][0:column].index(min(mat[0][1:column - 1]))
    for i in range(0, row):
        if mat[i][indicemax] != 0:
            mat[i][0] = float(mat[i][column - 1] / mat[i][indicemax])
            sm_cp_column.append(mat[i][0])
        if mat[i][indicemax] == 0:
            mat[i][0] = 0
            sm_cp_column.append(mat[i][0])
    for i in range(1, row):
        if sm_cp_column[i] > 0:
            sm_cp_column_pos.append(sm_cp_column[i])

    indicemin_sm_cp = sm_cp_column.index(min(sm_cp_column_pos))
    pivot = mat[indicemin_sm_cp][indicemax]

    for i in range(0, column):
        ligne_pivot.append(mat[indicemin_sm_cp][i])
        if pivot != 0:
            mat[indicemin_sm_cp][i] = mat[indicemin_sm_cp][i] / pivot

    for i in range(0, row):
        if i == indicemin_sm_cp:
            column_pivot.append(pivot)
            mat[i][indicemax] = 1
        if i != indicemin_sm_cp:
            column_pivot.append(mat[i][indicemax])
            mat[i][indicemax] = 0
    variableentrante[indicemin_sm_cp - 1] = "X%d" % indicemax
    for i in range(0, row):
        if i != indicemin_sm_cp:
            for j in range(0, column):
                if j != indicemax:
                    mat[i][j] = mat[i][j] - ((ligne_pivot[j] * column_pivot[i]) / pivot)



frametableau1 = Frame(minimisation_fen)
Label(frametableau1, text="tableau final", font=("Times New Roman", 20,'bold'),bg="white").pack(side=LEFT)

frametableau1.pack()

frameT = Frame(minimisation_fen)
Label(frameT, text="BASE", borderwidth=1, relief=SOLID, width=5,bg="white", font=("Times New Roman", 15)).pack(side=LEFT)
for i in range(1, int(var) + 1):
    Label(frameT, text="X%d" % i, borderwidth=1, relief=SOLID, width=5,bg="white", font=("Times New Roman", 15)).pack(
        side=LEFT)
for i in range(1, int(cont) + 1):
    Label(frameT, text="e%d" % i, borderwidth=1, relief=SOLID, width=5,bg="white", font=("Times New Roman", 15)).pack(
        side=LEFT)
Label(frameT, text="SM", borderwidth=1, relief=SOLID, width=5,bg="white", font=("Times New Roman", 15)).pack(side=LEFT)
frameT.pack(padx=20)
frametableau = Frame(minimisation_fen)
for i in range(0, row - 1):
    frametable = Frame(frametableau)
    Label(frametable, text="%s" % variableentrante[i], borderwidth=1,bg="white", relief=SOLID, width=5,
          font=("Times New Roman", 15)).pack(side=LEFT)
    for j in range(0, column - 1):
        Label(frametable, text="%.2f" % mat[i + 1][j + 1], borderwidth=1,bg="white", relief=SOLID, width=5,
              font=("Times New Roman", 15)).pack(side=LEFT)
    frametable.pack()
frametable = Frame(frametableau)
Label(frametable, text="Z", borderwidth=1, relief=SOLID, width=5,bg="white", font=("Times New Roman", 15)).pack(side=LEFT)
for j in range(1, column):
    if j != column - 1:
        Label(frametable, text="%.2f" % mat[0][j], borderwidth=1,bg="white", relief=SOLID, width=5,
              font=("Times New Roman", 15)).pack(side=LEFT)
    if j == column - 1:
        Label(frametable, text="%.2f" % mat[0][j], borderwidth=1,bg="white", relief=SOLID, width=5,
              font=("Times New Roman", 15), fg='red').pack(side=LEFT)

    frametable.pack()
frametableau.pack(padx=20)

Label(minimisation_fen, text="resultat", font=("Times New Roman", 20,'bold'),bg="white",fg="#17992b").pack()
frame_resultat = Frame(minimisation_fen)
for j in range(1, int(var) + 1):
    if not ("X%d" % j in variableentrante):
        Label(frame_resultat, text="X%d" % j,width=3, borderwidth=1,bg="white", relief=SOLID, font=("Times New Roman", 15)).pack(side=LEFT)
for i in range(1, row):
    Label(frame_resultat, text="%s" %variableentrante[i - 1], borderwidth=1,bg="white", relief=SOLID,width=len(str(mat[i][column - 1])), font=("Times New Roman", 15)).pack(side=LEFT)
Label(frame_resultat, text="Z",width=len(str(mat[0][column - 1])), borderwidth=1,bg="white", relief=SOLID, font=("Times New Roman", 15),fg="red").pack()

frame_resultat.pack(padx=20)

frame_resultat = Frame(minimisation_fen)
for j in range(1, int(var) + 1):
    if not ("X%d" % j in variableentrante):
        Label(frame_resultat, text="0.0",width=3, borderwidth=1,bg="white", relief=SOLID, font=("Times New Roman", 15)).pack(side=LEFT)
for i in range(1, row):
    Label(frame_resultat, text="%.1f" %mat[i][column - 1], borderwidth=1,bg="white", relief=SOLID,width=len(str(mat[i][column - 1])), font=("Times New Roman", 15)).pack(side=LEFT)
Label(frame_resultat, text="%.1f" % float(-1*mat[0][column - 1]),fg="red",bg="white", borderwidth=1, relief=SOLID,width=len(str(mat[0][column - 1])), font=("Times New Roman", 15)).pack()

frame_resultat.pack(padx=20)
framef=Frame(minimisation_fen).pack(pady=20)

minimisation_fen.update()
fenwidth = minimisation_fen.winfo_reqwidth()
fenheight = minimisation_fen.winfo_reqheight()
sw = minimisation_fen.winfo_screenwidth()
sh = minimisation_fen.winfo_screenheight()
minimisation_fen.geometry("%dx%d+%d+%d" % (fenwidth, fenheight, (sw - fenwidth) / 2, (sh - fenheight) / 2))
minimisation_fen.resizable(width="false", height="false")
minimisation_fen.mainloop()
