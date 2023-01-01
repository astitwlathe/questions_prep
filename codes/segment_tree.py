"""
Range max

For this question we will give you an array and a series of queries and updates. Each update can change 1 particular value 
in the array and each query will give you an interval where you have to return the maximum value on the interval. Each query 
or update will be a list of 3 elements. The first element is a number denoting a query or update operation, 1 will denote a 
query and 2 an update operation. If the number is a 1 the next 2 numbers will denote the interval that is to be queried in the 
0-indexed array. If the number is a 2 the next 2 numbers will denote the index i and value v in that order which means that 
index i in the array should be updated to v.

Input

    arr: original array of numbers
    operations: list of queries and updates on the array

Output

list containing the answer to all the queries
Examples
Example 1:

Input:

arr = [1,2,3,4,5]

operations = [[1,0,4], [2,4,7], [1,1,4]]

Output: [5,7]

Explanation:

We are given a 1 query operation which means we first query from interval 0 - 4 the largest number which is 5. We then are 
given a 2 update operation which means we update the array at index 4 to the value of 7. Therefore, our new array is [1,2,3,4,7]. 
Lastly, we query one more time between 1 and 4 where we get a largest value of 7.
Constraints

    1 <= arr.length <= 10000
    1 <= operations.length <= 10000
    Each value of arr will be in the range [1, 30000]

"""





class SegmentTree:
    def __init__(self, input_array):
        self.seg_array = [float("-inf")] * 3 * len(input_array)
        for i, v in enumerate(input_array):
            self.update(i, v, 0, len(input_array) - 1, 0)
    
    def update(self, input_array_index, value, curr_left, curr_right, curr_index):
        if curr_right < curr_left:
            return 
        if curr_left == curr_right == input_array_index:
            self.seg_array[curr_index] = value
            return
        curr_mid = curr_left + (curr_right - curr_left)//2
        if input_array_index <= curr_mid:
            self.update(input_array_index, value, curr_left, curr_mid, 2 * curr_index + 1)
        else:
            self.update(input_array_index, value, curr_mid + 1, curr_right, 2 * curr_index + 2)
        self.seg_array[curr_index] = max(self.seg_array[2 * curr_index + 1], self.seg_array[2 * curr_index + 2])
        return
    
    def query(self, query_left, query_right, curr_left, curr_right, curr_index):
        if query_right < curr_left or curr_right < query_left:
            return float("-inf")
        if query_left <= curr_left and curr_right <= query_right:
            return self.seg_array[curr_index]
        curr_mid = curr_left + (curr_right - curr_left)//2
        left_val = self.query(query_left, query_right, curr_left, curr_mid, 2 * curr_index + 1)
        right_val = self.query(query_left, query_right, curr_mid + 1, curr_right, 2 * curr_index + 2)
        return max(left_val, right_val)
        


def range_max(array, operations):
    st = SegmentTree(array)
    results = []
    for opcode, a, b in operations:
        if opcode == 1:
            result = st.query(a, b, 0, len(array) - 1, 0)
            results.append(result)
        else:    
            st.update(a, b, 0, len(array) - 1, 0)
    return results






if __name__ == "__main__":
    print(range_max([1,2,3,4,5], [[1,0,4], [2,4,7], [1,1,4]]) == [5, 7])


