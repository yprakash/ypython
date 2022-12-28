# @author: yprakash
from collections import Counter


class Solution:
    # https://leetcode.com/submissions/detail/853129705/
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1 = Counter(word1)
        word2 = Counter(word2)
        if word1.keys() != word2.keys():
            return False

        word1 = list(word1.values())
        word1.sort()
        word2 = list(word2.values())
        word2.sort()
        return word1 == word2
