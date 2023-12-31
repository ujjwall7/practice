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
merged_dict = {**my_dict, **new_dictionary}
print(merged_dict)













































