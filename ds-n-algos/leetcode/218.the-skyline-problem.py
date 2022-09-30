# @author: yprakash
import heapq


class Solution(object):
    # https://leetcode.com/submissions/detail/812148364/
    def getSkyline(self, buildings):
        points = []
        for b in buildings:
            points.append((b[0], -b[2]))
            points.append((b[1], b[2]))
        points.sort(key=lambda x: (x[0], x[1]))

        # prev stores the current height
        prev = 0
        pq = [0]
        results = []
        for p in points:
            if p[1] < 0:
                heapq.heappush(pq, p[1])
            else:
                if -p[1] in pq:
                    i = pq.index(-p[1])
                    pq[i] = pq[-1]
                    pq.pop()
                    if i < len(pq):
                        heapq._siftup(pq, i)
                        heapq._siftdown(pq, 0, i)

            current = -pq[0]
            if prev != current:
                results.append((p[0], current))
                prev = current
        return results
