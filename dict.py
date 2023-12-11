print("DICTIONARY\n")

kuda = {"makanan":"tumbuhan","kaki":"empat","hidup":"air","pernapasan":"insang"}

kuda["hidup"] = "darat"
kuda.pop("pernapasan")

print("Ciri-Ciri Kuda :\n",kuda)
#analisis
#diketahui inputan data yaitu, makanan:tumbuhan, kaki:empat, hidup:air, pernapasan:insang. Kemudian kuda["hidup"]="darat" artinya kata "hidup" digantikan dengan kata "darat". Pop artinya menghapus item dalam dict sehingga "pernapasan":"insang" tidak akan ditampilkan. Sehingga outputnya menjadi, makanan: tumbuhan, kaki: empat, hidup: darat.