from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    boxIndex = (i // 3) * 3 + j // 3
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[boxIndex][num] = boxes[boxIndex].get(num, 0) + 1
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[boxIndex][num] > 1:
                        return False
        return True
