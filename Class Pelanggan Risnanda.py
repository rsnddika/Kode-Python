class Pelanggan :
	#self.nama
	#self.id_pelanggan
	#self.alamat	
	
#method
	def inputDataPelanggan(self):
		self.nama = str(input("Nama : "))
		self.id_pelanggan = str(input("ID Pelanggan :"))
		self.alamat = str(input("Alamat : "))
		
	def tampilDataPelanggan(self):
		print("Nama 			 : ",self.nama)
		print("ID Pelanggan		 : ",self.id_pelanggan)
		print("Alamat 			 : ",self.alamat)

	#self.nama_baru
	#self.id_pelanggan
	#self.alamat	

#method
	def inputPelbaru(self):
		self.nama_baru = str(input("Nama Baru : "))
		self.id_pelanggan_baru = str(input("ID Pelanggan Baru : "))
		self.alamat = str(input("Alamat : "))
	
	def tampilPelbaru(self):
		print("Nama Baru 	: ",self.nama_baru)
		print("ID Pelanggan Baru : ",self.id_pelanggan_baru)
		print("Alamat 		: ",self.alamat)

x = Pelanggan()
x.inputDataPelanggan()
x.tampilDataPelanggan()
x.inputPelbaru()
x.tampilPelbaru()