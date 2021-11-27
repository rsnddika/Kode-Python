harga_makanan = int(input("Harga makanan: "))

if (harga_makanan<4000):
	print("Kriteria Murah")

elif (harga_makanan>7500):
	print("Kriteria Mahal")
	
elif (harga_makanan>4000 and harga_makanan<7500):
	print("Kriteria Sedang")