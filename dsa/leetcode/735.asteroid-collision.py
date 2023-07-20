# @author: yprakash
from collections import deque
from typing import List


# https://leetcode.com/problems/asteroid-collision/submissions/999020723/
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        for asteroid in asteroids:
            curr_asteroid_exploded = False
            while stack and stack[-1] > 0 > asteroid:
                if stack[-1] < abs(asteroid):
                    stack.pop()  # smaller one will explode
                else:
                    if stack[-1] == abs(asteroid):
                        stack.pop()  # both will explode
                    curr_asteroid_exploded = True
                    break

            if not curr_asteroid_exploded:
                stack.append(asteroid)

        return list(stack)


if __name__ == "__main__":
    testcases = [
        [8, -8],  # []
        [10, 2, -5],  # [10]
        [5, 10, -5],  # [5, 10]
        [-2, -1, 1, 2],  # [-2, -1, 1, 2]
    ]
    for testcase in testcases:
        obj = Solution()
        print(obj.asteroidCollision(testcase))
