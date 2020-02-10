# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
ListNode.__lt__ = lambda x, y: (x.val< y.val)

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        import heapq
        res = ListNode(0)
        heap = []
        temp = res
        for head in lists:
            if head:
                heapq.heappush(heap, head)

        while heap:
            currentSmallestNode = heapq.heappop(heap)
            temp.next = currentSmallestNode
            temp = temp.next
            if currentSmallestNode.next:
                heapq.heappush(heap, currentSmallestNode.next)
        return res.next
