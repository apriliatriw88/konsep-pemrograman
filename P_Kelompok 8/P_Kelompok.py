def pil () :
    try :
        print("1. Menulis Biodata")
        print("2. Tampilkan Biodata")
        print("3. Nilai")
        print("4. Keluar Program")
        pilihan = int(input("masukan pilihan : "))
        return pilihan
    except Exception:
        print("===Pilihan Berupa Angka===")

def tulis_biodata () : 
    file = open('biodata.txt','w')
    file.write(f"{'':_^45}\nNAMA\t\t: {nama}\nNIM\t\t: {nim}\nPRODI\t\t: {prodi}\nSEMESTER\t: {semester}\n{'':_^45}\n")

def tampil_biodata () :
    bio = open ("biodata.txt", "r")
    print(bio.read())
    return bio

def nilai (absen,matkul,tugas,kuis,uts,uas) : 
    mata_kuliah = matkul
    Absen = absen*10/100
    Tugas = int(tugas*30/100)
    Kuis = int(kuis*20/100)
    Uts = int(uts*20/100)
    Uas = int(uas*20/100)
    nilai_akhir=Absen+Tugas+Kuis+Uts+Uas
    return nilai_akhir

pilihan = int()
while (pilihan < 4) :
    pilihan = pil()
    if pilihan == 1 :
        nama = input ("masukan nama : ")
        nim = int(input("masukan nim : "))
        prodi = input("masukan program studi : ")
        semester = int(input("masukan semester : "))
        biodata = tulis_biodata()
        print(biodata)
    elif pilihan == 2 :
        bio = tampil_biodata()
        print(bio)
    elif pilihan == 3 :
        try :
            matkul = []
            matkul.append(input("masukan mata kuliah : "))
            absen = float(input("masukan nilai absen : "))
            tugas = float(input("masukan nilai tugas : "))
            kuis = float(input("masukan nilai kuis : "))
            uts = float(input("masukan nilai uts : "))
            uas = float(input("masukan nilai uas : "))
            nilai_akhir= nilai(absen, matkul, tugas, kuis, uts, uas)
            print("hasil nilai akhir adalah %i"%nilai_akhir)

            print(""" 
            -----------------------------------------------------------------------------------
            |                                  DATA MAHASISWA                                 |
            -----------------------------------------------------------------------------------
            -----------------------------------------------------------------------------------
            | No |       Mata Kuliah      | Absen | Tugas | Kuis |  Uts  | Uas  | Nilai Akhir |
            +---------------------------------------------------------------------------------+""")
            data = 1
            for i in range (data):
                kolom1=str(i+1)
                kolom2=str(matkul)
                kolom3=str(absen)
                kolom4=str(tugas)
                kolom5=str(kuis)
                kolom6=str(uts)
                kolom7=str(uas)
                kolom8=str(nilai_akhir)
                print(      '            | ' +kolom1 +(3-len(kolom1))*' '
                +'| ' +kolom2 +(15-len(kolom2))*' '
                +' | ' +kolom3 +(6-len(kolom3))*' '
                +'| ' +kolom4 +(6-len(kolom4))*' '
                +'| ' +kolom5 +(5-len(kolom5))*' '
                +'| ' +kolom6 +(6-len(kolom6))*' ' 
                +'| ' +kolom7 +(5-len(kolom7))*' '
                +'| ' +kolom8 +(12-len(kolom8))*' '+'| ')
                print(100*'-')
                print("=============== Hasil ================")
                if nilai_akhir >= 85 :
                    print("Grade = A")
                elif nilai_akhir >= 80 :
                    print("Grade = A-")
                elif nilai_akhir >= 76 :
                    print("Grade = AB")
                elif nilai_akhir >= 72 :
                    print("Grade = B+")
                elif nilai_akhir >= 68 :
                    print("Grade = B")
                elif nilai_akhir >= 65 :
                    print("Grade = B-")
                elif nilai_akhir >= 62 :
                    print("Grade = BC")
                elif nilai_akhir >= 59 :
                    print("Grade = C+")
                elif nilai_akhir >= 56 :
                    print("Grade = C")
                elif nilai_akhir >= 45 :
                    print("Grade = D")
                else :
                    print("Grade = E")

                if nilai_akhir >= 56 :
                    print("Keterangan = LULUS ")
                else:
                    print("keterangan = TIDAK LULUS")
                print("--------------------------------------")
        except ValueError:
            print("===Yang Anda Masukan salah, Mohon Coba Lagi===")
    else :
        print("==========+ ANDA KELUAR DARI PROGRAM +==========")
        break