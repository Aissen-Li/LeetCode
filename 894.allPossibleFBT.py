# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        res = []
        if N == 1:
            return [TreeNode(0)]
        if N % 2 == 0:
            return []
        left, right = 1, N - 1 - 1
        while right > 0:
            leftTree = self.allPossibleFBT(left)
            rightTree = self.allPossibleFBT(right)
            for i in range(len(leftTree)):
                for j in range(len(rightTree)):
                    root = TreeNode(0)
                    root.left = leftTree[i]
                    root.right = rightTree[j]
                    res.append(root)
            left += 2
            right -= 2
        return res