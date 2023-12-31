x = 15

print(f"old is x : {id(x)}")

def new():
    global x
    print(f"new is x : {id(x)}")
    print(f"x is {x+10}")
    x = 30

new()




