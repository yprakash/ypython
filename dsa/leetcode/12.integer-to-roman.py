# @author: yprakash

class Solution:
    # https://leetcode.com/submissions/detail/826292948/
    def intToRoman(self, num: int) -> str:
        roman = ''
        roman_int = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90),
                     ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

        for symbol, x in roman_int:
            while num >= x:
                roman += symbol
                num -= x

        return roman


if __name__ == "__main__":
    testcases = [
        3,  # "III"
        58,  # "LVIII"
        1994,  # "MCMXCIV"
    ]
    obj = Solution()
    for testcase in testcases:
        print(obj.intToRoman(testcase))
