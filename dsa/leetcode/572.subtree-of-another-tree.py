# @author: yprakash

class Solution:
    # https://leetcode.com/submissions/detail/837271042/
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def identical(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False
            return identical(node1.left, node2.left) and identical(node1.right, node2.right)

        def is_sub(node):
            if not node:
                return False
            if identical(node, subRoot):
                return True
            return is_sub(node.left) or is_sub(node.right)

        return is_sub(root)
