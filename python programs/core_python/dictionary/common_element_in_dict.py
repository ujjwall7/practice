# dict1 = {'a': 10, 'b': 20, 'c': 30}
# dict2 = {'b': 30, 'c': 40, 'd': 50}
# Output: {'b': 20, 'c': 30}


dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 30, 'c': 40, 'd': 50}

result_dict = {}
for key in dict1:
    if key in dict2:
        print(key)
        result_dict[key] = dict1[key]
print(result_dict)







