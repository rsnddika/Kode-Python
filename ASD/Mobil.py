class Mobil:
    def _init_(self, merk, tipe, warna, harga):
        self.merk = merk
        self.tipe = tipe
        self.warna = warna
        self.harga = harga
        self.nama = merk + ' ' + tipe

    def berjalan(self):
        print(f'Mobil {self.nama} berjalan...')

    def berhenti(self):
        print(f'Mobil {self.nama} berhenti...')

    def menabrak(self, mobil):
        print(f'Mobil {self.nama} menabrak mobil {mobil.nama}...')


mobil1 = Mobil('Toyota', 'Avanza', 'silver', 180_000_000)
mobil2 = Mobil('Honda', 'City', 'putih', 300_000_000)
mobil2.berjalan()
mobil1.berhenti()
mobil2.menabrak(mobil1)