"""
@author: yprakash

# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

from collections import deque


class Solution(object):
    # https://leetcode.com/submissions/detail/730863521
    def flatten(self, head):
        if not head:
            return head

        stack = deque()
        stack.append(head)
        prev = None

        while stack:
            curr = stack.pop()
            if prev:
                curr.prev = prev
                prev.next = curr

            while True:
                if curr.child:
                    if curr.next:
                        stack.append(curr.next)
                    curr.child.prev = curr
                    curr.next = curr.child
                    curr.child = None

                if curr.next:
                    curr = curr.next
                else:
                    prev = curr
                    break
        return head

