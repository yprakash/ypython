# @author: yprakash
# https://leetcode.com/contest/weekly-contest-329/submissions/detail/882766264/

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = 0
        for i, c in enumerate(str(n)):
            if i % 2 == 0:
                s += int(c)
            else:
                s -= int(c)

        return s
