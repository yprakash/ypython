# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/774130220/
    def romanToInt(self, s):
        num = 0
        prev = 0
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for r in reversed(s):
            if roman_dict[r] < prev:
                num -= roman_dict[r]
            else:
                num += roman_dict[r]
            prev = roman_dict[r]

        return num


testcases = [
    "III",  # 3
    "LVIII",  # 58
    "MCMXCIV",  # 1994
]
obj = Solution()
for testcase in testcases:
    print(obj.romanToInt(testcase))
