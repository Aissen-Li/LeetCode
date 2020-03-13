class Solution:
    def decodeString(self, s: str) -> str:
        stack, times, res = [], '', ''
        for char in s:
            if char == '[':
                stack.append([times, res])
                times, res = '', ''
            elif char == ']':
                copyTimes, lastRes = stack.pop()
                res = lastRes + int(copyTimes) * res
            elif '0' <= char <= '9':
                times += char
            else:
                res += char
        return res


s = Solution()
s.decodeString('3[a]2[bc]')