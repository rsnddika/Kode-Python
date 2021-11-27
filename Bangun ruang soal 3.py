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
	def __init__(self):
		super().__init__()
		self.nama = "\t\tTabung"
		self.tinggi = float(input("Masukkan tinggi: ",))
		self.jarijari = float(input("Masukkan jari: "))
		self.luasa = math.pi*self.jarijari**2

	def volumeTabung(self):
		self.volumeTabung = self.luasa*self.tinggi
		return self.volumeTabung

class balok(bangunRuang):
	def __init__(self):
		super().__init__()
		self.nama = "\t\tBalok"
		self.panjang = float(input("Masukkan Panjang :"))
		self.lebar = float(input("Masukkan Lebar :"))
		self.luasa = self.panjang * self.lebar
		self.tinggi = float(input("Masukkan Tinggi :"))

	def volumeBalok(self):
		self.volumeBalok = self.luasa * self.tinggi 
		return self.volumeBalok

class bola(bangunRuang):
	def __init__(self):
		super().__init__()
		self.nama = "\t\tBola"
		self.jarijari = float(input("Masukkan jari-jari: "))

	def volumeBola(self):
		volumeBola = 4/3*math.pi*self.jarijari**3
		return volumeBola
		

print("\t\tInput Tabung")
tab = tabung()
print("/"*37)
print(tab.nama)
print("jari - jari :",tab.jarijari)
print("Tinggi :",tab.tinggi)
print("Phi :",math.pi)
print("Volume Tabung :", tab.volumeTabung(),"cm**2")

print("/"*37)
print("\t\tInput Balok")
bal = balok()
print("/"*37)
print(bal.nama)
print("panjang :",bal.panjang)
print("Lebar :",bal.lebar)
print("Tinggi :",bal.tinggi)
print("Volume balok :",bal.volumeBalok(),"cm**3")

print("/"*37)
print("\t\tInput Bola")
bol = bola()
print("/"*37)
print(bol.nama)
print("jari jari :",bol.jarijari)
print("Volume Bola :",bol.volumeBola(),"cm**3")