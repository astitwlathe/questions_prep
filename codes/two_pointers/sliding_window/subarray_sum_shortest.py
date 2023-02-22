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