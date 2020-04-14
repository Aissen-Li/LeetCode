from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strNum = ''
        for digit in digits:
            strNum += digit
        res = []
        intNum = int(strNum) + 1
        for digit in str(intNum):
            res.append(digit)
        return res