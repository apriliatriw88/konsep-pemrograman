def pilihan ( ) :
	print ("Masukan pilihan")
	print ("1. keliling")
	print ("2. luas")

def keliling ( ) :
	print ("Menghitung keliling lingkaran")
	r=int(input("Masukan jari jari : "))
	keliling=2*3.14*r
	print ("Keliling lingkaran adalah", keliling)
	
def luas ( ) :
	print ("Menghitung luas lingkaran")
	r=int(input("Masukan jari jari : "))
	luas=3.14*r*r
	print ("Luas lingkaran adalah",luas)

while 1 :
	pilih=int(input("Masukan pilihan : "))
	if pilih==1 :
		keliling ( )
	elif pilih==2 :
		luas ( )
	else:
		print("Input tidak valid")