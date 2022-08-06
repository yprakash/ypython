# @author: yprakash

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        pigs = 0
        tests = int(1 + minutesToTest / minutesToDie)
        while tests ** pigs < buckets:
            pigs += 1
        return pigs


testcases = [
    [4, 15, 15],
    [4, 15, 30],
    [1000, 15, 60],
]
obj = Solution()
for testcase in testcases:
    print(obj.poorPigs(testcase[0], testcase[1], testcase[2]))
