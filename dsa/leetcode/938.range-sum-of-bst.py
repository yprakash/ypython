# @author: yprakash
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://leetcode.com/problems/range-sum-of-bst/submissions/855844841/
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def range_sum(node):
            if not node:
                return 0
            if low <= node.val <= high:
                total_sum = node.val
            else:
                total_sum = 0

            return total_sum + range_sum(node.left) + range_sum(node.right)

        return range_sum(root)
