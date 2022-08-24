# @author: yprakash
from math import log10


class Solution(object):
    # https://leetcode.com/submissions/detail/781737665/
    # Should be >= Python 3.5
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:  # Should check to avoid undefined ValueError: math domain error
            return False
        return (log10(n) / log10(3)).is_integer()

    # https://leetcode.com/submissions/detail/781723208/
    def isPowerOfThree1(self, n):
        # For all 3 powers, 3 is the only prime factor.
        # Take the biggest possible 3 power below 2^31 - 1
        if n > 0:
            return 1162261467 % n == 0
        return False


if __name__ == "__main__":
    obj = Solution()
    for i in range(1, 250):
        if (log10(i) / log10(3)).is_integer():
            print(i-1, obj.isPowerOfThree(i-1))
            print(i, obj.isPowerOfThree(i))
            print(i+1, obj.isPowerOfThree(i+1))
