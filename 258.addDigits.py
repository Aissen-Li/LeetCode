class Solution:
    def addDigits(self, num: int) -> int:
        while num // 10 != 0:
            numStr = str(num)
            tmp = 0
            for i in range(len(numStr)):
                tmp += int(numStr[i])
            num = tmp
        return num