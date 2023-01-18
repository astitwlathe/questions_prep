"""
Remove Duplicates

Given a sorted list of numbers, remove duplicates and return the new length. You must do this in-place and without using extra memory.

Input: [0, 0, 1, 1, 1, 2, 2].

Output: 3.

Your function should modify the list in place so the first 3 elements becomes 0, 1, 2. Return 3 because the new length is 3.
"""

class Solution:
    def unique_counts(self,  arr):
        slow_pointer = 0
        for fast_pointer in range(len(arr)):
            if arr[fast_pointer] != arr[slow_pointer]:
                slow_pointer += 1
                arr[slow_pointer] = arr[fast_pointer]
        return slow_pointer + 1
