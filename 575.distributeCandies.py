from typing import List
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        candyCount = {}
        for candy in candies:
            candyCount[candy] = candyCount.get(candy, 0) + 1
        candyNums = len(candyCount)
        if candyNums < len(candies) / 2:
            return candyNums
        else:
            return int(len(candies) / 2)