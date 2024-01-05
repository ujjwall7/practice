original_dict = {'a': 1, 'b': 2, 'c': 3}
# Output: {1: 'a', 2: 'b', 3: 'c'}
dict = {}
for key,values in original_dict.items():
    print(f"{key = },\n{values = }")
    dict[values] = key
print(f"{dict = }")







