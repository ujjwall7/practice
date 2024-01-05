dict_1 = {'a' : 1, 'b': 2, 'c' : 3}



def mdk(dict_1):
    mk = 1
    for i in dict_1.values():
        mk = mk * i
    print(mk)
mdk(dict_1)

def mdkwargs(**kwargs):
    mk = 1
    for i in dict_1.values():
        mk = mk * i
    print(f"kwargs : {mk}")

mdkwargs(**dict_1)