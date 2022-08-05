# @author: yprakash
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # https://leetcode.com/submissions/detail/753860544/
    def partition(self, head, x):
        p2 = None  # contains all nodes lesser than x
        new_head = None

        p1 = head
        while p1 and p1.val < x:
            p2 = p1
            p1 = p1.next
        if not p1 or not p1.next:
            return head

        starting = p1

        while p1.next:
            if p1.next.val < x:
                if p2:
                    p2.next = p1.next
                    p2 = p2.next
                else:
                    new_head = p1.next
                    p2 = new_head
                p1.next = p1.next.next
            else:
                p1 = p1.next

        if p2:
            p2.next = starting

        return new_head if new_head else head


def print_list(head, prefix=''):
    if not head:
        print('Empty List')

    s = prefix + ' [' + str(head.val)
    head = head.next
    while head:
        s += ', ' + str(head.val)
        head = head.next
    s += ']'
    print(s)


def prepare_sll(arr):  # Prepare singly Linked List from array
    if not arr:
        return None
    head = ListNode(arr.pop(0))
    curr = head

    for item in arr:
        curr.next = ListNode(item)
        curr = curr.next
    return head


nodes_list = [
    [2, [2, 1]],  # [1, 2]
    [3, [1, 4, 3, 2, 5, 2]],  # [1,2,2,4,3,5]
]
for lst in nodes_list:
    head = prepare_sll(lst[1])
    print_list(head, 'Original')
    obj = Solution()
    head = obj.partition(head, lst[0])
    print_list(head, 'Modified')
