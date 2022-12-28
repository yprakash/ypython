# @author: yprakash
import heapq
from sortedcontainers import SortedDict


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


# https://leetcode.com/submissions/detail/827332622/
class StockPrice2:
    def __init__(self):  # O(1)
        self.ts_price_map = SortedDict()
        self.price_count_map = SortedDict()

    def update(self, timestamp: int, price: int) -> None:  # O(logN)
        if timestamp in self.ts_price_map:
            old_price = self.ts_price_map[timestamp]
            self.price_count_map[old_price] -= 1
            if self.price_count_map[old_price] == 0:
                del self.price_count_map[old_price]

        self.ts_price_map[timestamp] = price
        self.price_count_map[price] = self.price_count_map.get(price, 0) + 1

    def current(self) -> int:  # O(logN)
        return self.ts_price_map.peekitem(-1)[1]

    def maximum(self) -> int:  # O(logN)
        return self.price_count_map.peekitem(-1)[0]

    def minimum(self) -> int:  # O(logN)
        return self.price_count_map.peekitem(0)[0]
