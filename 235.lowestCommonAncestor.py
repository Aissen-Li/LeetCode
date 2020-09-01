class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        pVal = p.val
        qVal = q.val
        while node:
            if pVal > node.val and qVal > node.val:
                node = node.right
            elif pVal < node.val and qVal < node.val:
                node = node.left
            else:
                return node