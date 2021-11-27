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
    def jarak (self):
        return sqrt(((self.b.x - self.a.x)**2)+((self.b.y - self.a.y)**2))
    @property
    def Waktu(self):
        kecepatan = 333.333
        kecepatan = float (kecepatan)
        memuat_sembako = 1
        memuat_sembako = float(memuat_sembako)
        selesai = 5
        selesai = float(selesai)
        return (((self.jarak*2) / kecepatan) + memuat_sembako + selesai)
        
    #input
Asnawi, Agung = Titik(0 , 0), Titik(-4 , -1)
Dayat, Arif= Titik(2 , -2), Titik(-2 , -2)
Hanafi, Nayla = Titik(6 , -1), Titik(7 , 1)
Kharisma, Ulfi = Titik(3, 3), Titik(-5 , 3)
Aris, Tika = Titik(-3, 5), Titik(2,7)

Jalan = [
	jalan(Asnawi, Agung),
	jalan(Asnawi, Dayat),
    jalan(Asnawi, Arif),
	jalan(Asnawi, Hanafi),
	jalan(Asnawi, Nayla),
	jalan(Asnawi, Kharisma),
	jalan(Asnawi, Ulfi),
	jalan(Asnawi, Aris),
    jalan(Asnawi,Tika),
]
#PROSES
jarak = 0
Waktu = 0
for rute in Jalan:
    jarak += rute.jarak
    Waktu += rute.Waktu
bolak_balik = jarak*2
print("Jarak Tempuhnya adalah: ", bolak_balik)
print("Waktu yang diperlukan : ", Waktu)

    
        
    