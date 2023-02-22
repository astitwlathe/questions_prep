"""
Least Consecutive Cards to Match

A bunch of cards is laid out in front of you in a line, where the value of each card ranges from 0 to 10^6. A pair of cards are matching 
if they have the same number value.

Given a list of integer cards, your goal is to match a pair of cards, but you can only pick up cards in a consecutive manner. What's the 
minimum number of cards that you need to pick up to make a pair? If there is no matching pairs, return -1.

For example, given cards = [3, 4, 2, 3, 4, 7], then picking up [3, 4, 2, 3] makes a pair of 3s and picking up [4, 2, 3, 4] matches two 4s. We 
need 4 consecutive cards to match a pair of 3s and 4 consecutive cards to match 4s, so you need to pick up at least 4 cards to make a match.
"""

class Solution:
    def closest_repeated_value_distance(self, cards):
        values_dict = {}
        min_distance = float("inf")
        for index, card in enumerate(cards):
            if card in values_dict:
                min_distance = min(index - values_dict[card] + 1, min_distance)
            values_dict[card] = index
        return min_distance if min_distance != float("inf") else -1