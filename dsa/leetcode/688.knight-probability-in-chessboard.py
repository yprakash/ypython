# @author: yprakash
from functools import lru_cache


class Solution(object):
    # https://leetcode.com/submissions/detail/780430440/
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [[-1, -2], [-2, -1], [-2, 1], [-1, 2],
                      [1, 2], [2, 1], [2, -1], [1, -2]]

        @lru_cache(maxsize=None)
        def rec_prob(m, r, c):
            if r < 0 or r >= n or c < 0 or c >= n:
                return 0  # position is off of the chess board
            if m == 0:
                return 1  # No moves to take

            prob = 0
            for x, y in directions:
                prob += rec_prob(m-1, r+x, c+y) / 8
            return prob

        return rec_prob(k, row, column)


if __name__ == "__main__":
    testcases = [
        [0, 2, 1, 2],  # 0
        [2, 3, 1, 1],  # 0
        [2, 0, 1, 1],  # 1
        [3, 2, 0, 0],  # 0.0625
        [1, 0, 0, 0],  # 1
        [6, 2, 2, 2],  # 0.53125
        [8, 30, 6, 4],  # 0.0001905256629833365
    ]
    obj = Solution()
    for n, k, r, c in testcases:
        print(obj.knightProbability(n, k, r, c))
