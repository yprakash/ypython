# @author: yprakash
from collections import Counter


class Solution(object):
    # https://leetcode.com/submissions/detail/760556566/
    def wordSubsets(self, words1, words2):
        freq = Counter(words2.pop())

        while words2:
            f = Counter(words2.pop())
            for c in f:
                if c not in freq or freq[c] < f[c]:
                    freq[c] = f[c]

        for word in words1:
            f = Counter(word)
            univ = True
            for c in freq:
                if c not in f or f[c] < freq[c]:
                    univ = False
                    break
            if univ:
                words2.append(word)

        return words2
