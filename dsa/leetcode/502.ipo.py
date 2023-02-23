# @author: yprakash
from heapq import heappush, heappop
from typing import List


# https://leetcode.com/problems/ipo/submissions/903665917/
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        i = 0
        pq = []  # heap / priority queue
        # projects = list(zip(capital, profits)) \n projects.sort()
        capital, profits = zip(*sorted(zip(capital, profits)))  # zip-sort-unzip

        while k:
            while i < len(capital) and capital[i] <= w:
                heappush(pq, -profits[i])
                i += 1
            if not pq:
                break

            w -= heappop(pq)
            k -= 1
        return w


if __name__ == "__main__":
    testcases = [
        [2, 0, [1, 2, 3], [0, 1, 1]],  # 4
        [3, 0, [1, 2, 3], [0, 1, 2]],  # 6
        [3, 0, [1, 2, 5, 7, 6, 8, 3, 1], [0, 1, 2, 6, 4, 3, 1, 1]],  # 12
    ]
    for t in testcases:
        obj = Solution()
        print(obj.findMaximizedCapital(t[0], t[1], t[2], t[3]))
