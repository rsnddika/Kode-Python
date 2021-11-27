class Pendaftaran:

	def PendaftaranServis(self, namaPelanggan, tipe, produsen):
		self.namaPelanggan = namaPelanggan
		self.tipe = tipe
		self.produsen = produsen


	def DataPendaftar(self):
		print("Nama Pelanggan :",self.namaPelanggan)
		print("Tipe :",self.tipe)
		print("Produsen :",self.produsen)

p = Pendaftaran()
p.PendaftaranServis("Risnanda","Mobil","Toyota")
p.DataPendaftar()