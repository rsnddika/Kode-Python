from tkinter import *
root = Tk()
root.title('Risnanda Rio Putra Mahadika')

class Hero(object):
	def __init__(self, nama= None, alias = None, kelompok = None, kondisi = None):
		self.nama = nama
		self.alias = alias
		self.kelompok = kelompok
		self.kondisi = kondisi
		
#List Hero
listHero = []
label1  = Label(root, text='Jumlah Hero :')
label1. grid(column = 0, row = 0)
ask =IntVar()
question = Entry(root,text = ask)
question.grid(column = 1, row = 0)

i = 0
def input():
	for i in range(ask.get()):
		labelNama = Label(root, text='Nama :')
		labelAlias = Label(root, text='Alias :')
		labelKelompok = Label(root, text='Kelompok :')
		labelKondisi = Label(root, text='Kondisi :')
			
		nama = Entry(root)
		alias = Entry(root)
		kelompok = Entry(root)
		kondisi = Entry(root)
		
		labelNama.grid()
		nama.grid()
		labelAlias.grid()
		alias.grid()
		labelKelompok.grid()
		kelompok.grid()
		labelKondisi.grid()
		kondisi.grid()
			
		listHero.append(Hero(nama, alias, kelompok, kondisi))
		button2 = Button(root, text="Cetak", command=panggilHero)
		button3 = Button(root, text="Keluar", command=root.quit)
		button2.grid(sticky=W)
		button3.grid(sticky=W)
	
def panggilHero():
	for Hero in listHero:
		print("Nama : {}\nAlias : {}\nKelompok : {}\nKondisi : {}\n\n".format(Hero.nama.get(), 
		Hero.alias.get(), 
		Hero.kelompok.get(), 
		Hero.kondisi.get()
		))
	assert(Hero.kondisi.get() == 'hidup'), 'kondisi : {}'.format(Hero.kondisi.get())
	return print('Hero masih bernyawa')

button1 = Button(root, text='Enter', command=input)
button1.grid(columnspan=2)
root.mainloop()