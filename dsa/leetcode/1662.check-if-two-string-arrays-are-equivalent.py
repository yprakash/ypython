# @author: yprakash
from itertools import zip_longest
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/829902169/
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)

    # https://leetcode.com/submissions/detail/829612986/
    def arrayStringsAreEqual2(self, word1: List[str], word2: List[str]) -> bool:
        s1, s2 = '', ''
        for w in word1:
            s1 += w

        for w in word2:
            s2 += w
        return s1 == s2

    # https://leetcode.com/submissions/detail/829900960/
    def arrayStringsAreEqual3(self, word1: List[str], word2: List[str]) -> bool:
        # build O(1) generators to avoid O(N) lists
        gen1 = (ch1 for w1 in word1 for ch1 in w1)
        gen2 = (ch2 for w2 in word2 for ch2 in w2)

        return all(c1 == c2 for c1, c2 in zip_longest(gen1, gen2))
