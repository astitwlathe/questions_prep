class Solution:
    def find_palindrome(self, s):
        s = s.lower()
        start_index, end_index = 0, len(s) - 1
        if s[end_index] == "?":
            end_index -= 1
        while start_index <= end_index:
            while s[start_index] == " ":
                start_index += 1
            while s[end_index] == " ":
                end_index -= 1   
            if s[start_index] != s[end_index]:
                return False
            start_index += 1
            end_index -= 1            
        return True