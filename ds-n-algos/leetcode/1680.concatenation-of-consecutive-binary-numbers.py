# @author: yprakash

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = 0
        mod = 1000000007
        size = 0  # no.of bits in i

        for i in range(1, 1+n):
            if i & i - 1 == 0:
                size += 1
            res = (res << size | i) % mod

        return res


if __name__ == "__main__":
    testcases = [1, 3, 12, 100000]
    for testcase in testcases:
        obj = Solution()
        print(obj.concatenatedBinary(testcase))
