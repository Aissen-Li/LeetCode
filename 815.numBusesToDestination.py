from typing import List
import collections
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        visited = [False for _ in range(len(routes))]
        routeDict = collections.defaultdict(set)
        for index, route in enumerate(routes):
            for station in route:
                routeDict[station].add(index)
        queue = collections.deque()
        queue.append((S, 1))
        while queue:
            current, res = queue.popleft()
            for busIndex in routeDict[current]:
                if visited[busIndex]:
                    continue
                for station in routes[busIndex]:
                    if station == T:
                        return res
                    queue.append((station, res + 1))
                visited[busIndex] = True
        return -1            