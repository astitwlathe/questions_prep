"""
Longest Substring without Repeating Characters

Find the length of the longest substring of a given string without repeating characters.

Input: abccabcabcc

Output: 3

Explanation: longest substrings are abc, cab, both of length 3

Input: aaaabaaa

Output: 2

Explanation: ab is the longest substring, length 2
"""

class Solution:
    def unique_chars_length(self, s):
        max_length = 0
        char_set = set()
        start_index = 0
        for char in s:
            while char in char_set:
                char_set.remove(s[start_index])
                start_index += 1
            char_set.add(char)
            max_length = max(len(char_set), max_length)
        return max_length