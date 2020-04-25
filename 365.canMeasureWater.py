class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        stack = [(0, 0)]
        visited = set()
        while stack:
            remainX, remainY = stack.pop()
            if remainX == z or remainY == z or remainX + remainY == z:
                return True
            if (remainX, remainY) in visited:
                continue
            visited.add((remainX, remainY))
            stack.append((x, remainY))
            stack.append((remainX, y))
            stack.append((0, remainY))
            stack.append((remainX, 0))
            stack.append((remainX - min(remainX, y - remainY), remainY + min(remainX, y - remainY)))
            stack.append((remainX + min(remainY, x - remainX), remainY - min(remainY, x - remainX)))
        return False