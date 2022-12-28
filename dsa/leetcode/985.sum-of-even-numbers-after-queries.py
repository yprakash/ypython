# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/804915055/
    def sumEvenAfterQueries(self, nums, queries):
        ans = []
        even_sum = sum([n for n in nums if n % 2 == 0])

        for val, i in queries:
            if nums[i] % 2 == 0:
                even_sum -= nums[i]
            nums[i] += val
            if nums[i] % 2 == 0:
                even_sum += nums[i]
            ans.append(even_sum)

        return ans
