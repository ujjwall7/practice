def cube(x) -> int:
    """cube of a number"""
    return x*x*x

l = [1,2,3,5,6,7,85,4,3,2]
# new = []
# for item in l:
#     new.append(cube(item))
# print(new)

# map mai chaiyeah sabse phele function name andlist
maps = map(cube, l)
print(list(maps))



