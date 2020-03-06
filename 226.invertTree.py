# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        queue = [root]
        while queue:
            node = queue.pop()
            temp = node.left
            node.left = node.right
            node.right = temp
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root


root = TreeNode(4)
root.left, root.right = TreeNode(2), TreeNode(7)
root.left.left, root.left.right = TreeNode(1), TreeNode(3)
root.right.left, root.right.right = TreeNode(6), TreeNode(9)
s = Solution()
s.invertTree(root)