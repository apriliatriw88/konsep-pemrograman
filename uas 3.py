def pil() :
    print("pilih salah satu dari fungsi berikut : ")
    print("1. mencetak nama")
    print("2. menghitung usia")
    print("3. keluar dari program")
    pilihan = int(input("masukan pilihan : "))
    return pilihan
def nama () :
	nama = input("masukan nama : ")
	return nama
def usia () :
	usia =sekarang-lahir
	return usia

pilihan=int()
while(pilihan<3) :
	pilihan = pil ()
	if pilihan == 3 :
		print("===selamat tinggal===")
		break
	elif pilihan == 2 :
        sekarang=int(input("masukan tahun ini : "))
        lahir=int(input("masukan tahun lahir : "))
        usia = sekarang-lahir
        if usia <=35 :
            print("muda")
        else :
            print("tua")

