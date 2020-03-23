from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord == endWord:
            return 0
        wordSet = set(wordList)
        wordLen = len(beginWord)
        stack = [(1, beginWord)]
        while stack:
            depth, word = stack.pop(0)
            for i in range(wordLen):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + j + word[i+1:]
                    if newWord == endWord:
                        return depth + 1
                    if newWord in wordSet:
                        stack.append((depth + 1, newWord))
                        wordSet.remove(newWord)
        return 0
