"""
Flexible Size Sliding Window - Longest

Recall finding the largest size k subarray sum of an integer array in Largest Subarray Sum. What if we dont need the 
largest sum among all subarrays of fixed size k, but instead, we want to find the length of the longest subarray with 
sum smaller than or equal to a target?

Given input nums = [1, 6, 3, 1, 2, 4, 5] and target = 10, then the longest subarray that does not exceed 10 is [3, 1, 2, 4], 
so the output is 4 (length of [3, 1, 2, 4]).
"""

class Solution:
    def longest_subarray_length_target(self, nums, target):
        start_index = 0
        curr_sum = 0
        max_length = 0
        for end_index, value in enumerate(nums):
            curr_sum += value
            if curr_sum <= target:
                max_length = max(end_index - start_index + 1, max_length)
            else:
                curr_sum -= nums[start_index]
                start_index += 1
        return max_length

