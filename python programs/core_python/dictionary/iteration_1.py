
my_dictionary = {
    "History":  10,
    "Civics": 45,
    "Geography": 41,
    "science" :100 
}

count = 0
for i in my_dictionary.keys():
    count = count + my_dictionary[i]
print(count)

