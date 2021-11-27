#jika kondisi 1 dan 2 bernilai benar
x=7

if((x - 4) or (x + 4) == 11):
	print("2 kondisi bernilai benar")

#jika kondisi 1 bernilai benar dan kondisi 2 bernilai salah
x=4

if((x - 4) == 0) or ((x * 4) == 11):
	print("salah satu kondisi bernilai salah")

#jika kedua kondisi bernilai salah
x=7

if((x * 4) == 3) or ((x + 4) == 51):
	print("2 kondisi bernilai salah")