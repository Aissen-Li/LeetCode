# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        from collections import deque
        deque = deque([root])
        res = []
        while deque:
            node = deque.popleft()
            if node:
                res.append(node.val)
                deque.append(node.left)
                deque.append(node.right)
            else:
                res.append('#')
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        listTreeNode = []
        for nodeVal in data:
            if nodeVal != '#':
                listTreeNode.append(TreeNode(nodeVal))
            else:
                listTreeNode.append(None)
        parent, child = 0, 1
        while parent < len(data) and child < len(data):
            if listTreeNode[parent]:
                listTreeNode[parent].left = listTreeNode[child]
                child += 1
                listTreeNode[parent].right = listTreeNode[child]
                child += 1
            parent += 1
        return listTreeNode[0]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))