from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        def generate(start, end):
            if start > end:
                return[None, ]
            allTrees = []
            for i in range(start, end + 1):
                leftTrees = generate(start, i-1)
                rightTrees = generate(i+1, end)
                
                for left in leftTrees:
                    for right in rightTrees:
                        currentNode = TreeNode(i)
                        currentNode.left = left
                        currentNode.right = right
                        allTrees.append(currentNode)
            return allTrees
        return generate(1, n) if n else []  
