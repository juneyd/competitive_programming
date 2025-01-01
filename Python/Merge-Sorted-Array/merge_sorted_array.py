class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Pointer for nums1 and nums2
        i, j, k = m - 1, n - 1, m + n - 1
        
        # While there are elements to compare
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # If there are remaining elements in nums2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
            
        # No need to copy the remaining elements from nums1, 
        # they are already in place
