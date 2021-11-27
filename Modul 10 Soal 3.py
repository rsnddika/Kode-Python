import tkinter
from tkinter import *

root = Tk()
root.title( ' SegiTiga ' )

def hitungLuas():
    print('Luas Segitiga = ',0.5*f.get()*h.get(),'cm2')

alas = Label(root, text='SISI ALAS :').place(x=5,y=15,height=20)
f = IntVar()
g = Entry( root , text = f ).place(x=120,y=14,height=20)

tinggi = Label(root, text='SISI TINGGI :').place(x=50,y=55,height=20)
h = IntVar()
i = Entry( root , text = h ).place(x=120,y=54,height=20)

j = Button( root , text = 'Luas Segi Tiga Adalah' , command = hitungLuas ).place(x=120,y=90,height= 20)

root.mainloop()