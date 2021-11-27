class mahasiswa:
	def __init__(self):
		self.__nama = "Risnanda Rio Putra Mahadika"
		self.__nim = "202103017"
		self.__prodi = "Sistem Informasi"
		self.__jeniskelamin = "Laki-laki"
		self.semester = "Dua"
		self.hobby = "Balap"
	def tampilProfil(self):
		print("Nama: ",self.__nama)
		print("NIM: ",self.__nim)
		print("Prodi: ",self.__prodi)
		print("Jenis Kelamin: ",self.__jeniskelamin)
		print("Semester: ",self.semester)
		print("Hobby: ",self.hobby)
#method private
	def getProfil(self,Nama,Nim,Prodi,Jeniskelamin):
		self.__nama = Nama
		self.__nim = Nim
		self.__prodi = Prodi
		self.__jeniskelamin = Jeniskelamin
		self.semester = "Tiga"
		self.hobby = "Game"
#sebelum perubahan
mhs = mahasiswa()

print("|         sebelum perubahan         |")

mhs.tampilProfil()
#setelah perubahan

print("|         setelah perubahan         |")

mhs.getProfil("Mas Bhe","034","Informatika","Pria")
getattr(mhs,"semester")
getattr(mhs,"hobby")
mhs.tampilProfil()