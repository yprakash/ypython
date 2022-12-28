# @author: yprakash

class Solution(object):
    def tree_str(self, node):
        if not node:
            return ''

        left = self.tree_str(node.left)
        right = self.tree_str(node.right)
        if right:
            return str(node.val) + '(' + left + ')(' + right + ')'
        if left:
            return str(node.val) + '(' + left + ')'
        return str(node.val)

    # https://leetcode.com/submissions/detail/793470872/
    def tree2str(self, root):
        return self.tree_str(root)
