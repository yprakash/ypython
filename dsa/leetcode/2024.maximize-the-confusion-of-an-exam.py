# @author: yprakash

class Solution:
    # https://leetcode.com/problems/maximize-the-confusion-of-an-exam/submissions/988718788/
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        char_count = {'T': 0, 'F': 0}
        left, max_freq = 0, 0
        for right, key in enumerate(answerKey):
            char_count[key] += 1
            max_freq = max(max_freq, char_count[key])
            if 1 + right - left > max_freq + k:
                char_count[answerKey[left]] -= 1
                left += 1

        return len(answerKey) - left


if __name__ == "__main__":
    testcases = [
        ["TTFF", 2],  # 4
        ["TFFT", 1],  # 3
        ["TTFTTFTT", 1]  # 5
    ]
    for akey, k in testcases:
        obj = Solution()
        print(obj.maxConsecutiveAnswers(akey, k))
