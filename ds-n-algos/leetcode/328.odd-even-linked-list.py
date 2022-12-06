# @author: yprakash
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # https://leetcode.com/problems/odd-even-linked-list/submissions/855360184/
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        even_head = head.next
        even = None
        curr = head

        while curr and curr.next:
            if even:
                even.next = curr.next
            even = curr.next
            curr.next = curr.next.next
            if not curr.next:
                curr.next = even_head
                break
            curr = curr.next

        even.next = None
        if curr:
            curr.next = even_head
        return head
