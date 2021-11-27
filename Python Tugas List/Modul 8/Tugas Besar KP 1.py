print("	        STREET BOBA         ")                                                   
print("                  Alamat                  ")                                 
print("Pantog Wetan,Banjaroyo,Kalibawang,Kulon Progo")                          
print("         No. Telp : 085047908890          ")
print(" ===||||||PRICELIST STREET BOBA||||||===  ")
def option( ) :
    print("=====================================================")
    print("Silahkan Pilih Salah Satu Dari Menu Boba Berikut Ini;")
    print("1. Astro Signature")
    print("2. Boba Popcorn")
    print("3. Sugus Jeruk")
    print("4. Sugus Anggur")
    print("5. keluar")
    pilihan = int(input("Masukkan Nomor Pilihan Anda Dan Tekan 5 Jika Keluar:"))
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

pilihan = option()
while pilihan:
	if (pilihan==5 or pilihan==0):
		print("       TERIMA KASIH ATAS PESANAN ANDA      ") 
		print("              MOHON DITUNGGU               ")
		break;
	else:
		banyak=int(input("List Jumlah Pesanan Yang Akan Dipesan:"))
		jenis=str(input("Jenis Ukuran Yang Dipilih(M/L):"))
		if(pilihan==1 and jenis=="M"):
			Am = ((18000)*banyak)
			print("Total biaya =%i"%Am)
		elif(pilihan==1 and jenis=="L"):
			Al = ((36000)*banyak)
			print("Total biaya =%i"%Al)
		elif(pilihan==2 and jenis=="M"):
			BPl = ((25000)*banyak)
			print("Total biaya =%i"%BPl)
		elif(pilihan==2 and jenis=="L"):
			BPl = ((50000)*banyak)
			print("Total biaya =%i"%BPl)
		elif(pilihan==3 and jenis=="M"):
			SJm = ((17000)*banyak)
			print("Total biaya =%i"%SJm)
		elif(pilihan==3 and jenis=="L"):
			SJm = ((34000)*banyak)
			print("Total biaya =%i"%SJm)
		elif(pilihan==4 and jenis=="M"):
			SJa = ((17000)*banyak)
			print("Total biaya =%i"%SJa)
		elif(pilihan==4 and jenis=="L"):
			SJa = ((34000)*banyak)
			print("Total biaya =%i"%SJa)
			break;
		else:
			print("Maaf Kode Yang Anda Masukan Salah")
		pilihan=option()