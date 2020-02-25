# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while root:
            stack.append(root)
            root = root.left
        while stack:
            currentNode = stack.pop()
            res.append(currentNode.val)
            if currentNode.right:
                currentNode = currentNode.right
                while currentNode:
                    stack.append(currentNode)
                    currentNode = currentNode.left
        return res