# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/779871788/
    def isPowerOfFour(self, n):
        # if n < 0: n = -n
        if n == 1:
            return True

        last_digit = n % 10
        if last_digit == 4 or last_digit == 6:
            return n & (n - 1) == 0
        return False


if __name__ == "__main__":
    obj = Solution()
    for i in range(-10, 100):
        if obj.isPowerOfFour(i):
            print(i)
