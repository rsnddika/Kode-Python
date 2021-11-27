a = float(input("Masukan nilai koefisien kuadrat: "))
if not a:
	print("koefisien kuadrat tidak boleh nol")
else:
	b = float(input("Masukkan nilai koefisien linier: "))
	c = float(input("Masukkan nilai koefisien konstan: "))

	D = b**2 - 4*a*c
	if D < 0:
		print("Deskripsikan negatif, persamaan tidak memiliki akar")
	elif D == 0:
		x = -b/(2*a)
		print("Akarnya adalah", x)
	else:
		x1 = (-b + sqrt(D))/(2*a)
		x2 = (-b - sqrt(D))/(2*a)
		print("Akarna adalah", x1, "dan", x2)