# @author: yprakash
from typing import List


# https://leetcode.com/problems/add-to-array-form-of-integer/submissions/898301466/
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = k + int(''.join(map(str, num)))
        return list(map(int, str(num)))
