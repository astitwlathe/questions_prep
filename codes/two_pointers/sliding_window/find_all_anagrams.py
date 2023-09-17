"""
Find All Anagrams in a String

Given a string original and a string check, find the starting index of all substrings of original that is an 
anagram of check. The output must be sorted in ascending order.
Parameters

    original: A string
    check: A string

Result

    A list of integers representing the starting indices of all anagrams of check.

Examples
Example 1

Input: original = "cbaebabacd", check = "abc"

Output: [0, 6]

Explanation: The substring from 0 to 2, "cba", is an anagram of "abc", and so is the substring from 6 to 8, "bac".
Example 2

Input: original = "abab", check = "ab"

Output: [0, 1, 2]

Explanation: All substrings with length 2 from "abab" is an anagram of "ab".
Constraints

    1 <= len(original), len(check) <= 10^5
    Each string consists of only lowercase characters in standard English alphabet.

"""


from collections import Counter

class Solution:
    def find_anagram_indices(self, original, check):
        target_counter = Counter(check)
        curr_counter = Counter()
        anagram_indices = []
        for i, char in enumerate(original):
            curr_counter[char] += 1
            if i - len(check) >= 0:
                prev_char = original[i - len(check)]
                curr_counter[prev_char] -= 1
                if curr_counter[prev_char] == 0:
                    del curr_counter[prev_char]
            if curr_counter == target_counter:
                anagram_indices.append(i - len(check) + 1)
        return anagram_indices
