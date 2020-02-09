class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        pair = {'(': ')', '[': ']', '{': '}'}
        order = deque([])
        for bracket in s:
            if bracket in pair.keys():
                order.append(bracket)
            else:
                if order:
                    former = order.pop()
                else:
                    return False
                if bracket != pair[former] or pair.get(former, False) == False:
                    return False
        if order:
            return  False
        return True


s = Solution()
print(s.isValid("()[]{}{{}}("))