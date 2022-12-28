# @author: yprakash
import heapq
from typing import List


class KthLargest:
    # https://leetcode.com/submissions/detail/825363519/
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        if nums:
            self.heap = nums[:k]
            heapq.heapify(self.heap)
        else:
            self.heap = []

        for i in range(k, len(nums)):
            if nums[i] > self.heap[0]:
                heapq.heappush(self.heap, nums[i])
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            self.heap.append(val)
            heapq.heapify(self.heap)
        elif val > self.heap[0]:
            heapq.heappush(self.heap, val)
            heapq.heappop(self.heap)

        return self.heap[0]


if __name__ == "__main__":
    testcases = [
        [[3, [4, 5, 8, 2]], 3, 5, 10, 9, 4],  # [4, 5, 5, 8, 8]
        [[1, []], -3, -2, -4, 0, 4],  # [-3, -2, -2, 0, 4]
        [[2, [0]], -1, 1, -2, -4, 3],  # [-1, 0, 0, 0, 1]
    ]
    for testcase in testcases:
        obj = KthLargest(testcase[0][0], testcase[0][1])
        print([obj.add(elem) for elem in testcase[1:]])
