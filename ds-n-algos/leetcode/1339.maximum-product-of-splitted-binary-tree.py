# @author: yprakash
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://leetcode.com/submissions/detail/838711521/
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def tree_sum(node):
            if not node:
                return 0
            return node.val + tree_sum(node.left) + tree_sum(node.right)

        def split_sum(node):
            if not node:
                return 0

            curr_sum = node.val + split_sum(node.left) + split_sum(node.right)
            diff = abs(total_sum - 2 * curr_sum)
            nonlocal min_diff, sum1, sum2
            if diff < min_diff:
                min_diff = diff
                sum1 = curr_sum
                sum2 = total_sum - curr_sum

            return curr_sum

        total_sum = tree_sum(root)
        sum1, sum2 = 0, 0
        min_diff = math.inf
        split_sum(root)
        return (sum1 * sum2) % (7 + 10**9)
