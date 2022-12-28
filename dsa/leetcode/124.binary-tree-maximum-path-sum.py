# @author: yprakash
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/859219794/
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global max_top
        max_top = -math.inf

        def parent_child_max_path(node):
            if not node:
                return 0

            l = parent_child_max_path(node.left)
            r = parent_child_max_path(node.right)
            max_single = max(node.val, node.val + max(l, r))
            global max_top
            max_top = max(max_top, max(max_single, l + r + node.val))
            return max_single

        parent_child_max_path(root)
        return max_top
