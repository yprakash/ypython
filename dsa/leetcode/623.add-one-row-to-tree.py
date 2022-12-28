# @author: yprakash
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://leetcode.com/submissions/detail/835557946/
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def add_children(node, level):
            if not node:
                return

            if level > 2:
                add_children(node.left, level - 1)
                add_children(node.right, level - 1)
            else:
                left = TreeNode(val)
                left.left = node.left
                node.left = left

                right = TreeNode(val)
                right.right = node.right
                node.right = right

        if depth <= 1:
            node = TreeNode(val)
            node.left = root
            return node

        add_children(root, depth)
        return root
