# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/739380467/
    def climbStairs(self, n):
        if n <= 3:
            return n
        a, b = 1, 2

        for i in range(2, n):
            a, b = b, a + b
        return b
