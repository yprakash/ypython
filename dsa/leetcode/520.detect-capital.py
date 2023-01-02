# @author: yprakash
# https://leetcode.com/problems/detect-capital/submissions/869347652/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word != word.upper():
            word = word[1:]
            return word == word.lower()
        return True
