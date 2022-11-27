# @author: yprakash

from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # https://leetcode.com/contest/weekly-contest-321/submissions/detail/850414639/
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = deque()
        node = head

        while node:
            while stack and stack[-1].val < node.val:
                stack.pop()
            stack.append(node)
            node = node.next

        head = None
        while stack:
            stack[-1].next = head
            head = stack.pop()

        return head
