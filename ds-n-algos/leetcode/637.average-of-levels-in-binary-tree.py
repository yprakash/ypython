# @author: yprakash
from collections import deque


class Solution(object):
    # https://leetcode.com/submissions/detail/789264513/
    def averageOfLevels(self, root):
        res = []
        q1 = deque()
        q1.append(root)

        while q1:
            m, n = 0.0, len(q1)  # m, the initial sum should be a float
            q2 = deque()

            while q1:
                node = q1.popleft()
                m += node.val

                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)

            q1 = q2
            res.append(float("%.5f" % (m / n)))

        return res
