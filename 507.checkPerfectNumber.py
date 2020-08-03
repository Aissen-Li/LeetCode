import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0:
            return False
        res = 0
        for i in range(int(math.sqrt(num)), 0, -1):
            if num % i == 0:
                res += i
                if i * i != num:
                    res += num // i
        return res == 2 * num