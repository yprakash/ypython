# @author: yprakash
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://leetcode.com/problems/leaf-similar-trees/submissions/856370207/
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaf_value_sequence(node, seq):
            if node.left:
                leaf_value_sequence(node.left, seq)
            if node.right:
                leaf_value_sequence(node.right, seq)
            elif not node.left:
                seq.append(node.val)

        seq1, seq2 = [], []
        leaf_value_sequence(root1, seq1)
        leaf_value_sequence(root2, seq2)
        return seq1 == seq2
