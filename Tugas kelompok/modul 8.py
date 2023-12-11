def pil() :
    print("pilih salah satu dari fungsi berikut : ")
    print("1. mencari luas persegi panjang")
    print("2. mencari keliling persegi panjang")
    print("3. keluar dari program")
    pilihan = int(input("masukan pilihan : "))
    return pilihan
def luas_persegi_panjang(panjang,lebar) :
    luas = panjang*lebar
    return luas
def keliling_persegi_panjang(panjang,lebar) :
    keliling = 2*(panjang+lebar)
    return keliling
pilihan = int()
while (pilihan<3):
    pilihan = pil()
    if (pilihan == 3 or pilihan == 0) :
        print("selamat tinggal")
        break
    else :
        panjang = int(input("masukan panjang : "))
        lebar = int(input("masukan lebar : "))
        if (pilihan == 1) :
            luas = luas_persegi_panjang(panjang, lebar)
            print("hasil luas persegi panjang adalah %i"%(luas))
        else :
           keliling = keliling_persegi_panjang(panjang, lebar)
           print("hasil keliling persegi panjang adalah %i"%keliling)