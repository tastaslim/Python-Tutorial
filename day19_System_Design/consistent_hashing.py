"""
Works well if we have fixed number of nodes which won't be the case in most real systems because our hash function
depends on the number of nodes, once the node changes, the same customer/requestId would start going to a different
machine which would waste all
"""
from bisect import bisect_right
from hashlib import sha256


class SimpleHashing:
    def __init__(self, nodes: list) -> None:
        self.nodes = nodes
        self.totalNodes = len(nodes) if nodes else 0

    def __hashKey(self, requestKey: str) -> int:
        return int(bytes(requestKey.encode('utf-8')), 16) % self.totalNodes

    def addNode(self, node):
        self.nodes.append(node)
        self.totalNodes += 1

    def removeNode(self, node):
        self.nodes.remove(node)
        self.totalNodes -= 1

    def getNode(self, requestKey: str):
        hashedKey: int = self.__hashKey(requestKey)
        # redirect request to this node
        return self.nodes[hashedKey]


"""
The problem with SimpleHashing is that, we have to remap almost all keys in case of addition/removal of servers which is
very costly. We want to minimise it and for that we will use ConsistentHashing. Also, as we saw the problem arises due
to variable hash function, hence in this case we would a fixed hash function. We define total_slots as the size of this 
entire hash space, typically of the order 2^256 or we can use SHA-256 to implement it.
Since the total_slots is huge and a constant, the hash function implementation is independent of the actual 
number of Storage Nodes present in the system and hence remains unaffected by events like scale-ups and scale-downs.
"""


class ConsistentHashing:
    def __init__(self, nodes: list):
        self.nodes = nodes
        self.totalNodes = len(nodes) if nodes else 0
        self.keys = []
        self.totalSlots = 2 ^ 256

    def __hashKey(self, requestKey: str) -> int:
        hashing = sha256()
        hashing.update(bytes(requestKey.encode('utf-8')))
        return int(hashing.hexdigest(), 16) % self.totalSlots

    def addNode(self, node) -> int:
        if self.totalNodes > self.totalSlots:
            raise Exception("Hash space is full")
        hashedNode: int = self.__hashKey(node)
        index: int = bisect_right(self.nodes, hashedNode)

        # if we have already seen the key i.e. node already is present
        # for the same key, we raise Collision Exception
        if index > 0 and self.nodes[index - 1] == hashedNode:
            raise Exception("Collision Occurred")

        # Perform data migration
        # insert the node_id and the key at the same `index` location.
        # this insertion will keep nodes and keys sorted w.r.t keys.
        self.nodes.insert(index, node)
        self.keys.insert(index, hashedNode)
        return hashedNode

    def removeNode(self, node):
        self.nodes.remove(node)
        self.totalNodes -= 1

    def getNode(self, requestKey: str):
        hashedKey = self.__hashKey(requestKey)
        return hashedKey
        # redirect request to this node
        # return self.nodes[hashedKey]
