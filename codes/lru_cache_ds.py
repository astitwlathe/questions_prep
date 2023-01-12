"""
LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support get and put operations.

    get(key): Get the value (which will always be positive) of the key if the key exists in the cache, otherwise return -1.
    put(key, value): Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate 
    the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Can you do both operations in O(1) time complexity?
Input

    operations: the operations

Output

the return values of get operations
Examples
Example 1:

Input:

operations = ```

LRUCache 2
put 1 1
put 2 2
get 1
put 3 3
get 2
put 4 4
get 1
get 3
get 4


**Output**: ````
1
-1
-1
3
4
"""
"""
Corrections to keep in mind
1. Remember to track cache size and pop if it exceeds the size constraint and continue ->  if len(self.cache) >= self.size:
2. Append the get value to result -> result.append(lru_cache.get(int(operation[1])))
"""

from collections import OrderedDict

class LRUCache1:
    def __init__(self, size):
        self.size = size
        self.cache = OrderedDict()

    def put(self, key: int, value: int) -> None:
        if len(self.cache) >= self.size:
            self.cache.popitem()
        self.cache[key] = value
        self.cache.move_to_end(key, last=False)
        return

    def get(self, key: int) -> None:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key, last=False)
        return self.cache[key]

def exec(operations: list[list[str]]) -> list[int]:
    lru_cache = None
    result = []
    for operation in operations:        
        if operation[0] == "LRUCache":
            lru_cache = LRUCache1(int(operation[1]))
        elif operation[0] == "put":
            lru_cache.put(int(operation[1]), int(operation[2]))
        else:
            result.append(lru_cache.get(int(operation[1])))
    return result

from typing import List

class DLLNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


"""
class DLLNode:
    def __init__(self, key, value):        
        self.next = self.prev = None
        self.key = key
        self.value = value

class LRUCache:
    def __init__(self, size):
        self.size = size
        self.head = self.tail = None
        self.elements = {}
        
    def put(self, key, value):
        if len(self.elements) >= self.size:
            del self.elements[self.tail.key]
            self.remove_tail()
        if key not in self.elements:
            node = DLLNode(key, value)            
            self.add_to_head(node)
            self.elements[key] = node        
        node = self.elements[key]
        self.move_to_head(node)
        return    
    
    def get(self, key):
        if key not in self.elements:
            return -1
        node = self.elements[key]
        self.move_to_head(node)
        return node.value
    
    def remove_tail(self):
        node = self.tail
        self.tail = self.tail.prev
        self.tail.next = node.prev = None
        return
    
    def add_to_head(self, node):
        if self.head == None:
            self.head = self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node
        return
    
    def move_to_head(self, node):
        if node == self.head:
            return
        elif node == self.tail:
            self.remove_tail()
            self.add_to_head(node)
            return
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.add_to_head(node)
        return
"""


"""
class DLLNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, size):
        self.size = size
        self.elements = {}
        self.head = None
        self.tail = None
        
    def put(self, key, value):
        if len(self.elements) >= self.size:
            del self.elements[self.tail.key]
            self.remove_last()
        if key not in self.elements:
            self.elements[key] = DLLNode(key, value)
        node = self.elements[key]
        self.move_to_head(node)
        return
    
    def get(self, key):
        if key not in self.elements:
            return -1
        node = self.elements[key]
        self.move_to_head(node)
        return node.value
    
    def remove_last(self):        
        if self.head == self.tail:
            self.head = self.tail = None
            return 
        node = self.tail
        self.tail.prev.next = None
        self.tail = self.tail.prev
        node.prev = None
        return
    
    def move_to_head(self, node):
        if self.head == self.tail == None:
            self.head = self.tail = node
            return
        if node == self.head:
            return
        elif node == self.tail:
            self.remove_last()                   
        elif node.next != node.prev != None:
            next_node = node.next
            prev_node = node.prev
            next_node.prev = prev_node
            prev_node.next = next_node
            node.next = node.prev = None            
        node.next = self.head
        self.head.prev = node
        self.head = node
        return    

"""

