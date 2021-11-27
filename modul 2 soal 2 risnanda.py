status = int(input("Apakah anda ingin mencari Luas lingkaran atau Keliling Lingkaran ? (1/2) :"))
r = int(input("Jari - jari :"))
phi_1 = 22/7
phi_2 = 3.14

if(status == 1):
	if(r / 7 == int):
		print("Luas lingkaran = ",phi_2 * (r*r))
	else:
		print("Luas lingkaran = ",phi_1 * (r*r))

elif(status == 2):
		if(r / 7 == int):
			print("Keliling lingkaran =",2*phi_2*r)
	1	else:
			print("Keliling lingkaran =",2*phi_1*r)

else:
	print("Input tidak valid")