class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            # If count is 0, choose a new candidate
            if count == 0:
                candidate = num
            
            # Increase count if the same as candidate, otherwise decrease count
            if num == candidate:
                count += 1
            else:
                count -= 1
                
        return candidate