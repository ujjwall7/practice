# Create a dictionary from two lists.
keys = ['a', 'b', 'c']
values = [1, 2, 3]

my_dict = dict(zip(keys,values))
print(my_dict)

# Check if all keys in one dictionary are present in another.
new = {'a': 1, 'b': 2, 'c': 35}
key = print(set(new.keys()))
print(set(new.keys()).issubset(set(my_dict.keys())))

# Find the length of a dictionary.
print(len(my_dict))
# print(my_dict.clear())

# Copy a dictionary.
new_dictionary = my_dict.copy()
print(new_dictionary)

# Merge two dictionaries.
dict_1 = {'a' : 1, 'b': 2, 'c' : 3}
dict_2 = {'d' : 100, 'e': 2, 'f' : 3}


merged_dict = {**dict_1, **dict_2}
print(merged_dict)














































