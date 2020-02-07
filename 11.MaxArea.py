class Solution1:
    def maxArea(self, height):
        opt = [0] * len(height)
        for i in range(1, len(height)):
            for j in range(0, i):
                if min(height[j], height[i]) * (i - j) >= opt[i]:
                    opt[i] = min(height[j], height[i]) * (i - j)
                else:
                    pass
        return max(opt)


"""暴力法，超时"""


class Solution2:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maxA = 0
        while left < right:
            b = right - left
            if height[left] < height[right]:
                h = height[left]
                left += 1
            else:
                h = height[right]
                right -= 1
            area = b * h
            if maxA < area:
                maxA = area
        return maxA


"""双指针法，一开始指向头尾两处，此时的底边最大，然后头尾两处比较，把较短的向内走一步，这样高发生变化，
底边减一，然后不断循环，寻找最大的面积"""