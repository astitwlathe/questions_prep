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