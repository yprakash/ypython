# @author: yprakash

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


# https://leetcode.com/submissions/detail/808200343/
class LRUCache:
    def __init__(self, capacity: int):
        self.map = {}
        self.head = None
        self.tail = None
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        self.delete_from_list(node)
        self.set_list_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:  # we just update and size won't be changed
            node = self.map[key]
            node.value = value
            self.delete_from_list(node)
            self.set_list_head(node)
        else:
            if len(self.map) >= self.capacity:
                node = self.map.pop(self.tail.key)
                self.delete_from_list(node)

            node = Node(key, value)
            self.map[key] = node
            self.set_list_head(node)

    def set_list_head(self, node):
        node.prev = None
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = node

    def delete_from_list(self, node):
        if not node:
            return
        if node.prev:
            node.prev.next = node.next
        else:  # it must be head node
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:  # it must be tail node
            self.tail = node.prev


if __name__ == "__main__":
    # Your LRUCache object will be instantiated and called as such:
    obj = LRUCache(2)
    print(obj.get(1))
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1))
    obj.put(3, 3)
    print(obj.get(2))
    obj.put(4, 4)
    print(obj.get(1))
    print(obj.get(3))
    print(obj.get(4))
    print()
