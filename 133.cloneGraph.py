class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        root = Node(node.val)
        visited = {}
        visited[root.val] = root
        queue = [node]
        while queue:
            currentNode = queue.pop()
            for neighbor in currentNode.neighbors:
                if neighbor.val not in visited:
                    visited[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[currentNode.val].neighbors.append(visited[neighbor.val])
        return root
                    