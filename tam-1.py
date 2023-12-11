#   Nama Tim:       Tam - 1
#   Nama Program:   Penghitung Gaji Karyawan

from datetime import date
tanggal = date.today().strftime("%d %B %Y")

pegawai = {
  "Rahmat": {
      "id": 123,
      "posisi": "Manager",
      "gaji": 25000000,
      "tunjangan": ["Istri", "Anak"]
      },
  "Dodi": {
      "id": 132,
      "posisi": "Kepala Divisi",
      "gaji": 12000000,
      "tunjangan": ["Istri"]
      }, 
  "Ganteng": {
      "id": 312,
      "posisi": "Karyawan Tetap",
      "gaji": 6000000,
      "tunjangan": ["Anak"]
      }, 
  "Toni": {
      "id": 321,
      "posisi": "Karyawan Kontrak",
      "gaji": 4000000,
      "tunjangan": []
      }, 
  }

def info_karyawan(nomor):
    try:
        print("\n    | Info Karyawan |\n")
        name = ""
        for nama, val in pegawai.items():
            if (val['id'] == nomor):
                name = nama
        posisi = pegawai[name]['posisi']
        gaji = pegawai[name]['gaji']
        tunjangan = ""
        print(f"ID: {nomor}")
        print(f"Nama Pegawai: {name}")
        print(f"Posisi Jabatan: {posisi}")
        for j in pegawai[name]['tunjangan']:
            tunjangan = j + " "
        print(f"Gaji Pokok: Rp.{gaji}")
        print(f"Tunjangan: {tunjangan}")
        return name, posisi, gaji, pegawai[name]['tunjangan']
    except Exception:
        print("Karyawan tidak ditemukan")
        

def hitung_pajak(gaji):
    pajak = (gaji * 5) / 100
    total = gaji - pajak
    return total, pajak

def hitung_tunjangan(gaji, tunjangan):
    total_tunjangan = 0
    for n in tunjangan:
        if (n == "Istri"):
            total_tunjangan = total_tunjangan + 4
        elif (n == "Anak"):
            total_tunjangan = total_tunjangan + 6
        else:
            total_tunjangan = total_tunjangan + 0
    total = (gaji * total_tunjangan) / 100
    gaji_tunjangan = gaji + total
    return gaji_tunjangan, total
    
try:
    print("\n    | Daftar Karyawan Perusahaan |\n")
    for name in pegawai.keys():
        print(f"ID: {pegawai[name]['id']}    Nama: {name} - {pegawai[name]['posisi']}")
    id_karyawan = int(input("\nMasukan ID karyawan: "))
    nama, posisi, gaji, tunjangan = info_karyawan(id_karyawan)
    gaji_tunjangan, jumlah_tunjangan = hitung_tunjangan(gaji, tunjangan)
    gaji_bersih, pajak = hitung_pajak(gaji_tunjangan)
    print("\n    | Slip Gaji |\n")
    print(f"Nama Karyawan: {nama}")
    print(f"Gaji Pokok: Rp.{gaji}")
    print(f"Tunjangan: Rp.{jumlah_tunjangan}")
    print(f"Pajak: Rp.{pajak}")
    print(f"Gaji Bersih: Rp.{gaji_bersih}")
    print(f"Tanggal: {tanggal}")
    
    
except Exception:
    print("Program error, coba ulangi lagi.")
