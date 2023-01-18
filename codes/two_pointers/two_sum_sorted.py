"""
Two Sum Sorted

Given an array of integers sorted in ascending order, find two numbers that add up to a given target. Return the indices of the two 
numbers in ascending order. You can assume elements in the array are unique and there is only one solution. Do this in O(n) time and 
with constant auxiliary space.

Input: [2 3 4 5 8 11 18], 8

Output: 1 3
"""

class Solution:
    def target_two_sum_sorted(self, array, target):
        start_index, end_index = 0, len(array) - 1
        while start_index <= end_index:
            if array[start_index] + array[end_index] == target:
                return start_index, end_index
            elif array[start_index] + array[end_index] < target:
                start_index += 1
            else:
                end_index -= 1
        return -1, -1                