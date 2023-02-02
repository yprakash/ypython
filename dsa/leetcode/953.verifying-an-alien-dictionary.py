# @author: yprakash
from typing import List


# https://leetcode.com/problems/verifying-an-alien-dictionary/submissions/889830269/
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {a: x for a, x in zip(order, 'abcdefghijklmnopqrstuvwxyz')}
        words = [''.join(order[c] for c in word) for word in words]
        return all(a <= b for a, b in zip(words, words[1:]))
