# @author: yprakash
# Write an algorithm to determine if a given number n is happy.

class Solution(object):
    # https://leetcode.com/submissions/detail/730902192/
    def isHappy(self, n):
        seen = set()

        while n not in seen:
            seen.add(n)
            sm = 0

            for d in str(n):
                sm += int(d) ** 2
            if sm == 1:
                return True
            n = sm

        return False
