# @author: yprakash
import string
from collections import deque, defaultdict
from typing import List


class Solution:
    # TLE https://leetcode.com/problems/word-ladder-ii/submissions/868144381/
    def findLadders4(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)
        nei = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1:]
                nei[pattern].append(word)

        proceed = True
        sequences = []
        visited = set()
        q = deque([[beginWord]])

        while proceed and q:
            for i in range(len(q)):
                sequence = q.popleft()
                visited.add(sequence[-1])

                for j in range(len(sequence[-1])):
                    pattern = sequence[-1][:j] + '*' + sequence[-1][j + 1:]

                    for word in nei[pattern]:
                        if word == endWord:
                            proceed = False
                            sequences.append(sequence + [word])
                        elif proceed and word not in visited:
                            q.append(sequence + [word])

        return sequences

    def findLadders3(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = {}
        sequences = []
        proceed = True
        q = deque([[beginWord]])
        wordList = set(wordList) - {beginWord}

        while proceed and q:
            for _ in range(len(q)):
                sequence = q.popleft()
                words = set()
                for w in wordList:
                    miss = 0
                    for a, b in zip(sequence[-1], w):
                        if a != b:
                            miss += 1
                            if miss > 1:
                                break
                    if miss == 1:
                        words.add(w)

                for word in words:
                    if word == endWord:
                        proceed = False
                        sequences.append(sequence + [word])
                    elif proceed:
                        q.append(sequence + [word])

            wordList -= words
        return sequences

    def findLadders2(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = {}
        sequences = []
        proceed = True
        q = deque([[beginWord]])
        wordList = set(wordList) - {beginWord}

        while proceed and q:
            for _ in range(len(q)):
                sequence = q.popleft()
                words = {w for w in wordList if sum(a != b for a, b in zip(sequence[-1], w)) == 1}

                for word in words:
                    if word == endWord:
                        proceed = False
                        sequences.append(sequence + [word])
                    elif proceed:
                        q.append(sequence + [word])

            wordList -= words
        return sequences

    # TLE(21/36) https://leetcode.com/problems/word-ladder-ii/submissions/867813804/
    def findLadders1(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        proceed = True
        sequences = []
        q = deque([[beginWord]])

        while proceed and q:
            for _ in range(len(q)):
                sequence = q.popleft()
                words = [w for w in wordList if w not in sequence
                         and sum(a != b for a, b in zip(sequence[-1], w)) == 1]

                for word in words:
                    if word == endWord:
                        proceed = False
                        sequences.append(sequence + [word])
                    elif proceed:
                        q.append(sequence + [word])

        return sequences


if __name__ == "__main__":
    testcases = [
        ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]],  # []
        ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]]
        # output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
    ]
    for b, e, l in testcases:
        obj = Solution()
        print(obj.findLadders(b, e, l))
