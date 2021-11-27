usia = int(input("Masukkan usia Anda: "))

if(usia >= 17):
 	print("Anda wajib memiliki KTP")

elif(usia<17 and usia>0):
	print("Usia dibawah 17 tahun tidak berhak memiliki KTP")

elif(usia<=0):
	print("Input tidak valid")