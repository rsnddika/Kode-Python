#mengetahui keanggotaan
set = {1,2,3,4,5}
data = 1 in set
print(data)

#mengetahui bukan  keanggotaan
set = {1,2,3,4,5}
data = 1 not in set
print(data)

#Mengetahui isi set merupakan keanggotaan dari set lainnya
a = {1,2,3,4,5}
b = {1,2,3,4}

#semua isi data dari set a merupakan keanggotaan dari set b
c = a <= b
print(c)

#semua isi data dari set b merupakan keanggotaan dari set a
c = a >= b
print(c)