class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        cur, pre = mid, None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        cur1, cur2 = head, pre
        while cur2:
            next1, next2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = next1
            cur1 = next1
            cur2 = next2