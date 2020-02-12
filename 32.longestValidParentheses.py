class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0]* len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    if i >= 2:
                        dp[i] = dp[i-2] + 2
                    else:
                        dp[i] = 2
                else:
                    if i-dp[i-1] >= 1 and s[i-dp[i-1]-1] == "(":
                        if i-1-dp[i-1]-1 >= 0:
                            dp[i] = dp[i-1] + 2 + dp[i-1-dp[i-1]-1]
                        else:
                            dp[i] = dp[i-1] + 2
        return max(dp)


class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res
