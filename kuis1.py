print("Jawaban a")
balon = {"hijau", "kuning", "kelabu", "merah muda", "biru"}
print(balon)

print ("Jawaban b")
balon.remove("hijau")
print(balon)

print("Jawaban c")
print(len(balon))

print("Jawaban d")
adik = {"hitam", "putih"}
semua=balon.union(adik)
print(semua)

print("Jawaban e")
for data in semua:
	print(data)