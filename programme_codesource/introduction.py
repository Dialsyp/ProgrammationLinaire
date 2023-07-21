import os
import subprocess

from tkinter import *

fen_intro=Tk()
fen_intro['bg']='white'
fen_intro.title("DIAL SYPHAX")
Label(fen_intro,text="TP PROGRAMMATION LINAIRE",font=("Times New Roman",20,'bold'),fg="green",bg="white").pack()
nom=Frame(fen_intro)
Label(nom,text="NOM :     ",font=("Times New Roman",20,'bold'),width=10,bg="white").pack(side=LEFT)
Label(nom,text="DIAL   ",font=("Times New Roman",20),width=10,fg="red",bg="white").pack(side=LEFT)
nom.pack()
prenom=Frame(fen_intro)
Label(prenom,text="PRENOM :",font=("Times New Roman",20,'bold'),width=10,bg="white").pack(side=LEFT)
Label(prenom,text="Syphax",font=("Times New Roman",20),width=10,fg="red",bg="white").pack(side=LEFT)
prenom.pack()
prenom=Frame(fen_intro)
Label(prenom,text="GROUPE :",font=("Times New Roman",20,'bold'),width=10,bg="white").pack(side=LEFT)
Label(prenom,text="4       ",font=("Times New Roman",20),width=10,fg="red",bg="white").pack(side=LEFT)
prenom.pack()


def demarre():
    fen_intro.destroy()
    subprocess.call(" python PL/variable_contrainte.py 1", shell=True)

    pass


btn=Button(fen_intro,text="Demarrer",font=("Times New Roman",18,'bold'), command=demarre,relief=SOLID,bg="#17992b", borderwidth=1).pack(pady=20)

fen_intro.update()
fenwidth = fen_intro.winfo_reqwidth()
fenheight = fen_intro.winfo_reqheight()
sw = fen_intro.winfo_screenwidth()
sh = fen_intro.winfo_screenheight()
fen_intro.geometry("%dx%d+%d+%d" % (fenwidth, fenheight, (sw-fenwidth)/2, (sh - fenheight*2)/2))
fen_intro.resizable(width="false", height="false")
fen_intro.mainloop()