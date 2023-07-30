# @author: yprakash
from collections import defaultdict
from typing import List


# https://leetcode.com/contest/weekly-contest-356/submissions/detail/1007347606/
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        left, right = 0, 0
        distinct = len(set(nums))
        counter = defaultdict(int)

        while right < n:
            counter[nums[right]] += 1
            while left <= right and len(counter) == distinct:
                ans += (n - right)
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1

            right += 1

        return ans
