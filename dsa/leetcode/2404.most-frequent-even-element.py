# @author: yprakash
from collections import Counter


class Solution(object):
    # https://leetcode.com/contest/weekly-contest-310/submissions/detail/796757605/
    def mostFrequentEven(self, nums):
        nums = [num for num in nums if num % 2 == 0]
        if not nums:
            return -1

        stats = Counter(nums)
        maxv = max(stats, key=stats.get)
        maxv = stats[maxv]
        res = 100001

        for k, v in stats.items():
            if v == maxv and k < res:
                res = k

        return res


if __name__ == "__main__":
    testcases = [
        [8154, 9139, 8194, 3346, 5450, 9190, 133, 8239, 4606, 8671, 8412, 6290]  # 3346
    ]
    for testcase in testcases:
        obj = Solution()
        print(obj.mostFrequentEven(testcase))
