from math import sqrt

class Titik:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

class jalan:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def jarak(self):
        return sqrt ((
        (self.b.x - self.a.x)**2) + ((self.b.y - self.a.y)**2))

    @property
    def Waktu(self):
        #cepatan waktu
        kecepatan = 333.333
        kecepatan = float (kecepatan)
        #memuat 
        memuat = 1
        memuat = float (memuat)
        #waktu selesai      
        selesai = 5
        selesai = float (selesai) 
        #jarak yang diperlukan
        return ((
        (self.jarak*2) / kecepatan) + memuat + selesai)

#Input
Asnawi, Arif = Titik(0 , 0), Titik(-2 , -2)
Agung, Ulfi = Titik(-4, -1), Titik(-5, 3)
Aris, Tika = Titik(-3, 5), Titik(2, 7)
Kharisma, Nayla = Titik(3, 3), Titik(7 , 1)
Hanafi, Dayat = Titik(6 , -1), Titik(2 , -2)

Jalan = [
	jalan(Asnawi, Arif),
	jalan(Asnawi, Agung),
    jalan(Asnawi, Ulfi),
	jalan(Asnawi, Aris),
	jalan(Asnawi, Tika),
	jalan(Asnawi, Kharisma),
	jalan(Asnawi, Nayla),
	jalan(Asnawi, Hanafi),
    jalan(Asnawi, Dayat),
]

#Proses
Waktu = 0
jarak = 0
for lama in Jalan:
    Waktu += lama.Waktu
    jarak += lama.jarak
bolak_balik = jarak*2
print("Waktu diperlukan : ", Waktu)
print("Jarak tempuh adalah: ", bolak_balik)