# @author: yprakash
from collections import Counter
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/772779264/
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        word_len = len(words[0])

        for i in range(1 + len(s) - word_len * len(words)):
            append = True
            word_set = Counter(words)

            for j in range(i, i + word_len * len(words), word_len):
                word = s[j:j+word_len]
                if word_set.get(word, 0) > 0:
                    word_set[word] -= 1
                else:
                    append = False
                    break

            if append:
                res.append(i)

        return res


testcases = [
    ["barfoothefoobarman", ["foo","bar"]],  # [0, 9]
    ["barfoofoobarthefoobarman", ["bar","foo","the"]],  # [6, 9, 12]
    ["wordgoodgoodgoodbestword", ["word","good","best","good"]],  # [8]
    ["wordgoodgoodgoodbestword", ["word","good","best","word"]],  # []
]
for testcase in testcases:
    obj = Solution()
    print(obj.findSubstring(testcase[0], testcase[1]))
