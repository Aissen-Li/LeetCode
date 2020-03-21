# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        slow, fast = head ,head
        leftEnd = None
        while fast and fast.next:
            leftEnd = slow
            slow = slow.next
            fast = fast.next.next
        if head == slow:
            return TreeNode(slow.val)
        root = TreeNode(slow.val)
        if leftEnd:
            leftEnd.next = None
        rightStart = slow.next
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(rightStart)
        return root