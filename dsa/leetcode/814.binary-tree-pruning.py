# @author: yprakash

class Solution(object):
    def prune_binary_tree(self, root):
        remove = True
        if not root:
            return remove

        if self.prune_binary_tree(root.left):
            root.left = None
        else:
            remove = False

        if self.prune_binary_tree(root.right):
            root.right = None
        else:
            remove = False

        return remove and root.val == 0

    # https://leetcode.com/submissions/detail/793215792/
    def pruneTree(self, root):
        if self.prune_binary_tree(root):
            return None
        return root
