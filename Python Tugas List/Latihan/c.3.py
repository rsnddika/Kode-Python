a = {"keju", "tepung", "garam", "gula", "coklat"}
b = {"garam", "gula", "coklat", "kecap"}
b.add("keju")

#c = barang yang sama(intersection) di pembelian pertama dan kedua

c = a&(b)
print(c)