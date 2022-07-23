# @author: yprakash
# Given an integer array nums and an integer k, return the kth largest element in the array

# The simple, O(n log n) way is to sort the list then get the last k elements.
# return sorted(nums)[-k]
# The proper way is to use a selection algorithm, which runs in O(n + k log k) time.
# Also, heapq.nlargest takes O(n log k) time on average
import heapq


class Solution(object):
    # https://leetcode.com/submissions/detail/731457421/
    def findKthLargest(self, nums, k):
        min_heap = []
        for i in range(k):
            heapq.heappush(min_heap, nums[i])

        for i in range(k, len(nums)):
            heapq.heappushpop(min_heap, nums[i])
        return min_heap[0]

    # one liner inbuilt and faster
    # https://leetcode.com/submissions/detail/731446525/
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

    # Hoare's QuickSelect algorithm
    def quick_select(self, a, lo, hi):  # O(N)
        if lo >= hi:
            return hi
        i, j = lo, lo
        # select a pivot element and place it in final position

        while j < hi:
            # Move all smaller elements < a[hi] to the left of array
            if a[j] < a[hi]:
                if i < j:
                    a[i], a[j] = a[j], a[i]
                i += 1
            j += 1

        a[i], a[hi] = a[hi], a[i]
        # return the index of the correctly placed pivot element
        return i

    # https://leetcode.com/submissions/detail/731390495/
    def findKthLargest(self, nums, k):
        k = len(nums) - k
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            x = self.quick_select(nums, lo, hi)
            if x < k:
                lo = x + 1
            elif x > k:
                hi = x - 1
            else:
                return nums[k]

        return None  # In any case, execution doesn't come here


obj = Solution()
nums = [3, 2, 1, 5, 6, 4]
print(obj.findKthLargest(nums, 2))
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
print(obj.findKthLargest(nums, 4))
