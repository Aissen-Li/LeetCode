class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def addString(str1, str2):
            res = ''
            carry = 0
            i = len(str1) - 1
            j = len(str2) - 1
            while i >= 0 or j >= 0:
                x = 0 if i < 0 else ord(str1[i]) - ord('0')
                y = 0 if j < 0 else ord(str2[j]) - ord('0')
                summary = (x + y + carry) % 10
                res += str(summary)
                carry = (x + y + carry) // 10
                i -= 1
                j -= 1
            return res[::-1]
        
        
        if num1 == '0' or num2 == '0':
            return '0'
        
        res = ''
        for i in range(len(num2)-1, -1, -1):
            carry = 0
            tmp = '0' * (len(num2) - 1 - i)
            char2 = ord(num2[i]) - ord('0')
            j = len(num1) - 1
            while j >= 0 or carry != 0:
                char1 = 0 if j < 0 else ord(num1[j]) - ord('0')
                product = (char1 * char2 + carry) % 10
                tmp += str(product)
                carry = (char1 * char2 + carry) // 10
                j -= 1
            res = addString(res, tmp[::-1])
        return res
s = Solution()
print(s.multiply('123', '456'))     