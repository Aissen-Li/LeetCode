import sys
from typing import List
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        count = sys.maxsize
        wordSet = set(wordList)
        if beginWord in wordSet:
            wordSet.remove(beginWord)
        wordLen = len(beginWord)
        visited = set()
        stack = [(1, [beginWord])]
        res = []
        while stack:
            step, currentPath = stack.pop(0)
            if step + 1 <= count:
                word = currentPath[-1]
                visited.add(word)
                for i in range(wordLen):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + j + word[i+1:]
                        if newWord in wordSet and newWord not in visited:
                            if newWord == endWord:
                                if step + 1 < count:
                                    currentPath.append(endWord)
                                    if currentPath not in res:
                                        res = [currentPath[:]]
                                        count = step + 1
                                    currentPath.pop()
                                if step + 1 == count:
                                    currentPath.append(endWord)
                                    if currentPath not in res:
                                        res.append(currentPath[:])
                                    currentPath.pop()
                            else:
                                if newWord in wordSet:
                                    currentPath.append(newWord[:])
                                    stack.append((step + 1, currentPath[:]))
                                    # wordSet.remove(newWord)
                                    currentPath.pop()
        return res