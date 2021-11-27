import tkinter
from tkinter import *
import math

class segitiga :
	def hitungLuasSegitiga(self):
		#self.root = root
		print('Luas Segitiga = ',0.5*self.alas.get()*self.tinggi.get(),'cm2')

	def sisiSegitiga(self):
		#root = Tk()
		#self.root = root
		root.title("Hitung Luas Bangun Datar")
		self.label = Label(root, text="Menghitung Luas Segitiga")

		self.Alas = Label(root, text='Sisi Alas:').place(x=5,y=15,height=20)
		self.alas = IntVar()
		self.alas2 = Entry( root , text = self.alas ).place(x=120,y=14,height=20)

		self.Tinggi = Label(root, text='Sisi Tinggi:').place(x=50,y=55,height=20)
		self.tinggi = IntVar()
		self.tinggi2 = Entry( root , text = self.tinggi ).place(x=120,y=54,height=20)

		self.hitung_button = Button( root , text = 'Luas Segitiga' , command = self.hitungLuasSegitiga ).place(x=120,y=90,height=20)
		

class persegi :
	def hitungLuasPersegi(self):
		print('Luas Persegi= ',self.sisi.get()**2,'cm2')
	
	def sisiPersegi(self):
		#root=Tk()
		self.Sisi = Label(root, text='Panjang Sisi:').place(x=5,y=15,height=20)
		self.sisi = IntVar()
		self.sisi2 = Entry( root , text = self.sisi ).place(x=120,y=14,height=20)

		self.hitung_button = Button( root , text = 'Luas Persegi' , command = self.hitungLuasPersegi ).place(x=120,y=90,height=20)

class lingkaran :
	def hitungLuasLingkaran(self):
		print('Luas Lingkaran = ',math.pi*self.jari.get()**2,'cm2')

	def sisiLingkaran(self):
		self.Jari = Label(root, text='Jari - jari:').place(x=5,y=15,height=20)
		self.jari = IntVar()
		self.jari2 = Entry( root , text = self.jari ).place(x=120,y=14,height=20)

		self.hitung_button = Button( root , text = 'Luas Lingkaran' , command = self.hitungLuasLingkaran ).place(x=120,y=90,height=20)

class luas (segitiga, persegi, lingkaran):
	def __init__ (self, root):
		self.root = Tk
		root.title("Hitung Luas Bangun Datar")
		self.label=Label(root, text="Pilih Bangun Datar")
		self.label.pack()
		self.segitiga_button = Button(root, text="Segitiga",command=self.sisiSegitiga)
		self.segitiga_button.pack()
		self.persegi_button = Button(root, text="Persegi",command=self.sisiPersegi)
		self.persegi_button.pack()
		self.lingkaran_button = Button(root, text="Lingkaran",command=self.sisiLingkaran)
		self.lingkaran_button.pack()
		self.keluar_button = Button(root, text="Keluar", command=root.quit)
		self.keluar_button.pack()


root = Tk()
file_gui = luas(root)
root.mainloop()