# @author: yprakash
from random import randrange


# Design a data structure to insert, delete and get a random number in O(1)
# https://leetcode.com/submissions/detail/812921451/
class RandomizedSet:
    def __init__(self):
        self.array = []  # use it store actual set elements
        self.hashmap = {}  # value to index map

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False

        self.hashmap[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        index = self.hashmap[val]

        if index < len(self.array)-1:  # If elem to remove is not last elem
            self.array[index] = self.array[-1]  # replace with last elem
            self.hashmap[self.array[index]] = index
        del self.hashmap[val], self.array[-1]
        return True

    def getRandom(self) -> int:
        return self.array[randrange(len(self.array))]
