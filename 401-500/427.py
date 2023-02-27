"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        size = len(grid)
        total = sum([sum(row) for row in grid])
        if total == 0 or total == size*size:
            node = Node(val=1 if total else 0, isLeaf=1, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            return node
        top_left = self.construct([row[:size//2] for row in grid[:size//2]])
        top_right = self.construct([row[size//2:] for row in grid[:size//2]])
        bottom_left = self.construct([row[:size//2] for row in grid[size//2:]])
        bottom_right = self.construct([row[size//2:] for row in grid[size//2:]])
        node = Node(val=1 if total else 0, isLeaf=0, topLeft=top_left, topRight=top_right, bottomLeft=bottom_left, bottomRight=bottom_right)
        return node
