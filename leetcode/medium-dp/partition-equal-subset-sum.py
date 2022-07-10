# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/741998965/
    # Bottom-up Dynamic Programming with Tabulation
    # Time Complexity: O(N * S) & Space: O(2*S)
    def canPartition(self, nums):
        if len(nums) < 1:
            return False
        s = sum(nums)
        if s % 2 != 0:
            return False
        n = len(nums)
        s = int(s / 2)
        row1 = [False] * (1+s)
        row1[0] = True

        for i in range(1, n):
            row = [False] * (1+s)
            row[0] = True
            for j in range(1, 1+s):
                # If curr i-th num can be included
                if j - nums[i] >= 0 and row1[j - nums[i]]:
                    row[j] = True
                elif row1[j]:  # when curr elem is excluded
                    row[j] = True
            row1 = row
        return row1[-1]

    # Brute Force Solution
    # try all combinations of partitioning the given numbers into two sets to see if any pair of sets has an equal sum.
    # This essentially transforms our problem to: Find a subset of the given numbers that has a total sum of sum / 2
    # Time Complexity: O(2^N) Space Complexity: O(N) (store recursion stack)
    def canPartition2(self, nums):
        s = sum(nums)
        if s % 2 != 0:
            return False
        return self.can_partition_recursive(nums, int(s/2), 0)

    def can_partition_recursive(self, nums, sum, current_index):
        if sum == 0:
            return True
        if len(nums) == 0 or current_index >= len(nums):
            return False
        if nums[current_index] <= sum:
            if self.can_partition_recursive(nums, sum-nums[current_index], current_index+1):
                return True
        return self.can_partition_recursive(nums, sum, current_index+1)


nnums = [
    [1, 2, 5],  # false
    [1, 2, 3, 5],  # false
    [2, 2, 3, 5],  # false
    [1, 5, 11, 5],  # true
    [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
    100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
    100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
    100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
    100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
    100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
    100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
    100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
    100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]  # false
]
obj = Solution()
for nnum in nnums:
    print(obj.canPartition(nnum))
