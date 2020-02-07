class Solution1:
    def longestPalindrome(self, s):
        start = end = 0
        for i in range(len(s)):
            len1 = self.expandstr(s, i, i)  # 回文数长度为奇数
            len2 = self.expandstr(s, i, i+1)  # 回文数长度为偶数
            lenmax = max(len1, len2)
            if lenmax > end - start + 1:
                start = i - (lenmax - 1)//2
                end = i + lenmax//2
        return s[start:end+1]

    def expandstr(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return end - start - 1


"""中心扩展法"""


class Solution2:
    def longestPalindrome(self, s):
        s = '#' + '#'.join(s) + '#'  # 变成奇数的字串
        pos = maxright = 0  # 初始化pos和maxright
        maxcenter = 0  #最长字串的中心位置
        p = [0]*len(s)
        for i in range(len(s)):
            if i < maxright:
                p[i] = min(p[2 * pos - i], maxright - i)
            else:
                p[i] = 1  # 只有自己记为1

            while p[i] + i < len(s) and i - p[i] >= 0 and s[i + p[i]] == s[i - p[i]]:  # 注意边界问题
                p[i] += 1

            if p[i] + i - 1 > maxright:
                maxright = p[i] + i - 1
                pos = i

            if p[i] > p[maxcenter]:
                maxcenter = i
        return s[maxcenter - p[maxcenter] + 1:maxcenter + p[maxcenter]].replace('#', '')


"""Manacher算法，p[i]-1才是需要的数值，232ms"""


class Solution3:
    def longestPalindrome(self, s: str) -> str:
        dp = [0 for i in range(len(s))]
        max_start = 0
        max_end = 0

        start = 0
        end = 0
        # 两字母回文
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i] = 1
                max_start = i
                max_end = i+1

        for i in range(len(dp)):
            if dp[i] != 1:
                continue

            j = 1
            while i - j >= 0 and i + j + 1 <= len(s) - 1:
                if s[i - j] == s[i + j + 1]:
                    start = i - j
                    end = i + j + 1
                    if end - start > max_end - max_start:
                        max_end = end
                        max_start = start
                    j += 1
                else:
                    break

        # 三字回文
        for i in range(len(s) - 2):
            if s[i] == s[i + 2]:
                dp[i] = 2
                if max_end - max_start < 2:
                    max_start = i
                    max_end = i + 2

        for i in range(len(dp)):
            if dp[i] != 2:
                continue

            j = 1
            while i - j >= 0 and i + j + 2 <= len(s) - 1:
                if s[i - j] == s[i + j + 2]:
                    start = i - j
                    end = i + j + 2
                    if end - start > max_end - max_start:
                        max_end = end
                        max_start = start
                    j += 1
                else:
                    break
        return s[max_start:max_end+1]


"""动态规划，要分成双字母和三字母的情况，3232ms"""


class Solution4():
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return s
        ss = s[::-1]
        s_len = len(s)
        res_len = 1
        res_str = s[0]
        for i in range(s_len):
            for j in range(i+res_len+1, s_len+1):
                if s[i:j] == ss[s_len-j:s_len-i]:
                    res_len = j-i
                    res_str = s[i:j]
        return res_str


"""字符串取逆然后逐位比较，4320ms"""