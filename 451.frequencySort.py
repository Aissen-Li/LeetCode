class Solution:
    def frequencySort(self, s: str) -> str:
        record = {}
        for char in s:
            record[char] = record.get(char, 0) + 1
        seq = sorted(record.items(), key=lambda x: x[1], reverse=True)
        res = ''
        for i in range(len(seq)):
            res += seq[i][0] * seq[i][1]
        return res