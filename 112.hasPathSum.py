from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        queue = deque([(root, root.val)])
        while queue:
            node, currentVal = queue.popleft()
            if not node.left and not node.right:
                if currentVal == sum:
                    return True
            if node.left:
                queue.append((node.left, currentVal + node.left.val))
            if node.right:
                queue.append((node.right, currentVal + node.right.val))
        return False    