# @author: yprakash
from typing import Optional


class Solution:
    # https://leetcode.com/submissions/detail/818839527/
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        lst = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            lst.append(node.val)
            inorder(node.right)

        inorder(root)
        if len(lst) < 2:
            return False
        p1, p2 = 0, len(lst) - 1

        while p1 < p2:
            if lst[p1] + lst[p2] == k:
                return True
            if lst[p1] + lst[p2] < k:
                p1 += 1
            else:
                p2 -= 1

        return False
