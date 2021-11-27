from abc import ABC, abstractmethod

class Hewan(ABC):

	def __init__(self,suara,jenis):
		self.suara = suara
		self.jenis = jenis
		super().__init__()

class Anjing(Hewan):

	def __init__(self):
		print("="*15)
		self.suara = str(input("Anjing :"))
		self.jenis = str(input("Jenis Makanan Anjing :"))

	def tamilJenis(self):
		print("Anjing: ",self.suara)
		print("Jenis Makanan Anjing:")

class Kucing(Hewan):

	def __init__(self):
		print("="*15)
		self.suara = str(input("Kucing :"))
		self.jenis = str(input("Jenis Makanan Kucing :"))

	def tamilJenis(self):
		print("Kucing: ",self.suara)
		print("Jenis Makanan Kucing:")

print("Anjing")
gukguk = Anjing()
print()

print("Kucing")
meoong = Kucing()
print()