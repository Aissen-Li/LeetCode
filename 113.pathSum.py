from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(path, res, target, node):
            if not node:
                return
            if target - node.val == 0:
                path.append(node.val)
                res.append(path)
                return
            dfs(path.append(node.val), res, target - node.val, node.left)
            dfs(path.append(node.val), res, target - node.val, node.right)
        res = []
        dfs([], res, sum, root)
        return res