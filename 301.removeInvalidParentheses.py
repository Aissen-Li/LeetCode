from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s: str) -> bool:
            leftCount = 0
            for char in s:
                if char == '(':
                    leftCount += 1
                if char == ')':
                    leftCount -= 1
                if leftCount < 0:
                    return False
            return leftCount == 0
        level = set(s)
        while True:
            valid = list(filter(isValid, level))
            if valid:
                return valid
            nextLevel = set()
            for c in level:
                for i in range(len(c)):
                    if c[i] in "()":
                        nextLevel.add(c[:i] + c[i+1:])
            level = nextLevel