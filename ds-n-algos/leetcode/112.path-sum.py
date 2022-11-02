# @author: yprakash
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://leetcode.com/submissions/detail/835559179/
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def path_sum(node, target):
            if not node:
                return False
            target -= node.val

            if node.left or node.right:  # If non-leaf node
                return path_sum(node.left, target) or path_sum(node.right, target)
            else:
                return target == 0

        return path_sum(root, targetSum)
