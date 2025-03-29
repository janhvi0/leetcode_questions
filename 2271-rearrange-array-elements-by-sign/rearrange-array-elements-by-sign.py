class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        v1, v2, ans = [],[],[]
        n = len(nums)
        
        for i in nums:
            if i >0 :
                v1.append(i)

            else: 
                v2.append(i)

        p1 , p2 = 0,0
        while p2 < n//2:
            ans.append(v1[p1])
            p1+=1
            ans.append(v2[p2])
            p2+=1

        return ans

        return 