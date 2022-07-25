# @author: yprakash
"""
Given an m*n grid 'rooms' initialized with three possible values
-1 : Wall or an obstacle
 0 : Gate
INF: Infinity means an Empty room. Use 2^31-1= 2147483647
Fill each empty room with the distance to its nearest gate, or INF if it is Impossible to reach any gate
"""


class Solution(object):
    def dfs(self, rooms, row, col, distance):
        if row < 0 or row >= len(rooms) or col < 0 or col >= len(rooms[0]):
            return
        if distance > rooms[row][col]:
            return

        rooms[row][col] = distance
        self.dfs(rooms, row-1, col, distance+1)
        self.dfs(rooms, row+1, col, distance+1)
        self.dfs(rooms, row, col-1, distance+1)
        self.dfs(rooms, row, col+1, distance+1)

    def wallsAndGates(self, rooms):
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:  # perform DFS when it is Wall
                    self.dfs(rooms, r, c, 0)
                # ToDo: Write BFS solution using one queue

        return rooms


inf = 2147483647
testcases = [
    [[inf, -1, 0, inf],    # 3, -1, 0, 1
     [inf, inf, inf, -1],  # 2, 2, 1, -1
     [inf, -1, inf, -1],   # 1, -1, 2, -1
     [0, -1, inf, inf]     # 0, -1, 3, 4
     ],
    [[inf, -1, 0, inf],   # inf, -1, 0, 1
     [-1, inf, inf, -1],  # -1, 2, 1, -1
     [inf, -1, inf, -1],  # 1, -1, 2, -1
     [0, -1, inf, inf]    # 0, -1, 3, 4
     ],
]
for testcase in testcases:
    obj = Solution()
    distances = obj.wallsAndGates(testcase)
    for distance in distances:
        print(distance)
    print('==============')
