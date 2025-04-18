# @author: yprakash
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        # Keep a copy of the original array to easily calculate the difference during updates.
        self.nums = list(nums)
        # Initialize 1-based indexing Fenwick (Binary Indexed) Tree
        self.bit = [0] * (self.n + 1)  # O(n) space
        for i, num in enumerate(nums):  # O(n log n) time
            self._update_bit(i, num)

    def _update_bit(self, index: int, val: int):
        """ O(log n) time
        This function updates the Fenwick tree when the value at a given index in the original array changes by val
        It traverses up the Fenwick tree. The key operation index += index & (-index) calculates the index of the
        next node to update in the tree. index & (-index) isolates the least significant bit (LSB) of index,
        and adding it to index moves to the parent node responsible for the range including the current index.
        """
        index += 1  # 1-based indexing for BIT
        print('\nupdating', index, val, self.bit)
        while index <= self.n:
            self.bit[index] += val
            print('    _update_bit', index, self.bit[index], self.bit)
            index += index & -index

    def _query_bit(self, index: int):
        """ O(log n) time
        This function calculates the prefix sum (sum from index 0 to index) using the Fenwick tree.
        It traverses down the Fenwick tree. The operation index -= index & (-index) moves to
        the index representing the next smaller range that contributes to the prefix sum.
        """
        index += 1  # 1-based indexing for BIT
        print('\nquerying', index, self.bit)
        psum = 0
        while index > 0:
            psum += self.bit[index]
            print('    _query_bit', index, psum, self.bit)
            index -= index & -index
        return psum

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        return self._update_bit(index, diff)

    def sumRange(self, left: int, right: int) -> int:
        return self._query_bit(right) - self._query_bit(left - 1)


if __name__ == "__main__":
    arr = [1, 3, 5]
    obj = NumArray(arr)
    print(obj.sumRange(0, 2))  # Output: 9
    obj.update(1, 2)  # Update index 1 to value 2
    print(obj.sumRange(0, 2))  # Output: 8
