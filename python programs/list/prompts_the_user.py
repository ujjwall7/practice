
def user_input():
    inputs = int(input("Input the length of digit : "))    # number 4
    new_list =[]   # new list jo bnegi

    for x in range(inputs):
        n = int(input("Enter number : "))
        new_list.append(n)
    return new_list

print(user_input())










