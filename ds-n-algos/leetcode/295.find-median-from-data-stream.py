# @author: yprakash
import heapq


# https://leetcode.com/submissions/detail/841699437/
class MedianFinder:
    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    def addNum(self, num: int) -> None:  # O(log N)
        if not self.left_heap:
            self.left_heap.append(-num)
            return
        if not self.right_heap:
            if num < -self.left_heap[0]:
                self.right_heap.append(-self.left_heap[0])
                self.left_heap[0] = -num
            else:
                self.right_heap.append(num)
            return

        if num < self.right_heap[0]:
            heapq.heappush(self.left_heap, -num)
            if len(self.left_heap) > 1 + len(self.right_heap):
                heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))
        else:
            heapq.heappush(self.right_heap, num)
            if len(self.left_heap) < len(self.right_heap):
                heapq.heappush(self.left_heap, -heapq.heappop(self.right_heap))

    def findMedian(self) -> float:
        if len(self.left_heap) > len(self.right_heap):
            return -self.left_heap[0]
        return round((-self.left_heap[0] + self.right_heap[0]) / 2, 5)


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(155)
    print(mf.findMedian())  # 155
    mf.addNum(66)
    print(mf.findMedian())  # 110.5
    mf.addNum(114)
    print(mf.findMedian())  # 114
    mf.addNum(0)
    print(mf.findMedian())  # 90
    mf.addNum(60)
    print(mf.findMedian())  # 66
    mf.addNum(73)
    print(mf.findMedian())  # 69.5
    mf.addNum(109)
    print(mf.findMedian())  # 73
    mf.addNum(26)
    print(mf.findMedian())  # 69.5
    mf.addNum(154)
    print(mf.findMedian())  # 73
    mf.addNum(0)
    print(mf.findMedian())  # 69.5
    mf.addNum(107)
    print(mf.findMedian())  # 73
    mf.addNum(75)
    print(mf.findMedian())  # 74
    mf.addNum(9)
    print(mf.findMedian())  # 73  =====

    print(mf.left_heap)
    print(mf.right_heap)
    mf.addNum(57)
    print(mf.findMedian())  # 69.5
    mf.addNum(53)
    print(mf.findMedian())  # 66
    mf.addNum(6)
    print(mf.findMedian())  # 63
    mf.addNum(85)
    print(mf.findMedian())  # 66
