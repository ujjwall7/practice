# Input: nums = [1,2,3,1]
# Output: true



nums = [1,2,3,1]
found = False
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j]:
            found =True
            print("Yes List contain duplicates")
            break

if not found:
    print("No, List contain duplicates")
                       













