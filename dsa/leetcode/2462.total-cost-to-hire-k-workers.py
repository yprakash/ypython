# @author: yprakash
import heapq
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/837836190/
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # if k <= 1: return min(costs) completely wrong
        if k == len(costs):
            return sum(costs)

        cost = 0
        i = candidates  # make sure it is the next element to add to the left heap
        heap1 = costs[:i]
        heapq.heapify(heap1)  # construct left heap O(candidates)

        j = max(candidates, len(costs) - candidates)
        heap2 = costs[j:]
        heapq.heapify(heap2)  # construct right heap O(candidates)
        j -= 1
        # make sure 'j' is the next element to add to the right heap (from reverse)

        for _ in range(k):  # this index is not used, but 'i' is used.  O(k)
            if not heap1:
                cost += heapq.heappop(heap2)
            elif not heap2:
                cost += heapq.heappop(heap1)  # O(log candidates)
            elif heap1[0] <= heap2[0]:
                cost += heapq.heappop(heap1)
                if i <= j:
                    heapq.heappush(heap1, costs[i])  # O(log candidates)
                    i += 1
            else:
                cost += heapq.heappop(heap2)
                if i <= j:
                    heapq.heappush(heap2, costs[j])
                    j -= 1

        # TC: O(max(candidates, k * log(candidates)))
        return cost


if __name__ == "__main__":
    testcases = [
        [3, 3, [1, 2, 4, 1]],  # 4
        [3, 4, [17, 12, 10, 2, 7, 2, 11, 20, 8]],  # 11
    ]
    for kk, cc, nums in testcases:
        obj = Solution()
        print(obj.totalCost(nums, kk, cc))
