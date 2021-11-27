class Motor():
	#Method
	def setProdusen(self):
		self.id_produsen = input("ID Produsen: ")
		self.jenis_kelamin = input("Jenis Kelamin: ")
		self.alamat = input("Alamat: ")

	def getProdusen(self):
		print("ID Produsen:", self.id_produsen)
		print("Jenis Kelamin:",self.jenis_kelamin)
		print("Alamat:", self.alamat)

#Nnak
class Matic(Motor):

	#Method
	def setTipe(self):
		Motor.setProdusen(self)
		self.merk = str(input("Merek: "))

	def getTipe(self):
		print("ID Produsen:", self.id_produsen)
		print("Jenis Kelamin:",self.jenis_kelamin)
		print("Alamat:", self.alamat)
		print("Merek:", self.merk)

a = Matic()
a.setTipe()
a.getTipe()