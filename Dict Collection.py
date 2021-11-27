d_nilai = {
	'dika': 'A',
	'maha': 'B',
	'putra': 'C',
	'rio': 'D',
}

print("Daftra Nilai:", d_nilai)

print("Panjang Dictionary:", len(d_nilai), "\n")

d_nilai['citra'] = 'B'
print("Perubahan Dict1:", d_nilai)

d_nilai['tony'] = 'A'
print("Perubahan Dict2:", d_nilai)
print("Panjang Dictionary:", len(d_nilai), "\n")

del d_nilai['citra']
print("Perubahan Dict3:", d_nilai)
print("Panjang Dictionary:", len(d_nilai), "\n")

d_nilai.clear()
print("Perubahan Dict4:", d_nilai)
print("Panjang Dictionary:", len(d_nilai), "\n")