class Solution:
    def intToRoman(self, num: int):
        res = ''
        hundred_dic = {1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM', 0: ''}
        ten_dic = {1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC', 0: ''}
        one_dic = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 0: ''}
        thousand = num // 1000
        num = num % 1000
        hundred = num // 100
        num = num % 100
        ten = num // 10
        one = num % 10
        res += thousand * 'M' + hundred_dic[hundred] + ten_dic[ten] + one_dic[one]
        return res


s = Solution()
print(s.intToRoman(102))