x=int(input("masukkan angka : "))
for y in range(x+1,1,-1):
	for i in range(0,y-1):
		print("*",end=" ")
	print()