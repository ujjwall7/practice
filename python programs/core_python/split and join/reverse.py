a = "HELLO WORLD THIS IS PYHTON"

# new = a.split()
# for i in new:
#     rev = i[::-1]
#     print(rev)


new_str = "Hello World"
new_list = []
new = new_str.split()
for i in new:
    rev = i[::-1]
    new_list.append(rev)

reverse_str = " ".join(new_list)
print(reverse_str)
