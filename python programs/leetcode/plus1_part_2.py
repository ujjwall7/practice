my_list =  [4,3,2,1]
new_str = ''

for i in my_list:
    new_str = new_str + str(i)
new_data = int(new_str) + 1
output = [int(i) for i in str(new_data)]

print(output)







