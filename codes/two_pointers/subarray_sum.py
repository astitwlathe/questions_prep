"""
Subarray Sum

Given an array of integers and an integer target, find a subarray that sums to target and return the start and end indices of the subarray.

Input: arr: 1 -20 -3 30 5 4 target: 7

Output: 1 4

Explanation: -20 - 3 + 30 = 7. The indices for subarray [-20,-3,30] is 1 and 4 (right exclusive).
"""

class Solution:
    def subarray_sum_target(self, array, target):
        prefix_sum = {0:0}
        current_sum = 0
        for i, value in enumerate(array):
            current_sum += value
            complement = current_sum - target
            if complement in prefix_sum:
                return prefix_sum[complement], i + 1
            prefix_sum[current_sum] = i + 1

        return -1, -1
    