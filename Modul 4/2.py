#a
H1={"keju", "tepung", "garam", "gula", "coklat"}
H2={"garam", "gula", "coklat", "kecap"}

print("Jawaban B")
H2={"garam", "gula", "coklat", "kecap"}
H2.add("keju")
print(H2)

print("Jawaban C")
H1={"keju", "tepung", "garam", "gula", "coklat"}
H2={"garam", "gula", "coklat", "kecap"}
print(H1.intersection(H2))

print("Jawaban D")
H1={"keju", "tepung", "garam", "gula", "coklat"}
H2={"garam", "gula", "coklat", "kecap"}
print(H1.difference(H2))

print("Jawaban E")
H1={"keju", "tepung", "garam", "gula", "coklat"}
H1.discard("garam")
print(H1)

print("Jawaban F")
H1={"keju", "tepung", "garam", "gula", "coklat"}
H2={"garam", "gula", "coklat", "kecap"}
print(H2.difference(H1))

print("Jawaban G")
H1={"keju", "tepung", "garam", "gula", "coklat"}
H2={"garam", "gula", "coklat", "kecap"}
print(H1.symmetric_difference(H2))

print("Jawaban H")
H1={"keju", "tepung", "garam", "gula", "coklat"}
print(H1)

print("Jawaban I")
H2={"garam", "gula", "coklat", "kecap"}
print(H2)