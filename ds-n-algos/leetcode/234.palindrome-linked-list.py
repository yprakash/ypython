# @author: yprakash
from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.left = None  # used only in recursive solution

    # https://leetcode.com/submissions/detail/781470399/
    # O(1) space and O(3N) Time
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1. Find out the middle node
        first = second = head
        while second and second.next:
            first = first.next
            second = second.next.next

        if second:  # odd no.of nodes in list
            mid = first
            curr = first.next
        else:
            curr = mid = first

        # 2. Reverse second half of the list
        second = None  # prev = None
        while curr:
            next = curr.next
            curr.next = second
            second = curr
            curr = next

        # 3. Compare first and second halves
        first = head
        while first != mid:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        # 4. Reverse second half and form original list
        return True

    # O(N) Time and O(1) space if recursive call stack is ignored
    # https://leetcode.com/submissions/detail/781377517/
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        self.left = head

        def is_palindrome(right):
            if not right:
                return True
            if not is_palindrome(right.next):
                return False

            if self.left.val != right.val:
                return False
            self.left = self.left.next
            return True

        return is_palindrome(head)

    # https://leetcode.com/submissions/detail/780892295/
    # Using O(N) space & Time
    def isPalindrome1(self, head: Optional[ListNode]) -> bool:
        q = deque()
        node = head

        while node:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop() != q.popleft():
                return False
        return True
