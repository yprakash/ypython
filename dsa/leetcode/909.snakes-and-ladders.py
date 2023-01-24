# @author: yprakash
from collections import deque
from typing import List


# https://leetcode.com/problems/snakes-and-ladders/submissions/884518028/
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        steps = list(range(1 + n * n))
        visited = [False] * (1 + n * n)
        visited[0] = visited[1] = True
        left_to_right = True

        for r in range(n-1, -1, -1):
            if left_to_right:
                left_to_right = False
                col_range = range(n)
            else:
                left_to_right = True
                col_range = range(n-1, -1, -1)

            for c in col_range:
                if board[r][c] > 0:
                    index = n - c if left_to_right else 1 + c
                    index += n * (n-1-r)
                    steps[index] = board[r][c]

        q = deque([(steps[1], 1)])
        while q:
            curr, moves = q.popleft()
            for i in range(curr + 1, min(curr + 6, n * n) + 1):
                if i + 1 >= len(steps) or 1 + steps[i] >= len(steps):
                    return moves
                if not visited[steps[i]]:
                    visited[steps[i]] = True
                    q.append((steps[i], 1 + moves))

        return -1


if __name__ == "__main__":
    testcases = [
        [[-1, -1], [-1, 3]],
        [[-1, -1, -1],
         [-1, 9, 8],
         [-1, 8, 9]],
        [[-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 35, -1, -1, 13, -1],
         [-1, -1, -1, -1, -1, -1],
         [-1, 15, -1, -1, -1, -1]]
    ]
    for testcase in testcases:
        obj = Solution()
        print(obj.snakesAndLadders(testcase))
