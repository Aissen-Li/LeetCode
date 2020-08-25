class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        secretDict = {}
        guessDict = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            secretDict[secret[i]] = secretDict.get(secret[i], 0) + 1
            guessDict[guess[i]] = guessDict.get(guess[i], 0) + 1
        for char in secretDict:
            if char in guessDict:
                cows += min(secretDict[char], guessDict[char])
        cows -= bulls
        return str(bulls) + 'A' + str(cows) + 'B'