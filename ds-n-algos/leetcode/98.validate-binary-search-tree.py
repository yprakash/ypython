# @author: yprakash

import math


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        mx = int(math.pow(2, 31))  # float('inf')
        mn = -1 * mx - 1      # int(float('-inf'))
        return self.is_valid_bst_rec(mn, root, mx)

    # https://leetcode.com/submissions/detail/754411629/
    def is_valid_bst_rec(self, mn, root, mx):
        if not root:
            return True
        if not mn < root.val < mx:
            return False
        if self.is_valid_bst_rec(mn, root.left, root.val):
            return self.is_valid_bst_rec(root.val, root.right, mx)
        return False
