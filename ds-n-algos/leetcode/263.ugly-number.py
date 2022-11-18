# @author: yprakash

class Solution:
    # https://leetcode.com/submissions/detail/845516582/
    def isUgly(self, n: int) -> bool:
        if not n:
            return False
        for factor in [5, 3, 2]:
            while n % factor == 0:
                n /= factor

        return n == 1
