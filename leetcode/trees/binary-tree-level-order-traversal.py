# @author: yprakash
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # https://leetcode.com/submissions/detail/740314319/
    # with only one Q
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)

        while q:
            n = len(q)  # first level with only 1 (root) node exists in queue
            level = []
            while n > 0:
                n -= 1
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)

        return res

    # https://leetcode.com/submissions/detail/740274017/
    def levelOrder(self, root):
        if not root:
            return []
        q1 = deque()
        q1.append(root)
        res = []

        while q1:
            res.append([node.val for node in q1])
            q2 = deque()
            while q1:
                node = q1.popleft()
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            q1 = q2

        return res
