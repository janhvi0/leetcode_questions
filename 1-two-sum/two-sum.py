class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force 
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i]+ nums[j] == target:
        #             return [i, j]
        # return []

        #optimal Approach 

        num_hash = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in num_hash:
                return [num_hash[comp], i]

            num_hash[num] = i

            

        