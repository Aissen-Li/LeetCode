from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskLength = len(tasks)
        if taskLength <= 1:
            return taskLength
        taskMap = {}
        for task in tasks:
            taskMap[task] = taskMap.get(task, 0) + 1
        sortedTask = sorted(taskMap.items(), key = lambda  x: x[1], reverse=True)
        maxTaskTimes = sortedTask[0][1]
        res = (maxTaskTimes - 1) * (n + 1)
        for otherTask in sortedTask:
            if otherTask[1] == maxTaskTimes:
                res += 1
        return max(res, taskLength)

