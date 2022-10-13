# @author: yprakash
# https://leetcode.com/submissions/detail/821289259/

class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
