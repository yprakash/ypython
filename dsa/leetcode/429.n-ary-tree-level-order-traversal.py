# @author: yprakash
from collections import deque


class Solution(object):
    def levelOrder(self, root):
        q1 = deque([root])
        # q1.append(root)
        res = []

        while q1:
            level = []
            q2 = deque()
            while q1:
                parent = q1.popleft()
                if not parent:
                    continue
                level.append(parent.val)
                for child in parent.children:
                    q2.append(child)

            if level:
                res.append(level)
            q1 = q2
        return res
