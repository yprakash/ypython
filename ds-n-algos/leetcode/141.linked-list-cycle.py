# @author: yprakash
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # https://leetcode.com/submissions/detail/730889854/
    def hasCycle(self, head):
        if not head:
            return False
        first = head
        second = head.next

        while first != second:
            if not second or not second.next:
                return False

            first = first.next
            second = second.next.next
        return True
