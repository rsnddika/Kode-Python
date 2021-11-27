#no 1
print("soal no satu")
dict={"mady":8, "roger":5, "paul":5, "lucy":7}
for index, data in  dict.items():
	print("nilai %s = %s"%(index,data))

#no 2
print("soal no dua")
dict2 = {"ken":8, "andrea":7, "smith":6}
for index, data in  dict2.items():
	print("nilai %s = %s"%(index,data))

#no 3
print("soal no tiga")
dict={"mady":8, "roger":5, "paul":5, "lucy":7}
dict2 = {"ken":8, "andrea":7, "smith":6}
dict.update(dict2)
for index, data in dict.items():
	print("nilai %s = %s" %(index,data))

#no 4
print("soal no empat")
dict={"mady":8, "roger":5, "paul":5, "lucy":7, "ken":8, "andrea":7, "smith":6}
dict["Roger"]=8
dict["Paul"]=8
dict["Smith"]=8
print(dict)

#no 5
print("soal no lima")
dict={"Mady=":8, "Roger=":5, "Paul =":5, "Lucy=":7, "Ken=":8, "Andrea=":7, "Smith=":6}
for index,data in dict.items():
	if data >= 8:
		print("Nama = %s nilai : %s"%(index,data))