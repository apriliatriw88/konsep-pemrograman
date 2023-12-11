#try:
#    a = 10/0
#except ArithmeticError:
#    print("Operasi aritmatika yang salah")

#try:
#    dictionary = {"satu":1,"dua":2}
#    print(dictionary["tiga"])
#except KeyError:
#    print("Key dictionary tidak tersedia")

#latihan

nama=[]
try :
    masukan = int(input("Berapa jumlah nama yang akan dimasukan : "))
    for i in range (masukan) :
        print(f"nama ke {i} : ")
        nm = input("masukan nama : ")
        nama.append(nm)
    memanggil=int(input("panggil nama index ke : "))
    print(f"nama index ke {memanggil} adalah {nama[memanggil]}")

except ValueError:
    print("Masukan nilai angka bilangan bulat, bukan string")
except IndexError:
    print("Index yang dimaksud tidak ada")
  