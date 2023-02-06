# class Solution:
#     def quick_sort(self, array, start, end):
#         if start < 0 or end - start <= 1:
#             return
#         pivot_index = self.partition(array, start, end)
#         print("Array", array, pivot_index)
#         self.quick_sort(array, start, pivot_index)
#         self.quick_sort(array, pivot_index + 1, end)

#     def partition(self, array, start, end):
#         start_index = start
#         end_index = end - 1
#         pivot = array[(start + end)//2]
#         print(pivot, start, end)
#         while True:  
#             # start_index += 1          
#             while start_index < end_index and array[start_index] < pivot:
#                 start_index += 1
#             # end_index -= 1
#             while start_index < end_index and array[end_index] >= pivot:
#                 end_index -= 1
#             if start_index >= end_index:
#                 break
#             array[start_index], array[end_index] = array[end_index], array[start_index]        
#         # if array[start_index] >= pivot:
#         array[start_index], array[end - 1] = array[end - 1], array[start_index]
#         #     return start_index
#         return start_index

from typing import List


def sort_list_interval(unsorted_list: List[int], start: int, end: int) -> None:

    if end - start <= 1:

        return

    pivot = unsorted_list[end - 1]

    start_ptr = start

    end_ptr = end - 1

    while start_ptr < end_ptr:

        while unsorted_list[start_ptr] < pivot and start_ptr < end_ptr:

            start_ptr += 1

        while unsorted_list[end_ptr] >= pivot and start_ptr < end_ptr:

            end_ptr -= 1

        if start_ptr == end_ptr:

            break

        unsorted_list[start_ptr], unsorted_list[end_ptr] = unsorted_list[end_ptr], unsorted_list[start_ptr]

    unsorted_list[start_ptr], unsorted_list[end - 1] = unsorted_list[end - 1], unsorted_list[start_ptr]

    sort_list_interval(unsorted_list, start, start_ptr)

    sort_list_interval(unsorted_list, start_ptr + 1, end)


def sort_list(unsorted_list: List[int]) -> List[int]:

    sort_list_interval(unsorted_list, 0, len(unsorted_list))

    return unsorted_list
if __name__ == "__main__":
    # soln = Solution()
    array = [2, 4, 3, 1, 10, 8, 9, 9, 7, 9, 19, 15]
    # soln.quick_sort(array, 0, len(array))
    sort_list(array)
    print(array)