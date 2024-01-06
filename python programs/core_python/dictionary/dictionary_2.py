my_dictionary = {
    "name":  "ujjwal",
    "age": 45,
    "gender": "Male"
}

# print(my_dictionary["name"])
# print(my_dictionary["age"])
# print(my_dictionary["gender"])

# print(my_dictionary.get("namee")) #if not key exists return None not error

key = input("Enter the key : ")
result = my_dictionary.get(key)
if result is not None:
    print(f"{key = }")
else:
    print("Key Not Exists!....")






