# @author: yprakash
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # https://leetcode.com/submissions/detail/743503495/
    def addRightNodes(self, parent, nodes, level):
        if not parent:
            return
        if len(nodes) < level:
            nodes.append(parent.val)
        self.addRightNodes(parent.right,nodes, level + 1)
        self.addRightNodes(parent.left, nodes, level + 1)

    def rightSideView2(self, root):
        res = []
        self.addRightNodes(root, res, 1)
        return res

    # https://leetcode.com/submissions/detail/740361554/
    def rightSideView(self, root):
        if not root:
            return []
        res = []
        q1 = deque()
        q1.append(root)

        while q1:
            q2 = deque()
            res.append(q1[0].val)
            while q1:
                node = q1.popleft()
                if node.right:
                    q2.append(node.right)
                if node.left:
                    q2.append(node.left)

            q1 = q2
        return res
