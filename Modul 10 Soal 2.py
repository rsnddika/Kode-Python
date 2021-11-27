from tkinter import *
root = Tk()

def cetak():
 	Label(root, text='Nama 	:').grid(column=0, row=7)
 	Label(root, text='NIM 	:').grid(column=0, row=8)
 	Label(root, text='Prodi 	:').grid(column=0, row=9)
#Hasil Mengambil Nilai
 	Label(root, text=inputNama.get()).grid(column=1, row=7)
 	Label(root, text=inputNim.get()).grid(column=1, row=8)
 	Label(root, text=inputProdi.get()).grid(column=1, row=9)

#Label
label = Label(root, text='Identitas',fg = 'blue').grid(column = 1,  row = 0)
labelNama = Label(root, text='Nama').grid(column = 0,  row = 1)
labelNim = Label(root, text='Nim').grid(column = 0,  row = 2)
labelProdi = Label(root, text='Prodi').grid(column = 0,  row = 3)

#Input
#1
inputNama = Entry(root)
inputNama.grid(column = 1, row = 1)
#2
inputNim = Entry(root)
inputNim.grid(column = 1, row = 2)
#3
inputProdi = Entry(root)
inputProdi.grid(column = 1, row = 3)

#Button
Button(root, text='Cetak', command=cetak).grid(column = 1, row = 4)

mainloop()