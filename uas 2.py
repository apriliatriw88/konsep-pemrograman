try :
    print("\nProgram Menghitung Rata-rata Sejumlah Bilangan")
    print("----------------------------------------------\n")
    jumlah = int(input("masukan jumlah bilangan : "))

    total = 0
    data = []

    for i in range(jumlah) :
        bilangan = int(input("bilangan : "))
        data.append(bilangan)
        total=total+bilangan

    ratarata = total/jumlah
    print("Rata-rata dari",jumlah,"data adalah : ", ratarata)

except ValueError:
    print("Error Inputan")
except ArithmeticError:
    print("Index diluar jangkauan yang tersedia")