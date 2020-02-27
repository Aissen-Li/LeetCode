# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = []
        if root:
            stack.append((1, root))
        depth = 0
        while stack:
            currentDepth, root = stack.pop()
            if root:
                depth = max(currentDepth, depth)
                stack.append((currentDepth + 1, root.left))
                stack.append((currentDepth + 1, root.right))
        return depth