# @author: yprakash

class Solution(object):
    def inorder_traversal(self, node, res):
        if not node:
            return
        self.inorder_traversal(node.left, res)
        res.append(node.val)
        self.inorder_traversal(node.right, res)

    # https://leetcode.com/submissions/detail/794363503/
    def inorderTraversal(self, root):
        res = []
        self.inorder_traversal(root, res)
        return res
