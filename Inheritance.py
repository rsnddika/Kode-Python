class Person :
	#self.nik
	#self.tinggi_badan
	#self.nama
	#self.jenis_kelamin
	#self.tempat_lahir
	#self.tanggal_lahir
	#self.golongan_darah
	#self.berat_badan
	#self.alamat	
	
#method
	def inputDataPerson(self):
		self.nama = str(input("Nama : "))
		self.nik = str(input("NIK :"))
		self.tinggi_badan = int(input("Tinggi Badan : "))
		self.jenis_kelamin = str(input("Jenis Kelamin : "))
		self.tanggal_lahir = str(input("Tanggal Lahir : "))
		self.golongan_darah = str(input("Golongan Darah : "))
		self.berat_badan = str(input("Berat Badan : "))
		self.tempat_lahir = str(input("Tempat Lahir : "))
		self.alamat = str(input("Alamat : "))
		
	def tampilDataPerson(self):
			print("Nama 	: ",self.nama)
			print("NIK 				: ",self.nik)
			print("Tinggi Badan 	: ",self.tinggi_badan)
			print("Jenis Kelamin 	: ",self.jenis_kelamin)
			print("Tanggal Lahir 	: ",self.tanggal_lahir)
			print("Golongan Darah 	: ",self.golongan_darah)
			print("Berat Badan 		: ",self.berat_badan)
			print("Tempat Lahir 	: ",self.tempat_lahir)
			print("Alamat 			: ",self.alamat)

p = Person()
p.inputDataPerson()
p.tampilDataPerson()

class Employee(Person):	
#atribut
#self.id_employee
#self.pekerjaan
#self.gaji
#self.tahun_masuk
#self.status
			
#method
	def inputDataEmployee(self):
		Person.inputDataPerson(self)
		self.id_employee = str(input("ID Employee : "))
		self.pekerjaan = str(input("Pekerjaan : "))
		self.gaji = int(input("Gaji : "))
		self.tahun_masuk = int(input("Tahun Masuk : "))
		self.status = str(input("Status : "))
		
	def tampilDataEmployee(self):
		print("Nama 	:",self.nama)
		print("NIK 				: ",self.nik)
		print("Tinggi Badan 	: ",self.tinggi_badan,"cm")
		print("Jenis Kelamin 	: ",self.jenis_kelamin)
		print("Tanggal Lahir 	: ",self.tanggal_lahir)
		print("Golongan Darah 	: ",self.golongan_darah)
		print("Berat Badan 		: ",self.berat_badan,"kg")
		print("Tempat Lahir 	: ",self.tempat_lahir)
		print("Alamat 			: ",self.alamat)
		print("ID Employee 		: ",self.id_employee)
		print("Pekerjaan 		: ",self.pekerjaan)
		print("Gaji 			: ","Rp.",self.gaji)
		print("Tahun Masuk 		: ",self.tahun_masuk)
		print("Status 			: ", self.status)

	def hitungMasaKerja(self,tahun_masuk):
		self.tahunSekarang = int(input("Tahun sekarang :"))
		lama = self.tahunSekarang - self.tahun_masuk
		print("Masa Kerja :", lama, "Tahun")

e = Employee ()
e.inputDataEmployee()
e.tampilDataEmployee()

class Customer(Person):	
#atribut
#self.id_customer
#self.poin
			
#method
	def inputDataCustomer(self):
		Person.inputDataPerson(self)
		self.id_customer = str(input('ID Customer : '))
		self.poin = str(input('Poin : '))
		
	def tampilDataCustomer(self):
		print("Nama 	:",self.nama)
		print("NIK 				: ",self.nik)
		print("Tinggi Badan 	: ",self.tinggi_badan,"cm")
		print("Jenis Kelamin 	: ",self.jenis_kelamin)
		print("Tanggal Lahir 	: ",self.tanggal_lahir)
		print("Golongan Darah 	: ",self.golongan_darah)
		print("Berat Badan 		: ",self.berat_badan,"kg")
		print("Tempat Lahir 	: ",self.tempat_lahir)
		print("Alamat 			: ",self.alamat)
		print("ID Customer 		: ",self.id_customer)
		print("Poin 			: ",self.poin)

	def tambahPoin(self,poin):
		self.tambahPoin = int(input("Tambah Poin :"))
		totalPoin = self.tambahPoin + self.poin
		print("Total Poin :", totalPoin, "Poin")

f = Customer ()
f.inputDataCustomer()
f.tampilDataCustomer()