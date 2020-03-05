# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        res = ListNode(0)
        previous = res
        current = head
        while current.next:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return res.next