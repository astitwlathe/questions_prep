"""
    Backtracking
    Combinatorial Search
    DFS with States

DFS with States

    Prereq: Recursion, DFS on Tree

Let's reinforce our understanding of the idea of the "states" with one more example.
Ternary Tree Paths

Given a ternary tree (each node of the tree has at most three children), find all root-to-leaf paths.

Try it yourself
"""

class Node:
    def __init__(self, val, children=None):
        self.val = val
        if children is None:
            children = []
        self.children = children       



class Solution:
    def dfs(self, node):
        result = []
        if node is not None:
            self.dfs_rec(node, result, [])
        return result

    def dfs_rec(self, node, result, path):
        path.append(str(node.val))
        if node.children == []:
            result.append("->".join(path))
        for child in node.children:
            self.dfs_rec(child, result, path)
        path.pop()
        return    