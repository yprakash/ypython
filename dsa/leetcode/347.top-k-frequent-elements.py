# @author: yprakash
import heapq
from collections import Counter
from typing import List


class Solution:
    # https://leetcode.com/submissions/detail/809213681/
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        topk = [0] * k

        for i, (key, val) in enumerate(freq.items()):
            if i < k:
                topk[i] = (val, key)
                continue

            heapq.heapify(topk)
            minv, mink = topk[0]
            if val > minv:
                topk[0] = (val, key)

        heapq.heapify(topk)
        return [key for val, key in topk]
