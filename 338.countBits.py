from typing import List
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num + 1):
            res.append(str(bin(i)).count('1'))
        return res