# author: yprakash
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://leetcode.com/submissions/detail/799265006/
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def pseudo_palindromic_paths(node, path_counter):
            nonlocal count
            if not node:
                return

            path_counter ^= (1 << node.val)
            if not node.left and not node.right:
                if bin(path_counter)[2:].count("1") <= 1:
                    count += 1
            else:
                pseudo_palindromic_paths(node.left, path_counter)
                pseudo_palindromic_paths(node.right, path_counter)
            return count

        count = 0
        pseudo_palindromic_paths(root, 0)
        return count
