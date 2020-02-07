class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)
        l = l1+l2
        if l == 0:
            return None
        if l == 1:
            if nums1:
                return nums1[-1]
            if nums2:
                return nums2[-1]
        num = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                num.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                num.append(nums2[j])
                j += 1
            else:
                num.append(nums1[i])
                num.append(nums2[j])
                i += 1
                j += 1
        while i < len(nums1):
            num.append(nums1[i])
            i += 1
        while j < len(nums2):
            num.append(nums2[j])
            j += 1
        if l % 2 == 0:
            return float((num[l//2-1]+num[l//2])/2)
        else:
            return float(num[l//2])

"""类似于数据结构中看到的某种排序算法（重新复习）"""


def median(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) / 2
    """
    始终保证左右部分长度相等且根据中间部分的大小关系调整i,因为i，j相关，实际是两个都进行了调整
    直到找到合适的i
    """
    while imin <= imax:
        i = (imin + imax) / 2
        j = half_len - i
        if i < m and B[j-1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect
            """特殊情况，i或j位于数组第一个数"""
            if i == 0: max_of_left = B[j-1]
            elif j == 0: max_of_left = A[i-1]
            else: max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:
                return max_of_left
            """另一种特殊情况，i或j位于数组最后一个数"""
            if i == m: min_of_right = B[j]
            elif j == n: min_of_right = A[i]
            else: min_of_right = min(A[i], B[j])
"""
LeetCode原解：
把两个数组分开，分成各分成左右，左左合并，右右合并，只要左右长度相等且左最大值不大于右最小值即可；
再对特殊情况进行特殊处理
"""