# program untuk mencari persamaan kuadrat
from math import sqrt
 
# input
a = float(input("Masukkan nilai koefisien kuadrat: "))
print(a) # khusus di ideone.com
b = float(input("Masukkan nilai koefisien linier: "))
print(b) # khusus di ideone.com
c = float(input("Masukkan nilai koefisien konstan: "))
print(c) # khusus di ideone.com
 
# proses
if not a:
	hasil = "Koefisien kuadrat tidak boleh nol"
else:
	D = b**2 - 4*a*c
	if D < 0:
		hasil = "Diskriminan negatif, persamaan tidak memiliki akar"
	elif D == 0:
		x = -b/(2*a)
		hasil = f"Akarnya adalah {x}"
	else:
		x1 = (-b + sqrt(D))/(2*a)
		x2 = (-b - sqrt(D))/(2*a)
		hasil = f"Akarnya adalah {x1} dan {x2}"
 
# output
print(hasil)