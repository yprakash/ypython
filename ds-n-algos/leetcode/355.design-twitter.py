# @author: yprakash
import heapq
from collections import defaultdict, deque
from typing import List


# https://leetcode.com/submissions/detail/813578740/
class Twitter:
    def __init__(self):
        self.count = 0
        self.tweets = {}  # userid -> list of (count, tweet id)
        self.follow_map = defaultdict(set)  # userid -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = deque(maxlen=10)
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follow_map[userId].add(userId)
        min_heap = []
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                count, tweet = self.tweets[followeeId][index]
                min_heap.append([count, tweet, followeeId, index - 1])

        heapq.heapify(min_heap)
        res = []  # ordered starting from recent
        while min_heap and len(res) < 10:
            count, tweet, followeeId, index = heapq.heappop(min_heap)
            res.append(tweet)
            if index >= 0:
                count, tweet = self.tweets[followeeId][index]
                heapq.heappush(min_heap, [count, tweet, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
