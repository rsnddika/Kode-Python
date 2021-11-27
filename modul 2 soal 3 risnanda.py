status = str(input("Apakah status anda langganan? (Y / N) :"))
lembar = int(input("Jumlah Lembar :"))

if(status == 'Y') or (status == 'y'):
	print("total bayar = Rp.",lembar * 100)

elif(status == 'N') or (status == 'n'):
	if(lembar < 100):
		print("total bayar = Rp.",lembar * 150)
	else:
		print("total bayar = Rp.",lembar * 125)
		
else:
	print("Input tidak valid")