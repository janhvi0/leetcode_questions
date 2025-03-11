class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=nums[0]
        n=len(nums)
        for i in range(n-1):
            nums[i+1] += sum 
            sum = nums[i+1]
        return nums 
