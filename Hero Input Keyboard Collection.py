class Hero(object):
	def __init__(self):
 		self.nama = nama
 		self.alias = alias
 		self.kelompok = kelompok

#Isian Berapa Yang Ingin Kita Masukkan 
listHero = []
ask = int(input('Mau Isi Berapa Data?'))

#Masukan Nama, Alias, Kelompok
i = 0
for i in range(ask):
	nama = input('Masukan Nama Hero:')
	alias = input('Masukan Nama Alias:')
	kelompok = input('Masukan Nama Kelompok:')

	listHero.append(Hero(nama, alias, kelompok))

print("Hero Pertama:", listHero[0].nama, "\n")
	
print("Daftar superhero:\n")

for Hero in listHero:
	print("Nama: {}\nAlias: {}\n\n".format(
		Hero.nama, Hero.alias, Hero.kelompok))