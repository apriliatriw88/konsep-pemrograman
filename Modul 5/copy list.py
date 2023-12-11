list=[1,4,3,4,5,2]
print(id(list))
list_new=list
print(id(list_new))

list_copy=list.copy()
print(id(list_copy))
print(list)
print(list_new)
print(list_copy)