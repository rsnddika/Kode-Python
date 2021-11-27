class mahasiswa():
	'dasar kelas untuk semua mahasiswa'
	jmlMhs = 0
	def __init__ (self, nama, prodi, nim, jk):
		self.nama = nama
		self.prodi = prodi
		self.nim = nim
		self.jk = jk
		mahasiswa.jmlMhs += 1
	def tampilJml(self):
		print("Total Mahasiswa: ", mahasiswa.jmlMhs)
	def tampilProfil(self):
		print("Nama : ", self.nama)
		print("Prodi : ", self.prodi)
		print("Nim : ", self.nim)
		print("Jk : ", self.jk)
		print()

#data mhs 1
mhs1 = mahasiswa('Angga', 'Sistem Informasi', '202103017', 'Laki Laki')
name = input("nama: ")
sp = input("prodi: ")
sn = input("nim :")
jk = input("jk :")
setattr(mhs1,"nama",name)
setattr(mhs1,"prodi",sp)
setattr(mhs1,"nim",sn)
setattr(mhs1,"jenis kelamin",jk)

#Memanggilan Atribut
print("Memanggilan Atribut")
print(mhs1.tampilProfil())

#Mengecek Atribut
print("Mengecek Atribut")
print("Apakah jenis kelamin sudah terdapat di class mahasiswa :",hasattr(mahasiswa,"jenis kelamin"))

print("Apakah jenis kelamin sudah terdapat di objek mhs1 :",hasattr(mhs1,"jenis kelamin"))

#Mengakses Nilai Atribut
print("Mengakses Nilai Atribut")
print("Jenis Kelamin :",getattr(mhs1,"jenis kelamin"))

#Menghapus Nilai Atribut
print("Menghapus Nilai Atribut")
print(delattr(mhs1,"jenis kelamin"))