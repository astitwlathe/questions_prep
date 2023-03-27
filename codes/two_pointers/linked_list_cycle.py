"""
Linked List Cycle

Given a linked list with potentially a loop, determine whether the linked list from the first node contains a cycle in it. 
For bonus points, do this with constant space.
Parameters

    nodes: The first node of a linked list with potentially a loop.

Result

    Whether there is a loop contained in the linked list.

Examples
Example 1

Input:

Output:

true
Example 2

Input:

Output:

false
Constraints

    1 <= len(nodes) <= 10^5

"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def detect_cycle(self, head):
        if head is None or head.next is None:
            return False
        first_pointer = head
        second_pointer = head.next.next
        while second_pointer is not None and second_pointer.next is not None:
            if first_pointer is second_pointer:
                return True
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next.next
        return False
