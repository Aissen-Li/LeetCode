from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [[]]
        dic = {}
        stack = [(root, 0, 0)]
        while stack:
            node, x, y = stack.pop(0)
            if dic.get((x, y)):
                dic[(x, y)].append(node.val)
            else:
                dic[(x, y)] = [node.val]
            if node.left:
                stack.append((node.left, x-1, y+1))
            if node.right:
                stack.append((node.right, x+1, y+1))
        res = []
        xFlag = -10000  # 判断是否建立新的层（垂线）
        tmp = []
        for x, y in sorted(dic.keys()):
            if x != xFlag:
                res.append(tmp)
                tmp = []
                xFlag = x
            tmp.extend(sorted(item for item in dic[(x, y)]))
        res.pop(0)
        res.append(tmp)
        return res



s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.left.right = TreeNode(14)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
s.verticalTraversal(root)