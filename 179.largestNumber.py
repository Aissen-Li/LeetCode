class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums):
        largestNum = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largestNum[0] == '0' else largestNum
