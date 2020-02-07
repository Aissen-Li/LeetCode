# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:40:29 2019

@author: 李亦凡
"""
"不要纯用数字做，可以用字符串切片不断更新最长子串！！！！！"
class Solution1:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_number = 0
        number = 0
        test = ''
        for i in s:
            if i not in test:
                test += i
                number += 1
            else:
                if number >= max_number:
                    max_number = number
                index = test.index(i)
                test = test[(index+1):] + i
                number = len(test)
        if number > max_number:
            max_number = number
        return max_number
    

"""i表示了最长子串的开头，j指针指向最长子串的结尾处；
   当发生重复时，利用字典st记录该字符最后出现的位置，
   比较的内容变成原最长子串与该重复字符之间的子串长度"""
class Solution2:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans