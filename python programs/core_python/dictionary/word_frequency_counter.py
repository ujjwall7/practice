text = "This is a sample text. This text is used for testing."
dictionary = {}
# count = 1
for i in text.split():
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
print(dictionary)















