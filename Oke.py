class Customer(Person):
	#atribut
	#self.id_cutomer
	#self.poin
	def inputDataCustomer(self):
		print("-"*37)
		print("|"," "*9,"Input Customer"," "*8,"|")
		print("-"*37)
		Person.inputDataPerson(self)
		self.id_customer = str(input("ID Customer :"))
		self.poin = int(input("Poin :"))
	def tampilDataCustomer(self):
		print("-"*37)
		print("|"," "*12,"Customer"," "*11,"|")
		print("-"*37)
		print("Nama :",self.nama)
		print("Tempat Lahir :",self.tempat_lahir)
		print("Tanggal Lahir :",self.tanggal_lahir)
		print("Jenis Kelamin :",self.jenisKelamin)
		print("NIK :",self.nik)
		print("Tinggi Badan :",self.tinggiBadan,"cm")
		print("Berat Badan :",self.beratBadan,"kg")
		print("Golongan Darah :",self.golonganDarah)
		print("Alamat :",self.alamat)
		print("ID Customer :",self.id_customer)
		print("Poin :",self.poin)
	def tambahPoin(self,poin):
		self.tambahPoin = int(input("Tambah Poin :"))
		totalPoin = self.tambahPoin + self.poin
		print("Total Poin :", totalPoin, "Poin")

b = Customer()
b.inputDataCustomer()
b.tambahPoin('poin')
b.tampilDataCustomer()