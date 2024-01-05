my_dict = {4: 'a', 3: 'b', 5: 'c', 2: 'd', 6: 'e'}
# Output: [2, 3, 4, 5, 6]


l = []

for key, values in sorted(my_dict.items()):
    print(f"{key = }")
    l.append(key)

print(l)



