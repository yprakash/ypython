# @author: yprakash
from collections import Counter
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/831443965/
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # collect indices from both images with value=1
        A = [(i, j) for i, row in enumerate(img1) for j, item in enumerate(row) if item]
        B = [(i, j) for i, row in enumerate(img2) for j, item in enumerate(row) if item]

        counts = Counter((ax-bx, ay-by) for ax, ay in A for bx, by in B)
        print(counts)
        ans = list(counts.values())
        ans.append(0)
        return max(ans)


if __name__ == "__main__":
    testcases = [
        [[[1, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [0, 1, 1], [0, 0, 1]]],  # 3
    ]
    for i1, i2 in testcases:
        obj = Solution()
        print(obj.largestOverlap(i1, i2))
