# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        if n == 1 and head.next is None:
            return None
        res = ListNode(0)
        res.next = head
        temp = res
        flag = head
        for _ in range(n):
            flag = flag.next
        while flag:
            temp = temp.next
            flag = flag.next
        temp.next = temp.next.next
        return res.next