"""
class DLLNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, size):
        self.size = size
        self.elements = {}
        self.head = None
        self.tail = None
        
    def put(self, key, value):
        if len(self.elements) >= self.size:
            del self.elements[self.tail.key]
            self.remove_last()
        if key not in self.elements:
            node = DLLNode(key, value)
            self.elements[key] = node
            node.next = self.head
            if self.head is None:
                self.tail = node
            else:    
                self.head.prev = node
            self.head = node
            return
        node = self.elements[key]
        self.move_to_head(node)
        return
    
    def get(self, key):
        if key not in self.elements:
            return -1
        node = self.elements[key]
        self.move_to_head(node)
        return node.value
    
    def remove_last(self):
        if self.head == self.tail:
            self.head = self.tail = None
            return
        node = self.tail
        self.tail = self.tail.prev
        self.tail.next = node.prev = None
        
    def move_to_head(self, node):
        if node == self.head:
            return
        elif node == self.tail:
            self.remove_last()
            node.next = self.head
            self.head.prev = node
            self.head = node
            return
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.next = self.head
        self.head.prev = node
        self.head = node

"""
# class LRUCache:
#     def __init__(self, size):
#         self.head = None
#         self.tail = None
#         self.elements = {}
#         self.size = size
        
#     def put(self, key, value):
# #         print("hi")
#         if len(self.elements) >= self.size:
# #             print("hello1", self.elements, self.head.key, self.tail.key)
#             del self.elements[self.tail.key]
#             tail_node = self.tail
#             self.remove_last()
#             tail_node.next = tail_node.prev = None
#         if len(self.elements) == 0:
#             self.head = self.tail = DLLNode(key, value)
#             self.elements[key] = self.head
#             return
#         elif key in self.elements:
#             node = self.elements[key]
#             self.move_to_head(node)
#             return
#         node = DLLNode(key,value)
#         node.next = self.head
#         self.head.prev = node        
#         self.head = node
#         self.elements[key] = node
# #         print("hello")
#         return
    
#     def get(self, key):
# #         print("hello get", self.elements, self.head.key, self.tail.key)
#         if key not in self.elements:
#             return -1
#         node = self.elements[key]
#         self.move_to_head(node)
# #         print("get", node.value, node.key)
#         return node.value
    
#     def remove_last(self):
#         if self.size == 1:
#             self.head = self.tail = None
#             return
#         prev_node = self.tail.prev
#         self.tail.prev = None
#         prev_node.next = None
#         self.tail = prev_node        
#         return

#     def move_to_head(self, node):
#         if node == self.head:
#             return
#         elif node == self.tail:
#             self.remove_last()
#             node.next = self.head
#             self.head.prev = node
#             self.head = node
#             return
#         prev_node = node.prev
#         next_node = node.next
#         prev_node.next = next_node
#         next_node.prev = prev_node
#         node.prev = None
#         node.next = self.head
#         self.head.prev = node
#         self.head = node
#         return
            
    
# def exec(operations: List[List[str]]) -> List[int]:
#     # WRITE YOUR BRILLIANT CODE HERE
#     result = []
#     lru_cache = None
#     for operation in operations:
#         if operation[0] == "LRUCache":
#             lru_cache = LRUCache(int(operation[1]))
#         elif operation[0] == "put":
#             lru_cache.put(int(operation[1]), int(operation[2]))
#         elif operation[0] == "get":
#             result.append(lru_cache.get(int(operation[1])))
#     return result


if __name__ == "__main__":
    input_string = """
10
LRUCache 2
put 1 1
put 2 2
get 1
put 3 3
get 2
put 4 4
get 1
get 3
get 4
"""
    operations = [ op_string.split() for op_string in input_string.split("\n")[2:-1]]
    print(f"operations={operations}", "result=[1, -1, -1, 3, 4]")
    result = exec(operations)
    print(result == [1, -1, -1, 3, 4])     