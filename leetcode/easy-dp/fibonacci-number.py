# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/739110272/
    def fib(self, n):
        if n <= 1:
            return n
        a, b = 0, 1

        for i in range(1, n):
            a, b = b, a+b
        return b


obj = Solution()
for i in range(31):
    print(obj.fib(i))
