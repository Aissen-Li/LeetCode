from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.record = {}
        self.maxTimes = 0
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def calculateVal(node: TreeNode):
            if not node:
                return 0
            left = calculateVal(node.left)
            right = calculateVal(node.right)
            subValue = node.val + left + right
            self.record[subValue] = self.record.get(subValue, 0) + 1
            self.maxTimes = max(self.maxTimes, self.record[subValue])
            return subValue
        if not root:
            return []
        calculateVal(root)
        res = []
        for key in self.record.keys():
            if self.record[key] == self.maxTimes:
                res.append(key)
        return res