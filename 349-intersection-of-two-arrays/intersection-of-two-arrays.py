class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #brute force with more time and space complexity
        arr=set()
        n=len(nums1)
        m=len(nums2)
        for i in range(n):
            for j in range(m):
                if nums1[i]==nums2[j]:
                    arr.add(nums1[i])

        return list(arr)