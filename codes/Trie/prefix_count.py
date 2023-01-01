"""
Prefix Count

Given a dictionary, containing a list of words, and a list of queries, which consists of a list of prefixes, compute the result 
of each query. Each query is simply a string denoting a prefix. For each query, return the number of words in the dictionary that 
contains that prefix.

Only lower-case English letters will be used.
Constraints

1 <= words.length <= 100001

1 <= words[i].length <= 10
Examples
Example 1:
Input: words = ["forgot", "for", "algomonster", "while"], prefixes = ["fo", "forg", "algo"]
Output: [2, 1, 1]
Explanation:

"forgot" and "for" have the prefix "fo". Only "forgot" has "forg", and only "algomonster" has the prefix "algo".
"""

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = [1, {}]
            else:
                node[char][0] += 1
            node = node[char][1]
        node["*"] = "*"
        return

    def count_words(self, prefix):
        node = self.root
        count = 0
        for char in prefix:
            if char not in node:
                return 0
            count = node[char][0]
            node = node[char][1]
        return count

def prefix_count(words: list[str], prefixes: list[str]) -> list[int]:
    trie = Trie()
    result_nums = []
    for word in words:
        trie.insert(word)
    for prefix in prefixes:
        result_nums.append(trie.count_words(prefix))
    return result_nums



if __name__ == "__main__":
    output = prefix_count(words=["forgot", "for", "algomonster", "while"], prefixes=["fo", "forg", "algo"])
    print(output == [2, 1, 1])
