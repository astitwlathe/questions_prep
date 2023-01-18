"""
Middle of a Linked List

Find the middle node of a linked list.

Input: 0 1 2 3 4

Output: 2

If the number of nodes is even, then return the second middle node.

Input: 0 1 2 3 4 5

Output: 3
"""

class Solution:
    def middle_value(self, head):
        first_pointer = second_pointer = head
        while first_pointer and first_pointer.next:
            first_pointer = first_pointer.next.next
            second_pointer = second_pointer.next
        return second_pointer.val
