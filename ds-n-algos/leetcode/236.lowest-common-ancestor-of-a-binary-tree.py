# @author: yprakash


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lca(self, root, p, q):
        if not root:
            return None
        if root == p or root == q:
            return root

        lca_left = self.lca(root.left, p, q)
        lca_right = self.lca(root.right, p, q)

        if lca_left:
            if lca_right:
                return root
            return lca_left
        return lca_right

    # https://leetcode.com/submissions/detail/757382187/
    def lowestCommonAncestor(self, root, p, q):
        return self.lca(root, p, q)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
nodes = [
    [root.left.left, root.left.right],
    [root.left.left, root.right.left],
    [root.left.left, root.left],
    [root.left.left, root.right]
]
obj = Solution()
for pair in nodes:
    res = obj.lowestCommonAncestor(root, pair[0], pair[1])
    print("LCA() = ", res.val)
