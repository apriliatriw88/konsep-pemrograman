print("cuaca dan kegiatan")
cuaca=input("masukan cuaca")
posisi=input("masukan posisi")
if (cuaca=="hujan") and (posisi=="dirumah"):
	ps=input("punya ps")
	if ps=="punya":
		print("main ps")
	tv=input("punya tv")
	if tv=="punya":
		print("nonton tv")
if cuaca=="tidak hujan" and posisi=="dirumah":
	print("pergi ke taman")