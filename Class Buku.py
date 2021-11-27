class buku():
	jmlbuku = 0
	def __init__(self,judul,halaman):
		self.judul=judul
		self.halaman=halaman
		buku.jmlbuku += 1

	def tampilJml(self):
		print("Total buku: ", buku.jmlbuku)
	def tampilProfil(self):
		print("judul: ", self.judul)
		print("halaman: ", self.halaman)
		print()

buku1 = buku('pemrograman c++','321')
buku2 = buku('bahasa python','123')

print(buku1.tampilProfil())
print(buku2.tampilProfil())

print(ininstance(buku1,buku))