from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict, deque
        graph = defaultdict(dict)
        res = []
        variables = set()
        for equ, val in zip(equations, values):
            x, y = equ[0], equ[1]
            variables.update(equ)
            graph[x][y] = val
            graph[y][x] = 1 / val

        def bfs(x, y):
            queue = deque([[x, 1.0]])
            visited = {x}
            while queue:
                tmp, val = queue.pop()
                if tmp == y:
                    return val
                for nxt in graph[tmp]:
                    if nxt not in visited:
                        visited.add(nxt)
                    queue.appendleft([nxt, val * graph[tmp][nxt]])
            return -1

        for x, y in queries:
            if x not in variables or y not in variables:
                res.append(-1)
            else:
                res.append(bfs(x, y))
        return res
