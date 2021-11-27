from math import sqrt

class Titik:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Sisi:
	def __init__(self, a, b):
		self.a = a
		self.b = b
		
	@property
	def panjang_sisi(self):
		return sqrt(
			(self.b.x - self.a.x)**2 + (self.b.y - self.a.y)**2
		)

# Input
A, B = Titik(1, 14), Titik(13,12)
C, D = Titik(4, 9), Titik(1, 6)
E, F = Titik(12, 8), Titik(14, 1)
G, H = Titik(5, 4), Titik(2, 2)
poligon = [
	Sisi(A, B),
	Sisi(B, C),
	Sisi(C, D),
	Sisi(D, E),
	Sisi(E, F),
	Sisi(F, G),
	Sisi(G, H)
]

# Proses
total = 0
for sisi in poligon:
	total += sisi.panjang_sisi

# Output
print(total)