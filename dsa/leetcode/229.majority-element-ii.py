# @author: yprakash
from collections import Counter, defaultdict
from typing import List


# https://leetcode.com/problems/majority-element-ii/submissions/882384683/
# TC: O(N) SC: O(N)
class Solution1:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        nums = Counter(nums)
        return [k for k, v in nums.items() if v > n]


# https://leetcode.com/problems/majority-element-ii/submissions/882392057/
# TC: O(N) SC: O(1) Count-min sketch algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x = len(nums) // 3
        val1, val2 = 10, 19
        map1 = defaultdict(int)
        map2 = defaultdict(int)

        for n in nums:
            map1[n % val1] += 1
            map2[n % val2] += 1

        res = set()
        for n in nums:
            if min(map1[n % val1], map2[n % val2]) > x:
                res.add(n)

        return list(res)
