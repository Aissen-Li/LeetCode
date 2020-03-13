# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def robParentOrChild(node: TreeNode):
            if not node:
                return [0, 0]
            left, right = robParentOrChild(node.left), robParentOrChild(node.right)
            return [node.val + left[1] + right[1], max(left) + max(right)]
        return max(robParentOrChild(root))