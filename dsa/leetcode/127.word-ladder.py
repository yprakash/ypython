# @author: yprakash
from collections import deque, defaultdict
from typing import List


class Solution:
    # Accepted https://leetcode.com/submissions/detail/835412204/
    # Hint: try to convert O(n^2 * m) to O(n * m^2)
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        nei = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1:]
                nei[pattern].append(word)

        visited = set()
        transformations = 1
        q = deque([beginWord])

        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return transformations

                visited.add(curr)
                for j in range(len(curr)):
                    pattern = curr[:j] + '*' + curr[j + 1:]

                    for word in nei[pattern]:
                        if word not in visited:
                            q.append(word)

            transformations += 1

        return 0

    # correct but Time Limit Exceeded
    # https://leetcode.com/submissions/detail/835123989/
    def ladderLength3(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # returns True only if there is exactly one character difference
        def can_transform(src, target):
            mute = False
            for x, y in zip(src, target):
                if x != y:
                    if mute:
                        return False
                    mute = True

            return mute

        visited = set()
        transformations = 1
        q = deque()
        q.append(beginWord)

        while q:
            size = len(q)
            while size > 0:
                size -= 1
                curr = q.popleft()
                if curr == endWord:
                    return transformations

                visited.add(curr)
                for word in wordList:
                    if word not in visited and can_transform(curr, word):
                        q.append(word)

            transformations += 1

        return 0

    # correct but Time Limit Exceeded
    # https://leetcode.com/submissions/detail/835121944/
    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        transformations = 1
        q = deque()
        q.append(beginWord)

        while q:
            size = len(q)
            while size > 0:
                size -= 1
                curr = q.popleft()
                if curr == endWord:
                    return transformations

                visited.add(curr)
                for word in wordList:
                    if word not in visited and sum(1 for x, y in zip(curr, word) if x != y) == 1:
                        q.append(word)

            transformations += 1

        return 0
