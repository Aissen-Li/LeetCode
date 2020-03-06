# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def findMid(head):
            slow = head
            fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse(head):
            previous = None
            current = head
            while current:
                temp = current.next
                current.next = previous
                previous = current
                current = temp
            return previous

        if not head or not head.next:
            return True
        mid = findMid(head)
        second = reverse(mid.next)
        first = head
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True