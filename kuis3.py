def pil () :
	print("Masukan pilihan dari 3 fungsi berikut : ")
	print("1. mencetak nama")
	print("2. menghitung berat badan ideal")
	print("3. keluar program")
	pilihan=int(input("masukan pilihan : "))
	return pilihan
def nama () :
	nama = input("masukan nama : ")
	return nama
def bb () :
	bb =tb-100
	return bb
pilihan=int()
while(pilihan<3) :
	pilihan = pil ()
	if pilihan == 3 :
		print("selamat tinggal")
		break
	elif pilihan == 2 :
		ideal = bb()
		bb=int(input("masukan bb : "))
		tb=int(input("masukan tb : "))
		print("hasil berat badan ideal adalah %i "%(ideal))
		if bb < 45 :
			print("kategori kurus")
		elif bb == 50 :
			print("kategori normal")
		else :
			print("kategori gemuk") 
	else :
			nama = nama()
			print(nama)
		
		
	
	
	