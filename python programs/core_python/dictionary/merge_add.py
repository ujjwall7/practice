dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 30, 'c': 40, 'd': 50}
# Output: {'a': 10, 'b': 50, 'c': 70, 'd': 50}
new_dict = {}

for i in dict1:
    new_dict[i] = dict1[i]

for i in dict2:
    if i in new_dict:
        new_dict[i] += dict2[i]
    else:
        new_dict[i] = dict2[i]
        
print(new_dict)




