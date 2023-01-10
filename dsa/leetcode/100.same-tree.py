# @author: yprakash
from typing import Optional


class TreeNode:  # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/same-tree/submissions/875091184/
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def are_same(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return a.val == b.val and are_same(a.left, b.left) \
                and are_same(a.right, b.right)

        return are_same(p, q)
