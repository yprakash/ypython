# @author: yprakash
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # https://leetcode.com/submissions/detail/822041869/
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head


if __name__ == "__main__":
    obj = Solution()
    for i in range(1, 11):
        head = ListNode(0)
        curr = head
        for j in range(1, i):
            curr.next = ListNode(j)
            curr = curr.next

        head = obj.deleteMiddle(head)
        if not head:
            print('Empty List')
            continue

        s = str(head.val)
        curr = head.next
        while curr:
            s += '->' + str(curr.val)
            curr = curr.next
        print(s)
