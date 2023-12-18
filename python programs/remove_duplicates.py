# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]


nums = [1,1,2]
new_list = []
ab = len(nums)
ab_length = ab
print(ab_length)

for x in nums:
    if x not in new_list:
        new_list.append(x)

cd = len(new_list)
cd_length = cd
print(cd_length)
try:
    new_append = ab_length - cd_length
except Exception as e:
    print(e)

if new_append:
    for i in range(new_append):
        new_list.append('_')

print(new_list)





