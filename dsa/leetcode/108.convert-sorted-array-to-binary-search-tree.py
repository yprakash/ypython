# @author: yprakash
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://leetcode.com/submissions/detail/770199028/
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.sorted_array_to_bst(nums, 0, len(nums)-1)

    def sorted_array_to_bst(self, nums, left, right):
        if left > right:
            return None
        if left == right:
            return TreeNode(nums[left])

        mid = int(left + (right-left) / 2)
        root = TreeNode(nums[mid])
        root.left = self.sorted_array_to_bst(nums, left, mid-1)
        root.right = self.sorted_array_to_bst(nums, mid+1, right)
        return root
