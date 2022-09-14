# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/797630293/
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        score, i, j = 0, 0, len(tokens) - 1
        max_score = 0  # Track the maximum while looping

        while i <= j:
            # Be Greedy. If the current power is sufficient to face up,
            # take next smallest token to increase/maximize score
            if power >= tokens[i]:
                power -= tokens[i]
                i += 1
                score += 1
                if max_score < score:
                    max_score = score
            # Face down biggest token and fuel power up,
            # to maximize score in next iterations
            elif score >= 1:
                power += tokens[j]
                j -= 1
                score -= 1
            else:
                break  # No other way

        return max_score


if __name__ == "__main__":
    testcases = [
        [50, [100]],  # 0
        [150, [100, 200]],  # 1
        [200, [100, 200, 300, 400]],  # 2
    ]
    for p, t in testcases:
        obj = Solution()
        print(obj.bagOfTokensScore(t, p))
