# Check if a key is present in a dictionary.
ab = {'new' : 150, 'happy': 41, 'gin' : 450, 'om' : 9}
if 'new' in ab:
    print('key is present')
else:
    print("not found")

#Remove a key-value pair from a dictionary
obj = ab.pop('gin')
print('removed item', obj)
print('ab : ',ab)
print()

# Iterate over keys in a dictionary.
for i in ab:
    print(i)

# Iterate over values in a dictionary.
for value in ab.values():
    print(f"{value = }")
print()

# Iterate over key-value pairs in a dictionary.
for key, value in ab.items():
    print(f"{key} : {value}")









