# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        def dfs(node, path):
            if not node:
                return 0
            path -= node.val
            return (1 if path == 0 else 0) + dfs(node.left, path) + dfs(node.right, path)
        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)