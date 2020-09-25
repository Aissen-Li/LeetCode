class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        from collections import deque
        if not root:
            return None
        level = [root]
        while level:
            nextLevel = []
            for i in range(len(level)):
                if i == len(level) - 1:
                    level[i].next = None
                else:
                    level[i].next = level[i+1]
                if level[i].left:
                    nextLevel.append(level[i].left)
                if level[i].right:
                    nextLevel.append(level[i].right)
            if not nextLevel:
                break
            level = nextLevel
        return root