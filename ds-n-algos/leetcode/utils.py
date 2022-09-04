# @author: yprakash
from collections import deque


def binary_tree_as_list(root):
    res = []
    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        if node:
            q.append(node.left)
            q.append(node.right)
            res.append(node.val)
        else:
            res.append(None)

    for i in range(len(res)-1, 0, -1):
        if res[i] is None:
            del res[i]
        else:
            break
    return res


def print_binary_tree(root):
    if not root:
        print('EMPTY Binary tree')
        return
    print(binary_tree_as_list(root))


def build_binary_tree_from_level_order_traversal(a=[]):
    if not a:
        return None
    q = deque()
    next_left = True  # condition to check to add as left or right child
    root = TreeNode(a[0])
    curr = root

    for i in range(1, len(a)):
        if next_left:
            if a[i] is not None:
                curr.left = TreeNode(a[i])
                q.append(curr.left)
            next_left = False
        else:
            if a[i] is not None:
                curr.right = TreeNode(a[i])
                q.append(curr.right)

            if not q:
                break
            curr = q.popleft()
            next_left = True

    return root


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
