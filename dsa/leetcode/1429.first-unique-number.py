# @author: yprakash
from collections import deque, Counter


class FirstUnique(object):
    def __init__(self, nums):
        self.dups = {}  # DS to store already seen (not unique) elements
        self.q = deque()  # DS to store stream

        for n, i in Counter(nums).items():
            self.dups[n] = i == 1

        for num in nums:
            if self.dups[num]:
                self.q.append(num)

    def showFirstUnique(self) -> int:
        while self.q:
            if self.dups[self.q[0]]:
                return self.q[0]
            self.q.popleft()
        return -1

    def add(self, value: int) -> None:
        if value in self.dups:
            self.dups[value] = False  # Duplicate
        else:
            self.dups[value] = True  # Not seen till now
            self.q.append(value)


if __name__ == "__main__":
    fu = FirstUnique([2, 3, 5])
    print(fu.showFirstUnique())  # 2
    fu.add(5)
    print(fu.showFirstUnique())  # 2
    fu.add(2)
    print(fu.showFirstUnique())  # 3
    fu.add(3)
    print(fu.showFirstUnique())  # -1
    fu.add(10)
    print(fu.showFirstUnique())  # 10
