# @author: yprakash
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/1011429834/

class Solution:
    def letterCombinations(self, digits: str):
        def backtrack(i):
            if i >= len(digits):
                return []
            if i == len(digits) - 1:
                return letters[digits[i]]

            lst = backtrack(i + 1)
            end = []
            for c in letters[digits[i]]:
                for l in lst:
                    end.append(c + l)
            return end

        letters = {
            '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        return backtrack(0)
