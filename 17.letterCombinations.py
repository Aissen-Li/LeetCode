class Solution:
    def letterCombinations(self, digits):
        numLetterDic = {'2': ['a', 'b', 'c'],
                        '3': ['d', 'e', 'f'],
                        '4': ['g', 'h', 'i'],
                        '5': ['j', 'k', 'l'],
                        '6': ['m', 'n', 'o'],
                        '7': ['p', 'q', 'r', 's'],
                        '8': ['t', 'u', 'v'],
                        '9': ['w', 'x', 'y', 'z']}

        res = []
        def bfs(letterCombination, nextDigits):
            if len(nextDigits) == 0:
                res.append(letterCombination)
            else:
                for letter in numLetterDic[nextDigits[0]]:
                    bfs(letterCombination + letter, nextDigits[1:])

        if digits:
            bfs("", digits)
        return res


s = Solution()
print(s.letterCombinations("23"))