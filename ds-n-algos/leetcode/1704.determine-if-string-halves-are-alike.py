# @author: yprakash

class Solution:
    # https://leetcode.com/submissions/detail/852593542/
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s) // 2
        left, right = 0, 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        for i, c in enumerate(s):
            if c in vowels:
                if i < n:
                    left += 1
                else:
                    right += 1

        return left == right
