# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def maxDepth(node):
            if not node:
                return 0
            self.res = max(self.res, maxDepth(node.left) + maxDepth(node.right) + 1)
            return max(maxDepth(node.left), maxDepth(node.right)) + 1
        if not root:
            return 0
        maxDepth(root)
        return self.res - 1