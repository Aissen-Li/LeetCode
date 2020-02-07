# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:50:20 2019

@author: 李亦凡
"""
"""暴力解，时间复杂度o(n^3)"""
class Solution1:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        return None

"""leetcode上别人的解法，复杂度o(nlogn),对id进行一次排序，从两边开始同时找"""  
class Solution2:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_id = sorted(range(len(nums)), key=lambda k: nums[k])
        head = 0
        tail = len(nums) - 1
        sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
        while sum_result != target:
            if sum_result > target:
                tail -= 1
            elif sum_result < target:
                head += 1
            sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
        return [sorted_id[head], sorted_id[tail]]


"""哈希表,enumerate这个函数返回的是（顺序，值）,一般用于遍历"""    
class Solution3:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None