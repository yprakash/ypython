# @author: yprakash
from collections import defaultdict


class TwoSum(object):
    # One hashmap for unique numbers, and their counts (to tackle multiple duplicate numbers issue)
    # If it's more add() intensive, then using O(1) time for add(), and O(n) time for find()
    # if it's more find() intensive, then use O(n) time for add(), and O(1) for find()
    def __init__(self):
        self.int_map = defaultdict(int)

    def add(self, number):
        self.int_map[number] += 1  # O(1) add intensive
        # For find-intensive, create 2 dicts for nums and their sums

    def find(self, value):
        for num, count in self.int_map.items():
            if num + num == value:
                if count > 1:
                    return True
            elif value - num in self.int_map:
                return True

        return False
