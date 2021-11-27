from tkinter import *
root = Tk()
root.config(bg= 'blue')
root.title('Daftar Judul Film 2021')

anak = Toplevel()
anak.config(bg= 'blue')
anak.title('Judul Pilihan')

class Film:
	def inputFilm(self):
		self.namaFilm = Entry(anak)
		self.jenisFilm = Entry(anak)
		self.sutradara = Entry(anak)
		self.tahunDibuat = Entry(anak)
		
		Label(anak, text='Nama Film').pack(pady=5)
		self.namaFilm.pack()
		Label(anak, text='Jenis Film').pack(pady=5)
		self.jenisFilm.pack()
		Label(anak, text='Sutradara').pack(pady=5)
		self.sutradara.pack()
		Label(anak, text='Tahun Dibuat').pack(pady=5)
		self.tahunDibuat.pack()

	def tampilFilm(self):
		print('Nama film 		:', self.namaFilm.get())
		print('Jenis film 		:', self.jenisFilm.get())
		print('Sutradara film 		:', self.sutradara.get())
		print('Tahun Dibuat film 	:', self.tahunDibuat.get())

class TokyoRevenge(Film):
	def inputTokyoRevenge(self):
		Label(anak, text='Tokyo Revenge').pack(pady=5)
		Film.inputFilm(self)
		self.genre = Entry(anak)
			
		Label(anak, text='Genre').pack(pady=5)
		self.genre.pack()
		Button(anak, text='Cetak', command= self.tampilTokyoRevenge).pack()

	def tampilTokyoRevenge(self):
		print('='*40)
		print('	  Film Tokyo Revenge')
		print('='*40)
		Film.tampilFilm(self)
		print('Genre film 		:', self.genre.get())
		print('='*40)
		
class AttackOnTitan(Film):
	def inputAttackOnTitan(self):
		Label(anak, text='Attack On Titan').pack(pady=5)
		Film.inputFilm(self)
		self.genre = Entry(anak)
		Label(anak, text='Genre').pack(pady=5)
		self.genre.pack()
		Button(anak, text='Cetak', command= self.tampilAttackOnTitan).pack()

	def tampilAttackOnTitan(self):
		print('='*40)
		print('	  Film Attack On Titan')
		print('='*40)
		Film.tampilFilm(self)
		print('Genre film 		:', self.genre.get())
		print('='*40)

class All(TokyoRevenge, AttackOnTitan):
	def __init__(self,root):
		self.root = root

		Label(root, text='Klik Film Pilihan Anda', bg='yellow').pack()
		button1 = Button(root, text='Tokyo Revenge',bg= 'green', command= self.inputTokyoRevenge)
		button2 = Button(root, text='Attack On Titan', bg= 'green', command= self.inputAttackOnTitan)
		button3 = Button(root, text='Keluar', bg= 'red', command= root.quit)
		
		button1.pack()
		button2.pack()
		button3.pack()


all = All(root)
root.mainloop()
anak.mainloop()