from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        print(nums)



sol = Solution()
nums = [0,1,0,3,12]
sol.moveZeroes(nums)