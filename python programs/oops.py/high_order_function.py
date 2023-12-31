# hof are 2 types 
# 1 function return kar rha hai dusra function
# 1 function ke andar 2nd function bheja hai vo function ko call kra hai

def create_multiplier(factor):
    def multiply(x):
        return x*factor
    return multiply

obj = create_multiplier(5)
obj1 = obj(5)
print(obj1)


