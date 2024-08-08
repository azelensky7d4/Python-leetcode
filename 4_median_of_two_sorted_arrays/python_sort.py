class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        new_array = sorted(nums1 + nums2)
        if len(new_array) % 2 == 0:
            return (new_array[len(new_array) // 2] + new_array[len(new_array) // 2 - 1]) / 2
        else:
            return new_array[int(len(new_array)/2)]


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(Solution().findMedianSortedArrays(nums1, nums2))
