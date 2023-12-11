print("Nomor 1")
h1={"mady":8,"roger":5,"paul":5,"lucy":7}
print(h1)

print("Nomor 2")
h2={"ken":8,"andrea":7,"smith":6}
print(h2)

print("Nomor 3")
h1.update(h2)
print(h1)

print("Nomor 4")
remidi={"roger":5,"paul":5,"smith":6}
hasil=dict.fromkeys(remidi,"8")
print(hasil)

print("Nomor 5")
uts={"roger":8,"paul":8,"smith":8,"mady":8,"lucy":7,"ken":8,"andrea":7}
for index, data in uts.items():
	if data >=8:
		print("index ke %s adalah %s"%(index,data))