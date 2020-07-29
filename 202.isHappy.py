class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            digitSum = 0
            while n > 0:
                n, digit = divmod(n ,10)
                digitSum += digit * digit
            return digitSum
        
        record = set()
        while n != 1 and n not in record:
            record.add(n)
            n = getNext(n)
        
        return n == 1