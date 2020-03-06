from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        if k > n:
            return [max(nums)]
        steps = n - k
        res = []
        for i in range(steps+1):
            res.append(max(nums[i: i+k]))
        return res


class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        n = len(nums)
        deque = deque()
        def dequeClean(i):
            if deque and deque[0] == i-k:
                deque.popleft()
            while deque and nums[i] > nums[deque[-1]]:
                deque.pop()
        maxIndex = 0
        for i in range(k):
            dequeClean(i)
            deque.append(i)
            if nums[i] > nums[maxIndex]:
                maxIndex = i
        res = [nums[maxIndex]]
        for i in range(k, n):
            dequeClean(i)
            deque.append(i)
            res.append(nums[deque[0]])
        return res


s = Solution2()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))