class mahasiswa:
	def __init__(self):
		self.__nama = "Risnanda Rio Putra Mahadika"
		self.__nim = "202103017"
		self.__prodi = "Sistem Informasi"
		self.__jeniskelamin = "Laki-laki"
		self.semester = "Dua"
		self.hobby = "Game"
	def tampilProfil(self):
		print("Nama: ",self.__nama)
		print("NIM: ",self.__nim)
		print("Prodi: ",self.__prodi)
		print("Jenis Kelamin: ",self.__jeniskelamin)
		print("Semester: ",self.semester)
		print("Hobby: ",self.hobby)

mhs = mahasiswa()
mhs.tampilProfil()
