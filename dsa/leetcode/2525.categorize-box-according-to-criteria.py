# @author: yprakash

# https://leetcode.com/contest/biweekly-contest-95/submissions/detail/873329567/
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        heavy = mass >= 100
        bulky = length >= 10000 or width >= 10000 or height >= 10000 or \
            length * width * height >= 10 ** 9

        if bulky:
            return "Both" if heavy else "Bulky"
        return "Heavy" if heavy else "Neither"
