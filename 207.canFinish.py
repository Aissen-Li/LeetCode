from typing import List
class Solution1:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = []
        for cur, pre in prerequisites:
            inDegrees[cur] += 1
            adjacency[pre].append(cur)
        for i in range(len(inDegrees)):
            if inDegrees[i] == 0:
                queue.append(i)

        while queue:
            pre = queue.pop(0)
            numCourses -= 1
            for cur in adjacency[pre]:
                inDegrees[cur] -= 1
                if inDegrees[cur] == 0:
                    queue.append(cur)
        return not numCourses


class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(adjacency, flags, i):
            if flags[i] == -1:
                return True
            if flags[i] == 1:
                return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(adjacency, flags, j):
                    return False
            flags[i] = -1
            return True


        flags = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(adjacency, flags, i):
                return False
        return True