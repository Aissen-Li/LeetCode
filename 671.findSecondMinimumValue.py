class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def preorder(root, val):
            if not root:
                return -1
            if root.val > val:
                return root.val
            left = preorder(root.left, val)
            right = preorder(root.right, val)
            if left < 0:
                return right
            if right < 0:
                return left
            return min(left, right)
        return preorder(root, root.val)