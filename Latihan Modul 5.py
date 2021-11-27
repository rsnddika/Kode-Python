class Buku:
	def _init_ (self, judul_buku, pengarang, tahun_terbit, penerbit):
		self.judul_buku=judul
		self.pengarang=pengarang
		self.tahun=tahun
		self.penerbit=penerbit
	def tampilProfil(self):
		print("Judul buku:", self.judul)
		print("Pengarang:", self.pengarang)
		print("Tahun terbit:", self.tahun)
		print("Penerbit:", self.penerbit)

class Novel(Buku):
	def _init_(self):
		print("Biodata Novel : ")
	def tampilProfil(self):
		self.judul = 'Judu novel : '
		self.pengarang = 'Pengarang novel : '
		self.tahun = 'Tahun terbit novel : '
		self.penerbit = 'Penerbit novel : '

bku1 = Buku('Mariposa','Tidak tahu','2015','Kurang tahu')

tampilProfil()