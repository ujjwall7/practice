# tuple immutable not changed
# there are only 2 methods count and index
# 

my_tuple = (12,23,54,23,654,21,21)
print(my_tuple)
print(my_tuple[0])
print(type(tuple))

print(my_tuple.index(54))
print(my_tuple.count(21))

print()
for i in my_tuple:
    print(i) 

print('REVERSED')

print()
for i in range(len(my_tuple)-1,-1,-1):
    print(my_tuple[i]) 




