"""
Autocomplete

For this question, we first give you a series of n words. For every word, we first add it to our dictionary, and then we type out 
the word using the minimum number of strokes to autocomplete the word. What is the minimum total number of strokes needed to type
out all the words?
Constraints

1 <= n <= 100001

Sum of the lengths of all the strings will not exceed 100001.

Words will only have lowercase letters.
Examples:
Example 1:
Input 1: words = ["hi", "hello", "bojack", "hills", "hill"]
Output 1: 11
Explanation:

We put "hi" in our dictionary and then we only need to type out "h", which is 1 stroke, before it autocompletes to "hi". We put "hello"
in our dictionary and then we only need to type out "he", which is 2 strokes, before it autocompletes to "hello". We put "bojack" in our
dictionary and then we only need to type out "b" which is 1 stroke, before it autocompletes to "bojack". We put "hills" in our dictionary
and then we only need to type out "hil"(since we have "hi") which is 3 strokes, before it autompletes to "hills". Lastly, we put "hill" 
in our dictionary and we need to type out "hill" which is 4 strokes. Adding these strokes up we have 1 + 2 + 1 + 3 + 4 = 11 which we then
output.
"""

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = [1, {}]
            else:
                node[char][0] += 1
            node = node[char][1]
        node["*"] = "*"    
        return

    def count_strokes(self, word: str) -> int:
        node = self.root
        count = 0
        for char in word:
            count += 1
            if char not in node:
                return -1
            if node[char][0] == 1:
                return count
            node = node[char][1]    
        return count

                    

def autocomplete(words: list[int]) -> int:
    trie = Trie()
    count = 0
    for word in words:
        trie.insert(word)
        count += trie.count_strokes(word)
    return count    


if __name__ == "__main__":
    words = ["hi", "hello", "bojack", "hills", "hill"]
    print(autocomplete(words))
