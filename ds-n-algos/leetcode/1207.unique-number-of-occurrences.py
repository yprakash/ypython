# @author: yprakash
from collections import Counter
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/852012469/
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = Counter(arr)
        return len(occurrences.values()) == len(set(occurrences.values()))
