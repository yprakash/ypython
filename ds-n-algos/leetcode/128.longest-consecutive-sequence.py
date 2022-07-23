# @author: yprakash

class Solution(object):
    # O(N) https://leetcode.com/submissions/detail/738926791/
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums = set(nums)
        max_len = 1

        for num in nums:
            if num-1 in nums:
                continue
            curr_len = 1
            num += 1

            while num in nums:
                curr_len += 1
                num += 1
            if max_len < curr_len:
                max_len = curr_len

        return max_len

    # O(N logN) for sort https://leetcode.com/submissions/detail/738711228
    def longestConsecutive2(self, nums):
        if not nums:
            return 0
        nums.sort()
        max_len = 1
        l, r = 0, 0

        for num in nums[1:]:
            if num == nums[r]:
                l += 1
                r += 1
            elif num > nums[r] + 1:
                if max_len <= r - l:
                    max_len = 1 + r - l
                r += 1
                l = r
            else:
                r += 1

        if max_len <= r - l:
            max_len = 1 + r - l
        return max_len


obj = Solution()
print(obj.longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4. The longest consecutive elements sequence is [1, 2, 3, 4]
print(obj.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
