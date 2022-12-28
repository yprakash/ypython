# @author: yprakash

from collections import deque, defaultdict, OrderedDict
from utils import build_binary_tree_from_level_order_traversal


class Solution(object):
    def __init__(self):
        self.min_col = 0
        self.max_col = 0

    # https://leetcode.com/submissions/detail/791184465/
    def verticalTraversal(self, root):
        dct = defaultdict(lambda: OrderedDict())
        q = deque()
        q.append((0, 0, root))

        while q:
            r, c, node = q.popleft()
            if c < self.min_col:
                self.min_col = c
            elif c > self.max_col:
                self.max_col = c

            if r not in dct[c]:
                dct[c][r] = []
            dct[c][r].append(node.val)

            if node.left:
                q.append((r+1, c-1, node.left))
            if node.right:
                q.append((r+1, c+1, node.right))

        res = []
        for c in range(self.min_col, 1 + self.max_col):
            row = []
            for vals in dct[c].values():
                vals.sort()
                row.extend(vals)
            res.append(row)

        return res


if __name__ == "__main__":
    testcases = [
        [3, 9, 20, None, None, 15, 7],  # [[9],[3,15],[20],[7]]
        [1, 2, 3, 4, 5, 6, 7],  # [[4],[2],[1,5,6],[3],[7]]
        [1, 2, 3, 4, 6, 5, 7],  # [[4],[2],[1,5,6],[3],[7]]
    ]
    for testcase in testcases:
        root = build_binary_tree_from_level_order_traversal(testcase)
        obj = Solution()
        print(obj.verticalTraversal(root))
