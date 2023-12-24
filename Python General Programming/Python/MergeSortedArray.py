class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0 or len(nums1)==0:
            nums1 = nums2[:n].sort()
        if n==0 or len(nums2)==0:
            nums1 = nums1[:m].sort()
        else:
            nums1 = nums1[0:m]
            nums2 = nums2[0:n]
            nums1+=nums2
            nums1.sort()
        print(nums1)
        