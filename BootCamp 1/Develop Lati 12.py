#Luas Lingkaran
phi = 3.14 # merupakan variabel global
def luas_lingkaran(r):
		d = (r + r) ^ 2 # d adalah variabel local
		luas = 1/4 * phi * d
		return luas

def keliling_lingkaran(r):
		keliling = 2 * phi * r
		return keliling

print(luas_lingkaran(7)) #memanggil fungsi 

print(keliling_lingkaran(14)) #memanggil fungsi keliling_lingkaran