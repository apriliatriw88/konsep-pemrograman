print("program menghitung body")
bb=int(input("masukan berat badan : " ))
tb=float(input("masukan tinggi badan : "))
bmi=int(bb/(tb*tb))
print("bmi adalah ", bmi)
if bmi < 18.5 :
	print("kategori kurus")
elif bmi < 25 :
	print("kategori normal")
elif bmi < 30 :
	print("kategori kelebihan berat badan")
else :
	print("kategori kegemukan")