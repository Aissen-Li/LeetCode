class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.inorderSort = []
        self.index = -1
        self.inorder(root)
        
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.inorderSort.append(root.val)
        self.inorder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        return self.inorderSort[self.index]
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index < len(self.inorderSort) - 1