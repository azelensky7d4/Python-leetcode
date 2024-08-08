class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        sorted_array = self.merge(nums1, nums2)
        if len(sorted_array) % 2 == 0:
            return (sorted_array[len(sorted_array) // 2] + sorted_array[len(sorted_array) // 2 - 1]) / 2
        else:
            return sorted_array[len(sorted_array) // 2]

    def merge(self, nums1, nums2) -> [int]:
        i = 0
        j = 0
        sorted_array = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sorted_array.append(nums1[i])
                i += 1
            else:
                sorted_array.append(nums2[j])
                j += 1
        while i < len(nums1):
            sorted_array.append(nums1[i])
            i += 1
        while j < len(nums2):
            sorted_array.append(nums2[j])
            j += 1
        return sorted_array