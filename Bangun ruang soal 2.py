import math

class bangunRuang():
	def __init__(self):
		super(bangunRuang,self).__init__()
		self.nama = "Bangun Ruang"
		self.luasa = None
		self.tinggi = None

	def volume(self,luasa,tinggi):
		self.volume = self.luasa*self.tinggi
		return self.volume

class tabung(bangunRuang):
	def __init__(self,nama,tinggi,jarijari):
		super().__init__()
		self.nama = "\t\tTabung"
		self.tinggi = tinggi
		self.jarijari = jarijari
		self.luasa = math.pi*self.jarijari**2

	def volumeTabung(self):
		self.volumeTabung = self.luasa*self.tinggi
		return self.volumeTabung

class balok(bangunRuang):
	def __init__(self,nama,panjang,lebar,tinggi):
		super().__init__()
		self.nama = "\t\tBalok"
		self.panjang = panjang
		self.lebar = lebar
		self.luasa = self.panjang * self.lebar
		self.tinggi = tinggi

	def volumeBalok(self):
		self.volumeBalok = self.luasa * self.tinggi 
		return self.volumeBalok

class bola(bangunRuang):
	def __init__(self,nama,jarijari):
		super().__init__()
		self.nama = "\t\tBola"
		self.jarijari = jarijari

	def volumeBola(self):
		volumeBola = 4/3*math.pi*self.jarijari**3
		return volumeBola

#main		
tab = tabung(" ",9,14)
print("/"*35)
print(tab.nama)
print("jari - jari :",tab.jarijari)
print("Tinggi :",tab.tinggi)
print("Phi :",math.pi)
print("Volume Tabung :", tab.volumeTabung(),"cm**2")

bal = balok(" ",9,6,10)
print("/"*35)
print(bal.nama)
print("panjang :",bal.panjang)
print("Lebar :",bal.lebar)
print("Tinggi :",bal.tinggi)
print("Volume balok :",bal.volumeBalok(),"cm**3")

bol = bola(" ",21)
print("/"*35)
print(bol.nama)
print("jari jari :",bol.jarijari)
print("Volume Bola :",bol.volumeBola(),"cm**3")