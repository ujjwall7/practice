# lambda is anonymous function


# def add(n1, n2, n3):
#     return n1 + n2 + n3

# print(add(12,3,4))

# ab = lambda n1, n2, n3: n1 + n2 + n3
# print(ab(1,2,3))


# cd = lambda n: [i for i in range(n)]
# new = cd(12)
# print(f"{new = }")

# ev = lambda n : n%2==0
# if ev==0:
#     True
# else:
#     False
# ph = ev(12)
# print(ph)


abcd = lambda num: print("Even") if num % 2 == 0 else print("Odd")

happy = abcd(124)
print(happy)


