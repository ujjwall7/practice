my_list = [5,10,15,20,25,30,35,40,45,50]
new = []
for i in range(len(my_list)):
    if my_list[i]%2!=0:
        new.append(my_list[i])
print(new)

# new_list = [x for x in my_list if x % 2 != 0]
# print(new_list)
