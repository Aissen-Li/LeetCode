from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        # build Trie
        for word in words:
            t = trie
            for char in word:
                t = t.setdefault(char, {})
            t["end"] = 1
        res = []
        row = len(board)
        col = len(board[0])
        # dfs
        def dfs(i, j, tree, s):
            currentChar = board[i][j]
            if currentChar not in tree:
                return
            tree = tree[currentChar]
            if "end" in tree and tree["end"] == 1:
                if s + currentChar not in res:
                    res.append(s + currentChar)
                    tree["end"] == 0
            board[i][j] = "#"
            for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                tmpX = i + x
                tmpY = j + y
                if 0 <= tmpX < row and 0 <= tmpY < col and board[tmpX][tmpY] != "#":
                    dfs(tmpX, tmpY, tree, s + currentChar)
            board[i][j] = currentChar
        for i in range(row):
            for j in range(col):
                dfs(i, j, trie, '')
        return res