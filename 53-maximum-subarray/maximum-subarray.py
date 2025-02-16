class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max=nums[0]
        n=len(nums)
        sum=0
        if n==1:
            return nums[0]
      
        for i in range(n):
            sum=sum+nums[i]
            if max<sum:
                max=sum
            if sum<0:
                sum=0
        return max











#brute force
        # for i in range(n):
        #     sum=0
        #     for j in range(i,n):
        #         sum+=nums[j]
        #         if max<sum:
        #             max=sum

        # return max
