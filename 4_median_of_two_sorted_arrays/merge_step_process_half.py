class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        len_1 = len(nums1)
        len_2 = len(nums2)
        i = 0
        j = 0
        forward_mid = 0
        back_mid = 0
        for element in range((len_1 + len_2) // 2 + 1):
            back_mid = forward_mid
            if i < len_1 and j < len_2:
                if nums1[i] < nums2[j]:
                    forward_mid = nums1[i]
                    i += 1
                else:
                    forward_mid = nums2[j]
                    j += 1
            elif i < len_1:
                forward_mid = nums1[i]
                i += 1
            else:
                forward_mid = nums2[j]
                j += 1
        if (len_1 + len_2) % 2 == 0:
            return (forward_mid + back_mid) / 2
        else:
            return forward_mid