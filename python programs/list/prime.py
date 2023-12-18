"""
prime logic

jo khud ke number se number se hi divide hou bas 

9 check
1,2,3,4,5,6,7,8,9
break

"""

my_list = [1,54,2,2,676,43,76,43,12,676,987,65,3]

prime_list = []

for x in range(len(my_list)):
    count_prime = 0
    for y in range(1,my_list[x]+1):
        if my_list[x] % y == 0:
            count_prime = count_prime + 1

    if count_prime == 2:
        prime_list.append(my_list[x])
                
print(prime_list)


# my_list = [1, 54, 2, 2, 676, 43, 76, 43, 12, 676, 987, 65, 3]
# prime_list = []

# for x in range(len(my_list)):
#     count_prime = 0
#     for y in range(1, my_list[x] + 1):
#         if my_list[x] % y == 0:
#             count_prime += 1

#     if count_prime == 2:  # A prime number has exactly two divisors: 1 and itself
#         prime_list.append(my_list[x])

# print(prime_list)










