# @author: yprakash
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/minimum-distance-between-bst-nodes/submissions/899482919/
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def flatten(node):
            if not node:
                return
            flatten(node.left)
            arr.append(node.val)
            flatten(node.right)

        if not root:
            return 10 ** 5
        arr = []
        flatten(root)
        return min(abs(a - b) for a, b in zip(arr, arr[1:]))
