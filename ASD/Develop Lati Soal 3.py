#Bilangan Prima
def is_prima(x):
  
  for i in range(2, x):
#Untuk mengetahui apakah suatu bilangan bisa dibagi oleh 
#bilangan lain adalah dengan operator modulus (%).
    if x % i == 0:		#Operator tersebut akan mengembalikan hasil bagi dari 2 operan. 
    					#Jika hasil bagi dari 2 operan bernilai 0, maka itu artinya bilangan tersebut memang bisa dibagi oleh angka pembagi.
      return False
  return True
#Sekarang, bisa panggil fungsi is_prima() 
#untuk memeriksa beberapa bilangan, apakah termasuk bilangan prima atau bukan:
print(is_prima(5))
print(is_prima(6))


#def cari_bilangan_prima (awal, akhir):
#  list_bilangan_prima = []

#  for x in range(awal, akhir + 1):
#    if is_prima(x):
#      list_bilangan_prima.append(x)

#  return list_bilangan_prima

#print(cari_bilangan_prima(1, 10))
#print(cari_bilangan_prima(20, 30))

