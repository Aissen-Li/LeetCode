from typing import List
import random

class Solution:
    def __init__(self, nums: List[int]):
        self.res = nums
        self.original = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.res = self.original
        self.original = self.original[:]
        return self.res

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.res)):
            swapIndex = random.randrange(i ,len(self.res))
            self.res[i], self.res[swapIndex] = self.res[swapIndex], self.res[i]
        return self.res
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()