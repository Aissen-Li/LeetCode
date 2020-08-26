class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if not root or (not root.left and not root.right):
            return 0
        def dfs(root: TreeNode) -> dict:
            if not root:
                return {}
            if not root.left and not root.right:
                return {root: 0}
            left = dfs(root.left)
            right = dfs(root.right)
            for k, v in left.items():
                left[k] = v + 1
            for k, v in right.items():
                right[k] = v + 1
            for leftk, leftv in left.items():
                for rightk, rightv in right.items():
                    if leftv + rightv <= distance:
                        self.res += 1
            left.update(right)
            return left
        self.res = 0
        dfs(root)
        return self.res