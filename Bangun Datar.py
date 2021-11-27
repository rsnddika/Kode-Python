from abc import ABC, abstractmethod
import math

#Class Induk
class BangunDatar(ABC):
	def __init__(self,a,b):
		self.a = a
		self.b = b
		super().__init__()

#Class Anak Persegi Panjang
class PersegiPanjang(BangunDatar):
	def __init__(self,a,b):
		print("PersegiPanjang")
		print('='*25)
		super().__init__(a,b)
	def hitungKelilingPersegiPanjang(self):
		keliling = 2 * (self.a + self.b)
		if self.a > self.b:
			print("Panjang :",self.a)
			print("Lebar :",self.b)

		else:
			print("Panjang ;",self.b)
			print("Lebar :",self.a)

		return print("Keliling :",keliling)
		print('='*25)

	def hitungLuasPersegiPanjang(self):
		luas = self.a * self.b
		return print("Luas :",luas)

#Class Anak Segi Tiga
class Segitiga(BangunDatar):
	def __init__(self,a,b):
		print("SegiTiga")
		print('='*25)
		super().__init__(a,b)

	def hitungKelilingSegiTiga(self):
		self.sm = math.sqrt((self.a**2) + (self.b**2))
		keliling = self.a + self.b + self.sm

		if self.a>self.b:
			print("Alas :",self.b)
			print("Tinggi :",self.a)

		else:
			print("Alas :",self.a)
			print("Tinggi :",self.b)
		print("Sisi Miring :",self.sm)
		return print("Keliling :",keliling)
		print('='*25)

	def hitungLuasSegitiga(self):
		luas = 0.5 * self.a * self.b
		return print("Luas :",luas)

a = PersegiPanjang(12,9)
a.hitungKelilingPersegiPanjang()
a.hitungLuasPersegiPanjang()

b = Segitiga(9,6)
b.hitungKelilingSegiTiga()
b.hitungLuasSegitiga()