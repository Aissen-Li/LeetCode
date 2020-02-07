class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        result = ''
        if s[0] == '+' or s[0] == '-':
            result += s[0]
            s = s[1:]
        result += s[::-1]
        if int(result) > 2147483647 or int(result) < -2147483648:
            return 0
        return int(result)

