"""
Flexible Size Sliding Window

Let's continue on finding the sum of subarrays. This time given a positive integer array nums, we want to find the length of 
the shortest subarray such that the subarray sum is at least target. Recall the same example with input nums = [1, 4, 1, 7, 3, 0, 2, 5] and 
target = 10, then the smallest window with the sum >= 10 is [7, 3] with length 2. So the output is 2.
"""
class Solution:
    def shortest_subarray_sum_target(self, nums, target):
        min_length = float("inf")
        start_index = curr_sum = 0
        for end_index, value in enumerate(nums):
            curr_sum += value
            while curr_sum > target:
                curr_sum -= nums[start_index]
                start_index += 1
            if curr_sum == target:
                min_length = min(end_index - start_index + 1, min_length)
        return min_length