class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        record = {}
        node = head
        while node:
            record[node] = Node(node.val, None, None)
            node = node.next
        
        node = head
        while node:
            record[node].next = record.get(node.next)
            record[node].random = record.get(node.random)
            node = node.next
        return record[head]      