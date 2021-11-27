class Buku:
	def InputData(self):
		self.Judul_buku = (input("Judul Buku : "))
		self.Nama_pengarang = (input("Nama Pengarang : "))
		self.Tahun_terbit = (input("Tahun Terbit : "))
		self.penerbit = (input("Penerbit : "))

class Komik(Buku):
	def inputKomik(self):
		print("-"*23)
		print("|"," "*14,"Komik"," "*14,"|")
		print("-"*23)
		Buku.InputData(self)
		self.Genre = input("Genre : ")
		self.Ilustrator = input ("Ilustrator :")
		
	def tampilKomik(self):
		print("-"*23)
		print("|"," "*14,"Hasil"," "*14,"|")
		print("-"*23)
		print("Judul :",self.Judul_buku)
		print("Nama Pengarang :",self.Nama_pengarang)
		print("Tahun Terbit :",self.Tahun_terbit)
		print("Penerbit :",self.penerbit)
		print("Genre :",self.Genre)
		print("Ilustrator :",self.Ilustrator)
		print("-"*23)
class Novel(Buku):
	def inputNovel(self):
		print("-"*23)
		print("|"," "*14,"Novel"," "*14,"|")
		print("-"*23)
		Buku.InputData(self)
		self.Halaman = int(input("Jumlah Halaman :"))
		self.Bahasa = input("Bahasa :")
	def tampilNovel(self):
		print("-"*23)
		print("|"," "*14,"Hasil"," "*14,"|")
		print("-"*23)
		print("Judul :",self.Judul_buku)
		print("Nama Pengarang :",self.Nama_pengarang)
		print("Tahun Terbit :",self.Tahun_terbit)
		print("Penerbit :",self.penerbit)
		print("Jumlah Halaman :",self.Halaman)
		print("Bahasa :",self.Bahasa)
		print("-"*23)
class Majalah(Buku):
	def inputMajalah(self):
		print("-"*23)
		print("|"," "*13,"Majalah"," "*13,"|")
		print("-"*23)
		Buku.InputData(self)
		self.Jenis = input("Jenis :")
	def tampilMajalah(self):
		print("-"*23)
		print("|"," "*14,"Hasil"," "*14,"|")
		print("-"*23)
		print("Judul :",self.Judul_buku)
		print("Nama Pengarang :",self.Nama_pengarang)
		print("Tahun Terbit :",self.Tahun_terbit)
		print("Penerbit :",self.penerbit)
		print("Jenis Majalah : ",self.Jenis)
		print("-"*23)
class bukuPejaran(Buku):
		def inputBukpel(self):
			print("-"*23)
			print("|"," "*10,"Buku Pelajaran"," "*9,"|")
			print("-"*23)
			Buku.InputData(self)
			self.Kurikulum = input("Kurikulum :")
		def tampilBukpel(self):
			print("-"*23)
			print("|"," "*15,"Hasil"," "*15,"|")
			print("-"*23)
			print("Judul :",self.Judul_buku)
			print("Nama Pengarang :",self.Nama_pengarang)
			print("Tahun Terbit :",self.Tahun_terbit)
			print("Penerbit :",self.penerbit)
			print("Kurikulum : ",self.Kurikulum)
			print("-"*23)

print("-"*23)
print("|"," "*10,"Daftar Pilihan"," "*9,"|")
print("-"*23)
print("|"," "*10,"1. Komik"," "*9,"|")
print("|"," "*10,"2. Novel"," "*9,"|")
print("|"," "*10,"3. Majalah"," "*9,"|")
print("|"," "*10,"4. Buku Pelajaran"," "*5,"|")
print("-"*23)

pilihan = float(input("Pilih Nomor : "))
if (pilihan == 1):
	a = Komik()
	a.inputKomik()
	a.tampilKomik()
elif (pilihan == 2):
	b = Novel()
	b.inputNovel()
	b.tampilNovel()
elif (pilihan == 3):
	c = Majalah()
	c.inputMajalah()
	c.tampilMajalah()
elif pilihan == 4:
	bp = bukuPelajaran()
	bp.inputBukpel()
	bp.tampilBukpel()
else:
	print("Membaca Adalah Jendela Ilmu, Dan Jangan Malas Membaca")