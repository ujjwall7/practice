class Solution:
    def plusOne(self, digits):
        new_list = []
        length = len(digits)

        for x in range(length):
            if x == length-1:
                new = digits[x]+1
                cd = new_list.append(new)
            if x == length-1:
                pass
            else:
                cd = new_list.append(digits[x])
        return new_list

obj = Solution()
ab = obj.plusOne([9])
print(ab)






