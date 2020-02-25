class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ''
        needsT = {}
        for charT in t:
            needsT[charT] = needsT.get(charT, 0) + 1

        needsLength = len(needsT)

        filtered = []
        for pos, charS in enumerate(s):
            if charS in t:
                filtered.append((pos, charS))

        left, right = 0, 0
        windowLength = 0
        window = {}
        ans = float('inf'), None, None

        while right < len(filtered):
            currentChar = filtered[right][1]
            window[currentChar] = window.get(currentChar, 0) + 1

            if window[currentChar] == needsT[currentChar]:
                windowLength += 1

            while left <= right and windowLength == needsLength:
                reduceChar = filtered[left][1]

                startPos = filtered[left][0]
                endPos = filtered[right][0]

                if endPos - startPos + 1 < ans[0]:
                    ans = (endPos - startPos + 1, startPos, endPos)

                window[reduceChar] -= 1
                if window[reduceChar] < needsT[reduceChar]:
                    windowLength -= 1
                left += 1
            right += 1
        if ans[0] == float('inf'):
            return ''
        return s[ans[1]: ans[2] + 1]
