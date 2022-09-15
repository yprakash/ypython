# @author: yprakash

class Solution(object):
    # https://leetcode.com/contest/weekly-contest-310/submissions/detail/796765949/
    def partitionString(self, s):
        res = 1
        prev = ''
        for c in s:
            if c in prev:
                prev = c
                res += 1
            else:
                prev += c
        return res


obj = Solution()
print(obj.partitionString("abacaba"))
print(obj.partitionString("ssssss"))
