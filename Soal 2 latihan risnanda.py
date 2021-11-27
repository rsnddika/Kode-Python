print("———Toko Risnanda———")
def total(harga,jumlah):
	"fungsi untuk menghitung Total bayar"
	return harga*jumlah

#input data
harga= int(input("masukan harga barang: "))
jumlah= int(input("masukan jumlah baju yang dibeli: "))
Total=total(harga,jumlah)

#diskon 5% tiap pembelian di atas Rp.1jt
if Total>1000000:
	Total=Total-0.05*Total
print("Total Harga = ", "Rp.",Total)
Bayar=int(input("Jumlah Nominal Uang =" ))
Kembalian= (Bayar-Total)
print("Uang Kembalian = ", "Rp.",Kembalian)

#diskon 10% tiap pembelian di atas Rp.2jt
if Total>2000000:
	Total=Total-0.10*Total
print("Total Harga = ", "Rp.",Total)
Bayar=int(input("Jumlah Nominal Uang =" ))
Kembalian= (Bayar-Total)
print("Uang Kembalian = ", "Rp.",Kembalian)