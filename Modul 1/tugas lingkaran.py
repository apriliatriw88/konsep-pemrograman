def keliling_lingkaran():
	while True:
		try:
			r = int(input("Masukan jari-jari : "))
		except ValueError:
			print("Input tidak valid")
		else:
			if r % 7 == 0 :
				keliling_lingkaran = 2*(22/7*r)
				hasil=[keliling_lingkaran]
			else :
				keliling_lingkaran = 2*3.14*r
				hasil = [keliling_lingkaran]
		break
	return hasil

def luas_lingkaran():
	 while True:
	 	try:
	 		r=int(input("Masukan jari-jari : "))
	 	except ValueError:
	 		print("Input tidak valid")
	 	else:
	 		if r % 7 == 0 :
	 			luas_lingkaran = 22/7*r*r
	 			hasil = [luas_lingkaran]
	 		else:
	 			luas_lingkaran = 3.14*r*r
	 			hasil = [luas_lingkaran]
	 	break
	 return hasil
	
			
print("Lingkaran")
print("1. Keliling lingkaran")
print("2. Luas lingkaran")

pilihan=input("Masukan pilihan (1/2) : ")

if pilihan == "1" :
	hasil = keliling_lingkaran()
	print("keliling lingkaran : { } ".format (hasil[0]))
elif pilihan == "2" :
	hasil = luas_lingkaran()
	print("luas lingkaran : { } ".format (hasil[1]))
else :
	print("Input Tidak Valid")