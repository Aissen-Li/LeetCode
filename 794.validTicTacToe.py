from typing import List
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        xCount = sum(row.count('X') for row in board)
        oCount = sum(row.count('O') for row in board)
        def win(board, player):
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):
                    return True
                if all(board[j][i] == player for j in range(3)):
                    return True
            return (player == board[0][0] == board[1][1] == board[2][2] or
                    player == board[0][2] == board[1][1] == board[2][0])
        if oCount not in [xCount, xCount-1]:
            return False
        if win(board, 'X') and xCount - oCount != 1:
            return False
        if win(board, 'O') and xCount != oCount:
            return False
        return True