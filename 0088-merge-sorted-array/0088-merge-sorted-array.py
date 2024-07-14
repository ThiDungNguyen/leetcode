class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
                # Start from the end of nums1 and nums2 ####
        nums1[m:] = []
        nums1 += nums2
        nums1.sort()
        print(nums1)

        