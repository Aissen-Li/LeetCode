# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def maxContribution(node:TreeNode):
            nonlocal res
            if not node:
                return 0
            leftContribution = max(maxContribution(node.left), 0)
            rightContribution = max(maxContribution(node.right), 0)
            res = max(res, node.val + leftContribution + rightContribution)
            return node.val + max(leftContribution, rightContribution)
        res = float('-inf')
        maxContribution(root)
        return res