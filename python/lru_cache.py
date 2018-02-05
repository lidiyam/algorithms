class Node(object):
    def __init__(self, K, V):
        self.K = K
        self.V = V
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, N):
        self.N = N
        self.dict = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertNode(self, node):
        # insert to the head
        first = self.head.next
        node.next = first
        first.prev = node
        node.prev = self.head
        self.head.next = node

    def deleteNode(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, K):
        if K in self.dict:
            node = self.dict[K]
            self.deleteNode(node)
            self.insertNode(node)
            return node.V
        return -1

    def put(self, K, V):
        if K in self.dict:
            node = self.dict[K]
            self.deleteNode(node)
            del self.dict[K]
        if len(self.dict) == self.N:
            node = self.tail.prev
            self.deleteNode(node)
            del self.dict[node.K]
        newNode = Node(K,V)
        self.insertNode(newNode)
        self.dict[K] = newNode

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)