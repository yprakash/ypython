# @author: yprakash
from collections import deque
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/835083496/
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        visited = set()
        mutations = 0
        q = deque()
        q.append(start)

        while q:
            size = len(q)
            while size > 0:
                size -= 1
                curr = q.popleft()
                if curr == end:
                    return mutations

                visited.add(curr)
                for gene in bank:
                    if gene not in visited and sum(1 for x, y in zip(gene, curr) if x != y) == 1:
                        q.append(gene)

            mutations += 1

        return -1


if __name__ == "__main__":
    testcases = [
        ["AACCGGTT", "AACCGGTA", ["AACCGGTA"]],  # 1
        ["AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]],  # 2
        ["AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]],  # 3
        ["AAAACCCC", "CCCCCCCC",
         ["AAAACCCA", "AAACCCCA", "AACCCCCA", "AACCCCCC", "ACCCCCCC", "CCCCCCCC", "AAACCCCC", "AACCCCCC"]],  # 4
    ]
    for s, e, b in testcases:
        obj = Solution()
        print(obj.minMutation(s, e, b))
