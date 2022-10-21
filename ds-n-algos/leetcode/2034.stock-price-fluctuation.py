# @author: yprakash
import heapq


class StockPrice1:
    # https://leetcode.com/submissions/detail/827492990/
    def __init__(self):
        self.prices = {}
        self.max_ts = 0
        self.min_heap = []
        self.max_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.prices[timestamp] = price
        self.max_ts = max(self.max_ts, timestamp)
        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        return self.prices[self.max_ts]

    def maximum(self) -> int:
        price, ts = heapq.heappop(self.max_heap)
        while self.prices[ts] != -price:
            price, ts = heapq.heappop(self.max_heap)

        heapq.heappush(self.max_heap, (price, ts))
        return -price

    def minimum(self) -> int:
        price, ts = heapq.heappop(self.min_heap)
        while self.prices[ts] != price:
            price, ts = heapq.heappop(self.min_heap)

        heapq.heappush(self.min_heap, (price, ts))
        return price
