# @author: yprakash
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/874909917/
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output = []
        stack = deque([root])

        while stack:
            node = stack.pop()
            output.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return output

    # https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/874380721/
    def preorderTraversalRec(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def preorder(node):
            if not node:
                return
            output.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return output
