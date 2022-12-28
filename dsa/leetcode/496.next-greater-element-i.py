# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/826008617/
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums1)
        hash_table = {num: index for index, num in enumerate(nums1)}

        for num in reversed(nums2):
            while stack and stack[-1] < num:
                stack.pop()

            if stack and num in hash_table:
                res[hash_table[num]] = stack[-1]
            stack.append(num)

        return res
