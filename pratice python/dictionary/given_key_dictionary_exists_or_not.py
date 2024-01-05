dict_1 = {'a' : 1, 'b': 2, 'c' : 3}

# key = True
# for key in dict_1:
#     if key:
#         print('key is present')
#         break
# if not key:
#     print('Key Not Found!')

user_input = input('Enter the key to be verified : ')
if user_input in dict_1.keys():
    print(f"user_input key found!")
print(f"Not found!")



