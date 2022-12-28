# @author: yprakash

class Solution(object):
    def num_digit_frequency(self, x):
        xn = 0
        freq = {}
        while x:
            xn += 1
            freq[x % 10] = 1 + freq.get(x % 10, 0)
            x = x // 10
        return xn, freq

    # As a naive approach, we can check if the number is the power of 2 for every permutation of the digits in N.
    # Time complexity = O((logN)! * logN) but the constraints condition 1 <= N <= 10^9 and for various power of 2,
    # 2^29 = 536870912 and 2^30 = 1073741824. So instead of checking whether the permutation of N is a power of 2,
    # we can check that any of the numbers among 2^x; x=0,1,2...29 has the same number of digits & frequency as of N.
    # https://leetcode.com/submissions/detail/783593136/
    def reorderedPowerOf2(self, n):
        if n == 1:
            return True

        num_digits, digit_frequency = self.num_digit_frequency(n)
        n = 1  # No need of original n from now

        for _ in range(30):
            n = n << 1
            nd, df = self.num_digit_frequency(n)
            if nd == num_digits and df == digit_frequency:
                return True

        return False


if __name__ == "__main__":
    testcases = [1, 10, 16, 24, 46]
    obj = Solution()
    for testcase in testcases:
        print(obj.reorderedPowerOf2(testcase))
