# @author: yprakash
import bisect
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://leetcode.com/contest/weekly-contest-320/submissions/detail/846661380/
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        def inorder(node, res):
            if not node:
                return
            inorder(node.left, res)
            res.append(node.val)
            inorder(node.right, res)

        answer, elems = [], []
        inorder(root, elems)

        for x in queries:
            pos = bisect.bisect_left(elems, x)
            if pos >= len(elems):
                answer.append([elems[-1], -1])
            elif x == elems[pos]:
                answer.append([x, x])
            elif pos == 0:
                answer.append([-1, elems[0]])
            else:
                answer.append([elems[pos-1], elems[pos]])

        return answer
