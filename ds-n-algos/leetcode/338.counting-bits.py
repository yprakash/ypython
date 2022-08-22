# @author: yprakash

class Solution:
    # https://leetcode.com/submissions/detail/780375037/
    # Using Brian Kernighan's algorithm
    def countBits(self, n):
        res = [0]
        for x in range(1, 1+n):
            count = 0
            while x:
                # x & (x-1) can be used to turn off the rightmost set bit of a number n
                x = x & (x-1)
                count += 1
            res.append(count)

        return res

    # https://leetcode.com/submissions/detail/739096609/
    # 0 <= n <= 10^5
    def countBits2(self, n):
        ans = [0, 1]
        while len(ans) <= n:
            ans.extend([1+x for x in ans])
        return ans[:n+1]


if __name__ == "__main__":
    obj = Solution()
    for n in range(20):
        print(obj.countBits(n))
