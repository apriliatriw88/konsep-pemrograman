x=3
if (x%2)==1 :
	print("Bilangan Ganjil")
else:
		print("Bilangan Ganjil")
	
x=3
print("Bilangan ganjil" if ((x%2)==1) else "Bilangan genap")

x=3
print(("Bilangan genap", "Bilangan ganjil")[((x%2)==1)])

x=3
print({True:"Bilangan ganjil",False:"Bilangan genap"}[((x%2)==1)])

x=3
print((lambda:"Bilangan genap", lambda:"Bilangan ganjil")[(x%2)==1]())

		