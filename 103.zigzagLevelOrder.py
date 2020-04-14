from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        level = 0
        while queue:
            nextQueue = []
            if level % 2 != 0:
                reverseQueue = queue[::-1]
                res.append([node.val for node in reverseQueue])
            else:
                res.append([node.val for node in queue])
            for node in queue:
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            level += 1
            queue = nextQueue
        return res

