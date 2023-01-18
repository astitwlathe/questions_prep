"""

"""
class Solution:
    def reorder_zeros(self, nums):
        new_index = 0
        while new_index < len(nums) and nums[new_index] != 0:
            new_index += 1
        for curr_index in range(new_index, len(nums)):
            if nums[curr_index] != 0:
                nums[new_index] = nums[curr_index]
                new_index += 1
                nums[curr_index] = 0
        return        