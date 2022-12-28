# @author: yprakash

class Solution:
    # https://leetcode.com/submissions/detail/838057254/
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            # any permutation of s is possible, because we can bring the second smallest to be after the smallest,
            # then the third smallest to be after the second smallest, and so on.
            # and the answer is the letters of s written in lexicographic order.
            return ''.join(sorted(s))
        else:
            # only rotations of s are possible, and the answer is the lexicographically smallest rotation. O(N ^ 2)
            return min(s[i:] + s[:i] for i in range(len(s)))
