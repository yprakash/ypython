# @author: yprakash
from collections import deque
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/854389897/
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        clr = image[sr][sc]
        if clr == color:
            return image

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        m, n = len(image), len(image[0])
        visited = set()
        q = deque()
        q.append((sr, sc))

        while q:
            r, c = q.popleft()
            visited.add((r, c))
            image[r][c] = color
            for d in directions:
                r0, c1 = r + d[0], c + d[1]
                if 0 <= r0 < m and 0 <= c1 < n and clr == image[r0][c1] \
                        and image[r0][c1] not in visited:
                    q.append((r0, c1))

        return image
