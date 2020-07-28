class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        insertPos = m + n - 1
        while nums2 and i >= 0:
            if nums1[i] < nums2[-1]:
                nums1[insertPos] = nums2.pop()
            else:
                nums1[insertPos] = nums1[i]
                i = i - 1
            insertPos = insertPos - 1

        if nums2: nums1[:len(nums2)] = nums2 # append to the end of nums1