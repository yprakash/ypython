# @author: yprakash
# https://leetcode.com/problems/zigzag-conversion/submissions/890391915/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s and numRows <= 0:
            return ''
        if numRows == 1:
            return s
        res = ''
        step = 2 * numRows - 2

        for r in range(numRows):
            for c in range(r, len(s), step):
                res += s[c]
                if r != 0 and r != numRows - 1:
                    tmp = c + step - 2 * r
                    if tmp < len(s):
                        res += s[tmp]

        return res
