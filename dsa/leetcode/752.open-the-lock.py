# @author: yprakash
from collections import deque
from typing import List


# https://leetcode.com/problems/open-the-lock/submissions/877372073/
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def prev_next(c):
            if c == '9':
                return '8', '0'
            if c == '0':
                return '9', '1'
            return str(int(c) - 1), str(int(c) + 1)

        visited = set(deadends)
        start = '0000'
        if start in visited:
            return -1

        visited.add(start)
        turns = 0
        q = deque()
        q.append(start)

        while q:
            for _ in range(len(q)):
                state = q.popleft()
                if target == state:
                    return turns

                for i in range(4):
                    p, n = prev_next(state[i])
                    if p:
                        p = state[:i] + p + state[1+i:]
                        if p not in visited:
                            visited.add(p)
                            q.append(p)
                    if n:
                        n = state[:i] + n + state[1+i:]
                        if n not in visited:
                            visited.add(n)
                            q.append(n)

            turns += 1

        return -1
