class Polygon:

	def __init__(self, banyak_sisi):
 		self.n = banyak_sisi
 		self.sisi = [0 for i in range(banyak_sisi)]
	def inputSisi(self):
 		print("Masukkan panjang sisi (dalam cm):")
 		self.sisi = [float(input("Sisi "+str(i+1)+":")) for i in range(self.n)]
 		print()
	def printSisi(self):
 		for i in range(self.n):
 			print("Panjang sisi",i+1,"adalah",self.sisi[i],"cm")

class Segitiga(Polygon):
# Nomor 2
	def __init__(self):
		Polygon.__init__(self,2)
		print("Segitiga")
	def hitungLuas(self):
		a,t = self.sisi
		l = a*t/2
		print("Luas Segitiga",l,"cm^2")
# Nomor 3
class SegiLima(Polygon):
	def __init__(self):
		Polygon.__init__(self,5)
		print("Keliling Segi Lima")
	def hitungKeliling(self):
		f,g,h,i,j = self.sisi
		k = f,g,h,i,j
		print("Keliling :",j,"cm")

# Nomor 4
s = Segitiga()
s.inputSisi()
s.printSisi()
s.hitungLuas()
k = SegiLima()
k.inputSisi()
k.printSisi()
k.hitungKeliling()