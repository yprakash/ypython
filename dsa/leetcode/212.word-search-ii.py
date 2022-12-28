# @author: yprakash
from typing import List


def print_trie(root):  # prints all possible trie paths as strings
    paths = []

    def traverse(path, node):
        if node.end_of_word:
            paths.append(path)
        for child in node.children:
            traverse(path + child, node.children[child])

    traverse('', root)
    for path in paths:
        print(path)


class Solution:
    # Build a TRIE data structure for all the possible paths in board
    # and for each word in given words, search if word path exists in TRIE
    # Correct but Time Limit Exceeded, TRIE should be the other way
    # because this trie can contain a depth of m*n (= 12*12 from constraints)
    # Searching 144 level tree for 10 length words is highly inefficient and impractical
    # https://leetcode.com/submissions/detail/837184683/
    def findWords1(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        # -- TRIE insert and Search methods -- #
        # class TrieNode():
        #     def __init__(self):
        #         self.children = {}

        def trie_insert(node, r, c):
            if r < 0 or r >= m or c < 0 or c >= n or visited[r][c]:
                return
            if board[r][c] not in node:
                node[board[r][c]] = {}  # TrieNode()

            visited[r][c] = True
            node = node[board[r][c]]
            trie_insert(node, r-1, c)
            trie_insert(node, r, c-1)
            trie_insert(node, r, c+1)
            trie_insert(node, r+1, c)
            visited[r][c] = False

        def trie_search(node, word):
            for c in word:
                if c not in node:
                    return False
                node = node[c]
            return True

        # ---------------------- #

        root = {}  # TrieNode()

        for r in range(m):
            for c in range(n):
                trie_insert(root, r, c)

        result = []
        for word in words:
            if trie_search(root, word):
                result.append(word)

        return result

    # ============
    # Build TRIE for dictionary of words and search board paths in it
    # https://leetcode.com/submissions/detail/837219565/
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = set()  # list can duplicate a word if word exists in multiple board paths
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        # -- TRIE insert and Search methods -- #
        class TrieNode:
            def __init__(self):
                self.children = {}
                # If words contains both 'ab' and 'abc', we can't find word 'ab' without this flag
                self.end_of_word = False

        def trie_insert(node, word):
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.end_of_word = True

        def trie_search(path, node, r, c):
            if r < 0 or r >= m or c < 0 or c >= n or visited[r][c]:
                return
            if board[r][c] not in node.children:
                return

            visited[r][c] = True
            path += board[r][c]
            node = node.children[board[r][c]]
            trie_search(path, node, r-1, c)
            trie_search(path, node, r, c-1)
            trie_search(path, node, r, c+1)
            trie_search(path, node, r+1, c)
            visited[r][c] = False
            if node.end_of_word:
                result.add(path)  # should be at the end of recursion

        # ---------------------- #

        root = TrieNode()
        for word in words:
            trie_insert(root, word)

        print_trie(root)
        for r in range(m):
            for c in range(n):
                trie_search('', root, r, c)

        return list(result)


if __name__ == "__main__":
    testcases = [
        [["abcb"], [["a", "b"], ["c", "d"]]],  # []
        [["oath", "pea", "eat", "oat", "rain"],
         [["o", "a", "a", "n"],
          ["e", "t", "a", "e"],
          ["i", "h", "k", "r"],
          ["i", "f", "l", "v"]]],
    ]
    for ws, mat in testcases:
        obj = Solution()
        print(obj.findWords(mat, ws))
