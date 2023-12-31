a = 15

def change():
    # local variable
    global a
    a=30
    print(a)

print(a)
change()
print(a)

"""
a = 15
a = 30
a = 15
"""


