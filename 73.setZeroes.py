from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowRecord = set()
        colRecord = set()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rowRecord.add(i)
                    colRecord.add(j)
        for i in rowRecord:
            for j in range(n):
                matrix[i][j] = 0
        for j in colRecord:
            for i in range(m):
                matrix[i][j] = 0