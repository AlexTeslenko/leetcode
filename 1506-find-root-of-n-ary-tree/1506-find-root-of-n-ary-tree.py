"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

from collections import deque
class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        num_visited_nodes_from_node = {}
        for node in tree:
            num_visited_nodes = 0
            queue = deque([node])
            while queue:
                cure_node = queue.popleft()
                num_visited_nodes += 1
                for child in cure_node.children:
                    if child in num_visited_nodes_from_node:
                        num_visited_nodes += num_visited_nodes_from_node[child]
                    else:
                        queue.append(child)
            
            num_visited_nodes_from_node[node] = num_visited_nodes
            
            if num_visited_nodes == len(tree):
                return node
        
            
        