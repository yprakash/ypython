# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/739183835/
    def minCostClimbingStairs(self, cost):
        a, b = cost[0], cost[1]
        for c in cost[2:]:
            a, b = b, c + min(a, b)
        return min(a, b)


obj = Solution()
print(obj.minCostClimbingStairs([10,15,20]))  # 15
print(obj.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))  # 6
