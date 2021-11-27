print("=====Boba rama=====")
def option():
    print("Pilih salah satu dari menu boba berikut ini :")
    print("1. Astro Signature")
    print("2. Boba Popcorn")
    print("3. Sugus Jeruk")
    print("4. Sugus Anggur")
    print("5. Classic Chocolate")
    print("6. Astro Berry")
    print("7. Es Kobar")
    print("8. Honey Latte")
    print("9. keluar")
    pilihan = int(input("Masukkan List Nomor Minuman:"))
    return pilihan

#1
def Astro_Signature_medium(banyak):
	Am = ((18000)*banyak)
	return A
def Astro_Signature_large(banyak):
	Al = ((36000)*banyak)
	return A

#2
def Boba_Popcorn_medium(banyak):
	BPm = ((25000)*banyak)
	return BPm
def Boba_Popcorn_Large(banyak):
	BPl = ((50000)*banyak)
	return BPl

#3
def Sugus_Jeruk_medium(banyak):
	SJm = ((17000)*banyak)
	return SJm
def Sugus_Jeruk_large(banyak):
	SJl = ((34000)*banyak)
	return SJl

#4	
def Sugus_Anggur_medium(banyak):
	SAm = ((17000)*banyak)
	return SAm
def Sugus_Anggur_large(banyak):
	SAl = ((34000)*banyak)
	return SAl

#5
def Classis_Chocolate_medium(banyak):
	CCm = ((24000)*banyak)
	return CCm
def Classis_Chocolate_large(banyak):
	CCl = ((48000)*banyak)
	return CCl

#6	
def Astro_Berry_medium(banyak):
	ABm = ((24000)*banyak)
	return ABm
def Astro_Berry_large(banyak):
	ABl = ((48000)*banyak)
	return ABl

#7
def Es_Kobar_medium(banyak):
	EKm = ((18000)*banyak)
	return EKm
def Es_Kobar_large(banyak):
	EKl = ((36000)*banyak)
	return EKl

#8
def Honey_Latte_medium(banyak):
	HLm = ((17000)*banyak)
	return HLm
def Honey_Latte_large(banyak):
	HLm = ((34000)*banyak)
	return HLm

pilihan = option()
while pilihan:
	if (pilihan==9 or pilihan==0):
		print("Terima kasih telah berkunjung di toko kami")
		break;
	else:
		banyak=int(input("List Jumlah Pesanan :"))
		jenis=str(input("Jenis Porsi Yang Dipilih (Medium/Large) :"))
		if(pilihan==1 and jenis=="medium"):
			Am = ((18000)*banyak)
			print("Total biaya =%i"%Am)
		elif(pilihan==1 and jenis=="large"):
			Al = ((36000)*banyak)
			print("Total biaya =%i"%Al)
		elif(pilihan==2 and jenis=="medium"):
			BPl = ((25000)*banyak)
			print("Total biaya =%i"%BPl)
		elif(pilihan==2 and jenis=="large"):
			BPl = ((50000)*banyak)
			print("Total biaya =%i"%BPl)
		elif(pilihan==3 and jenis=="medium"):
			SJm = ((17000)*banyak)
			print("Total biaya =%i"%SJm)
		elif(pilihan==3 and jenis=="large"):
			SJm = ((34000)*banyak)
			print("Total biaya =%i"%SJm)
		elif(pilihan==4 and jenis=="medium"):
			SJa = ((17000)*banyak)
			print("Total biaya =%i"%SJa)
		elif(pilihan==4 and jenis=="large"):
			SJa = ((34000)*banyak)
			print("Total biaya =%i"%SJa)
		elif(pilihan==5 and jenis=="medium"):
			CCm = ((24000)*banyak)
			print("Total biaya =%i"%CCm)
		elif(pilihan==5 and jenis=="large"):
			CCl = ((48000)*banyak)
			print("Total biaya =%i"%CCl)
		elif(pilihan==6 and jenis=="medium"):
			ABm = ((24000)*banyak)
			print("Total biaya =%i"%ABm)
		elif(pilihan==6 and jenis=="large"):
			ABl = ((48000)*banyak)
			print("Total biaya =%i"%ABl)
		elif(pilihan==7 and jenis=="medium"):
			EKm = ((18000)*banyak)
			print("Total biaya =%i"%EKm)
		elif(pilihan==7 and jenis=="large"):
			EKl = ((36000)*banyak)
			print("Total biaya =%i"%EKl)
		elif(pilihan==8 and jenis=="medium"):
			HLm = ((17000)*banyak)
			print("Total biaya =%i"%HLm)
		elif(pilihan==8 and jenis=="large"):
			HLl = ((34000)*banyak)
			print("Total biaya =%i"%HLl)
		else:
			print("input salah")
		pilihan=option()