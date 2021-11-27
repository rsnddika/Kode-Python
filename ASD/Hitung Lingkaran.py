from math import pi
 
class Lingkaran:
	def _init_(self, d):
		self.d = d
	@property
	def luas(self):
		r = self.d/2
		return pi*r**2
 
# input
A = Lingkaran(15)
B = Lingkaran(3)
C = Lingkaran(7)
 
# proses
luas = A.luas - B.luas - C.luas
 
# output
print(luas)