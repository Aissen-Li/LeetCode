from typing import List
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.res = []
        def dfs(arr, path, index):
            if index == len(arr):
                self.res.append(len(path))
                return
            for i in range(index, len(arr)):
                flag = True
                for char in arr[i]:
                    if char in path or arr[i].count(char) > 1:
                        flag = False
                        break
                if flag:
                    dfs(arr, path + arr[i], i + 1)
                else:
                    dfs(arr, path, i + 1)

        dfs(arr, '', 0)
        return max(self.res)