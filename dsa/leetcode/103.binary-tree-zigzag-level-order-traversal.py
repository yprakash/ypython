# @author: yprakash
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/submissions/900668937/
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        ltr = True  # push nodes from left to right
        q = deque()
        q.append(root)
        while q:
            if ltr:
                ans.append([node.val for node in q])
            else:
                ans.append([q[i].val for i in range(len(q)-1, -1, -1)])
            ltr = not ltr

            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return ans
