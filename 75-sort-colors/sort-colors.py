class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n= len(nums)
        l,m,h=0,0,n-1
        while m<=h:
            if nums[m]==0:
                nums[l],nums[m]=nums[m],nums[l]
                l+=1
                m+=1

            elif nums[m]==1:
                m+=1

            else:
                nums[m],nums[h]=nums[h],nums[m]
                h-=1
        return nums
















        # count0, count1, count2=0,0,0
      
        # for i in range(len(nums)):
        #     if nums[i]==0:
        #         count0+=1
        #     if nums[i]==1:
        #         count1+=1
        #     if nums[i]==2:
        #         count2+=1


        # pointer = 0
        # while count0>0:
        #     nums[pointer]=0
        #     pointer+=1
        #     count0-=1

        # while count1>0:
        #     nums[pointer]=1
        #     pointer+=1
        #     count1-=1


        # while count2>0:
        #     nums[pointer]=2
        #     pointer+=1
        #     count2-=1



