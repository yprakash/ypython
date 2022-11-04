# @author: yprakash
from heapq import heappush, heappop


class SORTracker:  # Accepted https://leetcode.com/submissions/detail/836552896/
    # We need lexicographically smaller location when two scores matches
    # So we need reverse order of strings, in the same way when we need a min heap for highest scores
    class MyString:
        def __init__(self, word):
            self.word = word

        def __lt__(self, other):
            return self.word > other.word

        def __eq__(self, other):
            return self.word == other.word

        def __str__(self):
            return self.word

    def __init__(self):
        # Employ two heaps: min heap (to maintain only 'i' best locations) and max heap for others
        self.i = 1
        self.min_heap = []
        self.max_heap = []

    def add(self, name: str, score: int) -> None:  # O(log N)
        # Add it to the min heap. If the size of the min heap exceeds i + 1, we move the head element to the max heap.
        heappush(self.min_heap, (score, self.MyString(name)))
        if self.i < len(self.min_heap):
            score, name = heappop(self.min_heap)
            heappush(self.max_heap, (-score, str(name)))

    def get(self) -> str:
        self.i += 1
        score, name = self.min_heap[0]
        # head element is i-th best. But before returning it, if the max heap is not empty, we maintain the
        # min heap to have the best i + 1 items by moving the best location from the max heap to the min heap.

        if self.max_heap:
            s2, n2 = heappop(self.max_heap)  # O(log N)
            heappush(self.min_heap, (-s2, self.MyString(n2)))  # O(log N)

        return str(name)


class SORTracker2:  # Ignore this Wrong Answer. https://leetcode.com/submissions/detail/836522190/
    class MyString:
        def __init__(self, word):
            self.word = word

        def __lt__(self, other):
            return self.word > other.word

        def __eq__(self, other):
            return self.word == other.word

        def __str__(self):
            return self.word

    def __init__(self):
        self.i = 0
        self.min_heap = []
        self.max_heap = []

    def add(self, name: str, score: int) -> None:
        heappush(self.max_heap, (-score, name))

    def get(self) -> str:
        self.i += 1

        score, name = heappop(self.max_heap)
        heappush(self.min_heap, (-score, self.MyString(name)))

        return str(self.min_heap[0][1])


if __name__ == "__main__":
    sor = SORTracker()
    sor.add("bradford", 2)
    sor.add("branford", 3)
    print(sor.get())  # branford
    sor.add("alps", 2)
    print(sor.get())  # alps

    sor.add("orland", 2)
    print(sor.get())  # bradford
    sor.add("orlando", 3)
    print(sor.get())  # bradford
    sor.add("alpine", 2)
    print(sor.get())  # bradford
    print(sor.get())  # orland
