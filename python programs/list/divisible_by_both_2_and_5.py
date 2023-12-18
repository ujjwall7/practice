my_list = [51, 85, 91.66, 52, 44, 100, 200, 5]
count_5 = 0
count_2 = 0

list_2 = []
list_5 = []

for x in my_list:
    if x%2==0:
        list_2.append(x)
        count_2 = count_2 + 1
    elif x%5==0:
        list_5.append(x)
        count_5 = count_5 + 1

print(f"divisible by 2 = {list_2}")
print(f"divisible by 5 = {list_5}")
    


