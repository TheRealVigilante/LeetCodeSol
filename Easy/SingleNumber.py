from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        nums.append(-1)
        for i in range(0,len(nums),2):
            if nums[i] != nums[i+1]:
                return nums[i]

sol = Solution()
print(sol.singleNumber([1,2,1]))