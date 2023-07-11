# @author: yprakash
from collections import deque
from typing import List


class TreeNode:  # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/submissions/992035399/
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []

        parent = {}  # We need to traverse through parent nodes also. Fill parent dict first
        visited = set()
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if node.left:
                parent[node.left.val] = node
                q.append(node.left)
            if node.right:
                parent[node.right.val] = node
                q.append(node.right)

        visited.add(target.val)
        # q = deque()  # No need as it became empty
        q.append(target)
        while k > 0 and q:
            k -= 1
            for _ in range(len(q)):
                node = q.popleft()

                if node.val in parent and parent[node.val].val not in visited:
                    visited.add(parent[node.val].val)
                    q.append(parent[node.val])
                if node.left and node.left.val not in visited:
                    visited.add(node.left.val)
                    q.append(node.left)
                if node.right and node.right.val not in visited:
                    visited.add(node.right.val)
                    q.append(node.right)

        return [node.val for node in q]
