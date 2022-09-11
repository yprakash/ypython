# @author: yprakash
import heapq


class Solution(object):
    # https://leetcode.com/submissions/detail/796722530/
    def maxPerformance(self, n, speed, efficiency, k):
        heap, total_speed, best = [], 0, 0
        engines = sorted(zip(efficiency, speed), reverse=True)

        for eff, speed in engines:
            heapq.heappush(heap, speed)
            if len(heap) <= k:
                total_speed += speed
            else:
                total_speed += speed - heapq.heappop(heap)
            best = max(best, eff * total_speed)

        return best % 1000000007


if __name__ == "__main__":
    testcases = [
        [6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2],  # 60
        [6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3],  # 68
        [6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 4],  # 72
    ]
    for a, b, c, d in testcases:
        obj = Solution()
        print(obj.maxPerformance(a, b, c, d))
