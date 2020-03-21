from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        root = TreeNode(postorder[-1])
        rootIndex = inorder.index(root.val)
        root.left = self.buildTree(inorder[:rootIndex], postorder[:rootIndex])
        root.right = self.buildTree(inorder[rootIndex+1:], postorder[rootIndex: -1])
        return root