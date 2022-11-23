# @author: yprakash
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/848334247/
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(x, y, axis):
            if axis == 0:
                cells = [board[x][j] for j in range(9) if board[x][j] != '.']
            elif axis == 1:
                cells = [board[i][y] for i in range(9) if board[i][y] != '.']
            else:
                cells = []
                for i in range(x, x+3):
                    for j in range(y, y+3):
                        if board[i][j] != '.':
                            cells.append(board[i][j])

            seen = set()
            for d in cells:
                if d in seen:
                    return False
                seen.add(d)
            return True

        for i in range(len(board)):
            if not is_valid(i, 0, 0):
                return False
        for i in range(len(board[0])):
            if not is_valid(0, i, 1):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not is_valid(i, j, 2):
                    return False

        return True
