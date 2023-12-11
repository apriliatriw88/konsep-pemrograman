#mendefinisikan dictionary
a={"a": "alpha", "b": "beta", "o": "omega"}
print(a)

#dict kosong lalu ditambahkan data
a={}
a["a"]="alpha"
a["b"]="beta"
a["o"]="omega"
print(a)

#menggunakan constructor
#keyword argument
a=dict(a="alpha", b="beta", o="omega")
print(a)

#iterable tuple
a=dict([("a","alpha"), ("b", "beta"), ("o","omega")])
print(a)

#iterable list
a=dict(zip(["a","b","o"],["alpha","beta","omega"]))
print(a)