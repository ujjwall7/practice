# agar yeah string digit hai toh integer mai convert karo nhi hai toh cannot convert to integer 


a = "122111"

x = a.isdigit()
print(x)
if x==True:
    new = int(a)
    print(new)
else:
    print('cannot convert to integer')


