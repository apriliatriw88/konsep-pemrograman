print("Menghitung volume prisma segitiga")
alas_segitiga=int(input("masukan alas, "))
tinggi_segitiga=int(input("masukan tinggi, "))
luas_alas=0.5*alas_segitiga*tinggi_segitiga
print("Luas alas=", luas_alas)
tinggi_prisma=int(input("Masukan tinggi prisma, "))
volume=luas_alas*tinggi_prisma
print("volume prisma segitiga adalah", volume, "cm3")