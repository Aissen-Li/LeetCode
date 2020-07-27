from collections import deque
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        res = 0 
        flip = 0
        queue = deque([])
        for i in range(n):
            while queue and queue[0] + K <= i:
                queue.popleft()
            if A[i] == len(queue) % 2:
                if i + K > n:
                    return -1
                queue.append(i)
                res += 1
        return res