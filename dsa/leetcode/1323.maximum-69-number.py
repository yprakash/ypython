# @author: yprakash

class Solution:
    # https://leetcode.com/submissions/detail/838406319/
    def maximum69Number (self, num: int) -> int:
        lst = list(str(num))

        for i, c in enumerate(lst):
            if c == '6':
                lst[i] = '9'
                return int(''.join(lst))

        return num
