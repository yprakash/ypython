# @author: yprakash
from typing import List


class Solution:
    # Accepted python2.7 https://leetcode.com/submissions/detail/837102496/
    def exist(self, board, word):
        path = set()
        m, n = len(board), len(board[0])

        def word_formed(word_index, row, col):
            if word_index == len(word):
                return True
            if row < 0 or row >= m or col < 0 or col >= n or \
                    board[row][col] != word[word_index] or (row, col) in path:
                return False

            path.add((row, col))
            formed = (word_formed(word_index + 1, row - 1, col) or
                      word_formed(word_index + 1, row, col - 1) or
                      word_formed(word_index + 1, row + 1, col) or
                      word_formed(word_index + 1, row, col + 1))

            path.remove((row, col))
            return formed

        for i in range(m):
            for j in range(n):
                if word_formed(0, i, j):
                    return True

        return False

    # check why above Backtracking solution Accepted python2.7
    # but the same approach below got Time Limit Exceeded in python3
    # TC: O(m * n * 4 ^ len(word)) both
    # https://leetcode.com/submissions/detail/837095201/
    def exist3(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        def word_formed(word_index, row, col):
            if word_index == len(word):
                return True
            if row < 0 or row >= m or col < 0 or col >= n or \
                    visited[row][col] or board[row][col] != word[word_index]:
                return False

            visited[row][col] = True
            formed = word_formed(word_index + 1, row - 1, col) or \
                     word_formed(word_index + 1, row, col - 1) or \
                     word_formed(word_index + 1, row + 1, col) or \
                     word_formed(word_index + 1, row, col + 1)

            visited[row][col] = False
            return formed

        for i in range(m):
            for j in range(n):
                if word_formed(0, i, j):
                    return True

        return False
