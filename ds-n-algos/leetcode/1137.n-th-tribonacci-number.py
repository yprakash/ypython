# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/739139567/
    def tribonacci(self, n):
        if n <= 1:
            return n
        a, b, c = 0, 1, 1

        while n > 2:
            a, b, c = b, c, a + b + c
            n -= 1
        return c


obj = Solution()
for i in range(38):
    print(obj.tribonacci(i))
