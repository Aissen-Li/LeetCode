from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        row, col = len(matrix), len(matrix[0])
        seq = 1
        res = []
        i, j = 0, -1
        while row > 0 and col > 0:
            for _ in range(col):
                j += seq
                res.append(matrix[i][j])
            for _ in range(row-1):
                i += seq
                res.append(matrix[i][j])
            row, col = row-1, col-1
            seq *= -1
        return res
