class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0
        recall = {}
        s1Count, s2Count, index = 0, 0, 0
        while True:
            s1Count += 1
            for char in s1:
                if char == s2[index]:
                    index += 1
                    if index == len(s2):
                        s2Count, index = s2Count + 1, 0
            if s1Count == n1:
                return s2Count // n2
            if index in recall:
                s1CountBefore, s2CountBefore = recall[index]
                preLoop = (s1CountBefore, s2CountBefore)
                nextLoop = (s1Count- s1CountBefore, s2Count - s2CountBefore)
                break
            else:
                recall[index] = (s1Count, s2Count)
        res = preLoop[1] + (n1 - preLoop[0]) // nextLoop[0] * nextLoop[1]
        rest = (n1 - preLoop[0]) % nextLoop[0]
        for i in range(rest):
            for char in s1:
                if char == s2[index]:
                    index += 1
                    if index == len(s2):
                        res += 1
                        index = 0
        return res // n2
