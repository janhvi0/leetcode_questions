class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum=0
        x=0
        n=len(nums)
        for i in range(n):
            sum+=nums[i]
            x=n*(n+1)//2 
        return x-sum


    