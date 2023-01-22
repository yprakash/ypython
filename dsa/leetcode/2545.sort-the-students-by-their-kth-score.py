# @author: yprakash
from typing import List


# https://leetcode.com/contest/weekly-contest-329/submissions/detail/882772277/
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, key=lambda x: x[k], reverse=True)
