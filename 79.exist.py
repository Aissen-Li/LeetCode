from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        mark = [[0] * n for _ in range(m)]

        def dfs(board, currentPos, mark, word):
            if len(word) == 0:
                return True

            for dir in direction:
                nextPos = (currentPos[0] + dir[0], currentPos[1] + dir[1])
                if 0 <= nextPos[0] < m and 0 <= nextPos[1] < n and board[nextPos[0]][nextPos[1]] == word[0]:
                    if mark[nextPos[0]][nextPos[1]] == 1:
                        continue
                    mark[nextPos[0]][nextPos[1]] = 1
                    if dfs(board, nextPos, mark, word[1:]):
                        return True
                    else:
                        mark[nextPos[0]][nextPos[1]] = 0
                return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    mark[i][j] = 1
                    if dfs(board, (i, j), mark, word[1:]):
                        return True
                    else:
                        mark[i][j] = 0
        return False


s = Solution()
s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
"ABCCED")