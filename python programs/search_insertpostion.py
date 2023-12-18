# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2

nums = [1,3,5,6]
target = 5
found = False

for i in range(0,len(nums)):
    if nums[i]==target:
        print(f'target: {nums[i]}, index number: {i}')
        found = True

if not found:
    print('Target Not Found')




