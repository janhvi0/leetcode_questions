class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = []
        for i in nums:
            if i in seen:
                seen.remove(i)

            else:
                seen.append(i)
        return seen[0]
    