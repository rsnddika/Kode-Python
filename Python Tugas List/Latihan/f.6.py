a = {"keju", "tepung", "garam", "gula", "coklat"}
b = {"garam", "gula", "coklat", "kecap"}
b.add("keju")

a.discard("garam")

#f = barang yang dibeli di hari kedua, tapi tidak dibeli dihari pertama

f = b.difference(a)
print(f)