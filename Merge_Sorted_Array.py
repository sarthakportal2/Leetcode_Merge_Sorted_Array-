class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #T(C(N)==O(C(N)) and S(C(N)==O(1)) as it requires Non memory space allocation iteratively
        for i in range(m,m+n):#Iterating through both List's Sizes
            nums1[i]=nums2[i-m]#Swapping Both array's Elements
        
        nums1.sort()#Sorting Both the Arrays
