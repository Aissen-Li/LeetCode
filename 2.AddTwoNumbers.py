# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 13:04:34 2019

@author: 李亦凡
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        r = result
        #进位符carry
        carry = 0
        while l1 or l2:
            p = l1.val if l1 else 0
            q = l2.val if l2 else 0
            s = p+q+carry
            carry = s//10
            r.next = ListNode(s%10)
            r = r.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if carry > 0:
            r.next = ListNode(1)
        return result.next
"""重点在于不能直接result.next，r是一个指针，不断替result把后面的值准备好并且连成
   链接表，要注意这种题以后全部带上carry来做，效果更好，不需要反过来"""    