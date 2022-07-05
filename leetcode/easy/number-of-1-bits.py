# @author: yprakash

class Solution(object):
    # From python3.1  https://leetcode.com/submissions/detail/739105103/
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()

    # https://leetcode.com/submissions/detail/739103619/
    def hammingWeight(self, n):
        n = bin(n)
        return n.bit_count()


obj = Solution()
print(obj.hammingWeight('00000000000000000000000000001011'))  # 3
print(obj.hammingWeight('00000000000000000000000010000000'))  # 1
print(obj.hammingWeight('11111111111111111111111111111101'))  # 31
