class mahasiswa():
	'dasar kelas untuk semua mahasiswa'
	jmlMhs = 0
	def __init__ (self, nama, prodi, nim):
		self.nama = nama
		self.prodi = prodi
		self.nim = nim
		mahasiswa.jmlMhs += 1
	def tampilJml(self):
		print("Total Mahasiswa: ", mahasiswa.jmlMhs)
	def tampilProfil(self):
		print("Nama : ", self.nama)
		print("Prodi : ", self.prodi)
		print("Nim : ", self.nim)
		print()

#data mhs 1
mhs1 = mahasiswa('Angga', 'Sistem Informasi', '202103016')
name = input("nama: ")
sp = input("prodi: ")
sn = input("nim :")
setattr(mhs1,"nama",name)
setattr(mhs1,"prodi",sp)
setattr(mhs1,"nim",sn)

print(mhs1.tampilProfil())