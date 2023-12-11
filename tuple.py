print("TUPLE\n")

herbivora = ("kambing","kuda","sapi")
karnivora = ("singa","harimau","serigala")


print("\n#Akses Nilai Tuple")
print(herbivora[1])

print("\n#Update Tuple")
hewan = herbivora + karnivora

print (hewan)

print("\n#Tuple Nested")
hewan = (herbivora, karnivora)

print(hewan)

print("\n#Sequence Unpacking")
her1, her2,her3 = herbivora
print(her1)
#analisis
#diketahui herbivora=kambing, kuda, sapi
#karnivora=singa, harimau, serigala. Akses nilai tuple dimulai dari angka 0 sehingga 0=kambing, 1=kuda, dan 2=sapi. sehingga print(herbivora[1]) akan menghasilkan output kuda.
#Update tuple yaitu untuk membuat tuple baru dengan membuat hewan=herbivora+karnivora, output dari tuple tersebut adalah penambahan dari herbivora dan karnivora yaitu, kambing, kuda, sapi, singa, harimau, serigala.
#Tuple nested, bisa untuk membuat tuple baru, yaitu dengan inputan hewan=(herbivora,karnivora). Berbeda dengan Update tuple yang merupakan penambahan, Tuple nested akan menghasilkan output (kambing, kuda, sapi),(singa, harimau, serigala) karena tidak ada penambahan makanya output herbivora dan karnivora terpisah tidak jadi satu kurungan.
#Squence unpacking untu mengambil ekstra dari seluruh isinya. her1=kambing,  her2=kuda, her3=sapi. Sehingga dari data itu berarti print her(1) akan menghasilkan output kambing.