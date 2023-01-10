# @author: yprakash

# https://leetcode.com/contest/biweekly-contest-95/submissions/detail/873396386/
class DataStream:
    def __init__(self, value: int, k: int):
        self.k = k
        self.len = 0
        self.value = value

    def consec(self, num: int) -> bool:
        if self.value == num:
            self.len += 1
            return self.len >= self.k
        self.len = 0
        return False
