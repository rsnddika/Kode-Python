class waktu:
	#def _init_(self, jam=0, menit=0, detik=0)
	def _init_(self, jam=0, menit=0, detik=0):
		self.jam = jam
		self.menit = menit
		self.detik = detik
	def ubahWaktu(self, jam, menit, detik=0):
		self.jam = jam
		self.menit = menit
		self.detik = detik
	
class tempat:
	# def _init_(self, nama, latitude, longitude):
		def _init_(self,namaTempat,latitude,longitude):
			self.namaTempat = namaTempat
			self.lattitude = latitude
			self.longitude = longitude

class kalender:
	# def _init_(self,hari,tanggal,bulan,tahun):
		def _init_(self,hari,tanggal,bulan,tahun):
			self.hari = hari
			self.tanggal = tanggal
			self.bulan = bulan
			self.tahun = tahun
			
		def ubahKalender(self,hari,tanggal,bulan,tahun):
			self.hari = hari
			self.tanggal = tanggal
			self.bulan = bulan
			self.tahun = tahun

class jadwal(waktu,tempat,kalender):
	def _init_(self):
		print("|"," "*11,"INPUT JADWAL"," "*8,"|")
		self.namaKegiatan = input("Nama Kegiatan :")
		self.jenisKegiatan = input("Jenis Kegiatan :")
		self.hari = input("Hari :")
		self.tanggal = int(input("Tanggal :"))
		self.bulan = int(input("Bulan :"))
		self.tahun = int(input("Tahun :"))
		self.jam = int(input("Jam :"))
		self.menit = int(input("Menit :"))
		self.namaTempat = input("Tempat :")

	def tampilJadwal(self):
		print("|              JADWAL               |")
		print("Nama Kegiatan :", self.namaKegiatan)
		print("Jenis Kegiatan :", self.jenisKegiatan)
		print("Hari/tgl :", self.hari, ",",self.tanggal, "/",self.bulan, "/",self.tahun)
		print("Waktu :", self.jam,":",self.menit,"WIB")
		print("Tempat :", self.namaTempat)

	def ubahJadwal(self):
		print("|"," "*11,"UBAH JADWAL"," "*9,"|")
		self.namaKegiatan = input("Nama Kegiatan :")
		self.jenisKegiatan = input("Jenis Kegiatan :")
		self.hari = input("Hari :")
		self.tanggal = int(input("Tanggal :"))
		self.bulan = int(input("Bulan :"))
		self.tahun = int(input("Tahun :"))
		self.jam = int(input("Jam :"))
		self.menit = int(input("Menit :"))
		self.namaTempat = input("Tempat :")
		
j=jadwal()
j.tampilJadwal()
j.ubahJadwal()
j.tampilJadwal()