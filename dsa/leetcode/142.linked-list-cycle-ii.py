# @author: yprakash
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Floyd's Tortoise and Hare Cycle Detection Algorithm
    # https://leetcode.com/submissions/detail/730956769/
    def detectCycle(self, head):
        hare = head
        tortoise = head

        while True:
            if not hare or not hare.next:
                return None  # NO cycle in linked list

            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                break  # should be like a do while loop

        hare = head
        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next
        return tortoise
