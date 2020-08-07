from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(x,y):
            while y != 0:
                  temp = x % y
                  x = y
                  y = temp
            return x
        if len(points) < 3: return len(points)
        # 判断当前点是否全部重复
        tag = 1
        for i in range(len(points) - 1):
            if points[i][0] != points[i + 1][0] or points[i][1] != points[i + 1][1]:
                tag = 0
                break
        if tag: return len(points)
        # 使用哈希表进行直线斜率的存储
        Hashmap = {}
        maxdot = 0
        # 对每个点进行直线点斜式判断,将相同斜率的存入同一键值中
        for i in range(len(points)):
            repeat = 0
            currentRes = 0
            # 避免重复计数
            Hashmap.clear()
            for j in range(i + 1,len(points)):
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]
                if x == 0 and y == 0:
                    repeat += 1
                    continue
                l1,l2 = int(x / gcd(x,y)),int(y / gcd(x,y))
                k = str(l1) + '/' + str(l2)
                Hashmap[k] = Hashmap.get(k, 0) + 1
                currentRes = max(currentRes,Hashmap[k])
            maxdot = max(maxdot,currentRes + repeat + 1)
        return maxdot
