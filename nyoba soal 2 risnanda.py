print(" ———Toko Risnanda———")
def total(harga):
	"fungsi untuk menghitung Total bayar"
	return harga

#input data
harga  = int(input("masukan total pembelian: "))
Total  = total(harga)

#diskon 5% total pembelian di atas Rp.1jt
if  Total>1000000:
	Total=Total-0.05*Total

elif Total>1000000:
	diskon=Total*(5/100)

else:
	diskon=Total*(0.10/100)

print("total harga = ", "Rp.",Total)