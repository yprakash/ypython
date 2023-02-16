# @author: yprakash
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/898862023/
    def maxDepthIterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        depth = 0

        while q:
            depth += 1
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return depth

    # https://leetcode.com/submissions/detail/740216774/
    # (Tail?) Recursion
    def recurse(self, root, depth):
        if not root:
            return depth
        depth += 1
        return max(self.recurse(root.left, depth), self.recurse(root.right, depth))

    def maxDepth(self, root):
        return self.recurse(root, 0)

    # https://leetcode.com/submissions/detail/740209569/
    # Recursion
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
