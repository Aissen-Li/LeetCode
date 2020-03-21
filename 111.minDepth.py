# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        res = float('inf')
        children = [root.left, root.right]
        for child in children:
            if child:
                res = min(res, self.minDepth(child))
        return res + 1


class Solution2:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack, res = [(1, root)], float('inf')
        while stack:
            depth, node = stack.pop()
            if not node.left and not node.right:
                res = min(res, depth)
            if node.left:
                stack.append((depth+1, node.left))
            if node.right:
                stack.append((depth+1, node.right))
        return res
