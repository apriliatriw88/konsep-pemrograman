#2 list atau lebih
a=[1,2,3,4,5]
b=[6,7,8,9]
c=a+b
print(c)
#perubahan list sebelumnya
a=[1,2,3,4,5]
b=[6,7,8,9]
a.extend(b)
print(a)
a.extend("slow")
print(a)