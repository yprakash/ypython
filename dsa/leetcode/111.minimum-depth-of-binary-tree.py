# @author: yprakash
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/991222711/
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def min_depth_rec(node):
            if not node:
                return 0
            min_left = min_depth_rec(node.left)
            min_right = min_depth_rec(node.right)
            if min_left and min_right:
                return 1 + min(min_left, min_right)
            return 1 + min_left if min_left > 0 else 1 + min_right

        return min_depth_rec(root)
