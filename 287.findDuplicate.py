from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        head, metPoint = 0, slow
        while head != metPoint:
            head = nums[head]
            metPoint = nums[metPoint]
        return head