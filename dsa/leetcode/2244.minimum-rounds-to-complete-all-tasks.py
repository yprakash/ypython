# @author: yprakash
from collections import Counter
from math import ceil
from typing import List


# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/submissions/870807865/
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        rounds = 0
        tasks = Counter(tasks)

        for task, freq in tasks.items():
            if freq < 2:
                return -1
            rounds += ceil(freq / 3)
        return rounds
