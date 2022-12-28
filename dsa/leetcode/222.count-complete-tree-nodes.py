# @author: yprakash
from typing import Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def complete_binary_tree_height(self, node):  # O(log N)
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    # https://leetcode.com/submissions/detail/744968832/
    def countNodes(self, root):
        height = self.complete_binary_tree_height(root)
        if height <= 1:
            return height
        left_leaves = 2 ** (height - 2)
        total_nodes = 2 * left_leaves

        while left_leaves:
            height -= 1
            if self.complete_binary_tree_height(root.right) < height:
                root = root.left
            else:
                root = root.right
                total_nodes += left_leaves

            left_leaves = left_leaves >> 1

        return total_nodes

    # https://leetcode.com/submissions/detail/843614246/
    def countNodes2(self, root: Optional[TreeNode]) -> int:
        def left_height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        def right_height(node):  # O(log N)
            h = 0
            while node:
                h += 1
                node = node.right
            return h

        def total_nodes(node):
            lh = left_height(node)
            rh = right_height(node)
            if lh == rh:
                return (1 << lh) - 1
            return 1 + total_nodes(node.left) + total_nodes(node.right)

        return total_nodes(root)


obj = Solution()
print('0 : ' + str(obj.countNodes(None)))

nodes = [TreeNode(1)]
root = nodes[0]
print('1 : ' + str(obj.countNodes(root)))

nodes.append(TreeNode(2))
root.left = nodes[-1]
print('2 : ' + str(obj.countNodes(root)))

nodes.append(TreeNode(3))
root.right = nodes[-1]
print('3 : ' + str(obj.countNodes(root)))

nodes.append(TreeNode(4))
root.left.left = nodes[-1]
print('4 : ' + str(obj.countNodes(root)))

nodes.append(TreeNode(5))
root.left.right = nodes[-1]
print('5 : ' + str(obj.countNodes(root)))

nodes.append(TreeNode(6))
root.right.left = nodes[-1]
print('6 : ' + str(obj.countNodes(root)))

nodes.append(TreeNode(7))
root.right.right = nodes[-1]
print('7 : ' + str(obj.countNodes(root)))

nodes.append(TreeNode(8))
root.left.left.left = nodes[-1]
print('8 : ' + str(obj.countNodes(root)))

nodes.append(TreeNode(9))
root.left.left.right = nodes[-1]
print('9 : ' + str(obj.countNodes(root)))

nodes.append(TreeNode(10))
root.left.right.left = nodes[-1]
print('10 : ' + str(obj.countNodes(root)))

nodes.append(TreeNode(11))
root.left.right.right = nodes[-1]
print('11 : ' + str(obj.countNodes(root)))

nodes.append(TreeNode(12))
root.right.left.left = nodes[-1]
print('12 : ' + str(obj.countNodes(root)))

nodes.append(TreeNode(13))
root.right.left.right = nodes[-1]
print('13 : ' + str(obj.countNodes(root)))

nodes.append(TreeNode(14))
root.right.right.left = nodes[-1]
print('14 : ' + str(obj.countNodes(root)))

nodes.append(TreeNode(15))
root.right.right.right = nodes[-1]
print('15 : ' + str(obj.countNodes(root)))

nodes.append(TreeNode(16))
root.left.left.left.left = nodes[-1]
print('16 : ' + str(obj.countNodes(root)))
