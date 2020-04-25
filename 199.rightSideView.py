from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        rightAtDepth = {}
        maxDepth = -1
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            if node:
                maxDepth = max(maxDepth, depth)
                if depth not in rightAtDepth.keys():
                    rightAtDepth[depth] = node.val
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
        return [rightAtDepth[depth] for depth in range(maxDepth+1)]