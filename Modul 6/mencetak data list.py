a={"a":"alpha", "b":"beta", "o":"omega"}
print(a["b"])

#isi menggunakan perulangan tp index
a={"a":"alpha", "b":'beta', "o":"omega"}
for i in a:
	print(i)

#isi menggunakan perulangan dg index
a={"a":"alpha", "b":"beta", "o":"omega"}
for index,data in a.items():
	print("index ke %s adalah %s"%(index,data))
	
#key menggunakan perulangan
a={"a":"alpha", "b":"beta", "o":"omega"}
for index in a.keys():
	print("index ke %s"%(index))

#nilai data menggunakan perulangan
a={"a":"alpha", "b":"beta", "o":"omega"}
for i in a.values():
	print("data %s"%(i))

