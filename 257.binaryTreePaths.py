class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
from collections import deque
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        queue = deque([[root]])
        while queue:
            currentPath = queue.pop()
            currentNode = currentPath[-1]
            if currentNode.left:
                queue.append(currentPath[:] + [currentNode.left])
            if currentNode.right:
                queue.append(currentPath[:] + [currentNode.right])
            if not currentNode.left and not currentNode.right:
                for i in range(len(currentPath)):
                    currentPath[i] = str(currentPath[i].val)
                res.append('->'.join(currentPath))
        return res