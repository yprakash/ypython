# @author: yprakash
from typing import List


# https://leetcode.com/contest/weekly-contest-356/submissions/detail/1007327520/
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(map(lambda h: h >= target, hours))
