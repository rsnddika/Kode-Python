def option():
    print("Pilih salah satu dari tiga fungsionalitas berikut:")
    print("1. Konversi suhu C-R")
    print("2. Konversi suhu C-F")
    print("3. Keluar dari program")
    pilihan = int(input("Masukkan pilihan Anda (1/2/3):"))
    return pilihan

def celcius_reamur(celcius):
    R=((4/5)*celcius)
    return R
    
def celcius_fahrenheit(celcius):
    F =(celcius * 9/5) + 32
    return F

pilihan = option()
while pilihan<4 : 
    if(pilihan==3 or pilihan==0):
        print("Terimakasih telah menggunakan program kami")
        break ;
    else:
        celcius= int(input("Masukan Suhu : "))
        if(pilihan==1):
            R = celcius_reamur(celcius)
            print("Konversi Reamur = %i"%(R))
        elif(pilihan==2):
            F = celcius_fahrenheit(celcius)
            print("Konversi fahrenheit = %i"%(F))
    pilihan = option()