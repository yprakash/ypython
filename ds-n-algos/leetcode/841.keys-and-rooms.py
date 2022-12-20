# @author: yprakash
from collections import deque
from typing import List


# https://leetcode.com/problems/keys-and-rooms/submissions/862399886/
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        q = deque()
        q.append(0)

        while q:
            room = q.popleft()
            visited[room] = True
            for room in rooms[room]:
                if not visited[room]:
                    q.append(room)

        return all(visited)
