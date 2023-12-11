def pil () :
    print("1. Menyimpan biodata")
    print("2. Tampilkan semua biodata")
    print("3. Keluar program")
    pilihan = int(input("masukan pilihan : "))
    return pilihan

def menyimpan_biodata () :
    file = open('database.txt','w')
    file.write("masukan nama : alex \n ")
    file.write("masukan tanggal lahir : 19 november 2002 \n ")
    file.write("masukan asal daerah : yogyakarta \n ")
    file.close() 
    return file

def tampilkan_semua_biodata () :
    biodata = open ("database.txt", "r")
    print(biodata.read())
    return biodata
pilihan = int()
while (pilihan<3):
    pilihan = pil()
    if pilihan == 3 :
        print("selamat tinggal")
        break
    elif pilihan == 1 :
        database = menyimpan_biodata ()
        print(database)
    else :
        biodata = tampilkan_semua_biodata ()
        print(biodata)