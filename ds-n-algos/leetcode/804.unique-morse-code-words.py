# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/775638303/
    def uniqueMorseRepresentations(self, words):
        res = set()
        codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
                 ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
                 "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        # for word in words:
        #     res.add(''.join([codes[ord(char) - 97] for char in word]))

        return len({''.join([codes[ord(char) - 97] for char in word]) for word in words})


testcases = [
    ["a"],  # 1
    ["gin", "zen", "gig", "msg"]  # 2
]
obj = Solution()
for testcase in testcases:
    print(obj.uniqueMorseRepresentations(testcase))
