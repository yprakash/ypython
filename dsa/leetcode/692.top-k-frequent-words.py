# @author: yprakash
from collections import Counter
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/825644473/
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        freq = Counter(words).most_common(k)
        freq.sort(key=lambda e: (-e[1], e[0]))
        return [key for key, val in freq]


if __name__ == "__main__":
    testcases = [
        [2, ["i", "love", "leetcode", "i", "love", "coding"]],  # ["i","love"]
        [3, ["i", "love", "leetcode", "i", "love", "coding"]],  # ["i","love","coding"]
        [4, ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]],  # ["the","is","sunny","day"]
    ]
    for k, words in testcases:
        obj = Solution()
        print(obj.topKFrequent(words, k))
