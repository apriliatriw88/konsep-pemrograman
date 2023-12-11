print("_______________________")
print("____program pembagian____")
print("_______________________")
try :
	bilangan1=int(input("masukan bilangan 1 : "))
	bilangan2=int(input("masukan bilangan 2 : "))
	hasil =bilangan1/bilangan2
	print("%i : %i = %f"%(bilangan1,bilangan2,hasil))
	
except ValueError :
	print("Masukan bukan integer")
except ArithmeticError :
	print("Operasi aritmatika yang salah")
