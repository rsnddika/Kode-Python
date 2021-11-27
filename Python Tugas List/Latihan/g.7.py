a = {"keju", "tepung", "garam", "gula", "coklat"}
b = {"garam", "gula", "coklat", "kecap"}
b.add("keju")

a.discard("garam")

#barang yang tidak sama di pembelian pertama dan kedua (symmetric difference)

a ^= (b)
print(a)