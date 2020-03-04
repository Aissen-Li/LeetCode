# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        temp, length, mergeLength = head, 0, 1
        while temp:
            temp = temp.next
            length += 1
        res = ListNode(0)
        res.next = head
        while mergeLength < length:
            temp1, temp2 = res, res.next
            while temp2:
                head1, remainLength = temp2, mergeLength
                while temp2 and remainLength:
                    temp2 = temp2.next
                    remainLength -= 1
                if remainLength > 0:
                    break
                head2, remainLength = temp2, mergeLength
                while temp2 and remainLength:
                    temp2 = temp2.next
                    remainLength -= 1
                c1, c2 = mergeLength, mergeLength - remainLength
                while c1 and c2:
                    if head1.val < head2.val:
                        temp1.next, head1, c1 = head1, head1.next, c1 - 1
                    else:
                        temp1.next, head2, c2 = head2, head2.next, c2 - 1
                    temp1 = temp1.next
                temp1.next = head1 if c1 > 0 else head2
                while c1 > 0 or c2 > 0:
                    temp1 = temp1.next
                    c1, c2 = c1 - 1, c2 - 1
                temp1.next = temp2
            mergeLength *= 2
        return res.next
