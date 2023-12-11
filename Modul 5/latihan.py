print("Jawaban a")
nama=["William", "Kate", "Anderson", "Jame", "Mady"]
rute=["Jakarta", "Ciamis", "Kebumen", "Yogyakarta"]
print(nama)
print(rute)

print("Jawaban b")
nama.append("Jones")
print(nama)

print("Jawaban c")
nama.remove("Anderson")
print(nama)
nama.insert(2,"Grace")
print(nama)

print("Jawaban d")
member="Thompson" in nama
print(member)

print("Jawaban e")
print(sorted(nama))

print("Jawaban f")
for i in nama :
	print(i)

print("Jawaban g")
nama.clear()
print(nama)
rute.clear()
print(rute)