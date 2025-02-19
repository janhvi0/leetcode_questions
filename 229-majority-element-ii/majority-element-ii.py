class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        candidate1,candidate2=None,None
        count1,count2=0,0

        for i in nums:
            if i == candidate1:
                count1+=1
            elif i==candidate2:
                count2+=1
            elif count1==0:
                candidate1=i
                count1=1
            elif count2==0:
                candidate2=i
                count2=1
            else:
                count1-=1
                count2-=1

        result=[]
        if nums.count(candidate1)>n//3:
            result.append(candidate1)

        if candidate2 is not None and candidate2 != candidate1 and nums.count(candidate2)>n//3:
            result.append(candidate2)

        return result
            