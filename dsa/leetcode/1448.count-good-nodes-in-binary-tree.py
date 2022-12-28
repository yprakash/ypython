# @author: yprakash

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # https://leetcode.com/submissions/detail/789062864/
    def goodNodes(self, root):
        def good_nodes(root, path_max):
            if not root:
                return 0
            if root.val < path_max:
                return good_nodes(root.left, path_max) + good_nodes(root.right, path_max)

            return 1 + good_nodes(root.left, root.val) + good_nodes(root.right, root.val)

        path_max = -10001  # set to lowest possible value based on constraint
        return good_nodes(root, path_max)
