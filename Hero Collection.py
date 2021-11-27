class Hero(object):
	def __init__(self, nama=None, alias=None, kelompok=None):
		self.nama = nama
		self.alias = alias
		self.kelompok = kelompok

listHero = []
listHero.append(Hero("Anthony Edward Stark","Iron Man","Avengers"))
listHero.append(Hero("Peter Jason Quill","Star-Lord","Guardians of Galaxy"))
listHero.append(Hero("Barry Allen","The Flash","Justice League"))
listHero.append(Hero("Thor Odinson","God of Thunder","Avengers"))
listHero.append(Hero("Bruce Wayne","Batman","Justice League"))

print("Hero Pertama:", listHero[0].nama, "\n")

print("Daftar Superhero:\n")
for Hero in listHero:
	print("Nama: {}\nAlias: {}\nKelompok: {}\n\n".format(Hero.nama, 
		Hero.alias, Hero.kelompok))