# Penggunaan try dan except
class Hero(object):
	def __init__(self, nama=None, alias=None, kelompok=None, kondisi=None):
		self.nama = nama
		self.alias = alias
		self.kelompok = kelompok
		self.kondisi = kondisi

listHero = []
listHero.append(Hero("Anthony Edward Stark","Iron Man","Avengers","Mati"))
listHero.append(Hero("Peter Jason Quill","Star-Lord","Guardians of Galaxy","Hilang"))
listHero.append(Hero("Barry Allen","The Flash","Justice League","Hidup"))
listHero.append(Hero("Thor Odinson","God of Thunder","Avengers","Hidup"))
listHero.append(Hero("Bruce Wayne","Batman","Justice League","Hidup"))

def panggilHero(pahlawan):
	assert(pahlawan.kelompok == "Avengers"), "Hero tidak bisa dipanggil."
	return print("Avengers Berkumpul!")

try:
	panggilHero(listHero[0])

#Assertion error pada program bisa digunakan sebagai output dengan mengganti sbb
except AssertionError as error:
	print(error)
	print('Hero bukan bagian dari Avengers!')

#Penggunaan try, except, dan else
else:
	k = listHero[0].kelompok
	print("Hero bagian dari",k+'!')

#Penggunaan finally
finally:
	print('Resume:')
	print('/'*30)
	print("Nama: {}\nAlias: {}\nKondisi: {}".format(listHero[0].nama, listHero[0].alias, listHero[0].kondisi))
	print('/'*30)