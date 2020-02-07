class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        if s == '':
            if p == '':
                return True
            else:
                return False

        slen = len(s)
        plen = len(p)
        i, j = 0, 0

        while True:
            if i + 1 < slen and j + 1 < plen:
                if s[i] != p[j]:  # 该位不相等
                    if p[j] == '.':  # 该位不相等但是是.
                        if p[j+1] != '*':
                            i += 1
                            j += 1
                            print(i, j)
                        else:
                            if j + 1 != plen - 1:
                                for k in range(i, slen):
                                    if s[k] != s[i]:
                                        i = k
                                        j += 2
                                        print(i, j)
                                        break
                            else:
                                if i == slen - 1:
                                    return True
                                else:
                                    for k in range(i, slen):
                                        if s[k] != s[i]:
                                            return False
                                        else:
                                            return True
                    else:
                        if p[j+1] != '*':
                            return False
                        else:
                            j += 2
                            print(i, j)
                            continue
                else:  # 首位相等
                    if p[j+1] != '*':
                        i += 1
                        j += 1
                        print(i, j)
                        continue
                    else:  # 首位相等且p的下一位是*
                        if j + 1 != plen - 1:
                            for k in range(i, slen):
                                if s[k] != s[i]:
                                    i = k
                                    j += 2
                                    print(i, j)
                                    break
                        else:
                            for k in range(i, slen):
                                if s[k] != s[i]:
                                    return False
                                else:
                                    return True

            if i == slen - 1 and j == plen - 1:
                return True
            if i == slen - 1 and j != plen - 1:
                return False
            if i != slen - 1 and j == plen - 1:
                return False


class Solution2:
    def isMatch(self, s, p):
        """ :type s: str :type p: str :rtype: bool """
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(2,len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        for i in range(1,len(s) + 1):
            for j in range(1,len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
                elif p[j-1] == '.' or s[i-1] == p[j - 1]:
                    dp[i][j] = dp[i-1][j-1]

        return dp[len(s)][len(p)]