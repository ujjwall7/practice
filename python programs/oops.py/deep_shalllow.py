a = [1,2,4,6,8,64,3]
b = a
b[0] = 100
print(f"{id(a) = }")
print(f"{id(b) = }")
print(a)
print(b)

