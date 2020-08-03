class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger:
            return True
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 == desiredTotal:
            return maxChoosableInteger % 2 == 1
        
        record = {}
        def howToWin(choice, desiredNum):
            if choice[-1] >= desiredNum:
                return True
            key = tuple(choice)
            if key in record:
                return record[key]
            for i in range(len(choice)):
                if not howToWin(choice[:i]+choice[i+1:], desiredNum-choice[i]):
                    record[key] = True
                    return True
            record[key] = False
            return False
        return howToWin(list(range(1, maxChoosableInteger + 1)), desiredTotal)