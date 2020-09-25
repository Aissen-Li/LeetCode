class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(head: ListNode, tail: ListNode) -> (ListNode, ListNode):
            pre = tail.next
            cur = head
            while pre != tail:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return tail, head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        while head:
            tail = pre
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            tmp = tail.next
            head, tail = reverse(head, tail)
            pre.next = head
            tail.next = tmp
            pre = tail
            head = tail.next
        return dummy.next