a = {"keju", "tepung", "garam", "gula", "coklat"}
b = {"garam", "gula", "coklat", "kecap"}
b.add("keju")

#menghapus "garam" pada pembelian pertama

a.discard("garam")
print(a)
