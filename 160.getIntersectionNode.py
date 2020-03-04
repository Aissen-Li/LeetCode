# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next
            pB = pB.next
            if pA == pB == None:
                return None
            if pA is None:
                pA = headB
            if pB is None:
                pB = headA
        return pA
