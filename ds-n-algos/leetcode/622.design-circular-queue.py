# @author: yprakash

# https://leetcode.com/submissions/detail/807943226/
class MyCircularQueue:
    # Initialize your data structure. Set the size of the queue to be k.
    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.front = 0
        self.rear = k - 1  # Imp
        self.q = [0] * k

    # Insert an element into the circular queue. Return true if the operation is successful.
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.k
        self.q[self.rear] = value
        self.size += 1
        return True

    # Delete an element from the circular queue. Return true if the operation is successful.
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    # Get the front item from the queue.
    def Front(self) -> int:
        return -1 if self.isEmpty() else self.q[self.front]

    # Get the last item from the queue.
    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


if __name__ == "__main__":
    # Your MyCircularQueue object will be instantiated and called as such:
    obj = MyCircularQueue(5)
    param_1 = obj.enQueue(18)
    param_2 = obj.deQueue()
    param_3 = obj.Front()
    param_4 = obj.Rear()
    param_5 = obj.isEmpty()
    param_6 = obj.isFull()
    print(param_1, param_2, param_3, param_4, param_5, param_6)
