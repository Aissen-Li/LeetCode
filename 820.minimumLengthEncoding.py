from typing import List
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        temp = set(words)
        for word in words:
            for k in range(1, len(word)):
                temp.discard(word[k:])
        return sum(len(word) + 1 for word in temp)