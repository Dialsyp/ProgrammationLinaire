import subprocess
from tkinter import *

simplexfen = Tk()
simplexfen.title("injection de donnees")
simplexfen['bg'] = 'white'
file = open("donnees/variable_contrainte.txt", "r")
v = file.readline()
c = file.readline()
file.close()

frameX = LabelFrame(simplexfen, name='fUNCTION_OBJECTIVE',text="Function objective",font=("Times New Roman",15,'bold'),borderwidth="0" ,relief=SOLID)
Label(frameX, text="Z =", bg="white",font=("Times New Roman",15)).pack(side=LEFT)
Entry(frameX, width=3, name="entreF%d" % 1,fg="red", bg='white',font=("Times New Roman",15),justify="center",borderwidth="1" ,relief=SOLID).pack(side=LEFT, padx=10)
Label(frameX, name='%d' % 1, text='X%d' % 1, bg='white',font=("Times New Roman",15)).pack(side=LEFT)
h = frameX.nametowidget('entreF%d' % 1)
h.insert(0, 0)
for i in range(2, int(v) + 1):
    Label(frameX, name='s%d' %i, text='+', bg='white', font=("Times New Roman", 15)).pack(side=LEFT)
    Entry(frameX, width=3, name="entreF%d" % i,fg="red", bg='white',font=("Times New Roman",15),justify="center",borderwidth="1" ,relief=SOLID).pack(side=LEFT, padx=10)
    Label(frameX, name='%d' % i, text='X%d' % i, bg='white',font=("Times New Roman",15)).pack(side=LEFT)
    h = frameX.nametowidget('entreF%d' % i)
    h.insert(0, 0)
frameX['bg'] = 'white'
frameX.pack()


frameC = LabelFrame(simplexfen, name='contain',text="Les contrainte", font=("Times New Roman", 15,'bold'),borderwidth="0" ,relief=SOLID)
frameC['bg'] = 'white'

for i in range(1, int(c) + 1):
    frame = Frame(frameC, name='frame%d' % i)
    Entry(frame, width=3, name='x%d' % 1, bg='white', fg="red", font=("Times New Roman", 15), justify="center",borderwidth="1" ,relief=SOLID).pack(side=LEFT, padx=10)
    Label(frame, name='h%d' % 1, text='X%d' % 1, bg='white', font=("Times New Roman", 15)).pack(side=LEFT)
    h = frame.nametowidget('x%d' % 1)

    h.insert(0, 0)
    for j in range(2, int(v) + 1):
        Label(frame, name='s%d' % j, text='+', bg='white', font=("Times New Roman", 15 )).pack(side=LEFT)
        Entry(frame, width=3, name='x%d' % j, bg='white',fg="red",font=("Times New Roman",15),justify="center",borderwidth="1" ,relief=SOLID).pack(side=LEFT, padx=10)
        Label(frame, name='h%d' % j, text='X%d'%j, bg='white', font=("Times New Roman", 15)).pack(side=LEFT)
        h = frame.nametowidget('x%d' % j)

        h.insert(0, 0)
    Label(frame, text='<=', bg='white',font=("Times New Roman",15)).pack(side=LEFT)
    Entry(frame, width=3, name='x%s' % str(j + 1),font=("Times New Roman",15),fg="red",justify="center",borderwidth="1" ,relief=SOLID).pack(side=LEFT, padx=10)
    h = frame.nametowidget('x%s' % str(j + 1))
    h.insert(0, 0)
    frame['bg'] = 'white'
    frame.pack()

frameC.pack(padx=5)

frameB = Frame(simplexfen, name='bouton')


def envoie():
    fileremplie = open("donnees/remplissagetableau.txt", "w")
    for i in range(1, int(v)):
        h = frameX.nametowidget('.fUNCTION_OBJECTIVE.entreF%d' % i)
        fileremplie.write(h.get() + ";")
    h = frameX.nametowidget('.fUNCTION_OBJECTIVE.entreF%s' % str(i + 1))
    fileremplie.write(h.get() + "\n")

    for i in range(1, int(c)+1):
        for j in range(1,int(v)+1):
            h = frameC.nametowidget('frame%d.x%d' % (i, j))
            fileremplie.write(h.get() + ";")
        h = frameC.nametowidget('frame%d.x%d' % (i, j+1))
        fileremplie.write(h.get() + "\n")
    fileremplie.close()
    simplexfen.destroy()
    subprocess.call(" python PL/PL_choix.py 1", shell=True)
    pass


b = Button(frameB, text='Envoyer', command=envoie,font=("Times New Roman",18,'bold'),relief=SOLID,bg="#17992b", borderwidth=1).pack()
frameB.pack(pady=10)


simplexfen.update()
fenwidth = simplexfen.winfo_reqwidth()
fenheight = simplexfen.winfo_reqheight()
sw = simplexfen.winfo_screenwidth()
sh = simplexfen.winfo_screenheight()
simplexfen.geometry("%dx%d+%d+%d" % (fenwidth, fenheight, (sw-fenwidth)/2, (sh - fenheight)/2))
simplexfen.resizable(width="false", height="false")
simplexfen.mainloop()
