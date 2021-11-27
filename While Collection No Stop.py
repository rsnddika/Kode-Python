class Hero(object):
	def __init__(self):
 		self.nama = nama
 		self.alias = alias
 		self.kelompok = kelompok

#Isian Berapa Yang Ingin Kita Masukkan 
listHero = []
ask = int(input('Mau Isi Berapa Data?'))

#Masukan (Nama, Alias, Kelompok)
stop = False
while(not stop):
	nama = input('Masukan Nama Hero:')
	alias = input('Masukan Nama Alias:')
	kelompok = input('Masukan Nama Kelompok:')
	print('/'*25)

	listHero.append(Hero(nama, alias, kelompok))
	
	ask = input('Apakah Ingin Lagi?[y/n]')
	if (ask == 'n' or ask == 'N')
		stop = True
		
print("Hero Pertama:", listHero[0].nama, "\n")
#Cetak Hero
print("Daftar superhero:\n")

for Hero in listHero:
	print("Nama: {}\nAlias: {}\n\n".format(
		Hero.nama, Hero.alias, Hero.kelompok))