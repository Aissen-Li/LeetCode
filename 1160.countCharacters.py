from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        flag = 1
        for word in words:
            for char in word:
                if word.count(char) > chars.count(char):
                    flag = 0
                    break
                else:
                    flag = 1
            if flag == 1:
                res += len(word)
        return res


s = Solution()
s.countCharacters(["cat","bt","hat","tree"], "atach")