"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        queue = [node]
        convert = {}
        seen = set()
        while queue:
            process = queue.pop()
            if process in seen:
                continue
            seen.add(process)
            convert[process] = Node(process.val)
            for neigh in process.neighbors:
                queue.append(neigh)
            
        traverse = [node]
        seen = set()
        while traverse:
            process = traverse.pop()
            if process in seen:
                continue
            current = convert[process]
            seen.add(process)
            neighbours = []
            for neigh in process.neighbors:
                traverse.append(neigh)
                neighbours.append(convert[neigh])
            
            current.neighbors = neighbours
        
        return convert[node]
        
