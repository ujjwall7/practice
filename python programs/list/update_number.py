my_list = [5, 10, 15, 20, 15]
old_number = int(input("Enter the old number : "))
new_number = int(input("Enter the new number : "))

for i in range(len(my_list)):
    if my_list[i] == old_number:
        my_list[i]=new_number;
print(my_list)



