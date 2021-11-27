# program untuk mencari persamaan kuadrat
from math import sqrt
 
# input
a = float(input("Masukkan nilai koefisien kuadrat: "))
print(a) # khusus di ideone.com
b = float(input("Masukkan nilai koefisien linier: "))
print(b) # khusus di ideone.com
c = float(input("Masukkan nilai koefisien konstan: "))
print(c) # khusus di ideone.com
 
try:
	# proses
	if not a:
		raise ValueError("Koefisien kuadrat tidak boleh nol")
	D = b**2 - 4*a*c
	if D < 0:
		raise ValueError("Diskriminan negatif, persamaan tidak memiliki akar")
	if D == 0:
		x = -b/(2*a)
		hasil = [x]
	else:
		x1 = (-b + sqrt(D))/(2*a)
		x2 = (-b - sqrt(D))/(2*a)
		hasil = [x1, x2]
 
	# output
	if len(hasil) == 1:
		print("Akarnya adalah", hasil[0])
	else:
		print("Akarnya adalah", hasil[0], "dan", hasil[1])
except ValueError as error:
	print(error)