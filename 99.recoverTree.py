class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first, second, pred = None, None, TreeNode(float('-inf'))
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if not first and pred.val > node.val:
                first = pred
            if first and pred.val > node.val:
                second = node
            pred = node
            node = node.right
        first.val, second.val = second.val, first.val  