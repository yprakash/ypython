# @author: yprakash
import heapq
from collections import deque, defaultdict


class MinHeap(object):
    def __init__(self):
        self.heap = deque()

    def _get_smaller_child_index(self, p):
        li = 1 + 2 * p
        if li >= len(self.heap):
            return None
        ri = 2 + 2 * p
        if ri >= len(self.heap):
            return li
        return li if self.heap[li] < self.heap[ri] else ri

    def push(self, item):
        c = len(self.heap)
        self.heap.append(item)

        while c > 0:  # heapify
            p = (c - 1) // 2
            if self.heap[c] >= self.heap[p]:  # adhering to min heap property
                break

            self.heap[p], self.heap[c] = self.heap[c], self.heap[p]
            c = p

    def is_empty(self):
        return len(self.heap) == 0

    def pop(self):
        if self.is_empty():
            return None
        if len(self.heap) <= 2:
            return self.heap.popleft()

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]  # Swap first and last items
        popped_item = self.heap.pop()  # Remove last(Min) elem
        p, c = 0, self._get_smaller_child_index(0)

        while c and self.heap[p] > self.heap[c]:
            self.heap[p], self.heap[c] = self.heap[c], self.heap[p]
            p, c = c, self._get_smaller_child_index(c)

        return popped_item


class Solution(object):
    # Using custom heap implementation and Greedy Dijkstra's shortest path algorithm
    # https://leetcode.com/submissions/detail/774319450/
    def networkDelayTime1(self, times, n, k):
        visited = set()
        heap = MinHeap()
        heap.push((0, k))
        dist = {node: float("inf") for node in range(1, n+1)}

        graph = defaultdict(list)
        for src, dst, time in times:
            graph[src].append((dst, time))

        while not heap.is_empty():
            time, node = heap.pop()
            if dist[node] > time:
                dist[node] = time

            for adj_node, adj_time in graph[node]:
                if adj_node not in visited:
                    heap.push((time + adj_time, adj_node))

            visited.add(node)

        max_delay = max(dist.values())
        if max_delay == float("inf"):
            return -1
        return max_delay

    # Using inbuilt heapq and Dijkstra's algorithm
    # https://leetcode.com/submissions/detail/774387002/
    # E: no.of edges, N: no.of nodes. Each edge update takes logN time to re-heapify while heap push
    # heap contains N elements and each pop takes logN to re-heapify
    # TC: O(E * logN + N * logN)
    # TC: O(E * logE) If E is always > N and E items will be pushed into heap instead of N
    # SC: O(E + N)
    def networkDelayTime2(self, times, n, k):
        graph = defaultdict(list)
        for src, dst, time in times:
            graph[src].append((dst, time))

        distances = [float('inf')] * (n + 1)
        distances[0] = 0  # [0] won't be used at all
        distances[k] = 0
        heap = []
        heapq.heappush(heap, (0, k))

        while heap:
            time, vertex = heapq.heappop(heap)
            for adj_node, adj_time in graph[vertex]:
                if distances[adj_node] > adj_time + time:
                    distances[adj_node] = adj_time + time
                    heapq.heappush(heap, (distances[adj_node], adj_node))

        max_delay = max(distances)
        return -1 if max_delay == float("inf") else max_delay

    # https://leetcode.com/submissions/detail/774576833/
    # Using DP Bellman–Ford Algorithm
    # TC: O(N*E)
    def networkDelayTime3(self, times, n, k):
        distance = [float('inf')] * (n + 1)
        distance[0] = 0
        distance[k] = 0

        for i in range(n-1):
            updated = False
            for j in range(len(times)):
                if distance[times[j][0]] + times[j][2] < distance[times[j][1]]:
                    distance[times[j][1]] = distance[times[j][0]] + times[j][2]
                    updated = True

            if not updated:
                break

        max_delay = max(distance)
        return -1 if max_delay == float("inf") else max_delay


testcases = [
    [[[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2],  # 2
    [[[1, 2, 1]], 2, 1],  # 1
    [[[1, 2, 1]], 2, 2]  # -1
]
obj = Solution()
for testcase in testcases:
    print(obj.networkDelayTime(testcase[0], testcase[1], testcase[2]))
