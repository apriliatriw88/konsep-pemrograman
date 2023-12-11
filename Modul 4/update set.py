#menggunakan set update
a={1,2,3,4,5}
b={"grape", "orange", "aple"}
a.update(b)
print (a)
#menggunakan set intersection
a={1,2,3,4,5}
b={4,5,6,7,8}
a&= (b)
print(a)
#menggunakan set difference
a={1,2,3,4,5}
b={4,5,6,7,8}
a-=(b)
print(a)
#menggunakan set symmetric
a={1,2,3,4,5}
b={4,5,6,7,8}
a^=(b)
print(a)
#menghapus semua elemen set
a={1,2,3,4,5}
a.clear()
print(a)