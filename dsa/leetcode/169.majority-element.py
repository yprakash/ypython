# @author: yprakash
# https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm

class Solution:
    def majorityElement2(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]

    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        maj_index = 0

        for i, num in enumerate(nums):
            if num == nums[maj_index]:
                count += 1
            else:
                count -= 1
                if count == 0:
                    count = 1
                    maj_index = i

        return nums[maj_index]

