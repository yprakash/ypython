# @author: yprakash

# def guess(num: int) -> int:
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

class Solution:
    # https://leetcode.com/submissions/detail/844224015/
    def guessNumber(self, n: int) -> int:
        lower, higher = 1, n

        while lower <= higher:
            num = randint(lower, higher)
            g = guess(num)
            if g == 0:
                return num
            if g < 0:
                higher = num - 1
            else:
                lower = num + 1

        return 0
