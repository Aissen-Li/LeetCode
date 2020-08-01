from typing import List
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        if not ops:
            return 0
        res = []
        for i in range(len(ops)):
            if ops[i] == '+':
                res.append(res[-2] + res[-1])
            elif ops[i] == 'C':
                res = res[:-1]
            elif ops[i] == 'D':
                res.append(res[-1] * 2)
            else:
                res.append(int(ops[i]))
        return sum(res) 