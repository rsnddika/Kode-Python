print("Mata Kuliah Mahasiswa Unjaya 2020")

Banyak_Mahasiswa=int(input("Banyak Mahasiswa = "))
for i in range(0, Banyak_Mahasiswa,):
	print("Mahasiswa_ke",i+1)
	for j in range(4):
		if(j==0):
			mata_kuliah=str(input("Konsep_Pemrograman:"))
		elif(j==1):
			mata_kuliah=str(input("Logika_Informatika:"))
		elif(j==2):
			mata_kuliah=str(input("Bahasa_Inggris:"))
		else:
			mata_kuliah=str(input("Pendidikan_Kewarganegaraan:"))