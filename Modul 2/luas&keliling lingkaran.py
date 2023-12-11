print("luas dan keliling lingkaran")
pilihan=int(input("masukan pilihan"))
if pilihan==1:
	phi=3.14
	jari_jari=7
	keliling=int(2*phi*jari_jari)
	print("keliling lingkaran", keliling)
elif pilihan==2:
	phi=3.14
	jari_jari=7
	luas=int(phi*jari_jari*jari_jari)
	print("luas lingkaran", luas)
else:
	print("lingkaran")
