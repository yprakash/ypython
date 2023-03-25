# @author: yprakash
from collections import Counter, defaultdict, deque
from typing import List


class Solution:
    # https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/submissions/921866183/
    # Using DFS, count no.of nodes in each connected component
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def dfs(v):  # source/starting vertex
            if visited[v]:
                return 0
            count = 1
            visited[v] = True
            for neighbor in adj[v]:
                count += dfs(neighbor)
            return count

        visited = [False] * n
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        counts = []
        for i in range(n):
            if not visited[i]:
                counts.append(dfs(i))

        ans = n * (n - 1) // 2
        for k in counts:
            ans -= k * (k - 1) // 2

        return ans

    # using Union-Find. Correct but TLE
    # https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/submissions/921853165/
    def countPairs6(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px < py:
                px, py = py, px

            parent[px] = py
            children[py].add(px)
            if px in children:
                for c in children[px]:
                    parent[c] = py
                    children[py].add(c)
                del children[px]

        parent = [i for i in range(n)]
        children = defaultdict(set)
        for a, b in edges:
            union(a, b)

        counter = list(Counter(parent).values())
        ans = 0
        for i in range(1, len(counter)):
            for j in range(i):  # This O(N^2) resulted in TLE
                ans += counter[i] * counter[j]

        return ans

    # https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/submissions/921610615/
    # BFS TLE because of last formula
    def countPairs3(self, n: int, edges: List[List[int]]) -> int:
        def bfs(src):
            if src == None or visited[src]:
                return 0
            count = 0
            q = deque()
            q.append(src)
            visited[src] = True

            while q:
                a = q.popleft()
                count += 1
                for b in adj[a]:
                    if not visited[b]:
                        visited[b] = True
                        q.append(b)

            return count

        visited = [False] * n
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        node_counts = []
        ans = 0
        for i in range(n):
            if not visited[i]:
                n = bfs(i)
                ans += sum(n * nc for nc in node_counts)
                node_counts.append(n)

        return ans


if __name__ == "__main__":
    testcases = [
        (3, [[0, 1], [0, 2], [1, 2]]),  # 0 - all 3 are connected
        (7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]),  # 14
        (16, [[0, 15], [1, 14], [2, 11], [4, 3], [5, 15], [8, 2], [14, 12]]),  # 110
        (11, [[5, 0], [1, 0], [10, 7], [9, 8], [7, 2], [1, 3], [0, 2], [8, 5], [4, 6], [4, 2]]),  # 0
    ]
    for v, e in testcases:
        obj = Solution()
        print(obj.countPairs(v, e))
