"""
Node: mid of merge partition is inclusive
"""

class Solution:
    def merge_sort(self, array):
        if len(array) <= 1:
            return
        mid = len(array)//2
        left_half_array = array[:mid]
        right_half_array = array[mid:]
        self.merge_sort(left_half_array)
        self.merge_sort(right_half_array)
        self.merge(left_half_array, right_half_array, array)

    def merge(self, left_array, right_array, array):
        left_index, right_index, index = 0, 0, 0
        while left_index < len(left_array) and right_index < len(right_array):
            if left_array[left_index] < right_array[right_index]:
                array[index] = left_array[left_index]
                left_index += 1
            else:
                array[index] = right_array[right_index]    
                right_index += 1
            index += 1
        while left_index < len(left_array):
            array[index] = left_array[left_index]
            index += 1
            left_index += 1
        while right_index < len(right_array):
            array[index] = right_array[right_index]
            index += 1
            right_index += 1
        return


        

print("Hi")


if __name__ == "__main__":
    soln = Solution()
    print("Hello")
    array = [2, 4, 3, 1, 10, 8, 9, 9, 7, 9, 19, 15]
    soln.merge_sort(array)
    print(array)
