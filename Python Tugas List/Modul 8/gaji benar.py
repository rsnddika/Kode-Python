def option():
    print("Pilih salah satu dari tiga fungsionalitas berikut:")
    print("A. Golongan 1")
    print("B. Golomgan 2")
    print("C. Golongan 3")
    print("D. Keluar")
    pilihan = int(input("Masukkan pilihan Anda (A/B/C/D):"))
    return pilihan

def golongan_1(golongan):
	A=(25000*(jam))
	return A
def golongan_2(jam):
	B=(40000*(jam))
	return B
def golongan_3(jam):
	C=(50000*(jam))
	return C

pilihan = option()
while pilihan<5 : 
	if(pilihan==4 or pilihan==0):
		print("Goodbye")
		break ;
	else:
		jam= int(input("Masukan jam lembur : "))
		if(pilihan==1):
			A=(25000*(jam))
			print("upah lembur yang diterima = %i"%(A))
		elif(pilihan==2):
			B=(40000*(jam))
			print("upah lembur yang diterima = %i"%(C))
		elif(pilihan==3):
			C=(50000*(jam))
			print("upah lembur yang diterima = %i"%(C))