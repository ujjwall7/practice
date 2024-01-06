my_dictionary = {
    "History":  10,
    "Civics": 45,
    "Geography": 41,
    "science" :100 
}

for i in my_dictionary.keys():
    print(f"{i} -> {my_dictionary[i]}")
print('\n---------------\n')
for key, value in my_dictionary.items():
    print(f"{key} -> {value}")

