class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        if not s:
            return res
        for center in range(2 * n - 1):
            left = int(center / 2)
            right = left + center % 2
            while left >= 0 and right < n and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res