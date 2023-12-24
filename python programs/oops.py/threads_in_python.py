import threading


def print_using_for(num):
    for i in range(1, num+1):
        print(i ,'For')

def print_using_while(num):
    i = 1
    while i <= num:
        print(i ,'While')
        i = i+1   

# print_using_for(10)
# print_using_while(10)

t1 = threading.Thread(target=print_using_for, args=(100,))
t2 = threading.Thread(target=print_using_while, args=(100,))
t1.start()
t2.start()

# t1.join()   #join yeah kaita hai jab tak T1 khatamm nhi ho jata tabtak t2 start mat karna
# t2.join()   










