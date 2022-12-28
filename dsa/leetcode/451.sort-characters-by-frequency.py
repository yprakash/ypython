# @author: yprakash
from collections import Counter


class Solution:
    # https://leetcode.com/submissions/detail/853652945/
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        counts = [(freq, char) for char, freq in counts.items()]
        counts.sort(reverse=True)
        return ''.join([char * freq for freq, char in counts])
