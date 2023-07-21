import os.path
import subprocess

from tkinter import *



if not(os.path.isdir("donnees")):
    os.mkdir("donnees")

















fen_prin = Tk()
fen_prin.title ("variable contrainte")
fen_prin['bg'] = 'white'
FramePL = Frame(fen_prin, relief=GROOVE)
Label(FramePL, text="programme de resolution simplex", bg="white", font=("Times New Roman", 20,'bold')).pack()
FramePL.pack(padx=30)
Framevar = Frame(fen_prin, relief=GROOVE)
Label(Framevar, text="Combien de variables de decision a le probleme?", bg="white", font=("Times New Roman", 15)).pack(
    side=LEFT)
entre1 = Entry(Framevar, textvariable=int, fg="red", width=5, font=("Times New Roman", 15), relief=SOLID)
entre1.pack(side=RIGHT, padx=10, pady=10)
Framevar.pack()
Framecont = Frame(fen_prin, relief=GROOVE)
Label(Framecont, text="Combien de constraints?", bg="white", font=("Times New Roman", 15)).pack(side=LEFT)
entre2 = Entry(Framecont, textvariable=int, width=5, font=("Times New Roman", 15), relief=SOLID, fg="red")
entre2.pack(side=RIGHT, padx=10, pady=10)
Framecont.pack()
Framecont['bg'] = 'white'
Framevar['bg'] = 'white'

entre1.insert(0, 2)
entre2.insert(0, 2)


def disst():
    file = open("donnees/variable_contrainte.txt", "w")
    file.write(str(entre1.get()))
    file.write("\n" + str(entre2.get()))
    file.close()
    fen_prin.destroy()
    subprocess.call(" python PL/injection_de_donnees.py 1", shell=True)
    pass


framebtn = Frame(fen_prin)
botton = Button(framebtn, text="Traiter", command=disst, font=("Times New Roman", 18,'bold'),relief=SOLID,bg="#17992b", borderwidth=1).pack()
framebtn.pack(pady=10)
fen_prin.update()
fenwidth = fen_prin.winfo_reqwidth()
fenheight = fen_prin.winfo_reqheight()
sw = fen_prin.winfo_screenwidth()
sh = fen_prin.winfo_screenheight()
fen_prin.geometry("%dx%d+%d+%d" % (fenwidth, fenheight, (sw - fenwidth) / 2, (sh - fenheight) / 2))

fen_prin.resizable(width="false", height="false")

fen_prin.mainloop()
