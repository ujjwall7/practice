import copy

a = [[1,2,4],[6],[8],[64,3]]
b = a.copy()
b[0] = 100
print(f"{id(a) = }")
print(f"{id(b) = }")
print(a)
print(b)


print('--------------------------')
print()
a = [[1,2,4],[6],[8],[64,3]]
# b = a.copy()
b = copy.deepcopy(a)
b[0][0] = 100
print(f"{id(a) = }")
print(f"{id(b) = }")
print(a)
print(b)