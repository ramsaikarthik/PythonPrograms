class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0 or len(nums1)==0:
            nums1 = nums2[:n].sort()
        if n==0 or len(nums2)==0:
            nums1 = nums1[:m].sort()
        if m>0 and n>0:
            nums1 = nums1[0:m]
            nums2 = nums2[0:n]
            nums1+=nums2
            nums1.sort()
        print(nums1)

mer = Solution()
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

# nums1 = [1]
# m = 1
# nums2 = []
# n = 0
# nums3=nums1+nums2

nums1 = []
m = 0
nums2 = [1]
n = 1
print(nums1[0:m]+nums2[0:n])
print(len(nums1))
print(len(nums2))
mer.merge(nums1, m, nums2, n)
