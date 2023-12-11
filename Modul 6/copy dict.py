a={"a":"alpha", "b":"beta", "o":"omega"}
b=a.copy()
print(id(a))
print(a)
print(id(b))
print(b)
b["o"]="orion"
print(b)