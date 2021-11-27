total=int(input("total = "))

if (1000000<total<2000000):
	diskon=total*(5/100)
elif (total>2000000):
	diskon=total*(10/100)
else:
	diskon=total*(0/100)

setelah_diskon=total-diskon

print('diskonnya yaitu:{}'.format(int(diskon)))
print('harga setelah diskon:{}'.format(int(setelah_diskon)))