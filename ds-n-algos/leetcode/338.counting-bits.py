# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/739096609/
    # 0 <= n <= 105
    def countBits(self, n):
        ans = [0, 1]
        while len(ans) <= n:
            ans.extend([1+x for x in ans])
        return ans[:n+1]


obj = Solution()
print(obj.countBits(2))  # [0,1,1]
print(obj.countBits(5))  # [0,1,1,2,1,2]
