# @author: yprakash

class Solution:
    # https://leetcode.com/contest/biweekly-contest-92/submissions/detail/850177390/
    def numberOfCuts(self, n: int) -> int:
        if n < 2:
            return 0
        return n if n % 2 == 1 else n // 2
