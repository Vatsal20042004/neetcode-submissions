class Node:
    __slots__ = ('key', 'value', 'prev', 'next')

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def unlink(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addfront(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def change (self, node):
        self.unlink(node)
        self.addfront(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.change(self.cache[key])
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.change(self.cache[key])
            self.change(self.cache[key])
            return

        
        node = Node(key, value)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            temp = self.tail.prev
            self.unlink(temp)
            del self.cache[temp.key]
        self.addfront(node)
        
