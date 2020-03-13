from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lenS, lenP = len(s), len(p)
        if len(s) < len(p):
            return []
        targetDict, windowDict = {}, {}
        diff = lenP
        for i in range(lenP):
            targetDict[p[i]] = targetDict.get(p[i], 0) + 1
            windowDict[p[i]] = 0
        for i in range(lenP):
            if s[i] in windowDict:
                if windowDict[s[i]] < targetDict[s[i]]:
                    diff -= 1
                windowDict[s[i]] += 1
        start, end = 0, lenP - 1
        res = []
        if diff == 0:
            res.append(0)
        while end + 1 < lenS:
            end += 1
            if s[end] in windowDict:
                if windowDict[s[end]] < targetDict[s[end]]:
                    diff -= 1
                windowDict[s[end]] += 1
            if s[start] in windowDict:
                if windowDict[s[start]] <= targetDict[s[start]]:
                    diff += 1
                windowDict[s[start]] -= 1
            start += 1
            if diff == 0:
                res.append(start)
        return res


s = Solution()
print(s.findAnagrams("cbaebabacd","abc"))