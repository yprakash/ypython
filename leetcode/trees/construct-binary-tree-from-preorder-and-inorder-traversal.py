# author: yprakash
from collections import deque


class TreeNode(object):  # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    index = 0  # Index in preorder traversal with which next TreeNode will be created
    table = None

    def build_binary_tree(self, preorder, inorder, lower, upper):
        if lower > upper:
            return None

        root = TreeNode(preorder[self.index])
        self.index += 1
        if lower == upper:
            return root

        root.left = self.build_binary_tree(preorder, inorder, lower, self.table[root.val]-1)
        root.right = self.build_binary_tree(preorder, inorder, self.table[root.val]+1, upper)
        return root

    # https://leetcode.com/submissions/detail/747013576/
    def buildTree(self, preorder, inorder):
        # construct hash table with key as the node.val and value as the index of it in inorder traversal
        self.table = {value: index for index, value in enumerate(inorder)}
        return self.build_binary_tree(preorder, inorder, 0, len(inorder)-1)


lists = [
    [[-1], [-1]],
    [[1, 2, 3], [3, 2, 1]],
    [[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]]
]
for pair in lists:
    obj = Solution()
    root = obj.buildTree(pair[0], pair[1])
    lst = []
    q1 = deque()
    q1.append(root)

    while q1:
        q2 = deque()
        while q1:
            node = q1.popleft()
            if node:
                q2.append(node.left)
                q2.append(node.right)
                lst.append(node.val)
            else:
                lst.append(None)
        q1 = q2

    print(lst)
