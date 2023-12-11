pelangi = {""}
langit = {"biru"}

print ("jawaban b")
langit.discard("biru")
langit.add("abu-abu")
print(langit)

print("jawaban c")
hujan = {"merah", "kuning", "hijau"}
pelangi.update(hujan)
print(pelangi)

print("jawaban d")
langit.add("jingga")
print(langit)

print("jawaban e")
for data in langit:
    print(data)
for i in pelangi :
    print(i)