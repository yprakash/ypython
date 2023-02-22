# @author: yprakash
from typing import List


# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/submissions/902670690/
# TC: O(n logC) where n: no.of weights and C is the sum of all weights
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_be_shipped(capacity):  # O(N)
            w, d = 0, 1
            for weight in weights:
                if w + weight <= capacity:
                    w += weight
                else:
                    w = weight
                    d += 1
            return d <= days

        if not weights or days < 1:
            return 0
        left = max(weights)
        right = sum(weights)
        min_capacity = right

        while left <= right:
            mid = left + (right - left) // 2
            if can_be_shipped(mid):
                min_capacity = mid
                right = mid - 1
            else:
                left = mid + 1

        return min_capacity


if __name__ == "__main__":
    testcases = [
        [[1, 2, 3, 1, 1], 4],  # 3
        [[3, 2, 2, 4, 1, 4], 3],  # 6
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5],  # 15
        [[10, 50, 100, 100, 50, 100, 100, 100], 5]  # 160
    ]
    for testcase in testcases:
        obj = Solution()
        print(obj.shipWithinDays(testcase[0], testcase[1]))
