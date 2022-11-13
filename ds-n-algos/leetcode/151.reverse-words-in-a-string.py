# @author: yprakash

class Solution:
    # https://leetcode.com/submissions/detail/842571533/
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s.reverse()
        return ' '.join(s)


if __name__ == "__main__":
    testcases = [
        " the sky is blue",  # "blue is sky the"
        "  hello world  ",  # "world hello"
        " a good   example ",  # "example good a"
    ]
    for testcase in testcases:
        obj = Solution()
        print(obj.reverseWords(testcase))
