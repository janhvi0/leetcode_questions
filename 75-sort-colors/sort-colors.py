class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0, count1, count2=0,0,0
      
        for i in range(len(nums)):
            if nums[i]==0:
                count0+=1
            if nums[i]==1:
                count1+=1
            if nums[i]==2:
                count2+=1


        pointer = 0
        for i in range(count0):
            nums[pointer]=0
            pointer+=1

        for j in range(count1):
            nums[pointer]=1
            pointer+=1


        for k in range(count2):
            nums[pointer]=2
            pointer+=1

