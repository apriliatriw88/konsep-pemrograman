def pil() :
    print("pilih salah satu dari fungsi berikut : ")
    print("1. identitas")
    print("2. pendidikan")
    print("3. keluar dari program")
    pilihan = int(input("masukan pilihan : "))
    return pilihan

def identitas () :
    nama = input("masukan nama : ")
    ttl = int ()
    ttl = input("masukan ttl : ")
    alamat = input("masukan alamat : ")
    email = int ()
    email = input("masukan email : ")
    no_hp = int(input("masukan no hp : "))
    return identitas

def pendidikan () :
    universitas = input("masukan universitas : ")
    fakultas = input("masukan fakultas : ")
    program_studi = input("masukan program studi : ")
    nim = int(input("masukan nim : "))
    return pendidikan
    
pilihan = int ()
while (pilihan < 3) :
    pilihan = pil()
    if pilihan == 3 :
        print("selamat tinggal")
        break
    elif pilihan == 1 :
        ident = identitas()
        print(ident)
    else :
        pend = pendidikan()
        print(pend)