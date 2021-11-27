#functional program untuk one liner
from functools import reduce
 
class Ruangan:
	def _init_(self, panjang, lebar):
		self.panjang = panjang
		self.lebar = lebar
	@property
	def luas(self):
		return self.panjang * self.lebar
 
 #input	
bangunan = [
	Ruangan(3, 4),
	Ruangan(4, 3),
	Ruangan(4, 3),
	Ruangan(8, 5),
	Ruangan(3, 4),
	Ruangan(4, 3),
	Ruangan(4, 4),
	Ruangan(4, 4),
	Ruangan(4, 4),
]
 
luas = reduce(lambda a, b: a + b.luas, bangunan, 0)
 
print(luas)