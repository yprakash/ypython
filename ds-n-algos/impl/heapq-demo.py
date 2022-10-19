# @author: yprakash
import heapq

if __name__ == "__main__":
    # If there’s already a list of elements that needs to be a heap, heapify() makes a list into a valid heap inplace.
    a = [3, 5, 1, 2, 6, 8, 7]
    heapq.heapify(a)
    print(a)
    print(heapq.heappop(a))
    print(a)
    print(heapq.heappush(a, 1))
    print(a)
