# @author: yprakash
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://leetcode.com/submissions/detail/833124878/
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        def add_node_height(node):
            if not node:
                return -1
            h = 1 + max(add_node_height(node.left), add_node_height(node.right))
            node.val = (node.val, h)
            return h

        def remove_node(node, value):
            if not node:
                return None
            if node.left and node.left.val[0] == value:
                return 1 + node.right.val[1] if node.right else 0
            if node.right and node.right.val[0] == value:
                return 1 + node.left.val[1] if node.left else 0

            val = remove_node(node.left, value)
            if val:
                return val
            return remove_node(node.right, value)

        add_node_height(root)
        return [remove_node(root, query) for query in queries]
