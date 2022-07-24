# @author: yprakash

class SegmentTreeNode(object):
    def __init__(self, start, end, val=0, left=None, right=None):
        self.start = start
        self.end = end
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/submissions/detail/754990105/
class NumArray(object):
    def __init__(self, nums):
        self.root = self.build_tree(nums, 0, len(nums)-1)

    # O(N), preorder traversal technique
    def build_tree(self, nums, start, end):
        if start > end:
            return None

        node = SegmentTreeNode(start, end, nums[start])
        if start == end:  # leaf node
            return node

        mid = int(start + (end - start) / 2)
        node.left = self.build_tree(nums, start, mid)
        node.right = self.build_tree(nums, mid+1, end)
        node.val = node.left.val + node.right.val
        return node

    def _update_helper(self, index, val, node):
        if node.start == node.end:  # Found leaf node to be updated
            diff = val - node.val
            node.val = val
            return diff

        # parent nodes across the path
        mid = int(node.start + (node.end - node.start) / 2)
        if index <= mid:
            diff = self._update_helper(index, val, node.left)
        else:
            diff = self._update_helper(index, val, node.right)
        node.val += diff
        return diff

    # O(log N)
    def update(self, index, val):
        diff = self._update_helper(index, val, self.root)
        print('Updated diff: ', int(diff))

    def _sum_range_helper(self, node, left, right):
        # If you found out the node that matches your search
        if node.start == left and node.end == right:
            return node.val

        mid = int(node.start + (node.end - node.start) / 2)
        if right <= mid:  # Move only in the left subtree
            return self._sum_range_helper(node.left, left, right)
        elif left > mid:  # Move only in the right subtree
            return self._sum_range_helper(node.right, left, right)

        return self._sum_range_helper(node.left, left, mid) + \
               self._sum_range_helper(node.right, mid+1, right)

    # O(log N)
    def sumRange(self, left, right):
        return self._sum_range_helper(self.root, left, right)
