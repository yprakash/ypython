# @author: yprakash

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # https://leetcode.com/submissions/detail/840127949/
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        curr = head
        while curr:
            curr.next = Node(curr.val, curr.next, curr.random)
            curr = curr.next.next

        new_head = head.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            # else: both are already None
            curr = curr.next.next

        curr = head
        while curr:
            temp = curr.next.next
            if temp:
                curr.next.next = temp.next
            # else: both are already None

            curr.next = temp
            curr = temp

        return new_head
