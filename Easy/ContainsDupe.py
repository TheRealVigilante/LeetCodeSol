from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset = {}
        for i in range(len(nums)):
            if nums[i] in myset:
                return True
            myset[nums[i]] = 1
        return False

solution = Solution()
print(solution.containsDuplicate([1,2,3])) # Expected: True