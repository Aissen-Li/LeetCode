# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        res = None
        carry = 0
        while s1 or s2 or carry:
            num1 = 0 if not s1 else s1.pop()
            num2 = 0 if not s2 else s2.pop()
            numSum = num1 + num2 + carry
            carry = numSum // 10
            current = numSum % 10
            tmp = ListNode(current)
            tmp.next = res
            res = tmp
        return res