print("=====================================================")
print("	        WOKEEE BOBA         ")                                                   
print("                  Alamat                  ")                              
print("Daerah Istimewa Yogyakarta, Sleman, 584785")                         
print("         No. Telp : 08**********          ")
print(" =========PRICELIST STREET BOBA=========  ")
def option( ) :
    print("=====================================================")
    print("Silahkan Pilih Salah Satu Dari Menu Boba Berikut Ini;")
    print("1. Susu Vanilla")
    print("2. Susu Mangga")
    print("3. Susu Jeruk")
    print("4. Susu Anggur")
    print("5. keluar")
    pilihan = str(input("Masukkan Nama Anda: "))
    pilihan = int(input("Masukkan Nomor Meja: "))
    pilihan = int(input("Masukkan Menu Pilihan Anda Dan Tekan 5 Jika Keluar: "))
    return pilihan

#1
def Susu_Vanilla_medium(banyak):
	Sm = ((45000)*banyak)
	return S
def Susu_Vanilla_large(banyak):
	Sl = ((65000)*banyak)
	return S

#2
def Susu_Mangga_medium(banyak):
	SMm = ((50000)*banyak)
	return SMm
def Susu_Mangga_Large(banyak):
	SMl = ((70000)*banyak)
	return SMl

#3
def Susu_Jeruk_medium(banyak):
	SJm = ((55000)*banyak)
	return SJm
def Susu_Jeruk_large(banyak):
	SJl = ((75000)*banyak)
	return SJl

#4	
def Susu_Anggur_medium(banyak):
	SAm = ((60000)*banyak)
	return SAm
def Susu_Anggur_large(banyak):
	SAl = ((80000)*banyak)
	return SAl

pilihan = option()
while pilihan:
	if (pilihan==5 or pilihan==0):
		print("       TERIMA KASIH ATAS PESANAN ANDA      ") 
		print("              MOHON DITUNGGU               ")
	else:
		banyak=int(input("List Jumlah Pesanan Yang Akan Dipesan:"))
		jenis=str(input("Jenis Ukuran Yang Dipilih(M/L):"))
		if(pilihan==1 and jenis=="M"):
			Sm = ((45000)*banyak)
			print("Total biaya =%i"%Sm)
		elif(pilihan==1 and jenis=="L"):
			Sl = ((65000)*banyak)
			print("Total biaya =%i"%Sl)
		elif(pilihan==2 and jenis=="M"):
			SMl = ((50000)*banyak)
			print("Total biaya =%i"%SMl)
		elif(pilihan==2 and jenis=="L"):
			SMl = ((70000)*banyak)
			print("Total biaya =%i"%SMl)
		elif(pilihan==3 and jenis=="M"):
			SJm = ((55000)*banyak)
			print("Total biaya =%i"%SJm)
		elif(pilihan==3 and jenis=="L"):
			SJm = ((75000)*banyak)
			print("Total biaya =%i"%SJm)
		elif(pilihan==4 and jenis=="M"):
			SJa = ((60000)*banyak)
			print("Total biaya =%i"%SJa)
		elif(pilihan==4 and jenis=="L"):
			SJa = ((80000)*banyak)
			print("Total biaya =%i"%SJa)
			break;
		else:
			print("Maaf Kode Yang Anda Masukan Salah")
		break;