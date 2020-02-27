# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        rootIndex = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:rootIndex+1], inorder[:rootIndex])
        root.right = self.buildTree(preorder[rootIndex+1:], inorder[rootIndex+1:])
        return root