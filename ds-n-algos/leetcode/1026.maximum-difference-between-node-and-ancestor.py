# @author: yprakash
from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def min_max_and_diff(node):
            if not node.left and not node.right:
                return 0, node.val, node.val

            if node.left:
                diff, mn, mx = min_max_and_diff(node.left)
            else:
                diff, mn, mx = -1, inf, -1

            if node.right:
                d, n, x = min_max_and_diff(node.right)
                mn = min(mn, n)
                mx = max(mx, x)
                diff = max(diff, d)

            if node.val <= mn:
                diff = mx - node.val
                mn = node.val
            elif mx <= node.val:
                diff = node.val - mn
                mx = node.val
            else:
                diff = max(diff, mx-node.val, node.val-mn)

            return diff, mn, mx

        return min_max_and_diff(root)[0]
