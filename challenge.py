No=3
Nama=["Ani", "Budi", "Candra"]
Alamat=["Boyolali", "Yogyakarta", "Jakarta"]
Prodi=["Informatika", "Sistem_Informasi","Teknologi_Informasi"]
print("Tabel mahasiswa")
print(55*"=")
print("""
=======================================================
|   No   |   Nama   |   Alamat   |   Prodi   |
=======================================================""")
for i in range (No) :
	kolom_1=str(i+1)
	kolom_2=Nama[i]
	kolom_3=Alamat[i]
	kolom_4=Prodi[i]
	print("|  "+kolom_1+(9-len(kolom_1))*" "
	+"| "+kolom_2+(9-len(kolom_2))*" "
	+"| "+kolom_3+(9-len(kolom_3))*" "
	+"| "+kolom_4+(9-len(kolom_4))*" ")
print(55*"=")

def show_data() :
    txt_alas = "Alas : %s"%(e1.get())
    txt_tinggi = "Tinggi : %s"%(e2.get())
    txt_miring = "Sisi Miring : %s"%(e3.get())
    tk.Label(master, text=txt_alas).grid(row=4, columnspan=2)
    tk.Label(master, text=txt_tinggi).grid(row=5, columnspan=2)
    tk.Label(master, text=txt_miring).grid(row=6, columnspan=2)

#if nilai_akhir >= 85 :
#            print("A")
#        elif nilai_akhir >= 80 :
#            print("A-")
#        elif nilai_akhir >= 76 :
#            print("AB")
#        elif nilai_akhir >= 72 :
#            print("B+")
#        elif nilai_akhir >= 68 :
#            print("B")
#        elif nilai_akhir >= 65 :
#            print("B-")
#        elif nilai_akhir >= 62 :
#            print("BC")
#        elif nilai_akhir >= 59 :
#            print("C+")
#        elif nilai_akhir >= 56 :
#            print("C")
#        elif nilai_akhir >= 45 :
#            print("D")
#        else :
#            print("E")
	