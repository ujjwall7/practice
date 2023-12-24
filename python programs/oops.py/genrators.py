# yield kar rha hai matlab de rha hai ,yield matlab dena 
# yield - genrate like iterate manually

def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    yield 7
    yield 8
    yield 9
    yield 10

for i in numbers():
    print(i)

# for i in range(1,11):
#     print(i)

x = numbers()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
# print(next(x))   #error aa jati hai vo cheez for loop senhi aati next ka kaam hota hai for i in same hai







