class Solution(object):
    def divide(self, dividend, divisor):
        if divisor < 0:
            new_divisor=divisor/-1
            new = dividend//new_divisor
            latest = new * -1
            return latest
        new = dividend//divisor
        return new

obj = Solution()
print(obj.divide(0,0))