# @author: yprakash

class Solution(object):
    def interleave(self, s1, s2, s3, i, j, bl):
        if i == len(s1) and j == len(s2):
            bl[i][j] = True
            return True
        if i < len(s1) and s1[i] == s3[i + j]:
            if self.interleave(i + 1, j):
                bl[i][j] = True
                return True
        if j < len(s2) and s2[j] == s3[i + j]:
            return self.interleave(i, j + 1)

    def isInterleave(self, s1, s2, s3):
        bl = [[None] * (1+len(s1))] * (1+len(s2))
        if len(s1) + len(s2) != len(s3):
            return False
        self.interleave(s1, s2, s3, 0, 0, bl)


obj = Solution()
strs = [
    ["", "", ""],
    ["aabcc", "dbbca", "aadbbcbcac"],
    ["aabcc", "dbbca", "aadbbbaccc"],
    ["bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
     "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
     "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababb" +
     "bababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"]
]
for s in strs:
    print(obj.isInterleave(s[0], s[1], s[2]))
