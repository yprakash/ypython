# @author: yprakash
from collections import Counter


class Solution(object):
    def isPossible(self, nums):
        counts = Counter(nums)
        starts = []  # starting number of subsequences
        ends = []  # Ending number of subsequences

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            curr_count = counts[num]

            prev_count = counts.get(num-1, 0)
            for j in range(curr_count - prev_count):
                starts.append(num)

            next_count = counts.get(num+1, 0)
            for j in range(curr_count - next_count):
                ends.append(num)

        # return starts, ends
        for end, start in zip(ends, starts):
            if end - start < 2:
                return False

        return True


if __name__ == "__main__":
    testcases = [
        [1, 2, 3, 3, 4, 5],  # True
        [1, 2, 3, 3, 4, 4, 5, 5],  # True
        [1, 2, 3, 4, 4, 5],  # False
    ]
    obj = Solution()
    for testcase in testcases:
        print(obj.isPossible(testcase))
