# @author: yprakash
from collections import deque


# https://leetcode.com/submissions/detail/813319229/
class BSTIterator(object):
    def __init__(self, root):
        self.stack = deque()
        self._partial_in_order(root)

    # With this the memory can be reduced from O(N) to O(h)
    def _partial_in_order(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        top = self.stack.pop()
        self._partial_in_order(top.right)
        return top.val

    def hasNext(self):
        return True if self.stack else False
