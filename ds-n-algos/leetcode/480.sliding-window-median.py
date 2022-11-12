# @author: yprakash
import heapq
from typing import List


class Solution:
    # Correct but Time Limit Exceeded  https://leetcode.com/submissions/detail/841898301/
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def move_from_right_to_left(left_heap, right_heap):
            while len(left_heap) < len(right_heap):
                n, i = heapq.heappop(right_heap)
                heapq.heappush(left_heap, (-n, i))

        if k <= 1:
            return nums

        right_heap = [(n, index) for index, n in enumerate(nums[:k])]
        heapq.heapify(right_heap)
        left_heap = []  # 1. create left(max), right(min) heaps
        move_from_right_to_left(left_heap, right_heap)

        if len(left_heap) > len(right_heap):  # 2. median of first k elements
            medians = [-left_heap[0][0]]
        else:
            medians = [round((right_heap[0][0] - left_heap[0][0]) / 2, 5)]

        for index, n in enumerate(nums[k:], start=k):
            # 3. Insert new element into the correct heap
            if n < right_heap[0][0]:
                heapq.heappush(left_heap, (-n, index))
            else:
                heapq.heappush(right_heap, (n, index))

            prev = nums[index - k]
            # 4. delete obsolete elem from the heap in which it exists
            if prev < right_heap[0][0] or (prev == right_heap[0][0] and index - k < right_heap[0][1]):
                while left_heap and left_heap[0][1] != index - k:
                    n, i = heapq.heappop(left_heap)
                    heapq.heappush(right_heap, (-n, i))
                if left_heap:  # Pop & ignore
                    heapq.heappop(left_heap)
                move_from_right_to_left(left_heap, right_heap)
            else:  # Obsolete elem exists in right heap
                while right_heap and right_heap[0][1] != index - k:
                    n, i = heapq.heappop(right_heap)
                    heapq.heappush(left_heap, (-n, i))
                if right_heap:  # Pop & ignore
                    heapq.heappop(right_heap)
                while 1 + len(right_heap) < len(left_heap):  # move_from_left_to_right
                    n, i = heapq.heappop(left_heap)
                    heapq.heappush(right_heap, (-n, i))

            if len(left_heap) > len(right_heap):
                medians.append(-left_heap[0][0])
            else:
                medians.append(round((right_heap[0][0] - left_heap[0][0]) / 2, 5))

        return medians


if __name__ == "__main__":
    testcases = [
        [3, [1, 3, -1, -3, 5, 3, 6, 7]],  # [1, -1, -1, 3, 5, 6]
        [3, [1, 2, 3, 4, 2, 3, 1, 4, 2]],  # [2, 3, 3, 3, 2, 3, 2]
    ]
    for kk, testcase in testcases:
        obj = Solution()
        print(obj.medianSlidingWindow(testcase, kk))
