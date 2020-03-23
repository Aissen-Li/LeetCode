class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        pos = [0, 0, 0]
        for i in range(1, n):
            minValue = min(res[pos[0]]*2, res[pos[1]]*3, res[pos[2]]*5)
            if minValue == res[pos[0]] * 2:
                res.append(minValue)
                pos[0] += 1
            if minValue == res[pos[1]] * 3:
                res.append(minValue)
                pos[1] += 1
            if minValue == res[pos[2]] * 5:
                res.append(minValue)
                pos[2] += 1
        return res[-1]